---
type: lesson
title: "Pick a property you will guarantee everywhere, and let it decide where operations get split in two"
figure: strachey
works: [the-main-features-of-cpl]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Pick a property you will guarantee everywhere, and let it decide where operations get split in two

**Lesson:** Choose one property that a whole category of thing in your system will be guaranteed to have — say, that evaluating something to obtain a value never disturbs anything — and then let that guarantee, rather than convenience, determine the shape of everything in the category. What makes this a design technique rather than a slogan is the specific consequences it forces. Operations that would violate the property cannot be in the category at all, so a second category has to exist for them. Things from the second category cannot be handed to things in the first, since that would let the violation in through the back door. Constructs that build a member of the first category out of a block of steps must forbid the steps that would break it. Each of these is a restriction nobody would adopt for its own sake, and all of them follow from one decision.

The most instructive consequence is what happens to an operation that comes in two variants distinguished by whether it consumes what it looks at. Under the guarantee they cannot both be the same kind of thing: reading-and-advancing changes the world and must be the second kind, while looking-without-advancing does not and can be the first. So the property forces a split that a designer thinking only about convenience would probably not make, and the split turns out to be exactly the one users want — a peek and a take, cleanly separated, with the difference visible in what kind of thing each one is rather than buried in documentation.

The general habit is to treat a chosen invariant as a design instrument rather than a checkable claim. Work through your existing operations asking which ones violate it, and for each violation ask whether the operation should be excluded from the category, restricted, or divided into a conforming part and a non-conforming part. The answers give you a decomposition derived from something you can state in a sentence, which is a far better provenance than taste, and the resulting boundaries tend to be the ones users would have asked for anyway.

**Source:** [The Main Features of CPL](../works/the-main-features-of-cpl.md) — the treatment of functions as free of side effects and the consequences drawn from it: routines excluded as parameters to functions precisely because functions cannot have side effects, the value-yielding block construct forbidden from assigning to non-local variables, and the input facilities split so that the symbol-consuming operation is a routine while the operations that inspect the next or last symbol without removing it are functions, the parenthetical reason given being that removal would be a side effect.
