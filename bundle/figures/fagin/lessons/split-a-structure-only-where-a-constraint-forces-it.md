---
type: lesson
title: "Split a structure only where a constraint forces it, never as far as it will go"
figure: fagin
works: [multivalued-dependencies-and-a-new-normal-form-for-relational-databases]
axes: [cognitive-load, primitive-count]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Split a structure only where a constraint forces it, never as far as it will go

**Lesson:** Once you have a mechanical procedure for decomposing a structure, the procedure will happily keep going past the point of usefulness. Fagin points this out against his own criterion: a structure can satisfy the strongest available standard and still be further divisible without loss, and the further division is simply not called for, because nothing was wrong with the undivided form. The standard is not "as decomposed as possible." It is "no remaining constraint is left unaccounted for by the identifiers." When every constraint is already a consequence of the identity of the records, there is no redundancy to eliminate, and any additional splitting is work with no corresponding defect being fixed.

This matters because decomposition has a real cost that the decomposition criterion does not measure: reassembly. Each split introduces a recombination step that some later reader or query has to perform mentally and some system has to perform physically. The reason to accept that cost in a particular place is that leaving the structure joined would force some fact to be stored many times, so that keeping the copies in agreement becomes a standing obligation. Where no such duplication is implied, the cost buys nothing. The paper also notes that the outcome depends on the order in which constraints are applied and that choosing well is an open problem, which is a fair warning that a mechanical process here produces defensible outputs rather than optimal ones.

Beyond schema design, this is a general position on refactoring driven by rules. Extract-until-atomic is the same failure as normalize-until-irreducible. The trigger for pulling something apart should be a named problem that the current shape causes, and the stopping point should be the disappearance of that problem, not the exhaustion of the technique. A programmer who has internalized this can articulate, for each boundary in a design, which specific duplication or inconsistency risk that boundary exists to prevent, and is willing to leave things joined when they cannot name one.

**Source:** [Multivalued Dependencies and a New Normal Form for Relational Databases](../works/multivalued-dependencies-and-a-new-normal-form-for-relational-databases.md) — the remark following the decomposition theorem that a schema already meeting the criterion may still be splittable further, with the observation that doing so gains nothing, plus the worked normalization example and its discussion of ordering heuristics.
