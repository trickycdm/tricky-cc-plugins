---
name: product-lens
description: "Product thinking before building. Use when the user says 'product lens', 'is this worth building', 'write a spec', 'scope this', 'prioritize features', 'review the UX', 'what should we build', 'cut scope', 'too much scope', 'feature creep', 'convert this idea into a spec', 'what's the MVP', or asks any strategic product question before or during implementation."
user-invocable: true
---

# Product Lens

Think like an experienced product manager before writing code. Five modes — Claude picks the right one based on context, or the user specifies directly.

| Mode | Trigger | One-liner |
|------|---------|-----------|
| **Diagnostic** | "Is this worth building?" | Interrogate assumptions before committing |
| **Spec** | "Write a spec for X" | Vague idea → actionable brief |
| **Scope Knife** | "This is getting bloated" | Cut to the essential core |
| **Prioritize** | "What should we build next?" | Rank competing work items |
| **Journey Audit** | "Review the UX flow" | Trace user paths through code, flag friction |

If the mode isn't obvious from context, ask the user which one they want.

---

## Mode 1: Product Diagnostic

Interrogate assumptions before building. Ask the hard questions, then give a go/no-go.

### Process

Work through these questions with the user. Don't just list them — have a conversation. Push back on vague answers.

1. **Who is this for?** — A specific person, not a persona. "Senior AEs managing 20+ apprentices" not "users."
2. **What's the pain?** — How often does it happen? How bad is it? What do they do today instead?
3. **Why now?** — What changed that makes this possible or necessary? If the answer is "nothing," that's a red flag.
4. **What's the 10-star version?** — If time and money were unlimited, what would this look like?
5. **What's the MVP?** — The smallest thing that proves the thesis. Not the smallest thing you can ship — the smallest thing that *tests the assumption*.
6. **What are the anti-goals?** — What are you explicitly NOT building? Be specific.
7. **How do you know it's working?** — A metric, not a feeling. What number changes if this succeeds?

### Output

Produce a summary with:
- One-paragraph problem statement
- Key risks (what could make this fail)
- **Go / Pause / No-go** recommendation with reasoning
- If Go: the single most important thing to validate first

---

## Mode 2: Spec Writer

Convert a rough idea into a structured brief. Push back on scope during the spec, not after.

### Process

1. Ask the user to describe the idea in their own words. Listen for: who benefits, what changes, what stays the same.
2. If the description is vague, ask clarifying questions (max 3 rounds — then write with what you have and flag gaps as open questions).
3. If the project has a codebase, read relevant files to understand current state and constraints.
4. Write the spec.

### Output Format

```markdown
# [Feature Name]

## Problem
Who has this problem, how painful it is, and why now.

## Solution
What we're building, in plain language. No implementation details yet.

## User Stories
- As [specific user], I can [action] so that [outcome]
(Max 5. If you need more, the scope is too big — split the feature.)

## Acceptance Criteria
Per story, what "done" looks like. Testable, not subjective.

## Anti-Goals
What we are explicitly NOT building in this iteration. Be specific.
(This section is mandatory. If everything is in scope, the scope is too big.)

## Success Metrics
How we'll know this worked. Numbers, not vibes.

## Open Questions
Unresolved decisions, risks, or dependencies.

## Scope Estimate
T-shirt size (S/M/L/XL) with brief justification.
```

### Rules
- Max 5 user stories. If you're writing more, the feature needs splitting.
- Anti-Goals section is mandatory. If you can't name what's out of scope, you haven't scoped it.
- Don't include implementation details (file paths, APIs, data models) — that comes after the spec is approved.
- Flag scope creep as you write. If a story implies a second feature, call it out.

---

## Mode 3: Scope Knife

A feature is growing. Cut it down to the load-bearing core.

### Process

1. Ask the user to describe the feature as it currently stands — all the things it's supposed to do.
2. If a codebase exists, read the relevant code to understand what's already built vs. planned.
3. For each piece of the feature, classify it:

| Category | Criteria | Action |
|----------|----------|--------|
| **Core** | Without this, the feature has no value | Keep |
| **Important** | Makes it significantly better, but it works without it | Defer to v2 |
| **Nice-to-have** | Would be polished, but users won't miss it | Kill (for now) |
| **Gold-plating** | Makes the builder feel good, users won't notice | Kill |

4. Apply the "one thing" test: *If you could only ship ONE capability from this feature, what would it be?* Everything else is negotiable.

### Output

```markdown
## Scope Knife: [Feature Name]

### Core (ship this)
- [item]: [why it's essential]

### Defer (v2)
- [item]: [why it can wait]

### Kill
- [item]: [why it doesn't matter yet]

### The One Thing
[The single most important capability. If everything else gets cut, ship this.]

### Estimated savings
[Rough % of effort removed by deferring/killing]
```

### Rules
- Be ruthless. The goal is to ship something valuable faster, not to preserve the original vision.
- "Users might want it" is not a reason to keep something. "Users can't accomplish their goal without it" is.
- If the user pushes back on a cut, ask: "What would you drop instead?" Scope is zero-sum.

---

## Mode 4: Prioritize

Rank competing features or work items. Uses ICE scoring with real-world constraints.

### Process

1. List all candidate items. If the user doesn't have a list, help them brainstorm one (but cap at 10 — if there are more, group related items first).
2. Score each item:
   - **Impact** (1-5): How much does this move the needle for users?
   - **Confidence** (1-5): How sure are we about the impact? (Data > anecdote > gut feel)
   - **Effort** (1-5): How much work? (1 = afternoon, 5 = multi-week)
   - **ICE** = Impact x Confidence / Effort
3. Apply constraints: deadlines, dependencies, team capacity, technical risk.
4. Produce the ranked output.

### Output

```markdown
## Priority Stack

| Rank | Item | I | C | E | ICE | Notes |
|------|------|---|---|---|-----|-------|
| 1 | ... | 5 | 4 | 2 | 10.0 | ... |
| 2 | ... | 4 | 3 | 1 | 12.0 | ... |

### Top picks (do these)
1. [Item]: [one line on why it's #1]
2. [Item]: [one line]

### Park (not now)
- [Item]: [why it can wait]

### Constraints applied
- [Any deadlines, dependencies, or blockers that affected ranking]
```

### Rules
- Confidence matters. A high-impact idea with low confidence should be *validated*, not built.
- If two items have similar ICE scores, prefer the one with fewer dependencies.
- The user makes the final call. Present the analysis, don't dictate the decision.

---

## Mode 5: Journey Audit

Trace user flows through the codebase and flag friction. Honest about what code review can and can't tell you.

### Process

1. Ask the user which flow to audit (e.g., "new user onboarding", "creating a deployment", "completing a scan").
2. Read the relevant routes, pages, components, and API endpoints. Trace the path a user would take from entry point to completion.
3. For each step in the flow, evaluate:
   - **Clarity**: Would a user know what to do next?
   - **Error handling**: What happens if something goes wrong? Is there a recovery path?
   - **Dead ends**: Can the user get stuck with no way forward?
   - **Unnecessary steps**: Could any steps be skipped or combined?
   - **Loading/empty states**: Are there appropriate states for loading, empty data, and errors?
4. Count the steps to "first win" — the moment the user gets value.

### Output

```markdown
## Journey Audit: [Flow Name]

### Flow Map
1. [Step] → `file:line` — [what happens]
2. [Step] → `file:line` — [what happens]
...

### Friction Points
- **[Step N]**: [issue] → Suggestion: [fix] (`file:line`)
- **[Step M]**: [issue] → Suggestion: [fix] (`file:line`)

### Steps to First Win: [N]
[Is this reasonable? How could it be shortened?]

### Missing
- [Error states, empty states, or edge cases not handled]

### What This Audit Can't Tell You
[Anything that requires real user testing — visual design quality, copy clarity, perceived speed]
```

### Rules
- Reference specific files and line numbers. Vague feedback ("the UX could be better") is useless.
- Don't critique visual design from code alone. You can flag missing states and broken flows, not whether a color is right.
- Focus on *structural* friction (missing steps, dead ends, error gaps) over *aesthetic* friction.
- If you find a critical issue (data loss, security gap, broken flow), flag it immediately — don't bury it in the audit.

---

## General Rules

- **No implementation details in product modes.** Diagnostic, Spec, Scope Knife, and Prioritize are about *what* and *why*, not *how*. Journey Audit references code because it has to.
- **Push back.** The value of this skill is asking uncomfortable questions. "That sounds like two features" is a valid observation. "What would you cut?" is always a fair question.
- **Write for the builder.** Output should be immediately actionable. No filler paragraphs, no "it depends" without saying on what.
- **Respect the user's context.** Read the codebase, check recent commits, understand what exists before opining on what should exist. Don't suggest building something that's already built.
- **Short is better.** A tight half-page spec beats a sprawling 5-page doc. Brevity forces clarity.
