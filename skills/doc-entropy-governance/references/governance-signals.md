# Governance Signals

## Purpose

Use these signals to detect when a repository's document system is no longer safe for `agent-first` reading and execution.

The goal is not to score prose quality. The goal is to find where the repository is misleading readers about current truth, document role, or reading priority.

## Main-Path Signals

- Entry documents mention many paths but do not establish reading priority.
- Key rules exist but are buried too deep to be discovered naturally.
- Important documents exist but are not routed from `README`, `AGENTS.md`, `CLAUDE.md`, or a visible index.
- Historical or reference material remains exposed on the main path.
- Top-level routing rules, local README guidance, and visible directory contents contradict each other.
- A top-level doc routes readers into an active directory that has no local index or README.

## Truth-Source Signals

- Multiple documents explain the same mechanism without authority labels.
- A summary document looks more current than the actual source.
- An old plan still appears side by side with the current rule path.
- A derived summary does not point back to its source.

## Currentness And Lifecycle Signals

- Documents claim to be "current", "only", or "temporary" without matching repository reality.
- Current status, long-term rule, and historical notes are mixed in one place.
- Drafts or WIP docs have no next step or disposition.
- Governance warnings have accumulated without closure conditions.
- Active-path docs route into deprecated areas for tracebacks, creating archive-semantic split.
- Planning outputs that are still under review or absorption are presented like stable truth.

## Responsibility And Structure Signals

- One document acts as entry, design note, historical log, and TODO list at the same time.
- Roadmaps contain large blocks of completed-version summaries.
- Collaboration docs keep growing through patch-style appends instead of routing outward.
- A large design or architecture doc should probably be split into overview plus topic documents.
- A decision surface or evidence surface is doing active work but is forced into a generic reference bucket.

## Overweight High-Weight Document Signals

Treat length as a structural warning when the document is high-weight, especially:

- `AGENTS.md`
- `CLAUDE.md`
- repository collaboration rules
- top-level entry or principle docs

An 800-line `AGENTS.md` usually means the main path has already degraded. The problem is not size by itself. The problem is that the entry path is carrying too many responsibilities.

## Rough Mapping From Signal To Action

- Main-path confusion -> repair routing, reduce exposure, restore reading order
- Truth-source ambiguity -> route to `safe-isolation` or `human-decision`
- Lifecycle ambiguity -> add state, next step, or reduce exposure
- Mixed responsibilities -> split or remove from active path
- Overweight high-weight entry -> consider entry + index + topic split
- Contradictory routing claims -> make active-path contradiction a `primary-theme` candidate
