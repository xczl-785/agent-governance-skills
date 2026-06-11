# Authority Triage

## Purpose

Use this when authority cannot be resolved automatically.

The goal is not to force a decision. The goal is to hand it to a human in a stable format.

## When To Use

Use authority triage when at least one is true:

- two or more top-ranked sources conflict
- top-level routing rules and local routing rules disagree
- current-status docs and visible directory state disagree
- a document appears operationally current but lives outside the expected active area
- deprecation, retention, or split choice changes authority semantics

Do not use this when the conflict is mechanically solvable.

## Triage Output

Every `human-decision` handoff for authority conflict should include five fields:

1. `claim`
2. `claiming-doc`
3. `conflicting-evidence`
4. `why-auto-fix-is-blocked`
5. `human-decision-needed`

## Minimal Table

Use a short table whenever possible:

| Field | Content |
| --- | --- |
| `claim` | What the document is asserting |
| `claiming-doc` | Which file makes the assertion |
| `conflicting-evidence` | Which file, directory state, or routing rule disagrees |
| `why-auto-fix-is-blocked` | Which hard gate fails |
| `human-decision-needed` | The exact choice the maintainer must make |

## Typical Questions To Hand Off

- Which file is the unique current planning entry?
- Is this material still active execution input, or only active research surface?
- Is this deprecated area still required for tracebacks?
- Does this governance doc carry current operational authority despite its location?
- Should this material be split, retained, or de-exposed?

## Tie-Break Guidance

Do not collapse everything into one vague “docs conflict” note.

Prefer separate rows when the conflict types differ:

- routing conflict
- currentness conflict
- authority conflict
- lifecycle conflict

## Sequencing Multiple Triage Rows

When multiple authority conflicts coexist, sequence them in this order:

1. conflicts that could start the wrong workstream
2. conflicts that could misroute current truth
3. conflicts that could misclassify lifecycle or disposition
4. conflicts that mainly add reading friction

Examples:

- wrong current planning entry beats archive naming ambiguity
- operational authority conflict beats local readability cleanup
- truth-source contradiction beats minor index incompleteness

## Hard Rules

- Do not choose a winner when the winner is not mechanically provable.
- Do not rewrite conflicting docs into artificial consistency.
- Do not downgrade the conflict into a style issue.
- Do not omit visible directory state when it is part of the conflict.
- Do not hand off “please review” without naming the exact decision needed.
