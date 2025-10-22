---
description: Analyze the current React component for best practices, performance, and code quality
---

# Component Analyzer

Analyze a React component for:
- Best practices adherence
- Performance issues
- Accessibility concerns
- TypeScript usage
- Code organization
- Potential bugs

## Usage

Open a component file and run:
```bash
/analyze-component
```

## What Gets Analyzed

1. **Component Structure**
   - Proper export patterns
   - Component naming
   - File organization

2. **React Best Practices**
   - Hooks usage (rules of hooks)
   - Props validation
   - Key props in lists
   - Event handler naming

3. **Performance**
   - Unnecessary re-renders
   - Missing memoization opportunities
   - Large component size
   - Expensive computations

4. **TypeScript**
   - Proper typing of props
   - Any types usage
   - Return type inference

5. **Accessibility**
   - Semantic HTML
   - ARIA attributes
   - Keyboard navigation

## Output

Provides a detailed report with:
- ✅ What's good
- ⚠️  Warnings
- ❌ Critical issues
- 💡 Suggestions for improvement

---

Claude will analyze the current file in context and provide detailed feedback on improvements.
