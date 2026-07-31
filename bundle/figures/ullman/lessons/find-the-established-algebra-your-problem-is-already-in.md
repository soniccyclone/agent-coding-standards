---
type: lesson
title: "Find the established algebra your problem is already in"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Find the established algebra your problem is already in

**Lesson:** When a computation is hard to distribute, the productive first move is not to design a distribution scheme for it but to ask which well-studied set of operators it can be re-expressed in. Numerical linear algebra over sparse matrices looks nothing like query processing until you notice that a matrix with mostly-zero entries is naturally a set of coordinate-value triples, at which point multiplying two matrices is a join on the shared index followed by grouping and aggregation — two operators that already have known parallel implementations, known cost models, known failure modes, and known optimisations. Nothing was invented. The problem was re-described until it landed inside a vocabulary where the answers already existed.

The reason this works is that a mature algebra is not just notation; it is an accumulated body of implementation knowledge attached to a small number of operator names. Everything anyone has learned about executing a join — how to partition it, when a broadcast beats a shuffle, what skew does to it — becomes available to you the instant your problem is recognisably a join. Building a bespoke distributed algorithm forfeits all of that and forces you to rediscover it, usually one production incident at a time. So the payoff for the translation effort is not elegance, it is inheritance.

Two cautions keep this from being a slogan. First, the translation is rarely exact, and the gap is where the thinking is: the join-then-aggregate reading of matrix product yields the wrong intermediate — a pairing of two operands rather than their product — and you have to see that a small modification inside the operator restores what you meant. Recognising that your problem is "almost X" is the useful state; insisting it is exactly X is how you get a wrong answer with a familiar shape. Second, the representation you choose determines whether the translation is even available: the same matrix stored as a dense positional layout offers no triples to join on, so the index has to be reconstructed from position before any of this applies. Which representation makes your problem visible as an instance of something known is itself a design decision, and often the only one that matters.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the MapReduce chapter's development of relational-algebra operators, and its treatment of matrix multiplication as a natural join on the shared index followed by grouping and aggregation, including the note that a sparse matrix is well represented as a relation of coordinate triples while a positional layout requires the coordinates to be reconstructed.
