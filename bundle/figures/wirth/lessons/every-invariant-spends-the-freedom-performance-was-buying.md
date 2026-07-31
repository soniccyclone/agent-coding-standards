---
type: lesson
title: "Every invariant spends the freedom that performance was buying"
figure: wirth
works: [algorithms-and-data-structures]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Every invariant spends the freedom that performance was buying

**Lesson:** Read any structural invariant as a statement about what it leaves undetermined, not only about what it fixes. An ordering condition on a structure typically pins down one aspect of an element's placement and says nothing about another, and that silence is not an oversight — it is the slack that the arrangement's efficiency is made out of. The reason a structure with an ordering condition can be shallow is that nothing in the condition dictates how deep any element sits, so a build procedure is free to choose depths that keep paths short. The efficiency is a consequence of the freedom, not of the constraint.

This makes invariant composition dangerous in a specific and predictable way. Take two conditions that each look modest because each constrains only one aspect, and impose both. Every configuration satisfying the conjunction satisfies both, so the admissible set is the intersection, which can be very much smaller than either — and in the worst case it is a single arrangement per input set, leaving nothing to choose. At that point the shape of the structure is fully determined by the data, all the discretion that was funding good behaviour is gone, and no bound survives. The tell is not that the conjunction is hard to implement; often it is easy. The tell is that you can no longer name a decision the builder gets to make.

So before combining conditions, count the degrees of freedom before and after, and check that at least one dimension of choice remains. If none does, you have not designed a better structure, you have written a specification of a unique object and inherited whatever performance that object happens to have. The same audit is worth running on invariants added one at a time to an existing design, since each addition is a withdrawal from the same account and the balance is only visible if someone is tracking it. And when the conjunction really is what the problem needs, expect that recovering good bounds will require an additional and substantially more intricate mechanism, layered on top rather than falling out — which is itself a signal to reconsider whether the problem can be narrowed instead.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 4.8's side-by-side statement of the search tree invariants and the priority tree invariants, with the observation that the first constrains only the horizontal positions so that vertical positions can be chosen freely to minimize path lengths while the second constrains only the vertical positions; the conjunction of the two into a single two-key invariant; and the immediately following assessment that the search properties of such trees are not particularly good because a considerable degree of freedom in positioning nodes has been taken away and is no longer available for choosing arrangements yielding short path lengths, so that no logarithmic bounds on searching, inserting or deleting can be assured and maintenance operations can become unwieldy, together with the note that recovering guaranteed logarithmic bounds required a separate and very intricate balancing scheme hardly used in practice.
