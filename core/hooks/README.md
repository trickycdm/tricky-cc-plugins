# Core Plugin Hooks

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

### Custom Status Line

**Script**: `scripts/statusline.sh`

Displays a custom status line showing:
- Current model
- Working directory
- Git branch
- Context usage with visual bar
- Session cost
- Session duration

To enable the status line, add to your `settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "path/to/plugin/core/scripts/statusline.sh",
    "padding": 2
  }
}
```

## Configuration

The hooks are automatically configured when the plugin is installed. The configuration is defined in `hooks/hooks.json`.

## Requirements

- `bash` shell
- `python3` (for plan organization)
- `jq` (for statusline)
- `git` (optional, for branch display)

## Customization

You can modify the scripts in the `scripts/` directory to customize behavior:
- Adjust plan naming conventions
- Change statusline display format
- Add additional hooks as needed