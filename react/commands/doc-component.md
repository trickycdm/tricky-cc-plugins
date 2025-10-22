---
description: Generate comprehensive JSDoc documentation for the current component
---

# Component Documentation Generator

Automatically generate JSDoc documentation for your React component, including:
- Component description
- Props documentation
- Usage examples
- Return type

## Usage

Open a component file and run:
```bash
/doc-component
```

## What Gets Generated

```typescript
/**
 * ComponentName - Brief description
 * 
 * @component
 * @example
 * return (
 *   <ComponentName prop1="value" prop2={true} />
 * )
 */
export const ComponentName: React.FC<Props> = ({ prop1, prop2 }) => {
  // ...
};
```

## Features

- Analyzes props automatically
- Generates usage examples
- Documents component purpose
- Maintains existing code

---

Claude will analyze the current component and generate appropriate JSDoc documentation.
