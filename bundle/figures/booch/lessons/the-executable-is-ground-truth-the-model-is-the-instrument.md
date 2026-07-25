---
type: lesson
title: "The executable is the only ground truth, and it is also the worst place to learn what the system means"
figure: booch
works: [architecting-the-unknown, the-future-of-software-engineering, the-promise-the-limits-and-the-beauty-of-software]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# The executable is the only ground truth, and it is also the worst place to learn what the system means

**Lesson:** Two claims that sound opposed are both true, and holding them together is the whole skill. The first: nothing but the running artifact settles a question about behavior. Documents, diagrams, and models all drift, and a project whose output is documents has produced nothing. The second: an implementation contains every structural decision while communicating almost none of them, because the decisions are smeared across thousands of locations with no marker saying which lines were the choice and which were consequence. Asking someone to point at the structure in the source usually produces gesturing, not because the structure is absent but because it is not locally observable anywhere.

The consequence is that notation is a reasoning instrument, not a deliverable, and it should be judged by exactly one criterion: which decisions does it let a group make that they could not otherwise make together? Under that criterion most modelling apparatus is overbuilt. A few views chosen for the questions actually at issue, plus the recurring arrangements that animate the system, usually exhaust what a team needs; the rest is detail that the implementation will settle anyway. Someone who helped standardize a large modelling language can still say the language is secondary, and that is not self-deprecation but a correct ordering: the notation earns its place by improving the quality of decisions, never by describing the artifact completely.

This resolves the recurring fight between design-first and code-first practice as a false dichotomy about sequence. The two modes are not phases but a loop running at short period: reason about structure, produce something that runs, let what runs contradict the reasoning, revise, repeat, at the granularity of days rather than quarters. A programmer who believes this stops writing specifications intended to be complete before implementation and stops treating the absence of documentation as a virtue. They keep a deliberately thin, deliberately current model whose only purpose is to make the next expensive decision legible to more than one person.

**Source:** [The Future of Software Engineering](../works/the-future-of-software-engineering.md) — the passage where the author, having co-created a widely adopted modelling notation, subordinates it to running code while insisting models and abstractions are what let teams build the right thing. Also [Architecting the Unknown](../works/architecting-the-unknown.md) — the argument that structure is genuinely present in an implementation but dispersed past recoverability, and the account of daily practice alternating between architectural reasoning and inspecting what was built overnight; and [The Promise, the Limits, and the Beauty of Software](../works/the-promise-the-limits-and-the-beauty-of-software.md) on the executable as the primary artifact of each increment.
