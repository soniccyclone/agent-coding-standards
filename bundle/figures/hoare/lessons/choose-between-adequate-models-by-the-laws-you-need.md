---
type: lesson
title: "Choose between two adequate models by the laws you need to hold, not by which can mimic the behaviour"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Choose between two adequate models by the laws you need to hold, not by which can mimic the behaviour

**Lesson:** Two models of the same thing can both reproduce every behaviour you care about and still differ in what you may conclude. Model a mutable variable as a small active participant that receives new values and hands out current ones, and everything an ordinary variable does is faithfully imitated. But each write is now an occurrence in the history, so two writes of the same value are two occurrences and cannot be collapsed into one, while the ordinary reading of assignment makes them plainly interchangeable. Behavioural adequacy did not settle the question. The law did, and the model that supports the law you actually reason with is the one to keep, even when the other model is more uniform, more elegant, or already built.

The general test is worth running deliberately, because the temptation always runs the other way. Having found a single primitive that can express everything, one wants to define everything in terms of it, and the resulting economy is real. The cost is paid in laws: the more expressive encoding makes distinctions the encoded notion does not make, and every distinction it adds is an equation you no longer have. Ask what you routinely rewrite when reasoning — that this is idempotent, that these two commute, that this one can be discarded — then check each against the candidate encoding. Where an equation fails, look for what is now observable that should not have been, since that is invariably the cause.

Two consequences for practice. Adopting a general mechanism to represent something narrower is a decision to be made against a list of laws you intend to keep, not on grounds of parsimony, and the list should be written before the decision rather than discovered afterwards by a broken proof. And the failure mode is quiet in exactly the wrong way: everything still runs, all the tests pass, and what has been lost is a rewriting step that people go on performing out of habit — a duplicate write elided, a repeated read hoisted, an idle update removed — which was sound under one model and is not under the other.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the assignment section of the sequential processes chapter, which introduces assignment, conditionals and loops directly, and then states explicitly that the earlier technique of modelling a program variable as a subordinate process communicating its value has been deliberately rejected because it does not have the desired properties, giving as the decisive case the wish that assigning a value twice equal assigning it once, against the fact that two output communications of the same value on a variable's channel are not equal to one.
