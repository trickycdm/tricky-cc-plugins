---
name: optimize-doc
description: "Optimize documentation for conciseness and clarity. Strengthens vague instructions with explicit criteria, removes redundancy while preserving meaning, and tightens prose. Use when the user says 'optimize this doc', 'tighten this', 'make this more concise', 'clean up this documentation', 'this doc is too long', 'remove redundancy', or asks to improve a markdown/documentation file."
user-invocable: true
---

# Optimize Documentation

Make documentation more concise and clearer. Strengthen vague instructions, remove redundancy, preserve meaning.

**Priority order**: Correctness > Efficiency > Conciseness. Never sacrifice meaning for brevity.

**Idempotent**: First pass strengthens and trims. Second pass tightens further. Subsequent passes produce no changes.

## Process

### 1. Identify Target

If the user specified a file, use it. Otherwise ask which file or directory to optimize.

Read the full document before making any changes.

### 2. Analyze Each Section

For every instruction section, apply the **Execution Test**:

```
Can Claude execute this correctly without the content in question?
├─ NO → KEEP (execution-critical)
└─ YES
    ├─ Does it explain WHY (rationale/educational)? → REMOVE
    ├─ Does it show WHAT "correct" looks like? → KEEP
    ├─ Does it extract a reusable decision rule? → KEEP
    └─ Is it redundant with another section? → REMOVE
```

### 3. Evaluate Instruction Clarity

Cover the examples and read only the instruction text:
- Can it be executed correctly without the examples?
- Does it use subjective terms ("properly", "clearly") without definition?
- Are there measurable criteria or explicit steps?

**If vague**: Strengthen the instruction first — replace subjective terms with explicit criteria, convert narrative to steps, add thresholds. Keep all examples until the instruction can stand alone.

**If clear**: Evaluate whether examples are still needed (see keep/remove guidance below).

### 4. Apply Changes

Strengthen vague instructions and remove redundancy in a single pass where possible. For complex documents, use multiple passes.

### 5. Report

Output a summary of changes:

```markdown
## Optimization Summary

**Changes:**
1. [Section] (Lines X-Y): [what changed and why]

**Metrics:** N lines removed | M sections strengthened

**Status:** Fully optimized | Run again for further tightening
```

## What to Keep

- **Executable commands**: bash, jq, git workflows, CLI examples
- **Data structures**: JSON formats, config schemas, API contracts
- **Success criteria**: What "correct" looks like, verification steps
- **Boundary examples**: Wrong vs right patterns, edge cases
- **Sequential workflows**: Numbered steps where order matters
- **Disambiguation**: Examples that resolve ambiguity in instruction wording
- **Pattern extraction**: Annotations that generalize examples into reusable rules (e.g., `→ Shows that "delete" means remove lines, not change checkbox`)
- **Quick-reference lists**: Even if a detailed section covers the same topic — they serve different purposes (scanning vs understanding)

## What to Remove

- **Rationale/educational content**: Explanations of WHY, not WHAT or HOW
- **Redundant restating**: Examples that just rephrase a clear instruction
- **Obvious applications**: Trivial demonstrations of clear rules
- **Duplicate templates**: Multiple versions of the same format
- **Verbose walkthroughs**: Narrative prose when numbered steps already exist
- **Generic commentary**: "This is a good practice" without extracting a decision rule

## Condensing with References

**Never replace with references:**
- Content inside sequential workflows (breaks execution flow)
- Quick-reference lists (different purpose than detailed sections)
- Success criteria at decision points (must be inline)

**OK to replace with references:**
- Explanatory content duplicated across sections
- Background/context at document boundaries
- Cross-references to related concepts

**Before consolidating duplicates, verify:**
1. Content is semantically equivalent (not just topically similar)
2. Same level of detail (don't replace a 7-item checklist with a 3-item summary)
3. Same purpose (don't replace "do X" with "when to do X")
4. No workflow interruption

## Conciseness Techniques

- Replace verbose phrases: "you MUST execute" → "execute", "in order to" → "to"
- Remove filler: "clearly", "obviously", "simply", "it should be noted that"
- Convert prose paragraphs to bulleted lists
- Use tables for multi-dimensional information
- Consolidate overlapping sections

**Never sacrifice for conciseness:**
- Vertical lists (don't convert to comma-separated prose)
- Section headers that aid navigation
- Explicit criteria ("ALL", "at least ONE", "NEVER")
- Measurable thresholds
- Prevention patterns (prohibited vs required)

## Rules

- Read the full document before editing
- Every change must preserve meaning AND executability
- If optimization reduces clarity, reject the change
- Don't auto-commit — present changes to the user first
- Strengthen vague instructions before removing their examples
