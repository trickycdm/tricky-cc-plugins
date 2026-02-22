---
name: github-project-tickets
description: Create and manage GitHub Project issues retrospectively using the GitHub CLI (gh). Use this skill whenever the user wants to push completed work to a GitHub Project board, create issues from git commit history, generate tickets from documentation or specs, add done work to a GitHub project after the fact, or retrospectively document engineering work as GitHub issues. Triggers on phrases like "add to the project", "create tickets from my commits", "push to github project", "retrospectively log this work", "create issues from git log", "document this work as tickets", "add these to the board", or any request to bridge completed work into a GitHub Project. Also triggers when the user pastes or references a document and wants tickets created from it.
---

# GitHub Project Tickets Skill

Creates GitHub Project issues retrospectively from two sources:
- **Git log** — clusters related commits into coherent, meaningful tickets
- **Documentation** — a file path passed by the user, or content already pasted in the conversation

Uses the `gh` CLI. Designed for Claude Code where you have full shell access.

## Prerequisites

```bash
gh auth status                       # must be authenticated
gh project list --owner <owner>      # find your project number
```

If `gh` isn't installed: `brew install gh` or https://cli.github.com

---

## Step 1: Establish Context

Detect what you can automatically, confirm the rest:

```bash
# Detect repo from current directory
git remote get-url origin

# List available projects
gh project list --owner <owner>
```

You need:
- **Repo** — infer from `git remote get-url origin`, strip to `owner/repo` format
- **Owner** — org or personal account (from the remote URL)
- **Project number** — list with `gh project list` if not specified
- **Source** — git log, a file path, or doc content already in the conversation

Only ask for what you can't infer.

---

## Step 2: Extract Work

### From Git Log

Fetch commits across a meaningful range, then cluster into logical units of work. One ticket per commit creates noise — aim for coherent features, fixes, or changes:

```bash
# Default: last 50 non-merge commits
git log --pretty=format:"%h %ad %s" --date=short --no-merges -n 50

# Since a specific date
git log --oneline --no-merges --since="2025-01-01"

# Between branches
git log main..HEAD --oneline --no-merges

# See which files changed — helps with grouping
git log --stat --no-merges -n 30
```

**Clustering strategy**: Group commits by theme using message text, file paths touched, and timestamps. A good ticket typically spans 1–10 related commits. Don't force unrelated changes into one ticket just to reduce count.

### From a File Path

If the user passes a path:

```bash
cat /path/to/spec.md
```

Read it and extract distinct pieces of completed or planned work — features, tasks, changes described in the doc.

### From Document in Context

If the user says "use the doc above" or has pasted content into the chat — use that directly. No file read needed. Extract the same way.

---

## Step 3: Draft Tickets

For each logical unit of work, produce a structured issue draft:

```
**Title**: [Action verb] + [what was done]
Good examples: "Add rate limiting to API endpoints", "Refactor auth middleware", "Fix memory leak in job queue"

**Body**:
## What was done
[2–4 sentences describing the change clearly]

## Why
[Brief rationale — infer from commit messages or doc context]

## Commits / References
- `abc1234` – commit message
- `def5678` – commit message
(omit this section if the source was a document)

## Notes
[Follow-ups, caveats, or anything worth capturing]
```

**Before creating anything**, present all drafted tickets to the user as a numbered list with title + body preview. Ask:

- Does this breakdown look right? Anything to rename, merge, or split?
- Any labels to add? (suggest from: `enhancement`, `bug`, `chore`, `docs`, `retrospective`)
- Should these be assigned to anyone?
- What status should they land at on the board? (e.g. Done, Closed, Backlog)

---

## Step 4: Create Issues and Add to Project

Once the user approves, create each issue and immediately add it to the project board:

```bash
# Create the issue — capture the URL from stdout
ISSUE_URL=$(gh issue create \
  --repo owner/repo \
  --title "Your title" \
  --body "Your body" \
  --label "enhancement" \
  2>&1 | grep "https://")

# Add to the project board
gh project item-add <project-number> \
  --owner <owner> \
  --url "$ISSUE_URL"
```

### Setting Status on the Board

To mark issues as "Done" (or any other status) after adding them:

```bash
# 1. Fetch field IDs — do this once per session, cache the result
gh project field-list <project-number> --owner <owner> --format json

# 2. Get item IDs for newly added issues
gh project item-list <project-number> --owner <owner> --format json

# 3. Update the status field
gh project item-edit \
  --project-id <project-id> \
  --id <item-id> \
  --field-id <status-field-id> \
  --single-select-option-id <done-option-id>
```

Fetch field and option IDs once, then reuse across all issues in the session.

---

## Step 5: Confirm

Report back with links to everything created:

```
✅ Created 4 issues and added to Project #5:

1. #42 – Add OAuth authentication
   https://github.com/org/repo/issues/42

2. #43 – Refactor database connection pooling
   https://github.com/org/repo/issues/43

3. #44 – Implement rate limiting middleware
   https://github.com/org/repo/issues/44

4. #45 – Update deployment pipeline for staging
   https://github.com/org/repo/issues/45

All marked as Done on the board.
```

---

## Quick Reference

| Task | Command |
|---|---|
| List projects | `gh project list --owner <owner>` |
| List project items | `gh project item-list <num> --owner <owner>` |
| View project fields | `gh project field-list <num> --owner <owner>` |
| Add label to issue | `gh issue edit <num> --add-label "chore"` |
| View issue | `gh issue view <num>` |

### Suggested Labels for Retrospective Work
- `retrospective` — logged after the fact
- `done` — already completed  
- `enhancement`, `bug`, `chore`, `docs` — standard categorisation

---

## Error Handling

| Error | Fix |
|---|---|
| `gh: command not found` | `brew install gh` or https://cli.github.com |
| `Not authenticated` | `gh auth login` |
| `Project not found` | `gh project list --owner <owner>` to find the right number |
| `Resource not accessible` | Check repo write access and `--owner` flag |
| Issue URL not captured | Run `gh project item-add` manually with the issue URL |
| Status field not updating | Fetch correct IDs with `gh project field-list --format json` |
