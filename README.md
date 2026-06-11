# Agent Governance Skills

Reusable Codex skills for keeping agent work aligned with durable project truth.

## Repository Description

Governance-oriented Codex skills for document entropy cleanup, capability docs, code-aware context, and test-backed agent workflows.

## Suggested Topics

`codex`, `codex-skills`, `ai-agents`, `agent-workflows`, `documentation-governance`, `knowledge-management`, `capability-docs`, `tdd`, `codegraph`, `developer-tools`

## Skills

### `doc-entropy-governance`

Use this when a documentation system no longer gives readers or agents a safe path to current truth.

Typical cases:

- Multiple docs appear authoritative for the same topic.
- Entry documents route readers to stale or conflicting material.
- Roadmaps, plans, archives, and working notes have mixed responsibilities.
- Cleanup is needed, but semantic authority cannot be guessed safely.

The skill favors low-risk governance cleanup: auto-fix mechanical issues, safe-isolate misleading exposure, and batch true human authority decisions.

### `working-with-project-capabilities`

Use this when a project already relies on capability documents, or when a maintainer explicitly chooses to adopt that mechanism.

Typical cases:

- A behavior change must stay aligned with an existing capability doc.
- A new behavior needs a stable capability boundary.
- Capability docs and implementation need to be updated together.
- A temporary capability index is needed to make current capability docs discoverable.

The skill intentionally asks before bootstrapping capability governance into a repository that does not already use it.

## Recommended Workflow

For larger repositories, pair these skills with a code structure explorer such as `codegraph`. A code graph helps identify real entry points, consumers, ownership boundaries, and dependency surfaces before writing governance claims into current-truth docs.

When implementation changes are involved, prefer a TDD loop:

1. Capture the expected behavior with a focused failing test.
2. Implement the smallest production change that satisfies the test.
3. Refactor only after the behavior is protected.
4. Update the relevant capability or governance docs after verifying the code.

This keeps documentation updates evidence-backed instead of speculative.

## Installation

Copy the desired skill directory into your Codex skills directory:

```powershell
Copy-Item .\skills\doc-entropy-governance $env:USERPROFILE\.codex\skills\doc-entropy-governance -Recurse
Copy-Item .\skills\working-with-project-capabilities $env:USERPROFILE\.codex\skills\working-with-project-capabilities -Recurse
```

Install only the skill you need if you do not want both.

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
