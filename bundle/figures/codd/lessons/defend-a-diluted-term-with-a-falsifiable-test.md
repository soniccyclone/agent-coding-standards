---
type: lesson
title: "Defend a diluted term with a falsifiable test"
figure: codd
works: [codds-12-rules, relational-database-a-practical-foundation-for-productivity]
axes: [verifiability]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Defend a diluted term with a falsifiable test

**Lesson:** When a technical term starts selling products, its meaning erodes toward whatever the weakest product can support. Codd's response to watching "relational" become a marketing sticker was not to argue about essence but to operationalize: one foundation criterion (the system must be manageable entirely through the capabilities the label names, whether or not other capabilities exist) and a numbered battery of independently checkable rules derived from it, plus a grading scheme. The foundation rule is the shrewd part, because it closes the loophole every dilution exploits: a system that offers the labeled capability as a veneer, while real work happens through a back door, fails outright. His nonsubversion rule closes the same loophole from below, forbidding lower-level interfaces from bypassing the integrity the higher level enforces.

The Turing lecture had already drawn the line's other edge: a minimal qualifying capability defined precisely enough (specific operators expressible without iteration or recursion) that "does not qualify" is a demonstrable fact, with graded tiers above it rather than a binary purity test. And the 12-rules article adds a diagnostic for reading vendor documentation: any advice to abandon the abstraction "to achieve acceptable performance" is an apology, an admission that the vendor skipped the implementation work the abstraction demands, since the model itself deliberately excludes nothing an optimizer needs. Performance escape hatches are confessions, not features.

A programmer who thinks this way defines contested labels (compliant, secure, real-time, lossless, idempotent) as test suites rather than prose, writes the criteria so that partial support scores partial marks and veneers score zero, and reads "for performance, drop to the unsafe path" in any product's manual as evidence about the vendor, not about the abstraction.

**Source:** [Codd's 12 Rules](../works/codds-12-rules.md) — Rule Zero and the twelve rules across both Computerworld parts, the grading discussion, and the performance-apology passage. Also [Relational Database: A Practical Foundation for Productivity](../works/relational-database-a-practical-foundation-for-productivity.md) (Section 4's minimal relational processing capability and the classification of systems it induces, sharpened by the postscript recounting why the rules were then published).
