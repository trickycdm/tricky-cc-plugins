# React Plugin for Claude Code

A comprehensive React development plugin providing code generation, analysis tools, and specialized AI agents.

## Overview

This plugin enhances Claude Code with React-specific development tools. It assumes you're working in a project created from a React template repository.

## Features

### 🛠️ Code Generation Commands

- `/component [name]` - Generate React components with TypeScript and arrow functions
- `/hook [name]` - Create custom React hooks
- `/util [name]` - Generate utility functions
- `/type [name]` - Create TypeScript type definitions

### 📊 Analysis & Documentation

- `/analyze-component` - Comprehensive component analysis for best practices
- `/suggest-refactor` - Get intelligent refactoring suggestions
- `/doc-component` - Generate JSDoc for components
- `/doc-props` - Document props interfaces

### 🤖 Specialized Agents

- **Component Agent** (`/agent component-agent`) - Expert in component architecture and design
- **Performance Agent** (`/agent performance-agent`) - Performance optimization specialist
- **Accessibility Agent** (`/agent accessibility-agent`) - A11y compliance expert

## Installation

This plugin is automatically installed when you bootstrap a React project using the project-bootstrapper skill.

**Manual installation:**
```bash
claude-code marketplace add https://github.com/trickycdm/tricky-cc-plugins
claude-code plugin install react
```

## Usage Examples

### Generate a Component

```bash
/component UserCard
```

Creates: `src/components/UserCard.tsx`

```typescript
import React from 'react';

interface UserCardProps {
  // Add your props here
}

/**
 * UserCard component
 */
export const UserCard: React.FC<UserCardProps> = (props) => {
  return (
    <div>
      {/* Component content */}
    </div>
  );
};
```

### Create a Custom Hook

```bash
/hook useAuth --path src/hooks
```

Creates: `src/hooks/useAuth.ts`

### Analyze Component Performance

```bash
/analyze-component
```

Get detailed analysis of:
- Performance issues
- Best practices adherence
- Accessibility concerns
- TypeScript usage
- Optimization opportunities

### Get Refactoring Suggestions

```bash
/suggest-refactor
```

Receive intelligent suggestions for:
- Extracting custom hooks
- Splitting large components
- Improving state management
- Better code organization

## Specialized Agents

### Component Agent

Expert in React component design and implementation.

```bash
/agent component-agent "Help me design a reusable data table component"
```

### Performance Agent

Analyzes and optimizes React performance.

```bash
/agent performance-agent "This component re-renders too often, help optimize it"
```

### Accessibility Agent

Ensures components meet WCAG standards.

```bash
/agent accessibility-agent "Review this form for accessibility issues"
```

## Code Style Conventions

This plugin follows these conventions:

- **Arrow functions** for components: `export const Component = () => {}`
- **TypeScript** for all files
- **Props interfaces** with PascalCase + "Props" suffix
- **Named exports** for components
- **Descriptive prop names**

## Requirements

- Node.js 18+
- TypeScript 5+
- React 18+
- Core plugin installed

## Project Structure Assumptions

The plugin assumes your project has:
```
src/
├── components/
├── hooks/
├── utils/
├── types/
├── styles/
└── assets/
```

## Customization

All generated code can be customized:
- Edit templates in the plugin scripts
- Adjust code style preferences
- Add your own commands

## Best Practices Enforced

- **TypeScript strict mode** - Full type safety
- **Component purity** - Predictable behavior
- **Hooks rules** - Proper hooks usage
- **Accessibility** - WCAG compliance
- **Performance** - Memoization and optimization

## Troubleshooting

**Command not found:**
- Run `/help` to see available commands
- Ensure the plugin is installed: `claude-code plugin list`

**Wrong component style:**
- The plugin uses arrow function components by default
- This can be customized in the plugin scripts

**Path not found:**
- Ensure the directory exists or use `--path` to specify location
- Default paths assume standard React project structure

## Version

1.0.0

## Dependencies

- `core` plugin (required)

## License

MIT

## Support

- **Plugin Docs**: https://docs.claude.com/en/docs/claude-code/plugins
- **Repository**: https://github.com/trickycdm/tricky-cc-plugins
- **Issues**: GitHub Issues

---

**Note:** This plugin is designed to work with projects bootstrapped from your template repository. It provides development tools, not project initialization.
