# Workflow Principles

Core principles for effective Claude Code development workflows.

## Planning

### Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately - don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### Plan Lifecycle
When executing work against a plan in the `plans/` directory:
- A `worklog.md` is auto-created in the plan folder alongside `plan.md`
- Append a row to the worklog table after completing each meaningful step
- Format: `| YYYY-MM-DD HH:MM | action | brief detail |`
- Keep entries terse — one line per action, not paragraphs
- If resuming a plan from a previous session, read the worklog first to pick up context

### Re-planning Rules
- **NEVER create a new plan file when re-planning.** Edit the existing `plan.md` in place.
- When a step fails, an assumption was wrong, or the approach needs to change:
  1. Log a `RE-PLAN` entry in the worklog: `| timestamp | RE-PLAN | reason for change |`
  2. Edit plan.md — update affected steps, ~~strikethrough~~ abandoned approaches, add new approach inline
  3. Add a `## Revision Log` section at the bottom of plan.md if it doesn't exist
- One plan folder = one consolidated artifact
- When done, run `/wrap-up` to finalize the plan and capture lessons

## Execution

### Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

### Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes - don't over-engineer
- Challenge your own work before presenting it

## Learning

### Self-Improvement Loop
- After ANY correction from the user: update the workspace level CLAUDE.md with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### Knowledge Capture
- Use `/learn` to update steering documentation
- Patterns that work become commands
- Commands that compose become workflows
- Workflows that repeat become skills

## Task Management

1. **Plan First**: Write plan before implementation
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add to existing plans and worklogs
6. **Capture Lessons**: Update lessons after corrections

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Follow KISS and DRY principles.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Autonomous Operation**: When given a bug report: just fix it. Don't ask for hand-holding.
- **Zero Context Switching**: Point at logs, errors, failing tests - then resolve them.

## The Development Lifecycle

```
Plan → Implement → Review → Test → Learn → Ship
 │         │         │       │       │       │
 │    worklog.md  /review  /test  /learn  /commit
 │                                   │
 └────────── Feedback Loop ──────────┘
```

Each phase feeds into the next, creating a compounding effect where every session improves future work.