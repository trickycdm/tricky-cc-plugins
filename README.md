# Tricky CC Plugins 🚀

> Professional Claude Code plugin collection with commands, agents, and skills for enhanced development workflows

[![Version](https://img.shields.io/badge/version-1.0.7-blue.svg)](https://github.com/trickycdm/tricky-cc-plugins)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-purple.svg)](https://claude.ai)

## Overview

**Tricky CC Plugins** is a comprehensive suite of productivity tools for Claude Code that supercharges your development workflow with intelligent automation, code review capabilities, and project management features.

### Key Features

- **🤖 Intelligent Agents** - Specialized AI agents for code review, security analysis, documentation generation, and more
- **⚡ Power Commands** - Streamlined commands for commits, testing, accessibility audits, and changelog generation
- **🛠️ Development Skills** - Advanced capabilities including Playwright testing, GitHub integration, and document optimization
- **📦 Easy Installation** - Single command to install the entire plugin suite

## Quick Start

### Prerequisites

- Claude Code desktop application installed
- Git configured on your system
- Node.js (for JavaScript/TypeScript projects)
- Python (for Python-based skills)

### Installation

1. **Add the plugin marketplace**:
   ```bash
   claude-code marketplace add https://github.com/trickycdm/tricky-cc-plugins
   ```

2. **Install the core plugin**:
   ```bash
   claude-code plugin install core
   ```

That's it! You now have access to all commands, agents, and skills.

## What's Included

### 🤖 Agents

Intelligent AI agents that work autonomously on complex tasks:

| Agent | Description | Usage |
|-------|-------------|-------|
| **code-reviewer** | Comprehensive code review with best practices | `/agent code-reviewer` |
| **security-reviewer** | Security vulnerability analysis | `/agent security-reviewer` |
| **test-generator** | Automatic test creation | `/agent test-generator` |
| **documentation-generator** | Generate comprehensive docs | `/agent documentation-generator` |
| **feature-creator** | Implement new features | `/agent feature-creator` |
| **tech-debt-reviewer** | Identify technical debt | `/agent tech-debt-reviewer` |
| **claude-md-generator** | Generate CLAUDE.md files | `/agent claude-md-generator` |
| **code-explorer** | Explore and understand codebases | `/agent code-explorer` |

### ⚡ Commands

Quick commands for common development tasks:

| Command | Description | Usage |
|---------|-------------|-------|
| **commit** | Smart git commits with conventional format | `/commit` |
| **review** | Quick code review | `/review` |
| **pw-test** | Run Playwright tests | `/pw-test` |
| **a11y-audit** | Accessibility audit | `/a11y-audit` |
| **gen-changelog** | Generate changelog | `/gen-changelog` |
| **product-lens** | Product perspective review | `/product-lens` |
| **optimize-doc** | Optimize documentation | `/optimize-doc` |
| **wrap-up** | Session wrap-up and notes | `/wrap-up` |
| **wt-merge** | Smart merge operations | `/wt-merge` |
| **warp** | Quick navigation | `/warp` |

### 🛠️ Skills

Advanced capabilities that Claude can use automatically:

- **a11y-audit** - Automated accessibility testing
- **gen-changelog** - Intelligent changelog generation
- **github-project-tickets** - GitHub project management
- **learn** - Learning and knowledge management
- **optimize-doc** - Document optimization
- **playwright-cli** - Playwright test automation
- **product-lens** - Product analysis
- **wrap-up** - Session management
- **wt-merge** - Advanced merge operations

## Usage Examples

### Code Review

```bash
# Quick review of current changes
/review

# Comprehensive review with security analysis
/agent security-reviewer
```

### Git Operations

```bash
# Smart commit with conventional format
/commit

# Generate changelog from commits
/gen-changelog
```

### Testing

```bash
# Run Playwright tests
/pw-test

# Generate tests for a component
/agent test-generator
```

### Documentation

```bash
# Generate project documentation
/agent documentation-generator

# Optimize existing docs
/optimize-doc
```

## Project Structure

```
tricky-cc-plugins/
├── .claude-plugin/
│   └── marketplace.json      # Plugin marketplace configuration
├── core/                     # Core plugin package
│   ├── .claude-plugin/
│   │   └── plugin.json       # Core plugin metadata
│   ├── agents/               # AI agent definitions
│   ├── commands/             # Quick command definitions
│   └── skills/               # Automated skill definitions
└── plans/                    # Project planning documents
```

## Configuration

The plugins work out of the box, but you can customize behavior through:

1. **Project-level CLAUDE.md** - Add a `CLAUDE.md` file to your project root for project-specific instructions
2. **Global settings** - Configure in `~/.claude/CLAUDE.md` for user-wide preferences

## Development

### Adding New Commands

Create a new markdown file in `core/commands/`:

```markdown
---
name: my-command
description: Does something useful
---

Instructions for Claude on how to execute this command...
```

### Adding New Agents

Create a new markdown file in `core/agents/`:

```markdown
---
name: my-agent
description: Specialized agent for X
---

You are an expert in X. Your task is to...
```

### Adding New Skills

Create a new directory in `core/skills/` with:
- `SKILL.md` - Skill definition and instructions
- `scripts/` - Supporting scripts
- `references/` - Reference documentation

## Troubleshooting

### Plugin Not Found

If you get a "plugin not found" error:
```bash
# Refresh the marketplace
claude-code marketplace refresh

# Try installing again
claude-code plugin install core
```

### Commands Not Working

Ensure Claude Code is up to date and restart the application after installation.

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Support

- **Issues**: [GitHub Issues](https://github.com/trickycdm/tricky-cc-plugins/issues)
- **Discussions**: [GitHub Discussions](https://github.com/trickycdm/tricky-cc-plugins/discussions)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Built with ❤️ for the Claude Code community by Tricky CDM.

---

*Happy coding! 🎉*