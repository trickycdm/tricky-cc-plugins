# Adding Project Bootstrapper Skill to Core Plugin

## Overview

The project-bootstrapper skill should be bundled with your **core plugin**. This way, when users install the core plugin, they automatically get the bootstrapping capability.

## Directory Structure

Your core plugin should have this structure:

```
core/
├── .claude-plugin/
│   └── plugin.json          # Add "skills": true to capabilities
├── skills/                  # ← ADD THIS DIRECTORY
│   └── project-bootstrapper/
│       ├── SKILL.md
│       ├── scripts/
│       │   └── bootstrap_project.py
│       └── references/
│           └── plugin_architecture.md
├── commands/                # Your existing core commands
├── agents/                  # Your existing core agents
└── hooks/                   # Your existing core hooks
```

## Installation Steps

### Step 1: Add Skills Directory to Your Core Plugin

```bash
cd tricky-cc-plugins/core

# Create skills directory if it doesn't exist
mkdir -p skills

# Copy the project-bootstrapper skill
cp -r /path/to/skills/project-bootstrapper skills/
```

### Step 2: Update plugin.json

Add `"skills": true` to your core plugin's capabilities:

```json
{
  "name": "core",
  "version": "1.0.0",
  "description": "Core utilities, agents, commands, and project bootstrapping",
  "capabilities": {
    "commands": true,
    "agents": true,
    "hooks": true,
    "skills": true
  }
}
```

### Step 3: Commit and Push

```bash
git add skills/
git commit -m "Add project-bootstrapper skill to core plugin"
git push origin main
```

### Step 4: Users Install Core Plugin

When users install the core plugin:

```bash
claude-code marketplace add https://github.com/trickycdm/tricky-cc-plugins
claude-code plugin install core
```

They automatically get:
- ✅ Core commands and agents
- ✅ Project bootstrapper skill
- ✅ Ready to bootstrap projects!

## How Users Will Use It

Once the core plugin is installed, users just tell Claude:

```
Bootstrap a new React project called my-app
```

Claude will:
1. Recognize the request (skill description triggers it)
2. Read the SKILL.md instructions
3. Run the bootstrap_project.py script
4. Clone template → Install plugins → Ready to code!

## Skill Discovery

The skill's description in SKILL.md makes it discoverable:

```yaml
description: Bootstrap new development projects by cloning template repositories 
and installing Claude Code plugins. Use when user requests to create, initialize, 
set up, or bootstrap a new project for React, Node backend, or other supported 
frameworks.
```

When users say things like:
- "Bootstrap a new React project"
- "Set up a React project"
- "Create a new frontend project"

Claude automatically uses this skill!

## What This Gives You

**Core Plugin now provides:**
- 🔧 Universal utilities and commands
- 🤖 Shared agents
- 🎯 Project bootstrapping capability
- 📦 One install = Everything users need

**Single installation:**
```bash
claude-code plugin install core
```

Gets users:
- All core functionality
- Project bootstrapping
- Template cloning
- Plugin orchestration

## Files Included

The `project-bootstrapper` skill includes:

1. **SKILL.md** - Instructions for Claude on how to bootstrap projects
2. **scripts/bootstrap_project.py** - Python script that does the work
3. **references/plugin_architecture.md** - Documentation on the system

## Testing

After adding the skill to your core plugin:

```bash
# Install the core plugin in a test project
claude-code plugin install core

# Test the skill
# In Claude Code, say:
"Bootstrap a new React project called test-app"

# Verify:
# - Template was cloned
# - Plugins were installed
# - Project is ready
```

## Why Bundle with Core Plugin?

✅ **Single installation** - Users get everything with one plugin
✅ **Automatic availability** - No separate skill installation needed
✅ **Logical grouping** - Core plugin = foundational tools
✅ **Easy distribution** - Through your existing plugin marketplace
✅ **Version control** - Skill versions with plugin versions

## Updating the Skill

To update the skill:

```bash
# Edit files in core/skills/project-bootstrapper/
# Commit and push
# Users get updates when they update the core plugin
```

## Next Steps

1. Add the `skills/` directory to your core plugin
2. Update core plugin's plugin.json
3. Commit and push to GitHub
4. Users install/update core plugin
5. Skill is automatically available!

No separate skill files needed - it's all bundled with the plugin.
