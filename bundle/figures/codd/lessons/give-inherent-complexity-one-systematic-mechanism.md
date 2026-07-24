---
type: lesson
title: "Give inherent complexity one systematic mechanism, not many local dodges"
figure: codd
works: [codds-12-rules, extending-the-database-relational-model-to-capture-more-meaning]
axes: [cognitive-load, verifiability]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# Give inherent complexity one systematic mechanism, not many local dodges

**Lesson:** Missing information is Codd's worked example of a general principle: when a difficulty is inherent to the problem, scattering per-case workarounds multiplies it, while a single systematic mechanism pays its cost once. The prevailing practice was a special sentinel value invented per field (a zero here, a blank there, a 9999 elsewhere), which forced every user to learn every column's private convention and made uniform treatment by tools impossible. His counter was one null marker independent of data type, with defined semantics everywhere the model can encounter it. To critics who found null handling complicated he answered that missing and inapplicable information is complicated, and that retreating to programmer-chosen defaults does not remove the complexity, it just relocates it into every consumer, unlabeled.

The systematic route has a price he paid openly: admitting an unknown mark into comparisons forces a third truth value, and RM/T works out the consequences through the whole operator set (which comparisons yield unknown, how duplicate elimination treats marks, how joins and unions must be extended so information is preserved rather than silently dropped when values are absent). The discipline shown is the lesson: having chosen a mechanism, follow it through every operator and boundary case until behavior is defined everywhere, guided by an explicit interpretation principle rather than per-operator improvisation. A mechanism defined only on the easy paths is a sentinel value with better marketing.

A programmer who takes this to heart recognizes the same fork wherever an awkward case recurs (absent config, unknown timestamps, partial failures, out-of-band values) and chooses one explicit, type-independent representation with worked-out semantics over a menu of local defaults, then audits every operation that can meet it. The complaint "this mechanism is complicated" gets answered with the question "is the complexity in the mechanism or in the world," and only mechanism-made complexity counts against the design.

**Source:** [Codd's 12 Rules](../works/codds-12-rules.md) — the systematic-nulls rule in part one and the discussion of nulls, aggregates, and defaults in part two. Also [Extending the Database Relational Model to Capture More Meaning](../works/extending-the-database-relational-model-to-capture-more-meaning.md) (Section 2.3's three-valued logic, the null substitution principle, and the maybe- and outer-operator extensions that carry null semantics through the whole algebra).
