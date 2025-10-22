---
name: project-bootstrapper
description: Bootstrap new development projects by cloning template repositories and installing Claude Code plugins. Use when user requests to create, initialize, set up, or bootstrap a new project for React, Node backend, or other supported frameworks. Automatically clones boilerplate and installs development tools.
---

# Project Bootstrapper

## Overview

Automates project initialization by combining template repositories (for boilerplate code) with Claude Code plugins (for development tools). This two-part approach gives you both a solid starting structure and AI-powered development assistance.

## Architecture

```
Template Repository          Claude Code Plugins
(Boilerplate & Setup)       (Development Tools)
        ↓                            ↓
   Clone repo               Install core + framework plugins
        ↓                            ↓
File structure,          Commands, agents, automation
  configs, deps            for development workflow
```

## When to Use This Skill

Use this skill when the user requests:
- "Bootstrap a new React project"
- "Set up a new frontend project"
- "Initialize a React/Node project"
- "Create a new [framework] project"

## Supported Frameworks

- **react** - React frontend with Vite, TypeScript, ESLint, and Prettier
  - Template: https://github.com/trickycdm/react-template
  - Plugin: Provides component/hook generation, analysis tools, specialized agents

- **node-backend** - Node.js backend (planned)
  - Template: https://github.com/trickycdm/node-backend-template
  - Plugin: TBD

## Bootstrap Workflow

Follow these steps in order:

### Step 1: Understand the Request

Identify:
- Project name
- Framework type (react, node-backend, etc.)
- Base directory (defaults to current directory)

Example requests:
- "Bootstrap a new React project called my-app"
- "Set up a React frontend in the projects folder"

### Step 2: Run the Bootstrap Script

Execute the bootstrap script with the appropriate parameters:

```bash
python scripts/bootstrap_project.py <project-name> <framework> [base-path]
```

Example:
```bash
python scripts/bootstrap_project.py my-react-app react
```

The script will:
1. Clone the template repository
2. Remove git history and reinitialize
3. Install project dependencies (npm install)
4. Install the framework-specific plugin (e.g., react)

**Note:** The core plugin and marketplace are already installed since you're using this skill.

### Step 3: Verify Installation

After the script completes, verify:
- Project directory was created
- Template files are present
- Dependencies were installed
- Framework plugin was installed successfully
- No error messages were displayed

### Step 4: Inform the User

Tell the user:
- The project has been bootstrapped successfully
- The project location
- What commands are available (e.g., `/component`, `/hook`, `/analyze-component`)
- Next steps: navigate to the project and run `claude-code`

## What Each Part Provides

### Template Repository Provides:
- ✅ Complete folder structure
- ✅ Configuration files (Vite, TypeScript, ESLint, Prettier)
- ✅ Package.json with dependencies
- ✅ Starter components and files
- ✅ Development and build scripts

### Claude Code Plugins Provide:
- ✅ Code generation commands (`/component`, `/hook`, `/util`, `/type`)
- ✅ Analysis tools (`/analyze-component`, `/suggest-refactor`)
- ✅ Documentation generators (`/doc-component`, `/doc-props`)
- ✅ Specialized AI agents (Component, Performance, Accessibility)
- ✅ Custom automation and workflows

## Plugin Architecture

The bootstrap process uses a two-tier plugin system:

1. **Core Plugin** - Provides essential utilities, agents, commands, and hooks for all projects (already installed)
2. **Framework Plugin** - Adds framework-specific development tools and workflows (installed during bootstrap)

**Note:** Since you're using this skill, the core plugin is already installed. The bootstrap script will only install the framework-specific plugin for your new project.

For detailed information about the plugin architecture, see `references/plugin_architecture.md`.

## Available Commands After Bootstrap

For React projects:
- `/component [name]` - Generate React component
- `/hook [name]` - Create custom hook
- `/util [name]` - Generate utility function
- `/type [name]` - Create TypeScript types
- `/analyze-component` - Analyze for best practices
- `/suggest-refactor` - Get refactoring suggestions
- `/doc-component` - Generate component docs
- `/doc-props` - Document props interface

Plus specialized agents:
- `/agent component-agent` - Component architecture expert
- `/agent performance-agent` - Performance optimization
- `/agent accessibility-agent` - A11y compliance

## Troubleshooting

### Template repository not found

```
❌ Failed to clone template repository
```

**Solution:** Ensure the template repository exists and is accessible:
- React: https://github.com/trickycdm/react-template
- Create the template repo if it doesn't exist

### Dependencies installation fails

```
⚠️  Failed to install dependencies
```

**Solution:** 
- Check Node.js and npm are installed
- Navigate to project and run `npm install` manually
- Check for network issues

### Plugin installation fails

```
❌ Failed to install plugin: react
```

**Solution:**
- Verify Claude Code is installed
- Ensure the framework plugin exists in the marketplace
- Check network connectivity
- Try running `claude plugin install react` manually from the project directory

## Extending for New Frameworks

To add support for a new framework:

1. **Create template repository:**
   - Set up your preferred boilerplate
   - Push to GitHub (e.g., `youruser/vue-template`)

2. **Create Claude Code plugin:**
   - Add framework-specific commands
   - Create specialized agents
   - Add automation hooks

3. **Update bootstrap script:**
   - Add template URL to `TEMPLATE_REPOS` dict
   - No other changes needed!

4. **Update marketplace.json:**
   - Add the new plugin to your plugin repository

## Resources

### scripts/bootstrap_project.py
Python script that automates the entire bootstrap process:
- Clones template repository
- Resets git history
- Installs dependencies
- Adds marketplace
- Installs plugins in correct order

### references/plugin_architecture.md
Comprehensive documentation on how the plugin system works, including the two-tier architecture, plugin responsibilities, and extension guidelines.
