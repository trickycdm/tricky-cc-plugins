---
description: Create a changelog by comparing stage to prod. 
---

Generate a changelog by comparing the latest release candidate tag against the latest production tag.

## Steps

1. Find the latest production tag using: `git tag -l 'v*' --sort=-v:refname | head -1`
2. Find the latest release candidate tag using: `git tag -l 'rc-*' --sort=-v:refname | head -1`
3. Get all commits between these tags: `git log <prod-tag>..<rc-tag> --pretty=format:'%h|%s|%an|%ad' --date=short`
4. Parse and categorize commits by conventional commit prefixes:
   - `feat:` → Features
   - `fix:` → Bug Fixes
   - `chore:`, `refactor:`, `ci:` → Maintenance
   - `docs:` → Documentation
   - `test:` → Tests
   - `perf:` → Performance
   - Everything else → Other

5. Generate a markdown changelog in this format:
```
# Changelog

## [<rc-tag>] → Production

Comparing against current production: **<prod-tag>**

### ✨ Features
- <commit message> (`<short-hash>`) - @<author>

### 🐛 Bug Fixes
- <commit message> (`<short-hash>`) - @<author>

### 🔧 Maintenance
- <commit message> (`<short-hash>`) - @<author>

### 📚 Documentation
- <commit message> (`<short-hash>`) - @<author>

### 🧪 Tests
- <commit message> (`<short-hash>`) - @<author>

### ⚡ Performance
- <commit message> (`<short-hash>`) - @<author>

### Other
- <commit message> (`<short-hash>`) - @<author>

---
**Summary:** X commits | Y contributors
**Full diff:** `git diff <prod-tag>..<rc-tag> --stat`
```

6. Only include sections that have commits
7. Save the output to `CHANGELOG.md` in the repo root
8. Display the changelog contents when complete