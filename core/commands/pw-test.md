---
description: Exploratory testing with Playwright, then write E2E tests
---

Perform exploratory testing using playwright-cli, then write E2E test files for future automated runs.

## Phase 1: Exploratory Testing
Use the playwright-cli skill to:
1. Open browser and navigate to the application
2. Interact with new/changed features
3. Verify expected behavior through snapshots
4. Test edge cases and error states
5. Document any issues found

## Phase 2: Test Generation
After confirming behavior:
1. Write Playwright test files based on the exploration
2. Follow the project's E2E testing standards if it documents them — common locations: `steering/E2E_TESTING.md`, `docs/E2E_TESTING.md`, or a dedicated section in the root `CLAUDE.md`
3. Include:
   - Happy path tests
   - Error handling tests
   - Accessibility checks
   - Any edge cases discovered during exploration

## Scope
- No arguments: Test pending git changes or last commit
- With arguments: Follow user's specific test requirements

## Output
- Exploration results summary
- New test files in appropriate test directory
- Instructions for running the tests
