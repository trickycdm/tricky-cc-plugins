---
description: Generate a new custom React hook with TypeScript
usage: /hook [hookName] [--path src/hooks]
---

# Hook Generator

Generate a custom React hook following best practices.

## Usage

```bash
/hook useCounter
/hook useFetch --path src/features/api/hooks
```

## What Gets Generated

Creates a new hook file with:
- TypeScript type definitions
- Proper naming (use prefix)
- Return type inference
- JSDoc comments

## Hook Template

```typescript
import { useState } from 'react';

/**
 * [hookName] hook
 * @returns Hook state and methods
 */
export const [hookName] = () => {
  // Hook implementation
  
  return {
    // Return values
  };
};
```

## Options

- `--path` - Specify custom path (default: `src/hooks`)

## Examples

**Basic hook:**
```
/hook useToggle
```
Creates: `src/hooks/useToggle.ts`

**Hook in custom location:**
```
/hook useAuth --path src/features/auth/hooks
```

## Best Practices

- Always prefix with "use"
- Return an object or array
- Document parameters and return values
- Keep hooks focused and reusable

---

```bash
python ${PLUGIN_DIR}/scripts/generate_hook.py "$@"
```
