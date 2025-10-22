---
description: Generate JSDoc documentation for component props interface
---

# Props Documentation Generator

Generate detailed JSDoc documentation for your component's props interface.

## Usage

Open a component file with a props interface and run:
```bash
/doc-props
```

## What Gets Generated

```typescript
interface ComponentProps {
  /**
   * Description of prop1
   * @type {string}
   */
  prop1: string;
  
  /**
   * Description of prop2
   * @type {boolean}
   * @default false
   */
  prop2?: boolean;
  
  /**
   * Click handler callback
   * @param {string} value - The value passed to the handler
   */
  onClick: (value: string) => void;
}
```

## Features

- Documents each prop
- Includes type information
- Notes optional props
- Documents default values
- Explains callback parameters

---

Claude will analyze the props interface and generate comprehensive documentation.
