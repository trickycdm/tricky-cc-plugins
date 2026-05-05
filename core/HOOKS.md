# Plugin Hooks

This plugin ships one Claude Code hook: the **rename-plan** hook, which auto-organises plan files into dated folders with worklogs.

## How it's wired

`hooks/hooks.json` registers a `PostToolUse` hook that runs after every `Write` or `Edit` tool call:

```json
{
  "description": "Automatic plan organization hooks",
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/rename-plan.sh"
          }
        ]
      }
    ]
  }
}
```

What each piece does:

- **`PostToolUse`** — fires after the tool succeeds, so the file already exists on disk when the script runs.
- **`matcher: "Write|Edit"`** — the `|` is treated as a literal alternation of exact tool names. The hook only fires for those two tools, not for every PostToolUse event.
- **`${CLAUDE_PLUGIN_ROOT}`** — resolves to the plugin's installation directory, so the script works regardless of where the plugin was installed or what the working directory is.

When the plugin is installed via `/plugin marketplace`, this file is registered automatically — no user action needed. The hooks register on plugin enable and unregister on disable.

## What the script does

`scripts/rename-plan.sh` reads the tool-call JSON from stdin, extracts `tool_input.file_path`, and acts only when the path matches `*/plans/.tmp/*.md`. Anything else exits 0 and the tool call proceeds normally.

For matching files:

1. **First write of a plan** — reads the first 1500 chars, asks Claude (`claude -p`) for a 3-5 word snake_case slug, and creates `plans/YYYY-MM-DD-<slug>/plan.md` plus a fresh `worklog.md`. The chosen slug is cached in a `<file>.name` sidecar so subsequent edits route to the same folder without re-prompting.
2. **Agent worklogs** — files named `<session>-agent-<id>.md` are routed to `plans/YYYY-MM-DD-<slug>/worklog-<id>.md` based on the parent session's namecard. If the parent plan hasn't been named yet, the worklog stashes in `plans/.tmp/pending/` and is adopted when the parent's folder is created.

The hook is idempotent — re-editing a plan file copies the updated content into the same target folder.

## Wiring it manually

If you're using these scripts outside the plugin (copied into your own project), drop the JSON above into one of:

- `~/.claude/settings.json` — applies to all your projects
- `.claude/settings.json` — project-scoped, can be committed
- `.claude/settings.local.json` — project-scoped, gitignored

…and replace `${CLAUDE_PLUGIN_ROOT}` with `"$CLAUDE_PROJECT_DIR"/path/to/rename-plan.sh` (quotes matter — `$CLAUDE_PROJECT_DIR` may contain spaces).

The script needs `python3`, `claude` (the CLI), `realpath`, and `find` on `PATH`. `claude -p` is only invoked on first-write, so existing plans don't pay the LLM cost.

## Custom status line

To use the bundled status line, add to your `~/.claude/settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "/path/to/plugin/core/scripts/statusline.sh",
    "padding": 2
  }
}
```

This is a separate Claude Code feature, not a hook — it doesn't go inside the `hooks` block.

The status line shows: model · cwd · branch · context-usage bar · session cost · duration.
