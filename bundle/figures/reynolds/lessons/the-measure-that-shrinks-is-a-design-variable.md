---
type: lesson
title: "The quantity you make shrink is a design choice, and changing it gives a different algorithm with the same shape"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, hardware-affinity]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# The quantity you make shrink is a design choice, and changing it gives a different algorithm with the same shape

**Lesson:** Any self-referential construction needs some integer attached to the problem that is bounded below, that can be solved outright at its minimum, and that strictly decreases on the way to each subproblem. It is tempting to treat that quantity as given by the problem — "the number of items," obviously. It is not given. It is chosen, and the choice is one of the few genuinely free decisions in the design. Two procedures can have the same text down to the ordering of their parts and still be different algorithms, with different termination arguments and different running times, purely because one is counting down on the amount of data and the other on the size of the space the data lives in.

That reframing is a search technique, not a curiosity. When the natural measure gives you an unsatisfying bound, ask what else about the problem is finite and shrinks as you descend. Sorting on the value range rather than the element count buys nothing when the range is large, and wins outright when a file has more records than the key field has distinct values — a situation the count-based measure cannot even see, because it never looks at the key space. The cost formula falls out the same way in both cases; only the substitution for depth changes, so you can compare the alternatives by writing the same derivation twice with a different quantity plugged in.

There are two disciplines attached. First, the measure has to be discharged honestly at each recursive site: the reason you subdivide the way you do is usually that the obvious subdivision does not guarantee a strict decrease in every case, and finding the arrangement that does is real work, not bookkeeping. Second, a measure that decreases on average is not a measure that decreases. When a construction's worst case and its typical case differ by an order of magnitude, you do not have a cost; you have two, and which one governs depends on whether the caller can survive the bad one. That is a deployment question about who is exposed, not a question you can settle by looking at the code.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.2.4's range-partitioning sort, whose notion of size is the size of the value interval rather than of the segment, together with the observation that its form is similar to quicksort's yet the reasons for termination and the times required are completely different, the resulting bound in terms of the log of the range, and the note that the situation arises in practice when sorting records on a key field with fewer possible values than there are records; and Section 3.2.3's construction of quicksort, where the straightforward partition gives no guarantee that both subsegments are nonempty and cannot be repaired by choosing the pivot better, so the outermost elements are handled separately, followed by the remark that the order-of-magnitude gap between worst-case and average behavior is a phenomenon not previously encountered and renders the method unsuitable for certain real-time applications.
