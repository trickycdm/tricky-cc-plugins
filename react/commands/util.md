---
description: Generate a new utility function file with TypeScript
usage: /util [utilName] [--path src/utils]
---

# Utility Generator

Generate a utility function file with TypeScript.

## Usage

```bash
/util formatDate
/util apiHelpers --path src/utils/api
```

## What Gets Generated

Creates a utility file with:
- TypeScript function signature
- JSDoc documentation
- Export statement
- Type-safe parameters and return types

## Examples

```
/util formatCurrency
```
Creates: `src/utils/formatCurrency.ts`

---

```bash
python ${PLUGIN_DIR}/scripts/generate_util.py "$@"
```
