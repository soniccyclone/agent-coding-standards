---
type: lesson
title: "Describe what an operation does as a relation between before and after, not as an assertion about after"
figure: jones
works: [tentative-steps-toward-a-development-method-for-interfering-programs]
axes: [expressiveness, verifiability]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Describe what an operation does as a relation between before and after, not as an assertion about after

**Lesson:** The cheapest way to say what a piece of code achieves is to assert something about the state it leaves behind, and for small pieces that works. It stops working as soon as the interesting content of the operation is a comparison — this value decreased, that structure was extended, nothing outside this region moved. To express those you have to be able to name the starting state inside the description of the outcome, which means the outcome is a relation over pairs of states rather than a predicate over one. Once you allow that, a specification can carry the actual input-output relation instead of an approximation of it, and the approximation is what usually leaks: single-state assertions force you to smuggle the initial values in as extra frozen variables or to weaken the claim until it no longer pins down what you meant.

There is a real cost, and it is worth naming honestly rather than pretending the relational style is free. Composition rules stated over relations are bulkier than the elegant chaining rule you get when an intermediate assertion is just a predicate: you end up with several small side conditions per construct instead of one. The trade is favourable in exactly the direction that matters for large work. Bulky rules made of many simple checks scale better than compact rules that require you to invent a strong enough intermediate assertion, because each check can be discharged in isolation and by inspection, whereas the invention cannot be delegated or mechanized. Prefer verbose obligations over clever ones when the problem is going to be big.

Concurrency then removes the choice entirely. If other activity can change shared state while your operation runs, the operation is not a function from states to states — the same start can honestly yield different ends, and no amount of care in phrasing a single-state postcondition recovers the ability to describe that. Relational description is not a stylistic preference that happens to also handle interference; it is the only vocabulary in which interference has anything to say. That is a general shape worth recognizing: when a notation is forced on you by the hardest case in your domain, adopt it for the easy cases too, so the easy cases come out as specializations rather than as a separate system you later have to reconcile.

**Source:** [Tentative Steps Toward a Development Method for Interfering Programs](../works/tentative-steps-toward-a-development-method-for-interfering-programs.md) — the outline of the sequential method, where postconditions of two states are contrasted with the single-state sequential-composition rule and the balance is argued to shift with problem size; and the remark in the interference-specification section that under interference an operation can no longer be regarded as a function from states to states.
