---
type: lesson
title: "When two camps' concepts look different, implement both in one substrate and see whether they collapse"
figure: steele
works: [scheme-an-interpreter-for-extended-lambda-calculus]
axes: [primitive-count, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# When two camps' concepts look different, implement both in one substrate and see whether they collapse

**Lesson:** Rival vocabularies make rival concepts look further apart than they are. One community describes a computational agent as a script plus the set of other agents it knows about, communicating by messages; another describes a procedure plus the environment it was defined in, communicating by application. Written down side by side in the same interpreter, those turn out to be the same data structure with the same behavior, and the message-dispatch discipline is recoverable as a procedure that inspects its argument and branches. The consequence is not a debating point about terminology — it means the primitive set is one construct smaller than the field believed, and that anything demonstrated about one formulation transfers wholesale to the other.

The method that produced that finding is the actual lesson, and this work is unusually candid about it. The unification was not deduced in advance; a working interpreter for one model was built inside the other with the intent of letting them coexist, and only after it ran did the identity become visible. The authors say outright that the clean result did not arrive as a single insight but was bootstrapped by experiment. Construction was the instrument of understanding, and the intuition that guided the build was wrong in its initial commitments — the first version used a different argument-evaluation order and had to be reworked once experiment showed that order was incompatible with iteration.

A programmer who takes this seriously treats "are these two abstractions really different?" as an empirical question with a cheap experiment attached: express both in one language and look at what you get. If the encodings coincide, delete one. If they do not, the residue is precisely the feature that distinguishes them, which is far more informative than any amount of comparative prose. This also lowers the status of design documents relative to prototypes — not because designing is worthless, but because the encoding is the thing that can actually be checked, and it routinely refutes the design.

**Source:** [Scheme: An Interpreter for Extended Lambda Calculus](../works/scheme-an-interpreter-for-extended-lambda-calculus.md) — the passage in the closures discussion that re-expresses an actor-style constructor as an ordinary nested procedure, together with the acknowledgements' account of how the project actually proceeded.
