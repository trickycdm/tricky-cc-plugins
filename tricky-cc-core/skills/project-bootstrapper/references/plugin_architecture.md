# Plugin Architecture

This document explains how the project bootstrapper skill combines template repositories with Claude Code plugins.

## Overview

The bootstrapper uses a two-part architecture:

1. **Template Repositories** - Provide complete boilerplate code and project structure
2. **Claude Code Plugins** - Provide development tools and AI assistance

This separation gives you the best of both worlds: quick setup from proven templates + powerful development tools.

## Architecture Diagram

```
User (already has core plugin installed)
        ↓
User Request: "Bootstrap a new React project"
        ↓
Clone template repo (all the boilerplate)
        ↓
Reset git history
        ↓
Install dependencies (npm install)
        ↓
Install react plugin (React-specific tools)
        ↓
Result: Full project + Development superpowers!
```

**Note:** The core plugin and marketplace must already be installed to use this bootstrapper skill.

## Template Repository

Repository: https://github.com/trickycdm/react-template (you'll create this)

**What the template provides:**
- ✅ Complete folder structure (components, hooks, utils, styles, types, assets)
- ✅ Vite configuration
- ✅ TypeScript configuration
- ✅ ESLint and Prettier setup
- ✅ Package.json with all dependencies
- ✅ Starter components and files
- ✅ Git configuration (.gitignore)
- ✅ Development and build scripts

**Why use templates:**
- Instant setup - no code generation needed
- Proven, tested structure
- Easy to maintain and update
- Can clone and start coding immediately
- Use GitHub's "Use this template" feature

## Claude Code Plugin System

Repository: https://github.com/trickycdm/tricky-cc-plugins

### Core Plugin

Provides utilities for ALL projects regardless of framework.

**Responsibilities:**
- Universal commands (commit messages, docs, testing)
- Common hooks and automation
- Shared agent capabilities
- Base MCP server connections

### Framework Plugins (e.g., React Plugin)

Provide framework-specific development tools.

**React Plugin Provides:**

*Commands:*
- `/component [name]` - Generate React components
- `/hook [name]` - Create custom hooks  
- `/util [name]` - Generate utility functions
- `/type [name]` - Create TypeScript types
- `/analyze-component` - Comprehensive analysis
- `/suggest-refactor` - Refactoring suggestions
- `/doc-component` - Generate JSDoc
- `/doc-props` - Document props

*Agents:*
- **Component Agent** - Component architecture expert
- **Performance Agent** - Performance optimization specialist
- **Accessibility Agent** - A11y compliance expert

*Automation:*
- Custom hooks for file watchers
- Auto-formatting on save
- Type generation from APIs
- Whatever you want to automate!

## Plugin Installation Order

**Context:** Since this bootstrapper is part of the core plugin, users already have:
- Core plugin installed (provides foundation)
- Marketplace configured (tricky-cc-plugins)

**During Bootstrap:** Only the framework plugin is installed:

```
Core plugin (already installed)
        ↓
Framework plugin (installed during bootstrap)
```

## Available Frameworks

### React
- **Template**: https://github.com/trickycdm/react-template
- **Plugin**: React development tools
- **Status**: Ready (plugin complete, template needs creation)

### Node Backend (Planned)
- **Template**: https://github.com/trickycdm/node-backend-template
- **Plugin**: Backend development tools
- **Status**: Planned

## Plugin Components

Each plugin can include:

### Commands (`commands/`)
Custom slash commands available in Claude Code.

**Example:** `/component Button`
- Defined in `commands/component.md`
- Executes `scripts/generate_component.py`

### Agents (`agents/`)
Specialized AI agents for specific tasks.

**Example:** `/agent performance-agent`
- Defined in `agents/performance-agent.md`
- Provides expert analysis and suggestions

### Scripts (`scripts/`)
Python/Bash scripts for automation.

**Example:** `generate_component.py`
- Creates files with proper structure
- Enforces code conventions
- Handles file system operations

### Hooks (Optional)
Event handlers that trigger automatically.

**Example:** On file save → auto-format
- Defined in `hooks/hooks.json`
- React to project events

### MCP Servers (Optional)
External tool integrations.

**Example:** Connect to API, database, or service
- Defined in `.mcp.json`
- Extend Claude's capabilities

## Why This Architecture?

### Template Repositories Handle:
- ✅ **Boilerplate** - All the repetitive setup code
- ✅ **Structure** - Proven folder organization
- ✅ **Configuration** - Build tools, linters, formatters
- ✅ **Dependencies** - All required packages
- ✅ **Quick start** - Clone and go in seconds

### Claude Code Plugins Handle:
- ✅ **Code generation** - Smart component/hook creation
- ✅ **Analysis** - Best practices, performance, accessibility
- ✅ **Refactoring** - Intelligent suggestions
- ✅ **Documentation** - Auto-generate docs
- ✅ **Specialized AI** - Expert agents for specific domains
- ✅ **Automation** - Custom workflows and hooks

## Extending the System

### Adding a New Framework

**1. Create Template Repository:**
```bash
# Set up your boilerplate
git init my-framework-template
# Add your preferred structure and configs
git add .
git commit -m "Initial template"
git push
```

**2. Create Claude Code Plugin:**
```
my-framework-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── [your-commands].md
├── agents/
│   └── [your-agents].md
└── scripts/
    └── [your-scripts].py
```

**3. Update Bootstrap Script:**
```python
TEMPLATE_REPOS = {
    "react": "https://github.com/user/react-template",
    "my-framework": "https://github.com/user/my-framework-template",  # Add this
}
```

**4. Update Marketplace:**
```json
{
  "plugins": [
    {"name": "core", ...},
    {"name": "react", ...},
    {"name": "my-framework", ...}  // Add this
  ]
}
```

**5. Done!**
```bash
# It just works
python bootstrap_project.py my-app my-framework
```

## Best Practices

**For Templates:**
- Keep them updated with latest best practices
- Include comprehensive README
- Provide example components
- Set up CI/CD configs
- Use semantic versioning tags

**For Plugins:**
- Focus on development workflow
- Provide clear command documentation
- Create specialized agents for complex tasks
- Test commands thoroughly
- Follow Claude Code plugin guidelines

## Template vs Plugin Decision Guide

**Put in Template if:**
- It's boilerplate that rarely changes
- It's needed for initial project setup
- It's configuration files
- It's static assets or starter code

**Put in Plugin if:**
- It generates code dynamically
- It analyzes existing code
- It provides AI assistance
- It automates development tasks
- It needs to adapt to context

## Claude Code Plugin Documentation

For complete details on plugin development:
https://docs.claude.com/en/docs/claude-code/plugins

## Summary

This architecture gives you:
- ⚡ **Fast setup** - Clone template in seconds
- 🎯 **Best practices** - Proven project structure
- 🤖 **AI superpowers** - Smart code generation and analysis
- 🔧 **Flexibility** - Easy to extend and customize
- 📦 **Reusability** - Templates and plugins both reusable

You get professional project structure instantly, plus powerful development tools that make you more productive!
