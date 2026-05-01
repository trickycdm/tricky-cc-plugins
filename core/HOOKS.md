# Plugin Hooks

This plugin includes hooks that enhance your Claude Code workflow.

## Included Hooks

### Plan Organization Hook

**Trigger**: After Write or Edit operations on plan files
**Script**: `scripts/rename-plan.sh`

Automatically organizes plans in the `plans/` directory:
- Creates dated folders with descriptive names (e.g., `2024-01-15-user-authentication`)
- Moves plan files from `.tmp/` to organized folders
- Creates and maintains worklogs
- Handles agent worklogs separately

## Hook Configuration

The hooks are defined in `hooks.json` at the plugin root level. They automatically activate when the plugin is installed.

## Custom Status Line

To use the custom status line, add to your `settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "path/to/plugin/core/scripts/statusline.sh",
    "padding": 2
  }
}
```

The status line displays:
- Current model
- Working directory and git branch
- Context usage with visual bar
- Session cost and duration