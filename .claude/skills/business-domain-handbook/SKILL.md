---
name: business-domain-handbook
description: This skill should be used when creating a Senior Business Analyst handbook for a new business domain in retail, wholesale, banking, finance, or insurance in Vietnam, following a 7-stage research workflow with source prioritization, citations, and a Markdown handbook output.
---

# Business Domain Handbook Skill

## Purpose
- Produce a Senior Business Analyst domain handbook from a single business domain input.
- Apply a 7-stage research workflow mapped to 13 checklist sections.
- Deliver a Markdown handbook with citations, versioning, and an appendix for assumptions.

## When to Use
- Trigger when asked to research a new business domain and create a handbook/playbook.
- Apply when the domain is retail, wholesale, banking, finance, or insurance in Vietnam.

## Core Inputs
- Domain name
- Optional: industry segment, geography specifics, target customer type

## Output Standard
- Format: Markdown with a table of contents and numbered headings.
- File name: `Research_[domain]_v[major].[minor].[yyyyddMM].md`
- Length target: 5 to 20 Word pages when converted.
- Template: `references/handbook-template.md`

## Data Sources (Priority Order)
1. Legal and regulatory documents
2. Internal documents (public releases, training, user guides)
3. Industry reports
4. Paid data sources
5. Public websites

## Geography Rules
- Use Vietnam as primary scope.
- If Vietnam data is insufficient, use APAC or global industry practices.
- Document applied geography scope in the Appendix.

## Evidence and Inference Rules
- Synthesize only from cited sources.
- Allow light inference only for root-cause and opportunity analysis.
- Label inference explicitly as "Inference" with a short rationale.
- Convert unknowns into open questions in the Appendix.

## 7-Stage Workflow (Mapped to Sections)
1. Domain Foundation: Sections 1–2
2. Stakeholders & Success: Sections 3–4
3. Work & Roles: Sections 5–6
4. Data & Systems: Sections 7–8
5. Issues & Causes: Sections 9–10
6. Opportunities & Synthesis: Sections 11–12
7. Finalization: Section 13

## Quality Gates
- Verify each stage against checklist-style quality gates in `docs/research-plan.md`.
- Require all stage outputs before finalization.

## Definition of Done
- Confirm the handbook enables BAs to draft survey/interview questions, clarify current state, analyze root causes, and propose solution directions.

## Assumptions and Unknowns Handling
- Record assumptions in an Appendix with numbered references from the body.
- Keep assumptions minimal; prefer verified facts with citations.
- Document unknowns as open questions for readers to validate.

## Review Note
- Mark output as ready for Senior BA review; do not perform the review in the workflow.
