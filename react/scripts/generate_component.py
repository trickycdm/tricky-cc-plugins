#!/usr/bin/env python3
"""
Generate a new React component with TypeScript.
"""

import os
import sys
from pathlib import Path
import argparse


def generate_component(name, path="src/components", with_props=True, styled=False):
    """
    Generate a React component file.
    
    Args:
        name: Component name (PascalCase)
        path: Directory path for the component
        with_props: Include props interface
        styled: Include styled-components boilerplate
    """
    # Ensure path exists
    component_dir = Path(path)
    component_dir.mkdir(parents=True, exist_ok=True)
    
    # Component file path
    component_file = component_dir / f"{name}.tsx"
    
    # Check if file already exists
    if component_file.exists():
        print(f"❌ Component already exists: {component_file}")
        overwrite = input("Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Cancelled.")
            return False
    
    # Generate component content
    content = generate_component_content(name, with_props, styled)
    
    # Write file
    with open(component_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Created component: {component_file}")
    return True


def generate_component_content(name, with_props, styled):
    """Generate the component file content."""
    
    imports = ["import React from 'react';"]
    
    if styled:
        imports.append("import styled from 'styled-components';")
    
    imports_section = '\n'.join(imports)
    
    # Props interface
    props_section = ""
    if with_props:
        props_section = f"""
interface {name}Props {{
  // Add your props here
}}
"""
    
    # Component parameters
    params = f"props: {name}Props" if with_props else ""
    
    # Styled components section
    styled_section = ""
    if styled:
        styled_section = f"""
const Container = styled.div`
  /* Add your styles here */
`;
"""
    
    # Component JSX
    container_tag = "Container" if styled else "div"
    
    component_section = f"""
/**
 * {name} component
 */
export const {name}: React.FC{f'<{name}Props>' if with_props else ''} = ({params}) => {{
  return (
    <{container_tag}>
      {{/* Component content */}}
    </{container_tag}>
  );
}};
"""
    
    return f"""{imports_section}
{props_section}{styled_section}{component_section}"""


def main():
    parser = argparse.ArgumentParser(description='Generate a React component')
    parser.add_argument('name', help='Component name (PascalCase)')
    parser.add_argument('--path', default='src/components', help='Component directory path')
    parser.add_argument('--no-props', action='store_true', help='Generate without props interface')
    parser.add_argument('--styled', action='store_true', help='Include styled-components boilerplate')
    
    args = parser.parse_args()
    
    # Validate component name (should be PascalCase)
    if not args.name[0].isupper():
        print(f"⚠️  Component name should start with uppercase: {args.name}")
        print(f"Did you mean: {args.name.capitalize()}?")
        response = input("Continue anyway? (y/n): ").lower()
        if response != 'y':
            return
    
    generate_component(
        args.name,
        args.path,
        with_props=not args.no_props,
        styled=args.styled
    )


if __name__ == '__main__':
    main()
