---
description: Create a changelog by comparing current main line to prod deployed tag. 
---

Generate a changelog by comparing the latest production tag against the head of the main branch. You will often be invoked from the luupdin-workspace directory, so unless told otherwise, you should only create changelogs for the frontend (luupdin-frontend) and backend (luupdin-backend) repos. This will mean cd into them and running fetching the data to then create consolidated changelog of all changes. 

## Steps

1. Find the latest production tag using: `git tag -l 'v*' --sort=-v:refname | head -1`
2. Get all commits on the main branch and compare changes between the prod tag and main branch
3. Parse and categorize commits by conventional commit prefixes:
   - `feat:` → Features
   - `fix:` → Bug Fixes
   - `chore:`, `refactor:`, `ci:` → Maintenance
   - `docs:` → Documentation
   - `test:` → Tests
   - `perf:` → Performance
   - Everything else → Other

4. Generate a markdown changelog in this format for each individual repo you fetch:
```
# Changelog

__date of generation__

## [<current main branch head hash>] → Production

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
**Full diff:** `git diff <prod-tag>..<main-head> --stat`
```

6. Only include sections that have commits
7. Save a consolidated version in the luupdin-workspace root `CHANGELOG.md`
8. Display the changelog contents when complete