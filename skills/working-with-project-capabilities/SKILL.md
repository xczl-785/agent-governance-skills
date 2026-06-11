---
name: working-with-project-capabilities
description: Use when a project already relies on capability documents, or when the user explicitly wants to adopt that mechanism for the current repository, and behavior changes must stay aligned with current capability docs
---

# Working with Project Capabilities

Use this only where capability docs are already part of the project's operating model, or where the user has explicitly chosen to introduce that mechanism.

## When to Use

- a repository already uses capability documents as current truth
- a behavior change must be tied to the right capability
- capability docs and code need to stay aligned after the change
- the user explicitly wants to bootstrap capability governance for this repository

Skip it for ordinary repos without capability governance unless the user has chosen to adopt it, and skip it for style-only changes or experiments that should not update current-truth docs.

## Loop

1. Detect whether the repository already has capability docs or a capability index.
2. If not, ask the user whether to adopt the capability mechanism before creating the first capability document.
3. Once the mechanism is confirmed, identify whether one capability, multiple capabilities, or a new capability is involved.
4. Read the light discovery path first, then the specific capability sections that matter.
5. Verify current truth in code before trusting the docs.
6. Make the code change with impact awareness across known entry points.
7. Write the updated current truth back to capability docs.

## Guardrails

- Do not treat historical discussion as current truth.
- Do not auto-bootstrap capability docs into a repository that has not opted into the mechanism.
- Do not read the whole repo when the capability scope can be layered and narrow.
- Use the references and script in this directory for creation rules, templates, and temporary indexing.
