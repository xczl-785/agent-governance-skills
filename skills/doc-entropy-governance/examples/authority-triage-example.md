# Authority Triage Example

## Situation

A top-level rule says there should be one unique active planning entry.

The local planning directory still exposes multiple plausible active planning docs.

## Wrong Response

- pick the newest-looking file
- update a few labels
- pretend the contradiction is resolved

## Better Response

Produce a short authority-triage table:

| Field | Content |
| --- | --- |
| `claim` | Only one planning handoff should remain active |
| `claiming-doc` | `AGENTS.md` |
| `conflicting-evidence` | The planning directory still contains multiple plausible active planning docs and a local README that permits active evaluation inputs |
| `why-auto-fix-is-blocked` | Target is not unique and authority semantics would change |
| `human-decision-needed` | Which file is the unique current planning entry, and which remaining files stay active versus move to reference or deprecated status |

## Why This Matters

The point is not to avoid action.

The point is to convert an unsafe hidden judgment into an explicit handoff that a maintainer can answer cleanly.

