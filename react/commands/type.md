---
description: Generate TypeScript type definitions file
usage: /type [TypeName] [--path src/types]
---

# Type Generator

Generate TypeScript type definition files for better type safety and code organization.

## Usage

```bash
/type User
/type ApiResponse --path src/types/api
```

## What Gets Generated

Creates a TypeScript file with:
- Type or interface definition
- Export statement
- JSDoc comments
- Helper types if needed

## Examples

```
/type User
```

Creates: `src/types/User.ts`

```typescript
/**
 * User type definition
 */
export interface User {
  id: string;
  name: string;
  email: string;
  // Add more properties
}
```

## Options

- `--path` - Specify custom path (default: `src/types`)
- `--type` - Generate `type` instead of `interface`

## When to Use

- Defining data models
- API response types
- Shared prop types
- Complex type definitions

---

```bash
python ${PLUGIN_DIR}/scripts/generate_type.py "$@"
```
