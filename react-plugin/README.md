# React Plugin for Claude Code

A comprehensive React development plugin that sets up a modern React frontend project with Vite, TypeScript, ESLint, and Prettier.

## Features

- **Modern Stack**: Vite + React 18 + TypeScript
- **Code Quality**: ESLint and Prettier pre-configured
- **Organized Structure**: Sensible folder structure for scalable apps
- **Type Safety**: Strict TypeScript configuration
- **Fast Development**: Hot Module Replacement (HMR) with Vite
- **Production Ready**: Optimized build configuration

## What Gets Created

### Folder Structure

```
project/
├── src/
│   ├── components/     # React components
│   ├── hooks/          # Custom React hooks
│   ├── utils/          # Utility functions
│   ├── styles/         # CSS files
│   │   ├── index.css   # Global styles
│   │   └── App.css     # App component styles
│   ├── types/          # TypeScript type definitions
│   ├── assets/         # Images, fonts, etc.
│   ├── App.tsx         # Main App component
│   ├── main.tsx        # React entry point
│   └── vite-env.d.ts   # Vite type definitions
├── public/             # Static files
├── index.html          # HTML entry point
├── package.json        # Dependencies and scripts
├── tsconfig.json       # TypeScript configuration
├── tsconfig.node.json  # TypeScript config for Node
├── vite.config.ts      # Vite configuration
├── .eslintrc.cjs       # ESLint configuration
├── .prettierrc         # Prettier configuration
└── .gitignore          # Git ignore rules
```

### Configuration Files

- **TypeScript**: Strict mode with path aliases (`@/*` → `src/*`)
- **ESLint**: React, TypeScript, and hooks rules
- **Prettier**: Consistent formatting (single quotes, 100 char width)
- **Vite**: Development server on port 3000

## Installation

This plugin is automatically installed when you bootstrap a React project using the project-bootstrapper skill.

Manual installation:
```bash
claude-code plugin install react
```

## Usage

### Automatic Setup

When installed, the plugin automatically:
1. Creates the folder structure
2. Generates all configuration files
3. Creates starter application files
4. Installs dependencies

### Manual Setup Command

Re-run setup or fix configuration:
```bash
/react-setup
```

## Available Commands

- `/react-setup` - Initialize or reconfigure React project

## NPM Scripts

After setup, use these commands:

- `npm run dev` - Start development server (http://localhost:3000)
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier

## Requirements

- Node.js 18+ 
- npm 9+
- Core plugin installed

## Dependencies

This plugin depends on the `core` plugin and must be installed after it.

## Customization

All generated files can be customized after creation:

- Modify `vite.config.ts` for build options
- Update `.eslintrc.cjs` for linting rules
- Adjust `.prettierrc` for formatting preferences
- Edit `tsconfig.json` for TypeScript options

## Troubleshooting

**Dependencies not installing:**
- Run `npm install` manually in your project directory

**Port 3000 already in use:**
- Edit `vite.config.ts` and change the port number

**ESLint errors:**
- Run `npm run lint` to see all issues
- Fix automatically with `npm run lint -- --fix`

## Version

1.0.0

## License

MIT
