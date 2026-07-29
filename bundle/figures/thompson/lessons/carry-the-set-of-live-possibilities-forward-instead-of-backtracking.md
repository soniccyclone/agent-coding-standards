---
type: lesson
title: "Carry the whole set of live possibilities forward instead of backtracking through one"
figure: thompson
works: [regular-expression-search-algorithm]
axes: [parallelizability, hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Carry the whole set of live possibilities forward instead of backtracking through one

The default shape for a search over choices is to commit to one branch, discover it fails, undo the commitment, and try the next. Thompson's alternative is to refuse the commitment entirely: maintain the set of all positions the search could currently be in, consume one item of input, and from that set compute the set of positions it could be in next. Nothing is ever undone, because nothing was ever chosen. The old set is discarded, the new one becomes current, and the input advances.

The change in cost profile is the point, and it is structural rather than a constant factor. A backtracking search's work is governed by the shape of the pattern, because the pattern determines how many paths exist to be tried and retried over the same input; the set-advancing search's work is governed by the input, because each item is examined exactly once against a set whose size is bounded by the pattern. That also means the input is consumed strictly once and forward, so the text never has to be retained, rewound, or re-read — a property that falls out of the reformulation rather than being engineered separately. Thompson attributes the speed to the parallel character of the method, and that is the right way to see it: the branches are not raced against each other in sequence, they are all advanced simultaneously by one step.

Recognizing when this reformulation is available is the transferable skill. It works when a failed path teaches you nothing that a surviving path does not already know — when the state a branch is in can be summarized independently of the history that got it there. If two branches at the same input position are in the same state, they will behave identically forever, and there was never any reason to explore them one at a time. The set is exactly the quotient of the search tree by that equivalence.

A programmer who believes this treats the presence of an undo operation in a search loop as a design smell rather than a necessity. Faced with save-position, try, restore-position, they ask what the frontier of live hypotheses actually is, whether it can be represented explicitly, and whether it can be advanced as a whole — and if it can, the bookkeeping that the backtracking version required disappears along with its worst case.

**Source:** [Regular Expression Search Algorithm](../works/regular-expression-search-algorithm.md) — the algorithm section, which opens by naming backtracking's storage and bookkeeping burden and replaces it with a current list of possible positions from which a next list is constructed as each character is read.
