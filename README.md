# Tricky CC Plugins 🚀

> Professional Claude Code plugin collection with commands, agents, and skills for enhanced development workflows

[![Version](https://img.shields.io/badge/version-1.0.7-blue.svg)](https://github.com/trickycdm/tricky-cc-plugins)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-purple.svg)](https://claude.ai)

## Overview

**Tricky CC Plugins** is a comprehensive suite of productivity tools for Claude Code that supercharges your development workflow with intelligent automation, code review capabilities, and project management features.

> *"30k lines of production code, not a line typed by hand."* - Built end-to-end with this workflow

### Key Features

- **🤖 Intelligent Agents** - Specialized AI agents for code review, security analysis, documentation generation, and more
- **⚡ Power Commands** - Streamlined commands for commits, testing, accessibility audits, and changelog generation
- **🛠️ Development Skills** - Advanced capabilities including Playwright testing, GitHub integration, and document optimization
- **📦 Easy Installation** - Single command to install the entire plugin suite
- **🔄 Compounding Workflow** - Every session sharpens the harness, building on lessons learned

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

## The Development Lifecycle

This plugin suite implements a proven 6-phase development workflow:

**Plan → Build → Review → Test → Learn → Ship**

Each phase has dedicated tools that work together to create a seamless development experience. See [WORKFLOW.md](WORKFLOW.md) for the complete lifecycle.

## Usage Examples

### Complete Feature Workflow

```bash
# Phase 1: Plan (handled in plan mode)
# Phase 2: Build (Claude writes the code)

# Phase 3: Review - Multi-agent code review
/review
# This fans out to 3 specialized agents:
# - tech-debt-reviewer (maintainability)
# - code-reviewer (logical bugs)
# - security-reviewer (attack surface)

# Phase 4: Test
/agent test-generator    # Generate unit tests
/pw-test                 # Run Playwright E2E tests

# Phase 5: Learn
/wrap-up                 # Close the plan, finalize worklog
/learn                   # Update steering docs with lessons

# Phase 6: Ship
/commit                  # Smart commit with doc updates
```

### Quick Commands

```bash
# Quick review of current changes
/review

# Smart commit with conventional format
/commit

# Generate changelog from commits
/gen-changelog
```

### Real-World Example: Skill Scan

Built entirely with this workflow - see [EXAMPLES.md](EXAMPLES.md) for detailed case studies.

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

The plugins work out of the box, but you can customize behavior through the CLAUDE.md hierarchy:

### CLAUDE.md Hierarchy

```bash
# Managed policy — deployable via MDM, org-wide
/Library/Application Support/ClaudeCode/CLAUDE.md

# User — your defaults, every project
~/.claude/CLAUDE.md              # Plan mode, subagents, verification
~/.claude/rules/*.md             # Personal cross-project rules

# Project — team-shared, in repo
{project}/CLAUDE.md              # The architecture bible
{project}/.claude/rules/*.md     # Path-scoped rules

# Directory — service boundaries
{project}/src/services/CLAUDE.md  # Directory-scoped, loads when editing inside
```

Each level inherits from the one above. Keep each file under ~200 lines for best adherence.

## Workflow Philosophy

### The Harness Concept

> **"Every session sharpens the harness."**

This isn't just a collection of tools - it's a living workflow that improves with every use:

1. **Start with CLAUDE.md** - Your steering document that guides every decision
2. **Commands become team verbs** - `/review`, `/commit`, `/deploy` standardize how your team works
3. **Lessons compound** - `/learn` captures patterns that improve future sessions
4. **Agents work together** - Complex tasks fan out to specialized sub-agents

### Best Practices

- **Plan first, code second** - Use plan mode for non-trivial tasks
- **Review always** - `/review` before every commit catches issues early
- **Learn deliberately** - End sessions with `/wrap-up` and `/learn`
- **Trust the workflow** - The 6-phase lifecycle works; don't skip steps

## Advanced Patterns

### Multi-Agent Workflows

The `/review` command demonstrates how to fan out work to specialized agents:

```markdown
# .claude/commands/review.md
Run these agents in parallel:
- tech-debt-reviewer: Check for maintainability issues
- code-reviewer: Find logical bugs and convention violations
- security-reviewer: Identify security vulnerabilities

Synthesize their outputs into a single review.
```

### Command Chaining

Commands can trigger other commands for complex workflows:

```markdown
# .claude/commands/ship.md
1. Run /review
2. If review passes, run /commit
3. Push to remote
4. Run /wrap-up
```

### Knowledge Capture

The `/learn` command updates steering docs, not code:
- Scans session for corrections and validated patterns
- Filters out one-offs with generalizability gate
- Writes only to CLAUDE.md and documentation
- Creates a feedback loop that improves future sessions

## Development

### Decision Matrix: Agent vs Command vs Skill

| Use Case | Choose | Example |
|----------|--------|---------|
| Complex multi-step task | Agent | `code-reviewer`, `feature-creator` |
| Quick single action | Command | `/commit`, `/review` |
| Automatic capability | Skill | `a11y-audit`, `playwright-cli` |
| Team-specific workflow | Command | `/deploy`, `/ship` |

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

## Learn More

- [WORKFLOW.md](WORKFLOW.md) - The complete 6-phase development lifecycle
- [EXAMPLES.md](EXAMPLES.md) - Real-world case studies and patterns
- [Core Plugin README](core/README.md) - Detailed documentation for all tools

## Acknowledgments

Built with ❤️ for the Claude Code community by Tricky CDM.

---

*Happy coding! 🎉*