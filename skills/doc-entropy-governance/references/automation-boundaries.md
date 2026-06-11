# Automation Boundaries

## Three Buckets

Every chosen theme must be exactly one of:

- `auto-fix`
- `safe-isolation`
- `human-decision`

## Auto-Fix

Use `auto-fix` only when:

- the rule is clear
- the target is unique
- the result is verifiable
- authority semantics do not change

Typical `auto-fix` actions:

- repair an internal relative link with one clear target
- replace a local absolute path with a repository-relative path
- add a standard state/disposition header to an obvious draft or reference doc
- add a truth-source pointer to a clear derived summary
- add a missing README entry when only one reasonable route exists

Do not use `auto-fix` for:

- conflict resolution
- authority selection
- deletion of potentially valuable historical material
- large rewrites
- non-unique split targets

## Safe-Isolation

Use `safe-isolation` when the problem is real but truth cannot be auto-decided.

Typical `safe-isolation` actions:

- add a standardized status/disposition marker
- add a truth-source pointer
- reduce exposure of material that should not stay on the main path
- generate a conflict report or candidate source explanation
- route unresolved issues to a stable output location

Safe isolation lowers misleading risk without pretending the conflict is solved.

## Human-Decision

Use `human-decision` when the repository needs a real semantic judgment.

Typical cases:

- multiple documents conflict and authority must be chosen
- rule docs and long-term asset docs disagree
- disposition between keep, split, deprecate, delete, or rewrite is not obvious
- terminology unification may rewrite historical meaning
- cross-repo or external dependency validity cannot be verified mechanically
- active routing rules and visible directory state contradict each other in a way that requires authority choice

Expected outputs:

- issue
- decision queue
- conflict summary
- PR draft
- authority-triage table

## Four Hard Gates Before Modification

Do not modify content unless all four are true:

1. The rule is clear.
2. The target is unique.
3. The result is verifiable.
4. Authority semantics do not change.

If any gate fails, fall back to `safe-isolation` or `human-decision`.

## Primary-Theme Tie-Breaker

When several high-risk themes coexist, prefer the theme most likely to send the next agent or user into the wrong workstream.

Examples:

- contradictory active-state signaling beats cosmetic routing cleanup
- authority conflict beats local readability polish
- wrong current-entry selection beats minor link repair

## Governance Markers

Markers are temporary governance objects, not conclusions.

Any governance marker must:

- use a finite state rather than free-form notes
- identify the target
- explain why it exists
- name the next step
- define when it should be removed

If a marker cannot satisfy these conditions, do not add it.

## Planning-Layer Stop Rules

Do not deprecate or de-expose material merely because it is not stable truth if it still serves one of these current roles:

- review-stage material awaiting absorption
- live evidence used for current decisions
- decision-surface documentation that governs current branching or promotion

Before reducing exposure, verify the downstream writeback target or decision target exists.
