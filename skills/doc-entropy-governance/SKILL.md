---
name: doc-entropy-governance
description: Use when a document-heavy repository has drifted, conflicting truth sources, or overloaded entry documents and needs low-risk governance cleanup
---

# Doc Entropy Governance

Use this when the main problem is that the documentation system no longer gives a safe reading path.

## When to Use

- entry documents no longer guide readers to current truth
- multiple documents appear to be authoritative for the same topic
- heavy documents mix current rules, drafts, and history
- governance cleanup is needed without rewriting the whole repo

Skip it for copyediting, formatting, or code correctness work.

## Loop

1. Recover the current reading path and authority order.
2. Inventory every governance theme discovered in the pass.
3. Assign each theme a risk, bucket, and disposition.
4. Choose the primary theme by misleading-risk first, landing-risk second.
5. Close what can be closed: auto-fix clear issues and safe-isolate misleading ones.
6. Batch true human authority decisions with recommendations and continue after approval.

## Theme Ledger

Narrow landing does not mean narrow accounting. Any governance issue observed during the pass counts as a discovered theme, even if it is outside the primary landing scope or not fully investigated.

Every discovered theme must leave the current run with one visible disposition:

- `fixed-now`
- `safe-isolated`
- `human-decision-queued`
- `deferred-with-condition`

For every non-fixed theme, name the target, why it cannot be auto-fixed, and the next condition that would unblock it.

Stop only when the ledger accounts for every discovered theme. Do not stop after the first low-risk fix while leaving other known themes implicit.

## Closure Default

Documentation governance is cleanup, not backlog creation. Prefer closure in this order:

1. `auto-fix` when the rule is clear, target unique, result verifiable, and semantics unchanged.
2. `safe-isolate` when truth cannot be chosen but misleading exposure can be reduced.
3. `human-decision` only when authority, deletion, deprecation, or current truth must be chosen.

Do not ask the user to decide things the repository already determines. Reversible status, routing, or preservation edits are not `human-decision` just because the document is important or the cleanup is larger than one line.

When human choice is required, batch all questions once, name the hard gate that failed, give a recommended option with reasons, then execute the approved choice.

Use `deferred-with-condition` only when the user declines a decision, external facts are unavailable, or the issue is outside the scan boundary.

## Output Contract

Final replies must be short and include:

- `Done`: fixes or isolations landed.
- `Needs decision`: batched human choices with the recommended option.
- `Not changed`: risky items intentionally left untouched and why.
- `Deferred`: only items with blocker and unblock condition.

See `examples/closure-ledger-example.md` for the expected shape.

## Guardrails

- Discover broadly, but land narrowly.
- Low-risk only limits modification. High-risk themes still need triage or handoff.
- Do not auto-resolve semantic truth conflicts.
- Do not use "later" as a disposition unless it has a target, blocker, and next condition.
- Use the examples and references in this directory for heavier governance patterns.
