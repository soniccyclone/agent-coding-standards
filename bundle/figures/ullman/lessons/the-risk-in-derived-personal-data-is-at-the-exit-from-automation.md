---
type: lesson
title: "The risk in derived personal data sits at the exit from automation, not at its collection"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# The risk in derived personal data sits at the exit from automation, not at its collection

**Lesson:** Arguments about systems that infer things about people usually collapse into a single axis — collect the data or do not — and that framing makes the question unanswerable, because the inference is what makes the service work and users mostly prefer the version that works. The more useful decomposition puts the danger somewhere else. A derived attribute consumed only by a program that immediately turns it into a selection, and then discards it, has a narrow and characterisable blast radius. The same attribute, materialised into a store that people can query, export, join against other stores, or be compelled to hand over, is a different object with a different risk profile, and almost all of the harm anyone actually fears lives on that second path.

This reframing gives you engineering handles where the collect-or-not framing gave you none. The boundary between machine-only use and human-reachable use is a real, enforceable line: it can be drawn in the architecture as a service that answers decisions rather than serving attributes, with the derived features never leaving the process that computes them and never landing in a queryable table. Retention becomes a design parameter rather than a policy footnote, since a feature needed only for the current decision need not outlive it. Access to the human-reachable side becomes an auditable, small, and expensive thing rather than an incidental consequence of the pipeline existing.

The design instruction that follows is to identify, for every derived attribute in a system, the exact set of paths by which it can reach a person, and to treat shrinking that set as the primary safety work — ahead of arguing about whether the attribute should exist. Two systems that collect the same signals and infer the same things can differ enormously in exposure depending only on whether the inference is a transient intermediate or a durable record, and that difference is entirely within the builders' control.

The honest caveat is that no arrangement here satisfies everyone, and pretending otherwise is worse than admitting it. Some will object to the inference regardless of where it goes; the argument does not have a technical resolution and should not be presented as one. What the decomposition buys is not consensus but a place to apply effort that actually reduces harm, instead of a debate that reduces none.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the advertising chapter's treatment of user-targeted display ads, which lists the several ways an interest can be inferred, declines to claim the resulting privacy question has any solution satisfying all concerns, and locates the potential for misuse specifically at the point where the information leaves the machines running the algorithms and reaches people.
