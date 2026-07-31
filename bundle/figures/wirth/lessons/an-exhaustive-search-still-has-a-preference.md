---
type: lesson
title: "An exhaustive search still has a preference, and it belongs to whoever drives the outer loop"
figure: wirth
works: [algorithms-and-data-structures]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# An exhaustive search still has a preference, and it belongs to whoever drives the outer loop

**Lesson:** A program that enumerates every valid answer looks impartial, and that appearance is exactly what makes it dangerous. The enumeration comes out in some order, and that order is decided by which of the problem's parties was chosen to drive the outermost level of the recursion and by the order in which that party's alternatives are tried. When the two sides of a matching problem each supply a ranked list and the search advances by letting one side propose in preference order, the answers that satisfy the proposing side appear early and the answers that satisfy the other side appear late. Nothing in the specification of a valid answer says the early ones are better. The bias is an artifact of the traversal, injected by a decision that was made for implementation convenience — someone had to go in the outer loop — and it is invisible in the output, which is just a list of equally valid answers.

The failure this sets up is not in the search but in its consumer. Anything downstream that takes the first result, or that stops the search early, or that shows a user the top of the list, has silently adopted the traversal order as a preference function it never defined and cannot defend. The discipline is to treat "which answer comes out first" as a specified property with a stated owner, the same way you would treat any other output, rather than as an incidental consequence of loop nesting. If you cannot say whose interest the ordering serves, you do not yet know what your program returns.

The structural remedy is to keep the representation symmetric even where symmetry is redundant. When each side of the problem gets its own preference table and its own rank lookup, mirroring the other, the roles of the two parties become interchangeable by exchanging the arguments — the bias becomes a parameter of the run rather than a commitment baked into the code, and producing the opposite-optimal answer costs a swap instead of a rewrite. This is the payoff that justifies carrying redundant symmetric structure even when one side could in principle be derived from the other: the redundancy is what makes the asymmetry of the algorithm removable. Generalize it as a habit: when a problem has two or more parties standing in the same relation to it, resist collapsing them into a driver and a driven at representation time, because the collapse is the point at which a fairness property quietly leaves the program.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 3.6's stable marriage program, where the two preference matrices and the two rank matrices mirror each other, and the closing observation that good solutions from the men's point of view are generated first while good ones from the women's appear toward the end, so the algorithm is biased toward one population by the nature of the chosen search strategy, together with the note that this is changed by systematically interchanging the two pairs of matrices; and the accompanying table distinguishing the male-optimal from the female-optimal stable solution among the nine computed.
