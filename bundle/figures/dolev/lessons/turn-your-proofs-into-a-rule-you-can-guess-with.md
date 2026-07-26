---
type: lesson
title: "Mine your proofs for a rule of thumb you can guess with before proving anything"
figure: dolev
works: [on-the-minimal-synchronism-needed-for-distributed-consensus]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Mine your proofs for a rule of thumb you can guess with before proving anything

**Lesson:** After grinding out a family of related proofs, most people file the theorems and move on. The higher-value output is the pattern the proofs all turned on, restated as something a person can apply in thirty seconds without proving anything. Here the family was thirty-two variants of the same coordination question under different environment assumptions, and the extracted rule is short enough to hold in one hand: coordination survives a failure budget exactly when that budget cannot erase the fact that a decisive event happened, or scramble the order of two such events. Ask how many parts must go silent for a pivotal transmission to leave no trace on anyone still running. That number is your tolerance ceiling, guessed in advance and usually right.

The rule earns its keep because it explains the cases that look arbitrary from the outside. Bound the delivery time and no failure can suppress a message for long enough to matter, so tolerance goes to the whole population. Fix the delivery order and the same thing happens by a different route. Narrow a transmission from everyone-at-once to one-peer-at-a-time and hiding it suddenly requires only two casualties, the sender and its single recipient, which predicts the strange result that such a system tolerates one failure and not two. None of that is obvious from the theorem statements, and all of it falls out of the rule.

There is a discipline implied about what a heuristic is for. It is not a substitute for the proof, and the honest version of this move admits that the real arguments are considerably more involved than the intuition, mostly in establishing that a pivotal event exists at all. What the heuristic buys is direction: which configurations are worth attempting, which are hopeless, where to spend the proof effort. A team that has one for its own domain stops arguing from analogy to systems it happens to have read about, and starts estimating from the mechanism.

For anyone designing coordination, the operational form of the question is about evidence and its erasure. Every guarantee you add — a deadline, an ordering promise, a wider fan-out, a durable log — is worth exactly as much as the amount of evidence it makes unerasable by the budgeted number of failures. Anything that does not make some event harder to hide is not buying tolerance, whatever else it is buying.

**Source:** [On the Minimal Synchronism Needed for Distributed Consensus](../works/on-the-minimal-synchronism-needed-for-distributed-consensus.md) — the stated secondary goal of understanding intuitively why the earlier impossibility result works, and the informal principle offered in the introduction about failures hiding an event or the relative order of events, applied there to explain each of the paper's own possibility and impossibility cases.
