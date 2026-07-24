---
type: lesson
title: "Undeclared redundancy is a latent inconsistency"
figure: codd
works: [derivability-redundancy-and-consistency-of-relations-stored-in-large-data-banks, a-relational-model-of-data-for-large-shared-data-banks]
axes: [verifiability]
subdomains: [databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# Undeclared redundancy is a latent inconsistency

**Lesson:** Before anyone can control duplication, "derivable" has to mean something exact, so Codd defines it as reachability through a fixed set of operations whose outputs are unique, holding over time rather than at one lucky instant. On that footing he can classify redundancy (data recomputable from the rest, versus data merely constrained by the rest) and state the operational consequence: every redundancy that exists must exist as a written constraint, because a system cannot deduce the semantic relationships among its own data and any attempt to induce them from observed values is fallible. Whatever is not declared cannot be checked, and what cannot be checked will silently diverge.

Consistency then gets an unusual and clarifying definition: it is a property of the instantaneous state against the declared constraints, deliberately independent of the history that produced the state and of whether the violating user erred by commission or omission. That separation is what makes checking mechanical (evaluate the constraints against a snapshot) and what makes response policy a separate, tunable decision: check on every mutation, or sweep in batch and trace violations through a journal, with the system escalating to a human when a violation persists. Detection is decoupled from blame and from repair.

Codd also splits the ledger by audience: redundancy in the user-facing set of relations exists for convenience and for keeping old programs alive, while redundancy in the stored set exists for performance, and only the latter is the administrator's to add or remove. A programmer holding this lesson treats every cache, denormalized column, materialized aggregate, and replicated config as a proposition that must be written down in checkable form, builds the checker alongside the duplication, and regards duplicated state with no declared invariant as a bug that merely has not fired yet.

**Source:** [Derivability, Redundancy, and Consistency of Relations Stored in Large Data Banks](../works/derivability-redundancy-and-consistency-of-relations-stored-in-large-data-banks.md) — Sections 5 and 6: the time-qualified definition of derivability, strong and weak redundancy, consistency against declared constraint statements, and the data bank control policies. Also [A Relational Model of Data for Large Shared Data Banks](../works/a-relational-model-of-data-for-large-shared-data-banks.md) (Section 2's polished treatment, including the state-not-history view of consistency and the omission/commission point).
