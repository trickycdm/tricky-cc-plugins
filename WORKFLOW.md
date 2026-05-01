# The 6-Phase Development Workflow

> *"Every session sharpens the harness."*

This document describes the battle-tested development lifecycle that has shipped 30k+ lines of production code without typing a single line by hand.

## Overview

The workflow consists of six distinct phases, each with specific tools and practices:

```
┌──────┐    ┌───────┐    ┌────────┐    ┌──────┐    ┌───────┐    ┌──────┐
│ PLAN │ -> │ BUILD │ -> │ REVIEW │ -> │ TEST │ -> │ LEARN │ -> │ SHIP │
└──────┘    └───────┘    └────────┘    └──────┘    └───────┘    └──────┘
```

Each phase builds on the previous one, creating a compounding effect where every session improves the next.

## Phase 1: Plan

### When to Enter Plan Mode

- Any task requiring 3+ steps
- Architectural decisions
- Complex refactoring
- Feature implementation

### Plan Structure

Plans live in `plans/` directory with this structure:

```
plans/
└── 2024-01-15-feature-name/
    ├── plan.md         # The implementation plan
    └── worklog.md      # Execution log
```

### Plan Contents

A good plan includes:
- **Context**: Why this work is needed
- **Success Criteria**: What "done" looks like
- **Implementation Steps**: Numbered, specific actions
- **Verification**: How to validate success

### Example Plan

```markdown
# Add User Authentication

## Context
The application needs user authentication to secure admin routes.

## Success Criteria
- [ ] Users can register and login
- [ ] Protected routes require authentication
- [ ] Sessions persist across restarts
- [ ] All tests pass

## Implementation Steps
1. Add auth database schema
2. Implement registration endpoint
3. Implement login endpoint
4. Add session middleware
5. Protect admin routes
6. Add auth UI components
7. Write integration tests

## Verification
- Manual testing of auth flow
- All existing tests still pass
- New auth tests pass
```

## Phase 2: Build

### Following the Plan

Claude executes the plan step by step, guided by your CLAUDE.md hierarchy:

```bash
# The guidance cascade:
/Library/Application Support/ClaudeCode/CLAUDE.md  # Org policy
~/.claude/CLAUDE.md                                 # User defaults
{project}/CLAUDE.md                                 # Project architecture
{project}/src/services/CLAUDE.md                   # Service boundaries
```

### Building with Agents

For complex implementations, use specialized agents:

```bash
/agent feature-creator     # Implements new features
/agent code-explorer      # Understands existing code first
```

### Tracking Progress

Update the worklog as you complete steps:

```markdown
| Timestamp | Action | Details |
|-----------|--------|---------|
| 09:15 | START | Beginning auth implementation |
| 09:30 | COMPLETE | Added database schema |
| 09:45 | BLOCKED | Need to clarify session storage approach |
| 10:00 | RE-PLAN | Switching to JWT from sessions |
```

## Phase 3: Review

### The Multi-Agent Review Pattern

The `/review` command orchestrates three specialized agents:

```
           /review
              │
    ┌─────────┴─────────┐
    ▼         ▼         ▼
tech-debt  code     security
reviewer   reviewer  reviewer
    │         │         │
    └─────────┬─────────┘
              ▼
         Synthesized
          Feedback
```

### What Each Reviewer Checks

**tech-debt-reviewer**:
- Dead code
- Duplicated logic
- Outdated patterns
- Architecture smells

**code-reviewer**:
- Edge cases
- Missed invariants
- Wrong assumptions
- Convention violations

**security-reviewer**:
- OWASP Top 10
- Injection vulnerabilities
- Unsafe crypto
- Exposed secrets

### Acting on Review Feedback

```bash
/review
# Read feedback carefully
# Fix identified issues
/review  # Run again to verify fixes
```

## Phase 4: Test

### Two-Layer Testing Strategy

**Unit Tests** (via test-generator agent):
```bash
/agent test-generator
# Generates tests for:
# - Individual functions
# - Component behavior
# - Edge cases
# - Error conditions
```

**E2E Tests** (via playwright-cli skill):
```bash
/pw-test
# Tests:
# - User workflows
# - Integration points
# - Accessibility
# - Performance
```

### Test-Driven Fixes

When tests fail:
1. Read the error carefully
2. Fix the root cause (not symptoms)
3. Re-run to verify
4. Add regression tests

### Accessibility Testing

```bash
/a11y-audit
# Checks:
# - WCAG compliance
# - Keyboard navigation
# - Screen reader support
# - Color contrast
```

## Phase 5: Learn

### Capturing Lessons

The learn phase creates a feedback loop that improves future sessions.

### /wrap-up Command

Finalizes the current plan:
- Marks all steps complete
- Stamps completion time
- Archives the plan folder

```bash
/wrap-up
# Updates plan.md with:
# - [✓] markers on completed steps
# - Completion timestamp
# - Final status
```

### /learn Command

Updates steering documentation:
- Scans session for corrections
- Identifies validated patterns
- Filters out one-offs
- Updates CLAUDE.md files

```bash
/learn
# Looks for:
# - User corrections
# - Successful patterns
# - Failed approaches
# - Generalizable lessons
```

### What Gets Captured

Good lessons are:
- **Specific**: "Use Repository pattern for data access"
- **Actionable**: "Check for null before accessing properties"
- **Generalizable**: Applies to future work
- **Validated**: Proven to work in practice

## Phase 6: Ship

### Smart Commits

The `/commit` command does more than just commit:

1. **Checks Documentation**: Updates CLAUDE.md if needed
2. **Atomic Changes**: Code + docs in one commit
3. **Conventional Format**: Follows Angular conventions
4. **Meaningful Messages**: Becomes your changelog

### Commit Message Format

```
type(scope): subject

body

footer
```

Examples:
```bash
feat(auth): add user registration endpoint

- Add POST /api/register endpoint
- Validate email and password
- Hash passwords with bcrypt
- Return JWT token

Closes #123
```

### From Commits to Changelog

```bash
/gen-changelog
# Generates from commit history:
# - Groups by type (feat, fix, etc.)
# - Includes breaking changes
# - Ready for release notes
```

## Workflow Patterns

### Pattern: Morning Startup

```bash
# 1. Read yesterday's wrap-up
cat plans/*/worklog.md | tail -20

# 2. Check failing tests
npm test

# 3. Review pending work
git status

# 4. Enter plan mode for today's work
```

### Pattern: Feature Development

```bash
# 1. Plan
# Enter plan mode, create structured plan

# 2. Build
/agent feature-creator

# 3. Review
/review

# 4. Test
/agent test-generator
/pw-test

# 5. Learn
/wrap-up
/learn

# 6. Ship
/commit
git push
```

### Pattern: Bug Fix

```bash
# 1. Reproduce
# Create failing test that demonstrates bug

# 2. Fix
# Make minimal change to pass test

# 3. Review
/review

# 4. Verify
# Run all tests

# 5. Ship
/commit
```

### Pattern: Refactoring

```bash
# 1. Establish baseline
/agent test-generator  # If tests don't exist

# 2. Plan refactor
# Enter plan mode

# 3. Refactor incrementally
# Small changes, test after each

# 4. Review for tech debt
/agent tech-debt-reviewer

# 5. Document changes
/learn

# 6. Ship
/commit
```

## The Compounding Effect

### How the Harness Sharpens

Each session improves the next through:

1. **CLAUDE.md Evolution**: Lessons become rules
2. **Command Refinement**: Commands encode best practices
3. **Pattern Recognition**: Common workflows become commands
4. **Team Alignment**: Shared commands create shared understanding

### Building Your Own Harness

Start simple and layer complexity:

```
Week 1: Basic CLAUDE.md + /commit
Week 2: Add /review command
Week 3: Add test-generator agent
Week 4: Add /learn for knowledge capture
...gradually add what provides value
```

### Measuring Improvement

Track these metrics:
- **Defect Rate**: Should decrease over time
- **Review Iterations**: Fewer rounds needed
- **Session Velocity**: More shipped per session
- **Pattern Reuse**: Less repeated mistakes

## Common Pitfalls

### Pitfall 1: Skipping Plan Phase

**Problem**: Jumping straight into code for complex tasks
**Result**: Rework, missed requirements, architectural issues
**Solution**: Use plan mode for anything 3+ steps

### Pitfall 2: Ignoring Review Feedback

**Problem**: Dismissing review comments as "false positives"
**Result**: Tech debt accumulation, security issues
**Solution**: Fix or explicitly document why not

### Pitfall 3: Not Capturing Lessons

**Problem**: Ending sessions without /learn
**Result**: Repeating same mistakes
**Solution**: Always /wrap-up and /learn

### Pitfall 4: Weak Commits

**Problem**: Generic commit messages like "fix bugs"
**Result**: Useless git history, poor changelog
**Solution**: Use /commit for structured messages

## Advanced Workflows

### Parallel Development

Run multiple agents simultaneously:

```bash
# In parallel:
/agent test-generator     # Generate tests
/agent documentation-generator  # Update docs
/review                  # Review current changes
```

### Cross-Service Changes

When changes span multiple services:

1. Plan at repository root level
2. Update each service's CLAUDE.md
3. Test integration points explicitly
4. Commit atomically

### Performance Optimization

```bash
# 1. Baseline
/agent test-generator  # Create performance tests

# 2. Profile
# Identify bottlenecks

# 3. Optimize
# Make targeted improvements

# 4. Verify
# Re-run performance tests

# 5. Document
/learn  # Capture optimization patterns
```

## Customization

### Creating Custom Commands

Commands that fit your workflow:

```markdown
# .claude/commands/ship.md
---
name: ship
description: Complete shipping workflow
---

1. Run /review
2. If review passes, run tests
3. If tests pass, run /commit
4. Push to remote
5. Run /wrap-up
```

### Team-Specific Agents

Agents for your domain:

```markdown
# .claude/agents/api-designer.md
---
name: api-designer
description: Design RESTful APIs
---

You are an API design expert. Follow these principles:
- RESTful conventions
- Consistent naming
- Proper status codes
- HATEOAS where appropriate
...
```

### Workflow Automation

Hook into the workflow:

```bash
# .claude/hooks/post-commit.sh
#!/bin/bash
# Auto-push after successful commit
git push origin main
```

## Conclusion

This workflow isn't about the specific tools—it's about the discipline of systematic improvement. Every session should leave your codebase and your process better than you found them.

Remember:
- **Plan before you build**
- **Review before you ship**
- **Learn from every session**
- **Let the harness sharpen**

The tools will evolve, but the workflow endures. Start with what provides immediate value, then layer in complexity as your needs grow.

*"Every session sharpens the harness. Make tomorrow's you grateful for today's discipline."*