---
type: lesson
title: "The power to mint a fresh value is a frontier, not a convenience"
figure: abiteboul
works: [datalog-extensions-for-database-queries-and-updates]
axes: [expressiveness, primitive-count]
subdomains: [foundations-of-computation, databases-and-data-management]
tags: [lesson]
---
# The power to mint a fresh value is a frontier, not a convenience

**Lesson:** Generating a new identifier feels like plumbing. You need a key, you ask for one, and no one thinks of it as a semantic event. This work locates it as a boundary in expressive power. Confine a computation to a fixed collection of relation shapes and to the values already present in its input, and everything it can hold at any moment is bounded by a polynomial in the size of that input, which caps what it can compute at polynomial space no matter how it is written. Admit a way to introduce values that were not in the input and the same language becomes complete, able to express every legitimate transformation of the data. One primitive separates a bounded language from an unbounded one, and the mechanism is small: a variable appearing in a rule's conclusion with no occurrence in its premises stands for something fresh.

The reason this matters beyond the classification result is what fresh values are used for once available. They serve as scratch identity. A computation that must remember which items it has already handled, or in what stage a particular fact was derived, can attach a new mark to each item and read the marks back later. The work shows that this is enough to reconstruct iterative control inside a language that has none, by using minted values as timestamps that gate when rules may fire. Retraction turns out to serve the same purpose from the other direction, since being able to remove a fact lets you reuse a fact as a reusable signal. Two features that look like unrelated conveniences are two ways of buying the same thing.

The practical reading is to treat identifier generation as a design commitment with consequences you should be able to state. If a component can mint values, its reachable state space is unbounded, and any argument you had about termination or exhaustive testing based on the input being finite no longer applies. If a component cannot mint values, some computations are simply outside it, and you should know whether the ones you need are among them. Between those, the interesting engineering question is what the minted values are actually carrying: identity that outlives the computation, or bookkeeping that exists only to sequence work. The second kind is scaffolding for control the language does not otherwise offer, and its presence in your code is evidence that you are building a mechanism the platform should have given you.

**Source:** [Datalog Extensions for Database Queries and Updates](../works/datalog-extensions-for-database-queries-and-updates.md) — the introduction's account of how completeness is obtained by admitting invented values and why a fixed schema without domain growth caps computation at polynomial space, and the concluding analysis of which features enable simulation of explicit control, which puts invented values and retraction side by side as the two mechanisms that suffice.
