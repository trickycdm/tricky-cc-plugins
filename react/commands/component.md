---
description: Generate a new React component with TypeScript and arrow function syntax
usage: /component [ComponentName] [--path src/components]
---

# Component Generator

Generate a new React component following the project's conventions.

## Usage

```bash
/component MyComponent
/component UserProfile --path src/features/user
```

## What Gets Generated

Creates a new `.tsx` file with:
- Arrow function component (preferred style)
- TypeScript interface for props
- Basic JSDoc comment
- Export statement

## Component Template

```typescript
import React from 'react';

interface [ComponentName]Props {
  // Add your props here
}

/**
 * [ComponentName] component
 */
export const [ComponentName]: React.FC<[ComponentName]Props> = (props) => {
  return (
    <div>
      {/* Component content */}
    </div>
  );
};
```

## Options

- `--path` - Specify custom path (default: `src/components`)
- `--no-props` - Generate component without props interface
- `--styled` - Include styled-components boilerplate (if using styled-components)

## Examples

**Basic component:**
```
/component Button
```
Creates: `src/components/Button.tsx`

**Component in custom location:**
```
/component UserCard --path src/features/users/components
```
Creates: `src/features/users/components/UserCard.tsx`

**Component without props:**
```
/component Loading --no-props
```

## After Generation

1. Open the generated file
2. Add your props to the interface
3. Implement the component logic
4. Import and use in your app

---

```python
python ${PLUGIN_DIR}/scripts/generate_component.py "$@"
```
