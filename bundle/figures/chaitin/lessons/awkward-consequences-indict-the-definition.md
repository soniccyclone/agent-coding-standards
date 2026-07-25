---
type: lesson
title: "When every consequence needs a correction term, the definition is wrong"
figure: chaitin
works: [a-theory-of-program-size-formally-identical-to-information-theory, algorithmic-information-theory-some-recollections]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# When every consequence needs a correction term, the definition is wrong

**Lesson:** A definition can be adequate in extension and still be wrong in structure. Chaitin had a measure of program size that picked out the right objects, agreed with the intuition it was meant to formalise, and matched what others had independently proposed. It also made every downstream identity come out with slop in it, error terms that grew without bound and had to be apologised for in each theorem. He read that slop as a verdict on the definition rather than a fact about the subject, threw away a decade of his own framing, and changed two things at the base: descriptions had to carry their own extent, and a relative measure was taken with respect to a shortest description of the condition rather than the condition itself. The correction terms collapsed to constants and the whole algebra of information theory became available for free.

The general principle is that awkwardness in the consequences is evidence about the primitives. Definitions are not neutral labels attached to pre-existing objects; they are the load-bearing design decisions, and the reasoning built on them either composes or does not. If a formalism keeps needing side conditions, exception clauses, and unbounded fudge factors to state its own laws, the boundary has been drawn across the grain of the thing being described. The tell is that the fudge factors do not concentrate in one place, they appear everywhere, because a mis-drawn boundary is crossed by every use.

For a programmer, the same signal appears at interfaces and data models. When every caller of a function needs a special case, when every consumer of a type has to check for the same degenerate value, when composing two components requires glue whose size scales with the number of components, the fix is upstream of the call sites. This also means resisting the argument that two designs are equivalent because they can express the same behaviours. Equal reach is not equal structure, and the one whose laws come out exact is the one to build on.

**Source:** [A Theory of Program Size Formally Identical to Information Theory](../works/a-theory-of-program-size-formally-identical-to-information-theory.md) - the introduction, which motivates the whole redefinition by the unpleasantness of prior error terms, plus the appendix showing the older convention makes the key identity unbounded. The decision is narrated from the inside in [Algorithmic Information Theory: Some Recollections](../works/algorithmic-information-theory-some-recollections.md), in the walk through successive versions of the theory and the point at which he abandons the earlier one permanently.
