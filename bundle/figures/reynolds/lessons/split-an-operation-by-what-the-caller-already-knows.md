---
type: lesson
title: "Split an operation by what the caller already knows, because that knowledge is worth an order of magnitude"
figure: reynolds
works: [the-craft-of-programming]
axes: [primitive-count, hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Split an operation by what the caller already knows, because that knowledge is worth an order of magnitude

**Lesson:** Two operations that produce the same result can have completely different costs when they differ only in what the caller can promise. Adding an item to a duplicate-free collection is linear if the item might already be there and constant if you know it is not, because the search exists only to check the thing the caller could have told you. Removing a named item requires finding it; removing whichever item is most convenient does not. The general pattern: whenever an implementation begins by establishing a fact, ask whether some callers already have that fact, and if so give them a second entry point that assumes it. The cost you were paying was for ignorance, and ignorance is not uniformly distributed across your callers.

This changes what the abstract phase of a design is for. It is normal to treat correctness reasoning as separate from performance work, and to discard the intermediate assertions once the argument is done. But some of those assertions are exactly the preconditions that unlock the cheap variants. If the invariant tells you that at this point in the program the element being inserted is definitely new, that fact is not proof residue — it is a performance asset, and throwing it away means the implementation will re-derive it at runtime, forever, on every call. So when you strike the scaffolding, keep the assertions that sit immediately above a primitive call, because they are the specification of which variant that call site is entitled to.

There is a discipline cost, and it is the honest reason people avoid this. Each extra variant is an obligation that somebody could violate, and a violation is silent — the cheap insert on an element that was already present corrupts the structure rather than being slow. So the variants belong on operations where the invariant that licenses them is written down and maintained, not spread as a general habit of offering unchecked fast paths. The distinction that earns its keep is the one you can point at an assertion to justify. The one you cannot is just an unguarded footgun with a good excuse.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.1.3's discussion of representing a finite set by a duplicate-free array segment, where insertion generally costs a linear search but is constant time when the element is known to be absent, and deleting a specified element costs a linear search while deleting an unspecified member costs constant time, noted as cases where a fine distinction in the nature of a primitive operation has a major effect on its efficiency; together with Section 5.1.2's decision to discard the intermediate assertions except the one establishing that the node being added to the unprocessed set is new, kept explicitly because it would matter for the choice of that set's representation.
