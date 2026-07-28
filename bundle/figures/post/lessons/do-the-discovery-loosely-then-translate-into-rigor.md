---
type: lesson
title: "Do the discovering in the loose register; rigor is translation, not invention"
figure: post
works: [recursively-enumerable-sets-of-positive-integers-and-their-decision-problems]
axes: [cognitive-load, verifiability]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Do the discovering in the loose register; rigor is translation, not invention

Post is unusually candid about his own working order: in every single case the loose argument came first, and turning it into a machine-checkable derivation afterward was mechanical labor rather than thought. He states this as a general report on his practice, not as an apology for it, and then delivers an entire research program in the loose register on purpose, flagging only the handful of claims that had not yet been through the second pass. The claim worth taking is not that rigor is optional but that rigor is a *different activity* from discovery, and that trying to do both in one pass makes you bad at both.

The reason this holds is a cognitive-budget argument. A formal derivation forces every step to be expressed in the vocabulary the checking apparatus accepts, and that vocabulary is chosen for mechanical checkability, not for human search. Search wants big moves, provisional objects, and the freedom to say "and then obviously we can generate all of these" — exactly the moves a formal system refuses to accept on credit. If you pay the encoding cost on every candidate step, you can only afford to explore a tiny neighborhood, and you will explore it in whatever direction the notation makes cheap rather than the direction the problem actually points. Discovery needs the loose language precisely because loose language lets a wrong step be cheap.

The complementary half is what makes this a discipline instead of an excuse: the loose argument has to be the kind of thing that *can* be translated, and you have to actually translate it, and you have to say which parts you have and have not translated yet. Post does all three. He carries a formal apparatus in the background of the whole paper and reaches down into it at the specific points where intuition would otherwise be doing real load-bearing work, and he marks the results still awaiting their formal pass rather than letting them pass as finished.

A programmer who believes this stops treating the informal phase as an embarrassing preliminary to be skipped or hidden. Design in prose, on a whiteboard, in a scrappy script that only works on the happy path — that is where the actual invention happens, and doing it in the type system or the proof assistant first will produce a worse design that is very well checked. Then translate deliberately: types, tests, proofs, invariants. And keep the ledger of which parts have made the trip, because the failure mode of this style is not sloppiness in the exploring, it is forgetting which conclusions never got translated.

**Source:** [Recursively Enumerable Sets of Positive Integers and Their Decision Problems](../works/recursively-enumerable-sets-of-positive-integers-and-their-decision-problems.md) — the introduction's account of how the results were obtained and why the paper is presented informally, together with the running practice of flagging which claims remain in the informal stage.
