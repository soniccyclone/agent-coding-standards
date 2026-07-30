---
type: lesson
title: "Encode the live set in the arrangement, so the hot loop has nothing to test"
figure: wirth
works: [algorithms-and-data-structures]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Encode the live set in the arrangement, so the hot loop has nothing to test

**Lesson:** When part of a collection becomes inactive during a computation, the obvious representation is a flag per element saying whether it is still in play, and the obvious consequence is that every pass over the collection must examine every element and test its flag. If that pass is the innermost, most frequently executed part of the program, the obvious representation is the wrong one. The alternative is to hold the identities of the active elements in the front of a separate index array and keep a count of how many are active, so that iterating over the live set means iterating over a contiguous prefix and no test is performed at all. Deactivating an element becomes a swap with the last active entry followed by a decrement of the count — a constant-cost operation that keeps the prefix property intact without preserving order, which is exactly the property you did not need.

The general form of the move is: shift information out of per-element data and into the arrangement of the data, so that a question the loop was asking becomes a question the loop no longer has to ask. It is not a micro-optimization in the usual sense, because nothing was made faster; work was removed. And it composes — where there are two nested notions of inactivity, one permanent and one lasting only until the end of the current output group, both can live in the same array with two counts marking two boundaries, so a temporarily excluded element is parked in the middle band and a permanently exhausted one beyond the far end. That the same array serves both is what keeps the scheme from becoming its own source of bugs.

Two conditions govern when to reach for this. First, it pays only where the frequency justifies the extra indirection, so decide by identifying the most frequently repeated part of the algorithm before choosing the representation, not after profiling reveals a surprise. Second, it costs you the ability to speak of an element by its original position, since the mapping now moves; if some other part of the program needs stable positions, that part has to go through the mapping too, and the cost of that must be counted. The habit worth keeping is the question itself: what is this loop testing on every iteration, and could the answer have been arranged in advance instead?

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 2.4.3's explicit rejection of an array of Boolean components indicating file availability in favour of a file index map whose first entries are the indices of the available sequences, chosen because the selection step is the most frequently repeated part of the entire algorithm, with the accompanying use of two counts to distinguish sequences eliminated permanently from those merely closed for the current output run, and the corresponding reassignments in the map.
