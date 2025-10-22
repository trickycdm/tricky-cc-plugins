#!/usr/bin/env python3
"""
Generate TypeScript type definitions.
"""

import os
import sys
from pathlib import Path
import argparse


def generate_type(name, path="src/types", use_type=False):
    """Generate a TypeScript type definition file."""
    type_dir = Path(path)
    type_dir.mkdir(parents=True, exist_ok=True)
    
    # Ensure PascalCase
    if not name[0].isupper():
        name = name.capitalize()
    
    type_file = type_dir / f"{name}.ts"
    
    if type_file.exists():
        print(f"❌ Type file already exists: {type_file}")
        overwrite = input("Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Cancelled.")
            return False
    
    # Choose between 'type' and 'interface'
    keyword = "type" if use_type else "interface"
    
    if use_type:
        content = f"""/**
 * {name} type definition
 */
export type {name} = {{
  // Add your type properties here
  id: string;
}};
"""
    else:
        content = f"""/**
 * {name} interface definition
 */
export interface {name} {{
  // Add your interface properties here
  id: string;
}}
"""
    
    with open(type_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Created {keyword}: {type_file}")
    print(f"\nNext steps:")
    print(f"1. Add your properties")
    print(f"2. Import where needed: import {{ {name} }} from '@/types/{name}'")
    return True


def main():
    parser = argparse.ArgumentParser(description='Generate TypeScript types')
    parser.add_argument('name', help='Type name (PascalCase)')
    parser.add_argument('--path', default='src/types', help='Type directory path')
    parser.add_argument('--type', action='store_true', help='Use "type" instead of "interface"')
    
    args = parser.parse_args()
    generate_type(args.name, args.path, args.type)


if __name__ == '__main__':
    main()
