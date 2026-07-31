---
type: lesson
title: "Collapse the equivalence your question cannot distinguish"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Collapse the equivalence your question cannot distinguish

**Lesson:** Before computing an expensive relation over a population, ask which members are interchangeable with respect to the specific question being asked. Interchangeability here is precise: two members are equivalent when every answer that involves one would be the same with the other substituted. If such classes exist, computing over individuals is computing the same answer once per member of each class. Collapse each class to a single representative, run the expensive computation over the collapsed population, and recover any individual answer by looking up which class the individual belongs to and consulting the collapsed result. Nothing is approximated — the collapsed computation carries exactly the information the original did, relative to this question.

The leverage is superlinear whenever the expensive computation grows faster than linearly in the population, which is the situation that made it expensive in the first place. Halving the population quarters a pairwise computation. That also means the collapse is worth doing even when it is partial: you are not obliged to find every class, and finding the few largest is most of the benefit. This is the key practical point, because complete and exact class-finding is often the harder problem. Stopping once the collapsed population is small enough to afford the real computation is a perfectly good termination condition, and far cheaper than pursuing the exact quotient.

Two properties make the recovery step trustworthy and are worth verifying for whatever equivalence you have chosen. Membership must be cheap to store and query, since every individual answer routes through it. And the equivalence must be genuine rather than approximate: if two members differ in some answer, collapsing them does not lose a little precision, it produces wrong answers with no indication of which ones. That distinction — exact quotient versus lossy clustering — is the whole difference between a reformulation and an approximation, and the two get conflated constantly.

Framed generally, this is the habit of asking what your question is invariant under, and quotienting by that invariance before doing any work. Symmetries, mutual dependencies, and shared fate are all sources of it. The pleasant part is that the invariance is a property of the question, so the same data may collapse very differently for two different queries — which argues for deriving the collapse per question rather than baking one canonical grouping into the data.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the transitive-closure-by-graph-reduction section of the social-network chapter, which collapses each strongly connected component to a single node on the grounds that all its members reach exactly the same nodes, notes that the reduction need only continue until the graph is small enough for a quadratic result to be feasible, and describes answering a reachability question about two original nodes by locating their components and querying the reduced graph.
