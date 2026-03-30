---
name: paul-plan
description: Enter PLAN phase for current or new plan
argument-hint: "[phase-plan]"
allowed-tools: [Read, Write, Glob, Question]
---

<objective>
Create or continue a PLAN for the specified phase.

**When to use:** Starting new work or resuming incomplete plan.
</objective>

<execution_context>
@~/.opencode/paul-framework-opencode/workflows/plan-phase.md
@~/.opencode/paul-framework-opencode/templates/PLAN.md
@~/.opencode/paul-framework-opencode/references/plan-format.md
</execution_context>

<context>
$ARGUMENTS

@.paul/PROJECT.md
@.paul/STATE.md
@.paul/ROADMAP.md
</context>

<process>
Follow workflow: @~/.opencode/paul-framework-opencode/workflows/plan-phase.md
</process>

<success_criteria>
- [ ] PLAN.md created in correct phase directory
- [ ] All acceptance criteria defined
- [ ] STATE.md updated with loop position
</success_criteria>
