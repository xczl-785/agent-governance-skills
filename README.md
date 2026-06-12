# Agent-First Governance Skills

[中文说明](README.zh-CN.md)

When agents participate in a project over time, the main risk is not that they fail a single task. The risk is that they act on the wrong truth: treating old plans as current state, archives as active entry points, temporary conclusions as rules, or undocumented behavior as a stable boundary.

This repository collects reusable governance skills that keep long-running agent work aligned with current project truth, capability boundaries, and verified evidence.

The goal is not to make documentation prettier. The goal is to help agents keep working steadily over long periods by preserving a safe path to current truth, while also helping cold-start agents enter the project quickly, understand the operating context, and begin work safely. These skills reduce the chance that agents act on documentation drift, authority conflicts, confusing entry points, overexposed historical material, or missing behavior boundaries.

## Problems This Solves

In agent-first projects, the common failure mode is not a single missing fact. It is that project truth becomes harder to read and maintain over time:

- Documentation, plans, and implementation drift apart.
- Multiple documents appear authoritative for the same topic.
- Entry documents route agents into stale, conflicting, or overloaded material.
- Roadmaps, plans, archives, working notes, and temporary conclusions accumulate in the same places.
- Behavior changes lack stable capability boundaries, so code and docs cannot be maintained together.
- Cold-start agents have to guess the reading order, current rules, and safe change surface.
- Teams keep relying on one-off prompt fragments instead of reusable operating mechanisms.

## How It Works

The skills in this repository are not general writing templates. They are governance mechanisms for long-running agent work:

- Establish safe reading paths so agents know where to start, what is current truth, and what is only historical or reference material.
- Make document authority explicit, separating issues that can be auto-fixed, safely isolated, or handed to humans for a real decision.
- Maintain capability boundaries by keeping behavior entries, current rules, impact surfaces, shared dependencies, and evidence discoverable.
- Support cold-start onboarding so new agents can enter through stable project context instead of blindly reading the whole repository.
- Turn one-off collaboration rules into installable, portable, maintainable skills.

## Current Skills

### `doc-entropy-governance`

Use this to govern documentation entropy and restore a current-truth path that agents and maintainers can safely follow.

It focuses on whether the documentation system itself is still reliable: whether entry points are clear, authority is unique, historical material is overexposed, and roadmaps or plans carry too many responsibilities. It does not guess semantic truth for maintainers. It separates findings into auto-fix, safe-isolation, and human-decision paths, with misleading-risk reduction as the priority.

Typical cases:

- Multiple documents appear authoritative for the same topic.
- Entry documents route readers or agents into stale, conflicting, or overloaded material.
- Roadmaps, plans, archives, and working notes are mixed together, making current state unclear.
- Governance cleanup is needed, but current truth cannot be chosen safely by automation.

### `working-with-project-capabilities`

Use this when a project already relies on capability documents, or when a maintainer explicitly chooses to adopt that mechanism, and behavior changes must stay aligned with capability boundaries.

A capability document is not ordinary prose documentation. It is the current truth source for a stable project capability: its boundary, entries, current rules, impact surface, shared dependencies, consumers, and verification evidence. This skill helps agents find the relevant capability before code changes and write verified current truth back after code changes.

Typical cases:

- A behavior change must stay aligned with an existing capability doc.
- A new behavior has formed an independent capability boundary that should be maintained.
- Capability docs and implementation need to be updated together.
- A temporary capability index is needed to make current capability docs discoverable.

This skill does not automatically bootstrap capability governance into a blank repository. It creates or maintains capability docs only when the project already uses the mechanism, or when the user explicitly confirms adoption.

## Recommended Use

For larger repositories, use code structure exploration before writing claims into governance or capability docs. Confirm real entry points, consumers, ownership boundaries, and dependency surfaces so current-truth docs are evidence-backed rather than speculative.

When implementation changes are involved, prefer a TDD loop:

1. Capture the expected behavior with a focused failing test.
2. Implement the smallest production change that satisfies the test.
3. Refactor only after the behavior is protected.
4. Update the relevant capability or governance docs after verifying the code.

If the problem is that agents can be misled by the documentation path, start with `doc-entropy-governance`. If the problem is that code behavior needs to stay synchronized with a capability boundary, start with `working-with-project-capabilities`.

## Operating Rules

General agent-first collaboration rules live in [docs/agent-first-operating-rules.zh-CN.md](docs/agent-first-operating-rules.zh-CN.md).

These rules are kept outside individual skills because they describe cross-cutting operating principles. If a rule set later gains a clear trigger, execution loop, and output contract, it can be promoted into a standalone skill.

## Installation

Copy the desired skill directory into your agent tool's skill directory:

```powershell
Copy-Item .\skills\doc-entropy-governance <your-skills-dir>\doc-entropy-governance -Recurse
Copy-Item .\skills\working-with-project-capabilities <your-skills-dir>\working-with-project-capabilities -Recurse
```

Install only the skill you need if you do not want both.

Other agent runtimes can reuse the same directories as long as they support skill-style instruction bundles.

## Layout

```text
skills/
  doc-entropy-governance/
    SKILL.md
    examples/
    references/
  working-with-project-capabilities/
    SKILL.md
    agents/
    references/
    scripts/
docs/
  agent-first-operating-rules.zh-CN.md
```

## Publishing Notes

Keep each skill self-contained:

- Put the trigger and main workflow in `SKILL.md`.
- Put reusable deep guidance in `references/`.
- Put executable helpers in `scripts/`.
- Put expected outputs or usage patterns in `examples/`.
- Avoid machine-local paths, private project names, secrets, and unstable historical notes.

## License

MIT. See [LICENSE](LICENSE).
