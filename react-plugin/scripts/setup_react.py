#!/usr/bin/env python3
"""
React Project Setup Script

This script initializes a React project with:
- Vite + React + TypeScript
- Proper folder structure
- ESLint and Prettier configuration
- TypeScript configuration
- Git setup
"""

import os
import subprocess
import json
import sys
from pathlib import Path


def run_command(cmd, cwd=".", check=True):
    """Run a shell command."""
    print(f"Running: {cmd}")
    result = subprocess.run(
        cmd,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=check
    )
    if result.stdout:
        print(result.stdout)
    if result.stderr and result.returncode != 0:
        print(result.stderr, file=sys.stderr)
    return result


def create_folder_structure(base_path):
    """Create the React project folder structure."""
    folders = [
        "src/components",
        "src/hooks",
        "src/utils",
        "src/styles",
        "src/types",
        "src/assets",
        "public",
    ]
    
    for folder in folders:
        path = Path(base_path) / folder
        path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {folder}")


def initialize_vite(base_path):
    """Initialize a Vite React TypeScript project."""
    print("\n📦 Initializing Vite + React + TypeScript...")
    
    # Use npm create vite to initialize
    result = run_command(
        f"npm create vite@latest . -- --template react-ts",
        cwd=base_path,
        check=False
    )
    
    if result.returncode == 0:
        print("✅ Vite project initialized")
    else:
        # If that fails, try manual setup
        print("⚠️  Using manual Vite setup...")
        create_vite_config(base_path)
        create_package_json(base_path)


def create_package_json(base_path):
    """Create a package.json with dependencies."""
    package_json = {
        "name": Path(base_path).name,
        "private": True,
        "version": "0.1.0",
        "type": "module",
        "scripts": {
            "dev": "vite",
            "build": "tsc && vite build",
            "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
            "preview": "vite preview",
            "format": "prettier --write \"src/**/*.{ts,tsx,css}\""
        },
        "dependencies": {
            "react": "^18.3.1",
            "react-dom": "^18.3.1"
        },
        "devDependencies": {
            "@types/react": "^18.3.3",
            "@types/react-dom": "^18.3.0",
            "@typescript-eslint/eslint-plugin": "^7.13.1",
            "@typescript-eslint/parser": "^7.13.1",
            "@vitejs/plugin-react": "^4.3.1",
            "eslint": "^8.57.0",
            "eslint-plugin-react-hooks": "^4.6.2",
            "eslint-plugin-react-refresh": "^0.4.7",
            "prettier": "^3.3.2",
            "typescript": "^5.2.2",
            "vite": "^5.3.1"
        }
    }
    
    with open(Path(base_path) / "package.json", "w") as f:
        json.dump(package_json, f, indent=2)
    print("✅ Created package.json")


def create_vite_config(base_path):
    """Create vite.config.ts."""
    vite_config = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
  },
})
"""
    with open(Path(base_path) / "vite.config.ts", "w") as f:
        f.write(vite_config)
    print("✅ Created vite.config.ts")


def create_tsconfig(base_path):
    """Create tsconfig.json."""
    tsconfig = {
        "compilerOptions": {
            "target": "ES2020",
            "useDefineForClassFields": True,
            "lib": ["ES2020", "DOM", "DOM.Iterable"],
            "module": "ESNext",
            "skipLibCheck": True,
            "moduleResolution": "bundler",
            "allowImportingTsExtensions": True,
            "resolveJsonModule": True,
            "isolatedModules": True,
            "noEmit": True,
            "jsx": "react-jsx",
            "strict": True,
            "noUnusedLocals": True,
            "noUnusedParameters": True,
            "noFallthroughCasesInSwitch": True,
            "baseUrl": ".",
            "paths": {
                "@/*": ["src/*"]
            }
        },
        "include": ["src"],
        "references": [{"path": "./tsconfig.node.json"}]
    }
    
    with open(Path(base_path) / "tsconfig.json", "w") as f:
        json.dump(tsconfig, f, indent=2)
    print("✅ Created tsconfig.json")
    
    # Create tsconfig.node.json
    tsconfig_node = {
        "compilerOptions": {
            "composite": True,
            "skipLibCheck": True,
            "module": "ESNext",
            "moduleResolution": "bundler",
            "allowSyntheticDefaultImports": True,
            "strict": True
        },
        "include": ["vite.config.ts"]
    }
    
    with open(Path(base_path) / "tsconfig.node.json", "w") as f:
        json.dump(tsconfig_node, f, indent=2)
    print("✅ Created tsconfig.node.json")


def create_eslint_config(base_path):
    """Create .eslintrc.cjs."""
    eslint_config = """module.exports = {
  root: true,
  env: { browser: true, es2020: true },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react-hooks/recommended',
  ],
  ignorePatterns: ['dist', '.eslintrc.cjs'],
  parser: '@typescript-eslint/parser',
  plugins: ['react-refresh'],
  rules: {
    'react-refresh/only-export-components': [
      'warn',
      { allowConstantExport: true },
    ],
  },
}
"""
    with open(Path(base_path) / ".eslintrc.cjs", "w") as f:
        f.write(eslint_config)
    print("✅ Created .eslintrc.cjs")


def create_prettier_config(base_path):
    """Create .prettierrc."""
    prettier_config = {
        "semi": True,
        "trailingComma": "es5",
        "singleQuote": True,
        "printWidth": 100,
        "tabWidth": 2,
        "useTabs": False
    }
    
    with open(Path(base_path) / ".prettierrc", "w") as f:
        json.dump(prettier_config, f, indent=2)
    print("✅ Created .prettierrc")


def create_gitignore(base_path):
    """Create .gitignore."""
    gitignore_content = """# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
"""
    with open(Path(base_path) / ".gitignore", "w") as f:
        f.write(gitignore_content)
    print("✅ Created .gitignore")


def create_index_html(base_path):
    """Create index.html."""
    index_html = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
"""
    with open(Path(base_path) / "index.html", "w") as f:
        f.write(index_html)
    print("✅ Created index.html")


def create_app_files(base_path):
    """Create main application files."""
    # Create src/main.tsx
    main_tsx = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './styles/index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
"""
    with open(Path(base_path) / "src/main.tsx", "w") as f:
        f.write(main_tsx)
    print("✅ Created src/main.tsx")
    
    # Create src/App.tsx
    app_tsx = """import './styles/App.css'

function App() {
  return (
    <div className="App">
      <h1>Welcome to React + TypeScript + Vite</h1>
      <p>Edit <code>src/App.tsx</code> and save to test HMR</p>
    </div>
  )
}

export default App
"""
    with open(Path(base_path) / "src/App.tsx", "w") as f:
        f.write(app_tsx)
    print("✅ Created src/App.tsx")
    
    # Create src/styles/index.css
    index_css = """* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
"""
    with open(Path(base_path) / "src/styles/index.css", "w") as f:
        f.write(index_css)
    print("✅ Created src/styles/index.css")
    
    # Create src/styles/App.css
    app_css = """.App {
  text-align: center;
  padding: 2rem;
}

h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

p {
  font-size: 1.2rem;
  color: #666;
}

code {
  background-color: #f4f4f4;
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
}
"""
    with open(Path(base_path) / "src/styles/App.css", "w") as f:
        f.write(app_css)
    print("✅ Created src/styles/App.css")
    
    # Create src/vite-env.d.ts
    vite_env = """/// <reference types="vite/client" />
"""
    with open(Path(base_path) / "src/vite-env.d.ts", "w") as f:
        f.write(vite_env)
    print("✅ Created src/vite-env.d.ts")


def install_dependencies(base_path):
    """Install npm dependencies."""
    print("\n📦 Installing dependencies (this may take a minute)...")
    result = run_command("npm install", cwd=base_path, check=False)
    if result.returncode == 0:
        print("✅ Dependencies installed")
    else:
        print("⚠️  Failed to install dependencies. Run 'npm install' manually.")


def setup_react_project(project_path="."):
    """
    Complete React project setup.
    
    Args:
        project_path: Path to the project directory
    """
    print("🚀 Setting up React project...\n")
    
    # Create folder structure
    print("📁 Creating folder structure...")
    create_folder_structure(project_path)
    
    # Create configuration files
    print("\n⚙️  Creating configuration files...")
    create_package_json(project_path)
    create_vite_config(project_path)
    create_tsconfig(project_path)
    create_eslint_config(project_path)
    create_prettier_config(project_path)
    create_gitignore(project_path)
    
    # Create application files
    print("\n📝 Creating application files...")
    create_index_html(project_path)
    create_app_files(project_path)
    
    # Install dependencies
    install_dependencies(project_path)
    
    print("\n✅ React project setup complete!")
    print("\nNext steps:")
    print("  1. npm run dev      - Start development server")
    print("  2. npm run build    - Build for production")
    print("  3. npm run lint     - Run ESLint")
    print("  4. npm run format   - Format with Prettier")


if __name__ == "__main__":
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    setup_react_project(project_path)
