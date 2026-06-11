# Pressure Scenarios

## How To Use These Scenarios

Use these scenarios to test baseline failure without the skill and compliance with the skill.

For each scenario, check both:

- what an agent does without governance guidance
- whether the skill prevents that failure or rationalization

## Agent-First Scenarios

### A1. Main-Path Misread On Cold Start

Setup:

- top-level entry docs exist
- a key rule is buried deeper
- the entry path does not surface it clearly

Baseline failure:

- the agent reads the top-level entry and starts work
- it assumes visible entry equals complete path

Expected with the skill:

- the agent questions whether the main path is actually complete
- it checks discoverability of high-weight rules before trusting the path

### A2. Overweight Entry Document

Setup:

- `AGENTS.md` or `CLAUDE.md` is very long
- current rules, history, exceptions, and patch notes are stacked together

Baseline failure:

- the agent assumes complete reading equals safe understanding
- priority and role boundaries remain unclear

Expected with the skill:

- the agent treats entry overweight as structural risk
- it considers entry routing, index routing, or topic split rather than linear accumulation

### A3. Roadmap Polluted By Completion Summaries

Setup:

- a roadmap mixes current plan with completed-version summaries and historical recaps

Baseline failure:

- the agent mistakes history for current planning signal
- it keeps appending into the same overloaded document

Expected with the skill:

- the agent considers split or active-path reduction
- it avoids patch-style continuation in the same overloaded route

### A4. Conflict Auto-Resolution

Setup:

- two documents disagree on the same mechanism
- one looks newer, one looks more authoritative

Baseline failure:

- the agent picks one by intuition
- it edits the other to unify wording

Expected with the skill:

- the agent stops short of truth resolution
- it routes the case to `safe-isolation` or `human-decision`

### A5. Draft Or Reference Leakage

Setup:

- draft or reference material remains exposed in active areas
- no status or truth-source pointer exists

Baseline failure:

- the agent treats the material as current
- it continues to build on the wrong document

Expected with the skill:

- the agent detects main-path pollution
- it favors status, pointer, de-exposure, or movement out of the active path

### A6. Mixed Responsibility Mishandling

Setup:

- a document contains redundancy and mixed roles
- some content remains valuable, some is obsolete

Baseline failure:

- the agent rewrites the whole document
- or leaves the whole document untouched because some value remains

Expected with the skill:

- the agent maps the problem toward deprecation or split-and-recover
- it does not let local value justify keeping the whole document on the active path

### A7. Marker Entropy

Setup:

- docs already contain notes like "check later" or "maybe stale"

Baseline failure:

- the agent adds more free-form warnings
- the notes do not converge toward closure

Expected with the skill:

- the agent refuses to add unstructured governance noise
- markers remain finite-state, trackable, and removable

### A8. Low-Hanging-Fruit Bias

Setup:

- the repository has both easy link issues and high-value truth-path risk

Baseline failure:

- the agent fixes only the easiest items
- it avoids the theme with the highest misleading risk

Expected with the skill:

- the agent chooses `primary-theme` by risk value first, landing risk second

### A9. Contradictory Active-Path Signaling

Setup:

- a top-level rule claims one unique active planning entry
- a local directory README permits multiple active planning or evaluation docs
- the visible directory contents support both readings

Baseline failure:

- the agent picks whichever doc feels newest
- or fixes minor wording while leaving the contradiction intact

Expected with the skill:

- the agent promotes active-path contradiction to a theme candidate
- it produces an authority-triage table instead of guessing

### A10. Deprecated Area Still Required For Traceback

Setup:

- active docs tell readers not to use deprecated content
- current status docs still route readers into deprecated areas for tracebacks

Baseline failure:

- the agent treats deprecated semantics as simple de-exposure
- it misses the archive-semantic split

Expected with the skill:

- the agent recognizes "deprecated for normal path, still required for tracebacks"
- it avoids naive cleanup recommendations

### A11. Multi-Theme Accumulation

Setup:

- one pass discovers several governance themes
- one theme is low-risk and easy to modify
- other themes are higher-risk, blocked, or require human authority choice

Baseline failure:

- the agent lands only the easy low-risk theme
- it says the skill only requires one current-run theme
- other discovered themes remain implicit or are vaguely left for later
- it relabels observed problems as signals, background, or out-of-scope notes to keep them out of the ledger

Expected with the skill:

- the agent creates a theme ledger for every discovered theme
- it lands only bounded safe changes, but triages blocked themes in the same run
- observed governance issues count even when they are outside the primary landing scope or not fully investigated
- no discovered theme exits without `fixed-now`, `safe-isolated`, `human-decision-queued`, or `deferred-with-condition`

### A12. Over-Questioning Instead Of Closure

Setup:

- a cleanup pass finds several mechanical or safely isolatable issues
- one or two issues require true authority choice
- the user expects end-of-work cleanup, not a long planning exchange

Baseline failure:

- the agent asks the user how to handle every theme
- it defers safe fixes while waiting for preference answers
- it upgrades reversible routing or status cleanup into human decision because the document is important
- final output is a backlog instead of a cleanup result

Expected with the skill:

- the agent directly fixes clear `auto-fix` items
- the agent safely isolates misleading exposure without deciding truth
- true human decisions are batched once with recommendations and reasons
- `Needs decision` names the hard gate that failed for each question
- final output separates `Done`, `Needs decision`, `Not changed`, and `Deferred`

## Human-Led Lightweight Scenarios

### H1. Rules Live In People's Heads

Baseline failure:

- the agent assumes the docs are sufficient because the team works fine synchronously

Expected with the skill:

- the agent treats missing documented priority as a real governance gap

### H2. Short Notes Without Authority Labels

Baseline failure:

- the agent mistakes concise notes for the full current route

Expected with the skill:

- the agent asks what role the note serves before trusting it

## Planning-Layer Scenarios

### P1. Evidence Promotion Pipeline

Setup:

- model outputs, review outputs, or test packages are still active inputs to planning
- they should not yet be treated as stable rule truth

Baseline failure:

- the agent collapses them into reference-only material
- or promotes them to stable truth too early

Expected with the skill:

- the agent recognizes evidence, review, absorption, and stable assets as distinct lifecycle states

### P2. Parallel Diagnostic Mainlines

Setup:

- one planning slice tracks structural correctness
- another tracks flavor, feel, or qualitative production readiness

Baseline failure:

- the agent treats the flavor diagnostic line as secondary note-taking
- it over-prioritizes whichever line looks more structural

Expected with the skill:

- the agent keeps parallel diagnostic mainlines visible when both are first-class planning inputs
