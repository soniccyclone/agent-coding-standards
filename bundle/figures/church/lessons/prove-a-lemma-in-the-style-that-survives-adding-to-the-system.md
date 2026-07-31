---
type: lesson
title: "Two proofs of the same lemma are not the same asset: one survives extending the system, the other silently expires"
figure: church
works: [introduction-to-mathematical-logic]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Two proofs of the same lemma are not the same asset: one survives extending the system, the other silently expires

Church closes his development of the second-order calculus with a remark that has nothing to do with what he proved and everything to do with how. Every derived rule established in that section, he notes, was established in a way that shows it keeps holding if further axioms are added later — explicitly in contrast with an earlier derived rule of the first-order system, where he had to warn in a footnote that the argument does not carry over to an extended system. The statements of the derived rules do not record this difference. Two rules can read identically and be worth different things, because one was obtained by exhibiting a derivation that uses only the axioms and rules in front of you, while the other was obtained by reasoning about the totality of what is currently provable.

The distinction is the difference between arguing from the parts and arguing from the whole. A proof that says "here is how to construct the conclusion from the premises using these steps" stays valid no matter what else you throw into the system, because adding axioms never removes a derivation. A proof that says "every theorem has property P, and anything with property P also yields the conclusion" is an argument by exhaustion over the current theorem set, and adding a single axiom voids it — not by making the conclusion false, necessarily, but by destroying the reason you had for believing it. The second style is often easier, sometimes much easier, and Church uses it when he must. What he does not do is let the two blur together in his head afterward.

The habit generalizes past logic, because software is full of results proved by exhaustion over the current world and then used as if they were structural. An invariant justified by "every implementation of this interface does X" expires the day someone writes a new implementation. A performance guarantee justified by enumerating the callers expires when a caller is added. A safety property justified by "no code path constructs that value" expires with the next commit, and the expiry is silent because the property is still stated in the header comment where it was true. The maintainable version of the same claim derives it from something the newcomer is forced to satisfy — a constructor that cannot produce the bad value, a type that cannot be inhabited wrongly — even when that costs more up front.

The practical move is to annotate the argument, not just the result. When you rely on a closed-world fact, say so where the conclusion is recorded, so that whoever opens the world knows what they invalidated. Church's whole apparatus of derived rules is reusable partly because he tells you, at the point of use, which ones are robust under extension and which one is not. That footnote is doing work no restatement of the rule could do.

**Source:** [Introduction to Mathematical Logic](../works/introduction-to-mathematical-logic.md) — the closing remark of §51, observing that the derived rules of that section, unlike the substitution rule discussed in an earlier footnote, were established so as to continue holding under the addition of any further axioms.
