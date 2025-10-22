---
description: Analyze component and suggest refactoring opportunities for better code quality
---

# Refactoring Suggestion Tool

Analyze the current component and get intelligent refactoring suggestions to improve:
- Code organization
- Reusability
- Maintainability
- Performance
- Readability

## Usage

Open a component file and run:
```bash
/suggest-refactor
```

## What Gets Analyzed

1. **Extract Custom Hooks**
   - Identify reusable logic
   - Suggest hook extraction

2. **Component Splitting**
   - Find large components
   - Recommend decomposition

3. **Props Optimization**
   - Simplify props interface
   - Suggest prop patterns

4. **State Management**
   - Identify state that could be lifted
   - Suggest context usage

5. **Code Organization**
   - Improve file structure
   - Better naming conventions

## Output Format

Provides:
- 🔍 What was analyzed
- 💡 Suggested refactorings
- 📝 Code examples (before/after)
- ✅ Benefits of each refactoring
- ⚠️  Considerations/trade-offs

## Example Suggestions

**Extract Hook:**
```
💡 Extract form logic into useForm hook
Benefits: Reusability, testability, cleaner component
```

**Split Component:**
```
💡 Split UserProfile into UserAvatar + UserDetails
Benefits: Single responsibility, easier maintenance
```

---

Claude will analyze the current file and provide actionable refactoring suggestions.
