# Core Plugin for Claude Code

> Essential utilities, agents, commands, and skills for enhanced Claude Code development workflows

## Overview

The Core Plugin provides a comprehensive set of tools to supercharge your Claude Code experience. It includes intelligent agents for code review and analysis, streamlined commands for common tasks, and advanced skills for automation.

## Installation

```bash
# Add the marketplace (if not already added)
claude-code marketplace add https://github.com/trickycdm/tricky-cc-plugins

# Install the core plugin
claude-code plugin install core
```

## Components

### 🪝 Hooks

Automated workflow enhancements:

- **Plan Organization** - Automatically organizes plan files into dated, descriptive folders
- **Custom Status Line** - Enhanced status display with model, context usage, cost, and git info

See [hooks/README.md](hooks/README.md) for configuration details.

### 🤖 Agents

Advanced AI agents that autonomously handle complex development tasks:

| Agent | Description | Usage |
|-------|-------------|-------|
| **code-reviewer** | Thorough code reviews with actionable feedback | `/agent code-reviewer` |
| **security-reviewer** | Security vulnerability identification | `/agent security-reviewer` |
| **tech-debt-reviewer** | Technical debt and maintainability analysis | `/agent tech-debt-reviewer` |
| **test-generator** | Comprehensive test suite generation | `/agent test-generator` |
| **documentation-generator** | Detailed documentation creation | `/agent documentation-generator` |
| **feature-creator** | New feature implementation | `/agent feature-creator` |
| **claude-md-generator** | CLAUDE.md configuration generation | `/agent claude-md-generator` |
| **code-explorer** | Codebase understanding and navigation | `/agent code-explorer` |

### ⚡ Commands

Quick commands for everyday development tasks:

| Command | Description | Usage |
|---------|-------------|-------|
| **commit** | Smart git commits with conventional format | `/commit` |
| **review** | Multi-agent code review synthesis | `/review` |
| **pw-test** | Execute Playwright tests | `/pw-test` |
| **a11y-audit** | Run accessibility audits | `/a11y-audit` |
| **gen-changelog** | Generate changelogs from git history | `/gen-changelog` |
| **product-lens** | Product perspective review | `/product-lens` |
| **optimize-doc** | Optimize documentation files | `/optimize-doc` |
| **wrap-up** | Finalize plans and capture sessions | `/wrap-up` |
| **wt-merge** | Smart merge operations | `/wt-merge` |
| **warp** | Quick navigation helper | `/warp` |

### 🛠️ Skills

Automated capabilities that Claude invokes when needed:

| Skill | Description | Activation |
|-------|-------------|------------|
| **a11y-audit** | Accessibility testing and reporting | When accessibility checking is needed |
| **gen-changelog** | Changelog generation from commits | When creating release notes |
| **github-project-tickets** | GitHub project management | When working with GitHub issues |
| **learn** | Knowledge capture and application | When updating steering docs |
| **optimize-doc** | Document optimization | When improving documentation |
| **playwright-cli** | Playwright test automation | When running E2E tests |
| **product-lens** | Product-focused analysis | When reviewing from user perspective |
| **wrap-up** | Session management | When concluding work sessions |
| **wt-merge** | Advanced git operations | When handling complex merges |

## Key Features

### Multi-Agent Review System

The `/review` command orchestrates three specialized agents in parallel:

- **tech-debt-reviewer**: Identifies maintainability issues, dead code, duplication
- **code-reviewer**: Finds logical bugs, edge cases, convention violations
- **security-reviewer**: Detects vulnerabilities, unsafe patterns, exposed secrets

Results are synthesized into a single, actionable review.

### Smart Commit System

The `/commit` command:
1. Checks if CLAUDE.md files need updating
2. Creates atomic commits with code and documentation
3. Formats messages using Angular conventions
4. Prepares content for changelog generation

### Knowledge Management

The learning system captures and applies patterns:
- `/wrap-up`: Finalizes plans, marks completion, archives work
- `/learn`: Extracts patterns from sessions and updates CLAUDE.md

## Usage Examples

### Complete Feature Development

```bash
# Plan phase (use Claude's plan mode)

# Build phase
/agent feature-creator

# Review phase
/review

# Test phase
/agent test-generator
/pw-test

# Learn phase
/wrap-up
/learn

# Ship phase
/commit
```

### Quick Code Review

```bash
# For current staged changes
/review

# For security-focused review
/agent security-reviewer
```

### Documentation Workflow

```bash
# Generate initial docs
/agent documentation-generator

# Optimize generated docs
/optimize-doc

# Create changelog
/gen-changelog
```

## Configuration

### Plugin Structure

```
core/
├── .claude-plugin/
│   └── plugin.json          # Plugin configuration
├── agents/                  # Agent definitions
│   ├── code-reviewer.md
│   ├── security-reviewer.md
│   └── ...
├── commands/                # Command definitions
│   ├── commit.md
│   ├── review.md
│   └── ...
├── skills/                  # Skill definitions
│   ├── a11y-audit/
│   ├── gen-changelog/
│   └── ...
├── hooks/                   # Hook configurations
│   ├── hooks.json          # Hook definitions
│   └── README.md           # Hook documentation
└── scripts/                 # Supporting scripts
    ├── rename-plan.sh      # Plan organization
    └── statusline.sh       # Custom status line
```

### Customization

Extend the plugin by adding:
- **New Agents**: Add `.md` files to `agents/`
- **New Commands**: Add `.md` files to `commands/`
- **New Skills**: Create directories with `SKILL.md` in `skills/`

## Best Practices

1. **Use agents for complex tasks** - Multi-step operations benefit from agent autonomy
2. **Use commands for quick actions** - Optimized for speed and specific outcomes
3. **Trust automatic skills** - Claude activates them when appropriate
4. **Chain tools together** - Commands and agents work well in combination
5. **Review before shipping** - Always run `/review` before `/commit`
6. **Capture knowledge** - End sessions with `/wrap-up` and `/learn`

## Troubleshooting

**Commands not recognized**
- Verify installation: `claude-code plugin list`
- Restart Claude Code after installation

**Agent not completing**
- Check Claude Code logs for errors
- Ensure you have the latest version

**Skills not activating**
- Be specific in your requests
- Check skill descriptions for trigger patterns

## Updates

```bash
# Update the plugin
claude-code plugin update core

# Or reinstall
claude-code plugin uninstall core
claude-code plugin install core
```

## Contributing

To contribute new capabilities:

1. **Agents**: Add markdown file with clear instructions to `agents/`
2. **Commands**: Add markdown file with specific actions to `commands/`
3. **Skills**: Create directory with SKILL.md and supporting files in `skills/`

Follow existing patterns and test thoroughly before submitting.

## Support

- Report issues: [GitHub Issues](https://github.com/trickycdm/tricky-cc-plugins/issues)
- Discuss features: [GitHub Discussions](https://github.com/trickycdm/tricky-cc-plugins/discussions)

## License

MIT License - Part of the Tricky CC Plugins suite

---

Built with ❤️ by Tricky CDM for the Claude Code community