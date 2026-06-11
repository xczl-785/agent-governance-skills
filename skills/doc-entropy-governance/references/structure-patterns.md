# Structure Patterns

## Runtime, Rule, Decision, Evidence, And Deprecated Areas

In `agent-first` governance, ask what current role the material serves before asking how history should be archived.

A stronger first-pass model is:

- runtime-active: current execution path and immediate execution inputs
- rule-truth: stable rules or long-lived truth sources
- decision-surface: materials that answer current branching, gating, or progression decisions
- live-evidence: current evidence or review outputs that still influence decisions
- reference: useful support material that is not currently authoritative
- deprecated: material that should not continue to guide current work

This is more useful than collapsing everything into active/reference/deprecated, especially in planning-heavy repositories.

## Function Over Location

Do not classify a document only by the directory it lives in.

A governance document can still be current operational authority if:

- the active path explicitly routes into it
- it constrains current execution, branching, or promotion
- current work would be unsafe without it

In that case, classify it by function first, then note that its physical location may be misleading.

## Operational Governance Truth Outside Nominal Active Areas

Some repositories keep a document outside the nominal active directory, but still require it for safe current execution.

Typical signs:

- the active path explicitly routes into it
- it defines current role boundaries, branching, promotion, or coordination
- current work would become unsafe if the document were ignored

In that case:

- do not downgrade it to reference merely because of location
- classify it as current operational authority
- if it conflicts with higher-surface routing, use authority triage rather than location-based cleanup

## Deprecation Before Archival

For this skill, `deprecated` matters more than `archived`.

Why:

- agents rarely need inactive assets except for decision tracing
- the main governance risk is continued exposure, not elegant storage
- many so-called archival actions are really active-path removal actions

Use `deprecated` when the material should no longer carry current responsibility, even if it still deserves preservation.

## Archive-Semantic Split

Some repositories use deprecated or archive-like areas in two ways at once:

- not part of the normal active reading path
- still required for tracebacks, provenance, or historical verification

Treat this as `archive-semantic split`, not as simple deprecation.

When active docs still route readers into such areas, do not recommend naive de-exposure before clarifying the traceback role.

## Two Main Mappings For Redundancy And Mixed Responsibility

When a document becomes redundant or overloaded, prefer one of two mappings:

1. exit the active path into deprecated semantics
2. split and route surviving content back to clearer target documents

Do not let "some of this is still useful" justify keeping the entire overloaded document as a current entry.

## Promotion Pipeline Pattern

Planning-layer repositories often need a promotion pipeline:

- evidence or test output
- review or absorption
- stable rule, mechanism, or template

Do not force all non-stable material into plain reference semantics. Some material is still current because it is awaiting absorption into a downstream stable target.

## Roadmap Split Pattern

A roadmap should not quietly become:

- current plan
- completion digest
- historical recap
- working log

When this happens, prefer:

- keep a current roadmap for forward-looking direction
- move completed-version summaries into separate recap/history material
- reduce historical exposure on the active path

## Entry + Index + Topic Pattern

This pattern is useful when a high-weight entry has become too long.

- entry: the shortest high-priority reading path
- index: discovery and routing only
- topic docs: detailed rules or topic truth

The index should not become a second giant rule doc. Its job is route clarity, not rule duplication.

## When Index Helps

An index is a good candidate when:

- key rules are real but too deep to discover naturally
- one entry doc has become overloaded
- multiple topic docs need a lightweight route layer

## When Index Becomes New Entropy

An index can backfire when:

- document assets change too fast for index maintenance
- the index repeats detailed rules instead of routing
- the index starts carrying current status or history directly

If index drift risk is too high, prefer smaller entry cleanup and topic routing before creating a new index layer.

## Authority Lattice

When multiple routing layers coexist, prefer this trust order unless the repository clearly defines a stricter one:

1. entry-routing rules
2. current state board
3. local index or local README
4. working docs
5. archive or reference areas

Always separate:

- safe reading order
- current active theme

Those are related, but they are not the same question.
