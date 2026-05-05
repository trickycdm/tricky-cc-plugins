# core — Claude Code workflow plugin

The plugin shipped by [tricky-cc-plugins](../README.md). It provides the agents, commands, skills, and hooks that implement the six-phase development lifecycle described in the root README. Install via the [root README](../README.md#install).

## At a glance

Components mapped onto the lifecycle:

| Phase  | Components                                                                |
|--------|---------------------------------------------------------------------------|
| Plan   | `rename-plan` hook · `/plan-status`                                       |
| Build  | `feature-creator`, `code-explorer`, `claude-md-generator` agents          |
| Review | `/review` · `code-reviewer`, `security-reviewer`, `tech-debt-reviewer` agents |
| Test   | `/pw-test`, `/a11y-audit` · `test-generator` agent · `playwright-cli`, `a11y-audit` skills |
| Learn  | `/wrap-up` · `learn`, `wrap-up` skills · `documentation-generator` agent  |
| Ship   | `/commit`, `/gen-changelog`, `/wt-merge` · `gen-changelog`, `wt-merge`, `github-project-tickets` skills |

## Agents

Long-running, autonomous workers for complex tasks.

| Agent | Purpose |
|-------|---------|
| `code-reviewer` | Logic bugs, edge cases, convention violations |
| `security-reviewer` | Vulnerability scanning, unsafe patterns, exposed secrets |
| `tech-debt-reviewer` | Maintainability, dead code, duplication |
| `test-generator` | Runner-agnostic TypeScript unit tests (Jest / Vitest / `node:test`); follows host project's testing standards |
| `feature-creator` | End-to-end feature implementation |
| `documentation-generator` | Architectural docs (the "why" / navigation); detects host's doc convention (CLAUDE.md / AGENTS.md / etc.) and updates in place |
| `claude-md-generator` | Bootstraps CLAUDE.md steering files |
| `code-explorer` | Codebase navigation and understanding |

Invoke via `/agent <name>` or trigger automatically through the commands that compose them (e.g. `/review`).

## Commands

Quick, single-shot slash commands.

| Command | Purpose |
|---------|---------|
| `/review` | Multi-agent review — fans out to `code-reviewer`, `security-reviewer`, `tech-debt-reviewer` in parallel and synthesises the results |
| `/commit` | Conventional-format commit; updates CLAUDE.md if affected; preps changelog content |
| `/pw-test` | Exploratory Playwright testing then E2E test generation |
| `/a11y-audit` | WCAG accessibility audit on changed files |
| `/gen-changelog` | Generates a categorised changelog from git history |
| `/wrap-up` | Finalises the active plan, captures lessons |
| `/wt-merge` | Squash-merge a worktree branch's PR and clean up |
| `/plan-status` | Lists status of every plan in `plans/` |
| `/product-lens` | Product-perspective review before building |
| `/optimize-doc` | Tightens a markdown/documentation file |
| `/warp` | Builds a session-summary you can paste into a fresh `/clear`'d session |

## Skills

Capabilities Claude invokes automatically when relevant.

| Skill | Activates when… |
|-------|------------------|
| `playwright-cli` | Browser automation or E2E testing is needed |
| `a11y-audit` | Accessibility checking is requested |
| `gen-changelog` | Release notes are being prepared |
| `github-project-tickets` | Pushing completed work to a GitHub Project board |
| `learn` | Updating steering docs after corrections |
| `optimize-doc` | Improving an existing markdown file |
| `product-lens` | Strategic product questions arise before building |
| `wrap-up` | Closing out plan execution |
| `wt-merge` | Merging worktree branches |

## Hooks

`hooks/hooks.json` registers a `PostToolUse` hook on `Write|Edit` that calls `scripts/rename-plan.sh`. The script:

- Moves new plan files out of `plans/.tmp/` into a dated, descriptively named folder (e.g. `plans/2024-01-15-user-authentication/plan.md`).
- Creates and maintains `worklog.md` alongside each plan.
- Keeps agent worklogs separate.

Setup details and the status-line config: [HOOKS.md](HOOKS.md).

## Extending the plugin

**Add an agent** — drop a markdown file into `agents/`:

```markdown
---
name: api-reviewer
description: Reviews API design
---

You are an API design expert…
```

**Add a command** — drop a markdown file into `commands/`:

```markdown
---
name: deploy
description: Deploy to production
---

Run deployment checks then push to production.
```

**Add a skill** — create a directory under `skills/` containing `SKILL.md` (skill definition), an optional `scripts/` folder, and an optional `references/` folder. Then add the path to the `skills` array in `.claude-plugin/plugin.json`.

## Troubleshooting

- **Commands not recognised** — verify install with `claude-code plugin list`; restart Claude Code after installation.
- **Agent not completing** — check Claude Code logs; ensure you're on the latest version.
- **Skills not activating** — be specific in your request; check the skill description for trigger language.

## Plugin layout

```
core/
├── .claude-plugin/
│   └── plugin.json          plugin metadata
├── agents/                  agent definitions (8 files)
├── commands/                slash-command definitions (11 files)
├── skills/                  skill directories with SKILL.md (9 skills)
├── hooks/
│   └── hooks.json           hook registrations
├── scripts/
│   ├── rename-plan.sh       plan-organising hook script
│   └── statusline.sh        status-line renderer
├── docs/
│   └── WORKFLOW_PRINCIPLES.md
├── HOOKS.md                 hooks + status-line setup
└── README.md                this file
```
