---
type: lesson
title: "Constrain a structure's shape so the question you cannot afford to ask stays cheap"
figure: thompson
works: [the-unix-time-sharing-system]
axes: [verifiability, expressiveness]
subdomains: [operating-systems-and-systems-programming]
tags: [lesson]
---
# Constrain a structure's shape so the question you cannot afford to ask stays cheap

**Lesson:** Every persistent structure has some question that has to be answerable for the system to stay correct — is this thing still reachable, is this resource still referenced, has this region been orphaned. Whether that question is cheap or ruinous is not a property of your cleverness at answering it; it is a property of the shape you allowed the structure to take. Permit arbitrary connections and reachability becomes a global traversal, meaning every local edit potentially changes a global answer and you can no longer tell from the edit alone whether you have leaked something. Restrict the shape so each node has exactly one way in, and the same question collapses to a count you can maintain incrementally at the point of every edit.

This inverts the usual order of design. The tempting move is to make the structure as expressive as possible and then go looking for an algorithm that can audit it. The better move is to identify the invariant you must be able to check cheaply, and then work backwards to the most permissive shape that still lets you check it that way. The expressiveness you give up is real — you genuinely lose configurations that some user would have wanted — but you are trading it for the ability to reason locally, forever, on every operation. That trade is almost always worth making, because the cost of the general structure is not paid once at design time; it is paid on every mutation, in perpetuity, by everyone who has to prove they didn't break something.

The tell that you are facing this decision is the phrase "we'd have to track" appearing in a design discussion. Bookkeeping that only becomes necessary because of a generalization is the generalization's true price, and it is usually much larger than it first appears, because the bookkeeping itself needs to be correct under concurrency, under crashes, and under partial completion. Refusing the generalization deletes the bookkeeping and everything that could go wrong inside it. A programmer who thinks this way treats structural restrictions not as limitations imposed by laziness but as deliberate purchases of decidability — and states, when imposing one, exactly which question the restriction is protecting.

**Source:** [The UNIX Time-Sharing System](../works/the-unix-time-sharing-system.md) — the file system section's two parallel refusals: constraining the directory structure to a rooted tree, and forbidding connections that span separate mounted volumes, both justified by what would otherwise become undetectable or require elaborate tracking.
