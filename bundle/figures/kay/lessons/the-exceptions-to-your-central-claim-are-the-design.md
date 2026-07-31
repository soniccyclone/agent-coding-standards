---
type: lesson
title: "The exceptions to a system's central claim are where the next design lives, so invert the default instead of encoding around them"
figure: kay
works: [the-early-history-of-smalltalk]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# The exceptions to a system's central claim are where the next design lives, so invert the default instead of encoding around them

**Lesson:** A well-regarded system usually advertises a single organizing claim — everything here is one kind of thing, combined one way — and then, on inspection, exempts a handful of its own most important constructs from that claim. The exemptions are typically not obscure; they are the constructs the system could not function without. The usual response is to admire the claim, treat the exemptions as regrettable engineering detail, and, if one is clever, show that they can be encoded in terms of the claim after all. That response wastes the most informative thing available. The exemptions are a measurement: they mark the exact places where the organizing idea, as formulated, was not strong enough to carry the system's own weight. Reformulating so that they are no longer exemptions is a different and much more productive project than encoding them away, because the encoding leaves the original formulation standing while the reformulation replaces it.

The move that usually does the work is inversion of the default. If the general form is the one that the special cases needed and the ordinary form is a restriction of it, then make the general form the rule and let the restriction be requested where it is wanted. The reason this is not obvious in advance is that the ordinary form is the one everybody writes most often, so it feels primitive; frequency of use is not the same as foundational status, and confusing the two is what produces the exemption in the first place. Nor should a demonstration that the special cases can be simulated inside the claim be taken as settling the matter — a simulation shows the claim is expressive enough, not that it is the right decomposition, and the flaw survives the demonstration.

A design habit follows. When adopting somebody's system as the basis of your own, catalogue the places where it violates its own stated principle before you catalogue what it does well, and treat that list as your agenda rather than as errata. Do the same to your own designs, on the understanding that you will not find the violations by asking whether the principle holds — it will appear to — but by asking which constructs you have quietly stopped applying it to. Those are the ones that are about to become somebody else's opportunity.

**Source:** [The Early History of Smalltalk](../works/the-early-history-of-smalltalk.md) — the discussion of studying the functional-language tradition and finding that a language claiming to be founded on functions had its most important components, including abstraction, quotation and conditionals, introduced as constructs that were not functions at all, with the observation that clever encodings of some of them into the base did not remove the flaw; and the resulting question of why the evaluating form was taken as fundamental rather than the non-evaluating one, which is described as the line of thought that led directly to the design of the message-passing scheme.
