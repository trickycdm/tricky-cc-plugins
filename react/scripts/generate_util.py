#!/usr/bin/env python3
"""
Generate a utility function file.
"""

import os
import sys
from pathlib import Path
import argparse


def generate_util(name, path="src/utils"):
    """Generate a utility function file."""
    util_dir = Path(path)
    util_dir.mkdir(parents=True, exist_ok=True)
    
    # Convert to camelCase if needed
    if name[0].isupper():
        name = name[0].lower() + name[1:]
    
    util_file = util_dir / f"{name}.ts"
    
    if util_file.exists():
        print(f"❌ Utility file already exists: {util_file}")
        overwrite = input("Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Cancelled.")
            return False
    
    content = f"""/**
 * {name} utility function
 * @param param - Description of parameter
 * @returns Description of return value
 */
export const {name} = (param: any): any => {{
  // Implementation here
  return param;
}};
"""
    
    with open(util_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Created utility: {util_file}")
    print(f"\nNext steps:")
    print(f"1. Update parameter types")
    print(f"2. Update return type")
    print(f"3. Implement the function logic")
    return True


def main():
    parser = argparse.ArgumentParser(description='Generate a utility function')
    parser.add_argument('name', help='Utility function name (camelCase)')
    parser.add_argument('--path', default='src/utils', help='Utility directory path')
    
    args = parser.parse_args()
    generate_util(args.name, args.path)


if __name__ == '__main__':
    main()
