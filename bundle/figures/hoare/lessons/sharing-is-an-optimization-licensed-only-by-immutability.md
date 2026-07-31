---
type: lesson
title: "Sharing one copy is an optimization licensed only by immutability, and the licence must travel with the technique"
figure: hoare
works: [notes-on-data-structuring]
axes: [hardware-affinity, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Sharing one copy is an optimization licensed only by immutability, and the licence must travel with the technique

**Lesson:** Replacing a value with a reference to a value is the most reliably tempting optimization there is, and it keeps being invented in new clothes: many variables likely to hold the same thing, so store it once and hand out addresses; several structures sharing a common part, so let them point at one instance; a large aggregate too big to sit in one place, so keep a table of addresses to its pieces. Every version buys the same things — less storage, and copying that costs one word instead of many — and every version carries the same condition. The moment any holder can change the shared thing in place, the change is visible to holders who never asked for it, and the model in which those holders were written has been silently violated. Sharing is sound exactly while the shared thing is treated as constant.

The discipline that follows is to attach the restriction to the technique rather than to the individual case. Whenever you introduce indirection for the sake of space or copying speed, state at the same moment that the shared thing may not be selectively updated, and treat that as part of the representation decision rather than as a caveat someone will remember. It matters because the restriction is invisible at the point where it gets broken: an in-place update to one component looks like an entirely local act, and there is nothing in the shape of the code to indicate that this particular value has other owners. What the discipline is protecting is the ability to reason about a variable by reading the code that names it, which is the one property that makes local reasoning possible at all.

Two further costs are worth pricing in before reaching for indirection, because they are usually left out of the comparison. It generally drags in dynamic allocation and reclamation, which is a whole mechanism with its own failure modes, adopted as a side effect of a decision that looked like it was only about layout. And it interacts badly with moving data between levels of storage, since an address is meaningful only in the space it came from — a structure full of pointers cannot simply be copied elsewhere and still work. Neither cost argues against sharing. They argue for making it a deliberate choice with its conditions written down, instead of the obvious thing you do because copying looked expensive.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the representations discussion in the chapter on the concept of type, which offers indirect representation for variable-size and commonly-equal values, notes that copying then costs only the pointer, warns that shared copies must never be selectively updated, and lists the accompanying costs of dynamic allocation, garbage collection and transfer between main and backing store; reinforced in the array chapter's tree representation, where matrices sharing rows may share a single copy of a row provided that row is not selectively updated.
