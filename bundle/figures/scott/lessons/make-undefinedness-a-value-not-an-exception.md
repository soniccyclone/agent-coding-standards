---
type: lesson
title: "Make undefinedness an ordinary value ordered by how much it tells you, not a hole outside the type"
figure: scott
works: [logic-and-programming-languages]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Make undefinedness an ordinary value ordered by how much it tells you, not a hole outside the type

**Lesson:** Real computations fail to produce answers — they diverge, they wait forever, they are asked about a case nobody defined. The reflex is to treat that as a defect living outside the value space: functions are partial, and partiality is handled by side conditions, error channels, or a promise to be careful. The move that unlocks a mathematical account of programming is the opposite one. Enlarge the value space with an element standing for *no information yet*, and every partial function becomes a total function on the enlarged space. The awkward case stops being an exception to reason around and becomes an ordinary inhabitant you can compute with.

What makes this more than bookkeeping is the ordering that comes with it. Compare two values not by equality but by information content: one is below another when everything the first tells you the second also tells you, and possibly more. The empty element sits at the bottom because it commits to nothing. Compound values inherit the order componentwise, so a structure with three fields filled and the rest unknown sits below the same structure with a fourth filled. This is a strictly weaker relation than equality, and the weakness is the point — it lets you talk about a partially known object as a legitimate object rather than a broken one, and it makes "more defined" a comparison you can prove things with instead of a phase in a debugging story.

Once information content is the ordering, the shape of the domain, not a convention, tells you which operations are sane. A function that respects the order can only ever turn more input information into more output information; it cannot retract a commitment when you tell it more. That monotonicity requirement rules out exactly the operations that inspect undefinedness and branch on it, which are the ones that would make the mathematics collapse and, not coincidentally, the ones no implementation can supply. The general habit: when a class of cases keeps escaping your model as exceptions, look for the enrichment of the value space that admits them as values, and then look for the order or invariant that comes with the enrichment. The enrichment usually pays for itself twice — once by removing the special cases, once by handing you a proof relation you did not have.

**Source:** [Logic and Programming Languages](../works/logic-and-programming-languages.md) — the introduction of the Boolean domain with an added undefined element, the reading of the partial order as containment of information content, and the componentwise extension of that order to sequences and pairs.
