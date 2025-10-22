#!/usr/bin/env python3
"""
Bootstrap a new project with Claude Code plugins.

This script:
1. Clones the template repository
2. Removes git history and reinitializes
3. Installs dependencies
4. Adds the Tricky CC plugins marketplace
5. Installs core plugin
6. Installs framework-specific plugin (react, node-backend, etc.)
"""

import os
import subprocess
import sys
import json
from pathlib import Path


# Template repository URLs
TEMPLATE_REPOS = {
    "react": "https://github.com/trickycdm/react-template",
    "node-backend": "https://github.com/trickycdm/node-backend-template",
}


def run_command(cmd, cwd=None, check=True):
    """Run a shell command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(
        cmd,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=check
    )
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result


def clone_template(template_url, project_name, base_path="."):
    """Clone the template repository."""
    project_path = Path(base_path) / project_name
    
    print(f"📥 Cloning template from {template_url}...")
    result = run_command(f'git clone {template_url} {project_path}', check=False)
    
    if result.returncode != 0:
        print(f"❌ Failed to clone template repository")
        return None
    
    print(f"✅ Cloned template to: {project_path}")
    return project_path


def reset_git_history(project_path):
    """Remove existing git history and reinitialize."""
    print("🔄 Resetting git history...")
    
    # Remove .git directory
    git_dir = project_path / ".git"
    if git_dir.exists():
        run_command(f'rm -rf .git', cwd=project_path)
    
    # Initialize new git repo
    run_command('git init', cwd=project_path)
    run_command('git add .', cwd=project_path)
    run_command('git commit -m "Initial commit from template"', cwd=project_path, check=False)
    
    print("✅ Git history reset")


def install_dependencies(project_path):
    """Install project dependencies."""
    print("\n📦 Installing dependencies...")
    
    # Check if package.json exists (for Node projects)
    package_json = project_path / "package.json"
    if package_json.exists():
        result = run_command("npm install", cwd=project_path, check=False)
        if result.returncode == 0:
            print("✅ Dependencies installed")
        else:
            print("⚠️  Failed to install dependencies. Run 'npm install' manually.")
    else:
        print("ℹ️  No package.json found, skipping dependency installation")


def add_marketplace(project_path):
    """Add the Tricky CC plugins marketplace."""
    marketplace_url = "https://github.com/trickycdm/tricky-cc-plugins"
    
    # Change to project directory
    original_cwd = os.getcwd()
    os.chdir(project_path)
    
    try:
        result = run_command(f'claude marketplace add "{marketplace_url}"', check=False)
        if result.returncode == 0:
            print(f"✅ Added marketplace: {marketplace_url}")
        else:
            print(f"⚠️  Marketplace may already be added or encountered an issue")
    finally:
        os.chdir(original_cwd)


def install_plugin(plugin_name, project_path):
    """Install a Claude Code plugin."""
    original_cwd = os.getcwd()
    os.chdir(project_path)
    
    try:
        result = run_command(f'claude plugin install {plugin_name}', check=False)
        if result.returncode == 0:
            print(f"✅ Installed plugin: {plugin_name}")
            return True
        else:
            print(f"❌ Failed to install plugin: {plugin_name}")
            return False
    finally:
        os.chdir(original_cwd)


def bootstrap_project(project_name, framework, base_path="."):
    """
    Bootstrap a new project with the specified framework.
    
    Args:
        project_name: Name of the project to create
        framework: Framework type (react, node-backend, etc.)
        base_path: Base directory where project will be created
    """
    print(f"\n🚀 Bootstrapping {framework} project: {project_name}\n")
    
    # Check if template exists for this framework
    if framework not in TEMPLATE_REPOS:
        print(f"❌ No template repository configured for framework: {framework}")
        print(f"Available frameworks: {', '.join(TEMPLATE_REPOS.keys())}")
        return False
    
    # Step 1: Clone template repository
    print("📋 Cloning template repository...")
    project_path = clone_template(TEMPLATE_REPOS[framework], project_name, base_path)
    if not project_path:
        return False
    
    # Step 2: Reset git history
    reset_git_history(project_path)
    
    # Step 3: Install dependencies
    install_dependencies(project_path)
    
    # Step 4: Add marketplace
    print("\n📦 Adding Tricky CC plugins marketplace...")
    add_marketplace(project_path)
    
    # Step 5: Install core plugin (must be first)
    print("\n🔧 Installing core plugin...")
    if not install_plugin("core", project_path):
        print("❌ Failed to install core plugin. Aborting.")
        return False
    
    # Step 6: Install framework-specific plugin
    print(f"\n⚛️  Installing {framework} plugin...")
    if not install_plugin(framework, project_path):
        print(f"❌ Failed to install {framework} plugin.")
        return False
    
    print(f"\n✅ Project '{project_name}' bootstrapped successfully!")
    print(f"📁 Location: {project_path.absolute()}")
    print(f"\nNext steps:")
    print(f"  1. cd {project_name}")
    print(f"  2. Run 'claude' to start developing")
    print(f"  3. Check out the Claude Code commands with '/help'")
    
    return True


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python bootstrap_project.py <project-name> <framework> [base-path]")
        print("Example: python bootstrap_project.py my-app react")
        print("Available frameworks: react, node-backend")
        sys.exit(1)
    
    project_name = sys.argv[1]
    framework = sys.argv[2]
    base_path = sys.argv[3] if len(sys.argv) > 3 else "."
    
    success = bootstrap_project(project_name, framework, base_path)
    sys.exit(0 if success else 1)
