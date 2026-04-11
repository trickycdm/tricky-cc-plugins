# Plan: Convert gen-changelog Command to Skill

## Context

The `gen-changelog` command is currently a full procedural command hardcoded to a specific workspace (luupdin) with a single comparison mode (HEAD vs latest `v*` tag). The user wants to:
1. Extract the logic into a **general-purpose skill** that handles multiple changelog generation modes
2. Make the existing command a **thin wrapper** that invokes the skill
3. Improve the content — the current version is too narrow

## Files to Create/Modify

| File | Action |
|------|--------|
| `core/skills/gen-changelog/SKILL.md` | **Create** — the new skill |
| `core/commands/gen-changelog.md` | **Modify** — replace with thin wrapper |
| `core/skills/gen-changelog/evals/trigger-evals.json` | **Create** — trigger evaluation cases |

## Step 1: Create `core/skills/gen-changelog/SKILL.md`

The skill supports 5 comparison modes, auto-detected from user input:

| Mode | Trigger | Resolved as |
|------|---------|-------------|
| **Unreleased** (default) | No args, or "what's unreleased" | HEAD vs latest tag |
| **Tag-to-tag** | Two tags mentioned | Older tag vs newer tag |
| **Since tag** | "since v1.5.0" | Specific tag vs HEAD |
| **Staging vs prod** | "staging", "rc", "preview vs prod" | Latest pre-release tag vs latest release tag |
| **Custom range** | Git range syntax `abc..def` | Passed through directly |

Key design decisions:
- **Auto-detect tag patterns** — don't hardcode `v*`; examine existing tags to infer naming convention
- **No repo/workspace hardcoding** — works in any git repo
- **Breaking changes surfaced first** — regardless of commit prefix
- **Display first, write second** — show changelog, then ask about file output
- **Graceful fallback** — repos without conventional commits get everything under "Other"
- **Monorepo awareness** — detect and offer per-package breakdown if applicable
- **Parallel git commands** in context-gathering step for efficiency

Structure of SKILL.md:
1. Frontmatter (name, description, user-invocable: true)
2. Overview with mode table
3. Step 0: Gather repo context (parallel git commands)
4. Step 1: Determine comparison mode
5. Step 2: Resolve BASE and HEAD refs
6. Step 3: Extract and categorize commits
7. Step 4: Generate output
8. Edge cases section
9. Rules

## Step 2: Update `core/commands/gen-changelog.md`

Replace with thin wrapper following the `pw-test.md` pattern:
```yaml
---
description: Create a changelog by comparing git refs.
---

Use the gen-changelog skill to generate a changelog. If invoked without 
arguments, compare HEAD against the latest tag. Otherwise follow the 
user's instructions for which refs to compare.
```

## Step 3: Create `core/skills/gen-changelog/evals/trigger-evals.json`

~20 entries (10 should_trigger: true, 10 false) covering:
- **True**: "gen changelog", "what's unreleased", "compare tags", "release notes", "what changed since v2.0", "staging vs prod changelog"
- **False**: "write a commit message", "summarize git log", "create a release tag", "review this PR", "deploy to production"

## Verification

1. Check skill is discoverable: confirm `gen-changelog` appears in the skill listing after plugin reload
2. Read through SKILL.md to verify all 5 modes are clearly documented with git commands
3. Verify the command wrapper references the skill correctly
4. Confirm evals cover the key positive/negative trigger cases
