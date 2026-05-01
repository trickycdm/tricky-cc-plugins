# Core Plugin for Claude Code 🎯

> Essential utilities, agents, commands, and skills for enhanced Claude Code development workflows

## Overview

The **Core Plugin** is the foundational plugin that provides a comprehensive set of tools to supercharge your Claude Code experience. It includes intelligent agents for code review and analysis, streamlined commands for common tasks, and advanced skills for automation.

> **Philosophy**: These aren't just tools - they're team verbs. `/review`, `/commit`, and `/deploy` become the shared language of how your team ships code.

## Features

### 🤖 Intelligent Agents

Advanced AI agents that autonomously handle complex development tasks:

- **code-reviewer** - Performs thorough code reviews with actionable feedback
- **security-reviewer** - Identifies security vulnerabilities and suggests fixes
- **test-generator** - Automatically generates comprehensive test suites
- **documentation-generator** - Creates detailed documentation for your codebase
- **feature-creator** - Implements new features following best practices
- **tech-debt-reviewer** - Analyzes and reports on technical debt
- **claude-md-generator** - Generates project-specific CLAUDE.md configuration files
- **code-explorer** - Helps understand and navigate complex codebases

### ⚡ Quick Commands

Streamlined commands for everyday development tasks:

- **commit** - Smart git commits with conventional commit format
- **review** - Quick code review for current changes
- **pw-test** - Execute Playwright tests
- **a11y-audit** - Run accessibility audits
- **gen-changelog** - Generate changelogs from git history
- **product-lens** - Review from a product perspective
- **optimize-doc** - Optimize documentation files
- **wrap-up** - Create session summaries and capture lessons learned
- **wt-merge** - Smart merge operations
- **warp** - Quick navigation helper

### 🛠️ Development Skills

Automated capabilities that Claude can invoke when needed:

- **a11y-audit** - Automated accessibility testing and reporting
- **gen-changelog** - Intelligent changelog generation from commits
- **github-project-tickets** - GitHub project and issue management
- **learn** - Learning system for capturing and applying lessons
- **optimize-doc** - Document optimization and improvement
- **playwright-cli** - Playwright test automation and management
- **product-lens** - Product-focused analysis and recommendations
- **wrap-up** - Session management and knowledge capture
- **wt-merge** - Advanced git merge operations

## Installation

This plugin is installed as part of the Tricky CC Plugins suite:

```bash
# Add the marketplace (if not already added)
claude-code marketplace add https://github.com/trickycdm/tricky-cc-plugins

# Install the core plugin
claude-code plugin install core
```

## The 6-Phase Development Workflow

This plugin implements a battle-tested development lifecycle:

### Phase 1: Plan
- Use Claude's plan mode for non-trivial tasks
- Create structured plans in `plans/` directory
- Break down complex features into manageable steps

### Phase 2: Build
- Claude writes the code following your CLAUDE.md
- Agents handle complex implementations
- Skills provide automatic capabilities

### Phase 3: Review
```bash
/review  # Fans out to 3 specialized agents
```
The review command orchestrates:
- **tech-debt-reviewer** - Maintainability and code smells
- **code-reviewer** - Logic bugs and convention violations
- **security-reviewer** - OWASP vulnerabilities and secrets

### Phase 4: Test
```bash
/agent test-generator    # Unit tests
/pw-test                 # E2E tests
/a11y-audit             # Accessibility
```

### Phase 5: Learn
```bash
/wrap-up    # Close plan, finalize worklog
/learn      # Update steering docs with lessons
```

### Phase 6: Ship
```bash
/commit     # Smart commit with doc updates
```

## Usage

### Complete Feature Example

Here's how the tools work together in practice:

```bash
# Start with plan mode
# Claude creates plan in plans/ directory

# Build phase - Claude writes code

# Review phase - comprehensive analysis
/review
# Output: Synthesized feedback from 3 agents

# Test phase - multi-layer validation
/agent test-generator
/pw-test

# Learn phase - capture knowledge
/wrap-up
/learn

# Ship phase
/commit
```

### Using Agents

Agents handle complex, multi-step tasks autonomously:

```bash
# Perform a comprehensive code review
/agent code-reviewer

# Generate tests for your code
/agent test-generator

# Analyze security vulnerabilities
/agent security-reviewer
```

### Using Commands

Commands provide quick access to common tasks:

```bash
# Create a smart commit
/commit

# Run accessibility audit
/a11y-audit

# Generate changelog
/gen-changelog
```

### Skills (Automatic)

Skills are automatically invoked by Claude when appropriate. For example:
- When you ask to "optimize this documentation", the `optimize-doc` skill activates
- When you request "wrap up this session", the `wrap-up` skill handles it
- When you need accessibility testing, the `a11y-audit` skill runs automatically

## Directory Structure

```
core/
├── .claude-plugin/
│   └── plugin.json          # Plugin configuration
├── agents/                  # Agent definitions
│   ├── code-reviewer.md
│   ├── security-reviewer.md
│   ├── test-generator.md
│   └── ...
├── commands/                # Command definitions
│   ├── commit.md
│   ├── review.md
│   ├── pw-test.md
│   └── ...
└── skills/                  # Skill definitions
    ├── a11y-audit/
    ├── gen-changelog/
    ├── playwright-cli/
    └── ...
```

## Configuration

### Plugin Metadata

The plugin is configured via `.claude-plugin/plugin.json`:

```json
{
    "name": "core",
    "description": "Core utils for working with Claude Code",
    "version": "2.0.1",
    "author": {
        "name": "Col Mack"
    }
}
```

### Customization

You can customize plugin behavior by:

1. **Project-level configuration** - Add a `CLAUDE.md` file to your project root
2. **Global configuration** - Update `~/.claude/CLAUDE.md` for user-wide settings

## Advanced Patterns

### Multi-Agent Orchestration

The `/review` command demonstrates parallel agent execution:

```markdown
# How /review works internally:
1. Reads staged diff
2. Fans out to 3 agents in parallel:
   - tech-debt-reviewer
   - code-reviewer
   - security-reviewer
3. Each agent analyzes independently
4. Main agent synthesizes results
5. Returns unified review
```

### Command Composition

Commands can trigger other commands:

```bash
# The /commit command:
1. Checks if CLAUDE.md needs updating
2. Commits code + docs atomically
3. Formats with Angular conventions
```

### Knowledge Management

The `/learn` command creates a feedback loop:

```bash
/learn
# Scans session for:
# - Corrections from user
# - Validated patterns
# - Generalizable lessons
# Updates CLAUDE.md, not code
```

## Examples

### Example: Complete Code Review Workflow

```bash
# 1. Quick review of changes
/review

# 2. Deep security analysis
/agent security-reviewer

# 3. Generate tests for new code
/agent test-generator

# 4. Commit with conventional format
/commit
```

### Example: Documentation Workflow

```bash
# 1. Generate initial documentation
/agent documentation-generator

# 2. Optimize the generated docs
/optimize-doc

# 3. Generate changelog
/gen-changelog
```

### Example: Accessibility Testing

```bash
# Run comprehensive accessibility audit
/a11y-audit

# The skill will automatically:
# - Scan your application
# - Generate detailed reports
# - Suggest WCAG-compliant fixes
```

### Example: Session Wrap-up

```bash
# End of session routine
/wrap-up    # Finalizes plan, stamps completion
/learn      # Captures lessons for next time
```

## Best Practices

1. **Use agents for complex tasks** - Let agents handle multi-step operations
2. **Use commands for quick actions** - Commands are optimized for speed
3. **Trust automatic skills** - Claude will invoke skills when appropriate
4. **Combine tools** - Chain agents and commands for comprehensive workflows
5. **Review agent output** - Always review generated code and documentation
6. **Follow the workflow** - Plan → Build → Review → Test → Learn → Ship
7. **Capture lessons** - End every session with `/wrap-up` and `/learn`
8. **Let commands become verbs** - Standardize team workflows around commands

## Troubleshooting

### Commands not recognized

Ensure the plugin is properly installed:
```bash
claude-code plugin list
```

### Agent not completing tasks

Check Claude Code logs and ensure you have the latest version of both Claude Code and the plugin.

### Skills not activating

Skills activate automatically based on context. Be specific in your requests to trigger the appropriate skill.

## Updates

The plugin is regularly updated with new features and improvements. To update:

```bash
# Update the plugin
claude-code plugin update core

# Or reinstall
claude-code plugin uninstall core
claude-code plugin install core
```

## Contributing

Contributions are welcome! To add new capabilities:

1. **New Agents** - Add `.md` file to `agents/` directory
2. **New Commands** - Add `.md` file to `commands/` directory
3. **New Skills** - Create directory structure in `skills/`

See the main repository README for detailed contribution guidelines.

## Support

For issues, feature requests, or questions:
- Open an issue on [GitHub](https://github.com/trickycdm/tricky-cc-plugins/issues)
- Check existing [Discussions](https://github.com/trickycdm/tricky-cc-plugins/discussions)

## License

This plugin is part of the Tricky CC Plugins suite and is licensed under the MIT License.

---

Built with ❤️ by Tricky CDM for the Claude Code community