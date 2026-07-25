---
type: work
title: "Data Semantics"
figure: abrial
description: A 1974 paper proposing an abstract model of a database as objects connected by relations, described with a binary relational structure and a language of predicates rather than record-and-field schemas. It treats the database as a working model of an evolving external world, covering how facts are acquired, deduced, and kept consistent as that world changes. Predates the B-Method by two decades but the paper's relation-and-predicate style of thinking about state is visibly the ancestor of Abrial's later specification calculi.
subdomains: [databases-and-data-management, programming-environments-and-object-systems]
year: 1974
url: https://hal.univ-grenoble-alpes.fr/hal-05150953/file/JeanRaymondAbrial-DataSemantics-1974.pdf
access: public
host: institutional
tags: [work]
---

# Data Semantics

**Venue/year:** IFIP Working Conference on Data Base Management, Cargèse (Corsica), France, April 1974 (proceedings pp. 1-60, ed. Klimbie & Koffeman, North-Holland).
**Source:** https://hal.univ-grenoble-alpes.fr/hal-05150953/file/JeanRaymondAbrial-DataSemantics-1974.pdf — deposited on HAL (France's national open-access repository, hosted by Université Grenoble Alpes), title/author/date confirmed via HAL's public metadata API (`api.archives-ouvertes.fr`, halId `hal-05150953`, produced date 1974-04-01). Note (revised in Phase 4): HAL's HTML *landing page* is gated by an Anubis anti-bot proof-of-work challenge, but the `/file/` path above is not — plain `curl -sL` against it returns HTTP 200 and the full 4.2MB PDF. The original Phase 3 note said the gating blocked fetches outright; it only blocks the landing page, so do not skip the fetch. Separately, the deposited PDF is a 30-sheet page scan with no text layer (two logical proceedings pages per sheet, printed page numbers 3-59), so it must be read visually — an empty `pdftotext` result here is not a failed download. Linked from the memorial/archive blog run by a colleague at jean-raymond-abrial.blogspot.com, which cites this as the paper having "disappeared from university libraries" before this deposit.

## Lessons
- [When a formalism feels almost right, check whether its primitive was borrowed from the mechanism you were escaping](../lessons/suspect-the-primitive-you-inherited.md)
- [A model's silence is not the world's absence; represent what you do not know as carefully as what you do](../lessons/model-ignorance-as-deliberately-as-knowledge.md)
- [Asking a question should not reveal whether the answer is stored, computed, or remembered](../lessons/asking-must-not-reveal-how-the-answer-is-produced.md)
- [Hanging behavior on the primitive operations unifies concerns that would otherwise be subsystems, and quietly destroys the ability to read a program locally](../lessons/one-extension-point-buys-uniformity-and-costs-local-reasoning.md)
- [Order is a claim you either make or decline, and declining it is the same act for a collection as for a sequence of statements](../lessons/order-is-a-claim-and-parallelism-is-its-absence.md)
- [Make hypothesis a first-class scope, so that asking what if uses the same machinery as recording what is](../lessons/give-hypothesis-the-same-standing-as-fact.md)
- [Begin at a level of description you cannot run, then descend along two axes that are never mixed](../lessons/start-above-executability-and-descend-along-two-axes.md)
- [The urge to invent a language is a programmer's reflex; mathematics already has the vocabulary, and the design belongs in a structure rather than a text](../lessons/borrow-mathematics-instead-of-inventing-a-notation.md)
