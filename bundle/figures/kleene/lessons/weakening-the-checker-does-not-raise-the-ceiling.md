---
type: lesson
title: "A structural ceiling does not move when you loosen the rules or improve the ideas inside them"
figure: kleene
works: [recursive-predicates-and-quantifiers]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# A structural ceiling does not move when you loosen the rules or improve the ideas inside them

**Lesson:** Once a limit has been derived from the *shape* of a mechanism rather than its contents, the natural escape attempts can be evaluated in advance, and most of them fail for the same reason. Try relaxing what counts as a valid check: instead of demanding that a candidate proof be recognizably correct or recognizably incorrect, accept a checker that confirms good proofs but may run forever on bad ones. Feels like a real weakening. It buys nothing — the resulting notion of provability, once you compress the two nested searches into one, has exactly the same logical shape as before, and every limitation that applied to the strict version applies unchanged. Redesignate the steps of the checking process as the proof steps and you are back where you started.

Try instead admitting inference steps that are not effectively checkable at all, licensed by objects whose validity nobody can verify mechanically. That is a genuine gain, and the size of the gain is calculable: it moves the notion of provability up the alternation scale by a bounded amount, so such a system can be complete for questions one or two levels higher and is still provably incomplete for questions above that. You escape one ceiling by paying for it with non-effectiveness, and you land under another. And a system whose non-effective criterion is as hard to recognize as the truth of the propositions it certifies has bought nothing usable — the recognition cost was merely relocated.

The sharpest form of the point concerns quality rather than rules. Imagine a system handed to you by someone who can survey infinitely many facts at once, correct but inexplicable, its axioms far beyond anything you could have justified. It is subject to the same limitation, because the limitation was derived from the bare fact that proofs are finite checkable objects, and never once consulted the nature of the evidence behind the rules. Brilliance inside a structure does not lift the structure's ceiling.

This is the most practically deflationary lesson in the corpus for anyone who has tried to escape a verification limit by loosening a tool. Making the analysis unsound-but-fast, or partial, or heuristic, or clever, changes the constant factors and the ergonomics; it does not change what class of properties the tool can certify, because that class was fixed by the form of the certificate. Escaping requires changing the form — accepting non-checkable steps, restricting the property to a smaller domain, or asking a different question — and each of those has a stated price. A programmer who knows this stops iterating on the tool and starts negotiating the problem.

**Source:** [Recursive Predicates and Quantifiers](../works/recursive-predicates-and-quantifiers.md) — the discussion of incomplete and weakened theories in Part III, which shows that a checker terminating only on valid proofs yields the same provability form as a fully decidable one, then locates provability in logics with non-effective steps at a specific higher level of the same hierarchy, and argues that the result depends on no detail of a system's constitution or the evidence behind it.
