---
type: lesson
title: "Decompose the exact computation before you approximate it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, verifiability]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Decompose the exact computation before you approximate it

**Lesson:** An expensive exact computation is usually approximated by replacing the whole thing with a cheaper method that computes something similar. There is a better move available whenever the exact computation happens to be a sum of many independent, interchangeable pieces: keep the exact method and run it on a random sample of the pieces. The estimate you get is unbiased with respect to the true answer by construction, its error shrinks predictably with the number of pieces you keep, and — the part that matters in practice — you have not introduced a second algorithm whose behaviour has to be understood and defended separately. Scaling the partial sum up is the entire approximation.

This is why it is worth looking hard at the structure of an expensive procedure before conceding that it is too expensive. Cost of the form "repeat this traversal once per element and add up the results" is a very different situation from cost of the form "one traversal whose work grows with the square of the input," even when the two have the same complexity. The first decomposes and is therefore both sampleable and trivially parallel; the second is neither. Complexity notation deliberately erases that distinction, so reading it off the notation is impossible — you have to look at the loop nesting and ask whether the outer iterations depend on each other.

Independence is the condition, and it is worth checking rather than assuming. If a per-piece contribution depends on results accumulated from earlier pieces, sampling silently biases the total, and the bias is invisible because the output still looks like a number in the right range. When the pieces are genuinely independent, the same property that licenses sampling also licenses distribution across machines and incremental recomputation when the input changes locally — one structural observation buying three separate capabilities.

The generalisable habit is to treat "decompose, then decide how much of the decomposition to evaluate" as the default response to an unaffordable exact answer, and inventing a different algorithm as the fallback. Notice too that the choice of how many pieces to keep is a dial you can turn at run time against a budget, which the substitute-algorithm route rarely gives you; the same code path serves the exact answer, the cheap estimate, and everything in between.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the sidebar on speeding up the betweenness calculation in the social-network chapter, which notes that the cost is one breadth-first traversal per node and that using a randomly chosen subset of nodes as roots yields an approximation adequate for most applications.
