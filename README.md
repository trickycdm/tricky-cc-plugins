# Tricky CC Plugins

> Professional Claude Code plugin collection for enhanced development workflows

[![Version](https://img.shields.io/badge/version-1.0.7-blue.svg)](https://github.com/trickycdm/tricky-cc-plugins)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-purple.svg)](https://claude.ai)

## Overview

A comprehensive suite of productivity tools for Claude Code that implements a structured development workflow with intelligent automation, code review capabilities, and continuous learning mechanisms.

## Quick Start

### Installation in Claude Code

Install directly in Claude Code with these commands:

```
/plugin marketplace add trickycdm/tricky-cc-plugins
/plugin install core@tricky-cc-plugins
```

### Alternative Installation

Using the command line:

```bash
# Add the marketplace
claude marketplace add https://github.com/trickycdm/tricky-cc-plugins

# Install the core plugin
claude plugin install core
```

## Development Workflow

This plugin suite implements a 6-phase development lifecycle:

### 1. Plan → 2. Build → 3. Review → 4. Test → 5. Learn → 6. Ship

Each phase has dedicated tools that work together:

| Phase | Purpose | Key Tools |
|-------|---------|-----------|
| **Plan** | Structure complex tasks | Plan mode, auto-organized folders via hooks |
| **Build** | Implement features | Agents (feature-creator, code-explorer) |
| **Review** | Ensure quality | `/review` (multi-agent synthesis) |
| **Test** | Validate behavior | `/pw-test` (explore + generate), `/a11y-audit` |
| **Learn** | Capture patterns | `/wrap-up`, `/learn` |
| **Ship** | Deploy changes | `/commit`, `/gen-changelog` |

## Core Components

### Hooks & Automation

Built-in workflow automation:
- **Plan Organization** - Auto-organizes plans into dated, descriptive folders
- **Custom Status Line** - Enhanced display with context usage, cost, and git info

### Commands

Quick actions for common tasks:

- `/review` - Multi-agent code review (fans out to 3 specialized reviewers)
- `/commit` - Smart commits with conventional format and doc updates
- `/wrap-up` - Finalize plans and capture session outcomes
- `/learn` - Update steering documentation with lessons learned
- `/pw-test` - Exploratory testing + E2E test generation with Playwright
- `/a11y-audit` - Accessibility testing
- `/plan-status` - Review status of all active plans

[Full command list →](core/README.md#commands)

### Agents

Autonomous AI agents for complex tasks:

- **code-reviewer** - Logical bugs and conventions
- **tech-debt-reviewer** - Maintainability issues
- **security-reviewer** - Vulnerability scanning
- **test-generator** - Comprehensive test creation
- **feature-creator** - New feature implementation

[Full agent list →](core/README.md#agents)

### Skills

Automatic capabilities that activate when needed:

- **playwright-cli** - Advanced Playwright operations
- **a11y-audit** - Accessibility compliance
- **gen-changelog** - Changelog generation
- **github-project-tickets** - GitHub integration

[Full skills list →](core/README.md#skills)

## Configuration Hierarchy

Claude Code uses a cascading configuration system:

```bash
# Organization policy (managed, deployable via MDM)
/Library/Application Support/ClaudeCode/CLAUDE.md

# User defaults (your preferences, every project)
~/.claude/CLAUDE.md
~/.claude/rules/*.md

# Project configuration (team-shared, in repo)
{project}/CLAUDE.md
{project}/.claude/rules/*.md

# Directory-specific (service boundaries)
{project}/src/services/CLAUDE.md
```

Each level inherits from the one above. Keep files under ~200 lines for best adherence.

## Key Patterns

### Multi-Agent Review

The `/review` command demonstrates parallel agent execution:

```
     /review
        │
    ┌───┴───┐
    ▼   ▼   ▼
 tech  code sec
    └───┬───┘
        ▼
   Synthesized
    Feedback
```

### Knowledge Capture

The learning loop ensures continuous improvement:

1. `/wrap-up` - Finalizes the current plan
2. `/learn` - Scans for patterns and updates CLAUDE.md
3. Future sessions benefit from captured lessons

### Command Composition

Create custom commands that chain existing tools:

```markdown
# .claude/commands/ship.md
1. Run /review
2. If passing, run tests
3. Run /commit
4. Push to remote
```

## Best Practices

1. **Plan complex tasks** - Use plan mode for anything requiring 3+ steps
2. **Review before shipping** - `/review` catches issues early
3. **Capture lessons** - End sessions with `/wrap-up` and `/learn`
4. **Follow the phases** - Each phase builds on the previous
5. **Keep CLAUDE.md focused** - Under 200 lines, specific patterns only

## Project Structure

```
tricky-cc-plugins/
├── .claude-plugin/
│   └── marketplace.json      # Plugin marketplace configuration
├── core/                     # Core plugin package
│   ├── .claude-plugin/
│   │   └── plugin.json       # Plugin metadata
│   ├── agents/               # AI agent definitions
│   ├── commands/             # Quick commands
│   ├── skills/               # Automatic capabilities
│   ├── hooks/                # Hook configurations
│   │   └── hooks.json       # Hook definitions
│   ├── scripts/              # Supporting scripts
│   ├── docs/                 # Workflow documentation
│   └── README.md            # Detailed plugin documentation
└── README.md                # This file
```

## Advanced Usage

### Creating Custom Commands

Add markdown files to `core/commands/`:

```markdown
---
name: deploy
description: Deploy to production
---

Run deployment checks then push to production
```

### Adding Agents

Create specialized agents in `core/agents/`:

```markdown
---
name: api-reviewer
description: Review API design
---

You are an API design expert...
```

### Building Skills

Add directories to `core/skills/` with:
- `SKILL.md` - Skill definition
- `scripts/` - Supporting scripts
- `references/` - Documentation

## Troubleshooting

**Commands not recognized**: Ensure plugin is installed with `claude-code plugin list`

**Agents not completing**: Check Claude Code logs and verify latest version

**Skills not activating**: Be specific in requests to trigger appropriate skills

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Support

- [GitHub Issues](https://github.com/trickycdm/tricky-cc-plugins/issues)
- [Discussions](https://github.com/trickycdm/tricky-cc-plugins/discussions)

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

Built with ❤️ for the Claude Code community by Tricky CDM