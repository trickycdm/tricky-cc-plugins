#!/usr/bin/env python3
"""
Generate a custom React hook.
"""

import os
import sys
from pathlib import Path
import argparse


def generate_hook(name, path="src/hooks"):
    """Generate a React hook file."""
    hook_dir = Path(path)
    hook_dir.mkdir(parents=True, exist_ok=True)
    
    # Ensure hook name starts with "use"
    if not name.startswith("use"):
        print(f"⚠️  Hook names should start with 'use': {name}")
        name = f"use{name.capitalize()}"
        print(f"Using: {name}")
    
    hook_file = hook_dir / f"{name}.ts"
    
    if hook_file.exists():
        print(f"❌ Hook already exists: {hook_file}")
        overwrite = input("Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Cancelled.")
            return False
    
    content = f"""import {{ useState }} from 'react';

/**
 * {name} hook
 * @returns Hook state and methods
 */
export const {name} = () => {{
  // Hook implementation
  const [state, setState] = useState();
  
  // Add your hook logic here
  
  return {{
    state,
    setState,
    // Add more return values
  }};
}};
"""
    
    with open(hook_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Created hook: {hook_file}")
    return True


def main():
    parser = argparse.ArgumentParser(description='Generate a React hook')
    parser.add_argument('name', help='Hook name (should start with "use")')
    parser.add_argument('--path', default='src/hooks', help='Hook directory path')
    
    args = parser.parse_args()
    generate_hook(args.name, args.path)


if __name__ == '__main__':
    main()
