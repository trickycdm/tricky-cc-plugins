---
name: gen-changelog
description: "Generate a changelog from git history. Compares tags, branches, or commits to produce a categorized, human-readable changelog. Handles multiple scenarios: what's unreleased on HEAD vs latest tag, tag-to-tag comparisons, staging/RC vs production, or any custom git range. Invoke with /gen-changelog or trigger naturally with phrases like 'what changed since v2.0', 'release notes', 'compare staging to prod', 'what's unreleased'."
user-invocable: true
---

# Generate Changelog

Generate a categorized changelog by comparing two points in git history. Works in any repo with any tag naming convention.

## Comparison Modes

| Mode | When to use | Example invocation |
|------|------------|-------------------|
| **Unreleased** (default) | What's on HEAD but not yet tagged | `/gen-changelog` |
| **Tag-to-tag** | Compare two specific releases | `changelog v2.1.0 vs v2.0.0` |
| **Since tag** | Everything since a known release | `what changed since v1.5.0` |
| **Staging vs prod** | Pre-release tags against release tags | `changelog staging vs prod` |
| **Custom range** | Any two git refs | `changelog abc123..def456` |

## Step 0: Gather Repo Context

Run these commands in parallel to understand the repo:

```bash
git rev-parse --show-toplevel
git tag -l --sort=-v:refname | head -30
git branch --show-current
git rev-parse --short HEAD
git status --porcelain | head -5
```

From the output:
1. **Identify the tag naming pattern.** Look at the existing tags — they might be `v*` (semver), `rc-*`, CalVer (`2024.01.15`), or something custom. Don't assume any pattern.
2. **Separate release tags from pre-release tags.** Tags containing `-rc`, `-beta`, `-alpha`, `rc-`, or `staging-` are pre-release. Everything else is a release tag.
3. **Note if there are no tags.** If `git tag -l` returns nothing, you'll need the user to provide two refs explicitly.

## Step 1: Determine Comparison Mode

Based on user input, select the mode:

1. **No arguments** — Default to **Unreleased** mode (HEAD vs latest tag)
2. **Two tags or refs mentioned** (e.g., "v2.1.0 vs v2.0.0", "compare tag-a to tag-b") — **Tag-to-tag** mode
3. **"since" + a tag/ref** (e.g., "since v1.5.0", "what changed after rc-42") — **Since tag** mode
4. **"staging", "preview", "rc" vs "prod"** mentioned — **Staging vs prod** mode
5. **Git range syntax** (`..` or `...`) — **Custom range** mode

If the intent is ambiguous, list the discovered tags and ask the user to pick.

## Step 2: Resolve BASE and HEAD

Each mode resolves to a `{BASE}` and `{HEAD}`:

### Unreleased (default)
```bash
# BASE = latest tag
git tag -l --sort=-v:refname | head -1
# HEAD = current HEAD
```

If no tags exist: tell the user "No tags found. Provide two commit refs to compare, or specify a range like `HEAD~20..HEAD`."

### Tag-to-tag
Both refs come from the user. Verify both tags exist:
```bash
git rev-parse --verify <tag1> && git rev-parse --verify <tag2>
```
Determine chronological order using `git log -1 --format=%ai <tag>` so BASE is always the older ref.

### Since tag
```bash
# BASE = user-specified tag
git rev-parse --verify <tag>
# HEAD = current HEAD
```

### Staging vs prod
Auto-discover the latest pre-release and release tags:
```bash
# Find latest release tag (exclude pre-release patterns)
git tag -l --sort=-v:refname | grep -v -E '(-rc|-beta|-alpha|^rc-|^staging-)' | head -1
# Find latest pre-release tag
git tag -l --sort=-v:refname | grep -E '(-rc|-beta|-alpha|^rc-|^staging-)' | head -1
```
BASE = latest release tag, HEAD = latest pre-release tag. Confirm both were found, show them to the user, and proceed.

### Custom range
Parse the range directly from user input. Validate both sides exist with `git rev-parse --verify`.

## Step 3: Extract and Categorize Commits

### Get the commit list
```bash
git log {BASE}..{HEAD} --pretty=format:"%h|%an|%s" --no-merges
```

### Get summary stats
```bash
git shortlog -sn --no-merges {BASE}..{HEAD}
git diff --stat {BASE}..{HEAD} | tail -1
```

### Categorize by conventional commit prefix

| Prefix | Category | Heading |
|--------|----------|---------|
| `feat:` `feature:` | Features | ### Features |
| `fix:` `bugfix:` | Bug Fixes | ### Bug Fixes |
| `perf:` | Performance | ### Performance |
| `docs:` `doc:` | Documentation | ### Documentation |
| `test:` `tests:` | Tests | ### Tests |
| `refactor:` | Refactoring | ### Refactoring |
| `chore:` `ci:` `build:` | Maintenance | ### Maintenance |
| `style:` | Style | ### Style |
| `revert:` | Reverts | ### Reverts |
| Everything else | Other | ### Other |

Parsing rules:
- Match the prefix case-insensitively: `^(feat|fix|docs|...)(\\(.*\\))?!?:\\s*`
- Strip the prefix and optional scope from the display message (show only the human-readable part)
- If the prefix ends with `!` or the body contains `BREAKING CHANGE`, also add the commit to a **Breaking Changes** section at the top
- If the repo doesn't use conventional commits, everything lands in "Other" — that's fine, the changelog is still useful

## Step 4: Generate Output

Produce markdown in this format:

```markdown
# Changelog

_Generated: YYYY-MM-DD_

## {HEAD_LABEL} vs {BASE_LABEL}

Comparing **{HEAD_REF}** against **{BASE_REF}**

### Breaking Changes
- description (`hash`) - @author

### Features
- description (`hash`) - @author

### Bug Fixes
- description (`hash`) - @author

[...remaining categories with commits...]

---
**Summary:** X commits | Y contributors | Z files changed
**Range:** `git log {BASE}..{HEAD}`
```

Where:
- `{HEAD_LABEL}` / `{BASE_LABEL}` are human-readable — e.g., "Unreleased (main)", "v2.1.0", "rc-2024.03.15"
- Only include category sections that have commits
- Breaking Changes always comes first when present
- Order remaining categories: Features, Bug Fixes, Performance, Refactoring, Documentation, Tests, Maintenance, Style, Reverts, Other

### Output handling

1. **Always display the changelog first** — print it in the conversation
2. Then ask: "Write to a file? (suggest CHANGELOG.md at repo root, or the user can specify a path)"
3. If the user invoked this non-interactively or said "save it", write to `CHANGELOG.md` at the repo root without asking

## Edge Cases

- **No commits between refs**: Report "No changes found between {BASE} and {HEAD}." and stop.
- **Dirty working tree**: Warn "Working tree has uncommitted changes — changelog reflects committed state only." but proceed.
- **Detached HEAD**: Use the commit hash as the HEAD label.
- **Shallow clone**: If commit count seems unexpectedly low, suggest `git fetch --unshallow` or `git fetch --tags`.
- **Missing tags**: If a user-specified tag doesn't exist, list similar tags (`git tag -l '*partial*'`) to help them find the right one.
- **Monorepo**: If the user asks for a per-package or per-service changelog, scope the git log with path filters: `git log {BASE}..{HEAD} -- <path>`.

## Rules

- Never hardcode repository names, workspace paths, or tag patterns
- Auto-detect tag naming conventions from what exists in the repo
- Only include category sections that have commits
- Strip conventional commit prefixes from display text for readability
- Display the changelog before writing to any file
- Handle repos that don't use conventional commits gracefully
- Work with both annotated and lightweight tags
