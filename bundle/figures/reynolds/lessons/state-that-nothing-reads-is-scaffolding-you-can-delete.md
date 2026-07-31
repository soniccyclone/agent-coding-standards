---
type: lesson
title: "State that nothing reads is scaffolding, and the criterion for removing it is purely syntactic"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# State that nothing reads is scaffolding, and the criterion for removing it is purely syntactic

**Lesson:** There is a category of variable whose only job is to make an argument sayable. You cannot state why a loop terminates without naming the set of things already handled; you cannot state why work is never repeated without naming the partition between done and pending. So you introduce those variables, maintain them faithfully, and use them in the invariants. Then you notice the finished program does not need them. The condition that licenses removal is worth stating exactly, because it is checkable by inspection rather than by insight: a variable is inert if every place its name appears is inside a statement whose sole effect is to assign to that variable, or to another variable in the same group. Inert variables cannot steer a branch and cannot reach any value the program actually produces, so deleting their declarations and their updates changes nothing observable.

The payoff is a licence to be generous during construction and strict at the end. Most people ration the state they introduce while designing, because they are imagining the cost of carrying it. That instinct suppresses exactly the intermediate concepts that would have made the correctness argument easy to write. If you know in advance that any state you can prove inert will evaporate, you can afford to name every quantity the argument wants — the processed set, the pending set, the count of things settled — carry them explicitly through the derivation, and let the syntactic test decide afterward which of them were real and which were scaffolding. The proof and the artifact do not have to have the same variables.

Notice also what the criterion does when it fails. If you go to delete a quantity and find its name inside a test, you have learned something concrete: that idea was not bookkeeping, the program genuinely depends on it, and it deserves a permanent place. So the check is a classifier and not just a cleanup pass. It sorts the concepts you invented into the ones the machine needs and the ones only the reader needed, and it does so without any appeal to your judgement about which was which.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.1.2, which introduces the processed and unprocessed set variables solely to establish that the reachability loop terminates within a bound, defines a variable (or a set of variables) as auxiliary when all its occurrences lie within statements whose only effect is to assign to it, observes that such a variable can affect neither the flow of control nor the value of any non-auxiliary variable, and then eliminates the processed set from the finished abstract program as scaffolding used to construct it.
