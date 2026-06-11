# Closure Ledger Example

Scenario: one pass finds eight governance risks near project closeout.

## Theme Ledger

| Theme | Bucket | Disposition | Action / reason |
| --- | --- | --- | --- |
| Broken README link | `auto-fix` | `fixed-now` | Repaired unique relative link. |
| Draft exposed from README | `safe-isolation` | `safe-isolated` | Removed from normal path; kept source reachable from review notes. |
| Old roadmap mixed with completion notes | `safe-isolation` | `safe-isolated` | Added status and routed completed notes to recap path. |
| Duplicate active-plan claims | `human-decision` | `human-decision-queued` | Recommend `docs/current-plan.md` as active source because it is routed from README; approval needed before demoting review output. |
| AGENTS.md mixes rules and history | `human-decision` | `human-decision-queued` | Recommend entry + topic split; approval needed because extraction changes authority surface. |
| Archive referenced for traceback | `safe-isolation` | `safe-isolated` | Labeled traceback-only; did not de-expose archive completely. |
| Derived summary lacks source pointer | `auto-fix` | `fixed-now` | Added pointer to source decision doc. |
| External policy reference stale | `human-decision` | `deferred-with-condition` | External source unavailable; unblock when policy URL/version is confirmed. |

## Final Reply Shape

Done:
- fixed the README link and source pointer
- isolated draft, roadmap recap, and traceback-only archive exposure

Needs decision:
- choose whether `docs/current-plan.md` is the single active plan source; recommended yes because it is the routed entry
- approve AGENTS.md entry + topic split; recommended yes because current rules and history share one high-weight path

Not changed:
- did not rewrite conflicting active-plan text before authority is chosen

Deferred:
- external policy reference; blocked until source version is confirmed
