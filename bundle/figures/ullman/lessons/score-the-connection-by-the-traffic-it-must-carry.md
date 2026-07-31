---
type: lesson
title: "Score the connection by the traffic it must carry, not by its endpoints"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Score the connection by the traffic it must carry, not by its endpoints

**Lesson:** When you need to break a structure into its natural parts and the local signals are useless — every link looks exactly like every other link, every element resembles its neighbours equally — stop trying to score the elements and score the *links*, using a quantity that only exists at global scale. The one that works is load: for every pair of elements in the whole structure, work out the cheapest route between them, and credit each link with how much of that traffic it is obliged to carry. A link inside a well-connected region carries almost nothing, because everything it could route has half a dozen alternatives. A link that is the only crossing between two regions is forced to carry every route between them, and its score is roughly the product of the two region sizes. The signal that was invisible locally is enormous globally.

The inversion in how this signal is read is the part worth internalising. Ordinarily a high score means "keep this, it is important." Here a high score means "this is a bridge, cut it" — the quantity measures the extent to which a link joins things that are otherwise apart, so the maximum is a boundary, not a core. Once you have edge scores you can build the partition from either direction: add links back in ascending order of load and watch components merge, or start whole and delete in descending order until the structure falls into as many pieces as you want. Both produce the same nested family of partitions, which is the honest output of the method.

Two properties make this a general technique rather than a graph trick. It needs no notion of similarity at all, so it applies wherever you have connectivity but no meaningful attributes — call graphs, message flows, transitive dependencies. And it is computed by a shortest-path traversal from each element, accumulating credit from the far end back toward the source and splitting a node's credit across its incoming links in proportion to how many routes arrive by each — so the whole thing is a sum of independent per-source contributions, which is what makes it tractable and, as a bonus, approximable by sampling sources.

The habit to carry away is: when local comparison fails, ask what quantity is defined only over the whole structure and would concentrate on exactly the features you are looking for. Necessity is often that quantity. Whatever every route is forced through is a structural chokepoint, and forced-ness is measurable precisely because alternatives are what dilute it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the betweenness and Girvan-Newman sections of the social-network chapter: defining an edge's betweenness as the number of shortest paths through it with credit split across ties, the golf analogy that a high score is bad, the breadth-first labelling and bottom-up credit propagation with each root visited once, and the use of increasing-order addition or decreasing-order removal to expose communities.
