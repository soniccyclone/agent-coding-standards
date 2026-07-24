---
type: lesson
title: "Refine a definition until its arbitrary distinctions vanish"
figure: codd
works: [recent-investigations-in-relational-data-base-systems, further-normalization-of-the-data-base-relational-model]
axes: [primitive-count, verifiability]
subdomains: [databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# Refine a definition until its arbitrary distinctions vanish

**Lesson:** A concept's first published definition usually carries scaffolding from the path of its discovery. Codd's original normal forms leaned on a classification of attributes as prime or non-prime, on a designated primary key, and on auxiliary notions of full and transitive dependence; his own 1974 survey calls the prime/non-prime distinction somewhat arbitrary and reports the replacement he and Boyce reached, a single condition quantified uniformly over all attribute collections, with no privileged key and no auxiliary vocabulary. The payoff he records is not elegance for its own sake: dropping the case analysis significantly simplified the normalizing algorithm. A cleaner statement of what a thing is directly shortened the procedure for producing it.

That is the transferable method. Treat every special case, privileged element, or helper concept inside a definition as a debt to be discharged, and keep restating the definition until either the distinction disappears or it proves load-bearing. The test for arbitrariness is whether the distinction tracks anything in the underlying structure or merely tracks the order in which the ideas were found; under the discovery framing, the definition with fewer moving parts is the closer approximation to the structure that was there all along, and the sign that a reformulation is right is that things downstream of it (proofs, algorithms, explanations) get shorter. The survey also shows the corrective loop running socially: Codd folds in Kent's improvements and credits Boyce, revising his own published foundations within three years of laying them.

A programmer who works this way audits definitions the way others audit code: a spec whose rules enumerate cases, a type hierarchy with a blessed subclass, an invariant stated with exceptions, all get the same challenge — restate it uniformly and see what breaks. When nothing breaks and the implementation shrinks, the original distinction was scaffolding, and leaving it in the published definition would have taxed every future user of the concept.

**Source:** [Recent Investigations in Relational Data Base Systems](../works/recent-investigations-in-relational-data-base-systems.md) — the normalization section reporting Kent's improvements and the Boyce-Codd reformulation of third normal form, with the explicit note that the simpler definition simplifies the normalizing algorithm. Read against [Further Normalization of the Data Base Relational Model](../works/further-normalization-of-the-data-base-relational-model.md), whose prime/non-prime machinery is the scaffolding the reformulation removed.
