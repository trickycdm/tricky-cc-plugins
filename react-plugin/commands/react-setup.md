---
description: Set up or reconfigure React project structure, Vite, TypeScript, ESLint, and Prettier
---

# React Setup Command

This command initializes or reconfigures your React project with:
- Vite + React + TypeScript
- Proper folder structure (components, hooks, utils, styles, types, assets)
- ESLint and Prettier configuration
- TypeScript configuration with strict mode
- Git ignore file

## Usage

```
/react-setup
```

## What This Command Does

1. **Creates folder structure:**
   - `src/components` - React components
   - `src/hooks` - Custom React hooks
   - `src/utils` - Utility functions
   - `src/styles` - CSS and styling files
   - `src/types` - TypeScript type definitions
   - `src/assets` - Images, fonts, and other assets
   - `public` - Static files

2. **Configures build tools:**
   - Vite for fast development and optimized builds
   - TypeScript with strict mode and path aliases
   - Hot Module Replacement (HMR)

3. **Sets up code quality tools:**
   - ESLint with React and TypeScript rules
   - Prettier for consistent code formatting
   - Pre-configured npm scripts

4. **Creates starter files:**
   - `index.html` - Entry point
   - `src/main.tsx` - React root
   - `src/App.tsx` - Main App component
   - CSS files with basic styling

5. **Installs dependencies:**
   - Runs `npm install` to install all required packages

## After Setup

Run these commands:
- `npm run dev` - Start development server (http://localhost:3000)
- `npm run build` - Build for production
- `npm run lint` - Check code with ESLint
- `npm run format` - Format code with Prettier

## Reconfiguration

Safe to run multiple times. Existing files won't be overwritten, but missing configuration files will be created.

---

```bash
python ${PLUGIN_DIR}/scripts/setup_react.py ${PROJECT_DIR}
```
