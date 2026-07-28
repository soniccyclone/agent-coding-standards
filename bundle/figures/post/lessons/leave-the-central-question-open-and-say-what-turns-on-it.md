---
type: lesson
title: "Publish the question your framework cannot answer, along with what breaks either way"
figure: post
works: [recursively-enumerable-sets-of-positive-integers-and-their-decision-problems]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Publish the question your framework cannot answer, along with what breaks either way

Post ends thirty pages of new machinery by saying plainly that he is undecided on the question the whole development was built to settle, and he does not dress the admission up. He goes further and lists the questions he passed over while keeping his gaze on the one he failed to answer, plus additional questions his own definitions provoke. Most notably he explains the stake: if all the unsolvable problems in this class turn out to be equally hard, then reducing a new problem to a known-hard one is *the* general method for proving new problems unsolvable; if not, it is only one method among others, and practitioners will need more tools. The open question is presented with its consequences attached, so a reader can tell what changes about their own work depending on which way it goes.

This is a different move from ordinary hedging. Hedging weakens a claim to make it harder to falsify. What Post does is state a sharp claim's *absence* sharply — here is exactly the proposition I want, here is the precise form it takes now that the notion of comparison has been made rigorous, here is why my partial results do not reach it, here is what its resolution would change. That is a specification for work someone else can pick up. It is also the reason the question survived as a named target and was eventually resolved by a technique nobody in 1944 possessed; a vaguely gestured-at difficulty would have left nothing for the technique to be invented against.

The behavior holds because a clearly posed open problem carries most of the value of a solved one for everybody downstream. It tells other people not to assume the answer, tells them where the boundary of the current theory sits, and tells them which of their own conclusions are conditional. Its absence has the opposite effect: readers infer from a confident-sounding framework that the central question is settled or unimportant, and build on the gap without knowing it is there. The cost of the omission lands on people who cannot see it, which is why the incentive to omit has to be resisted deliberately.

In practice this means the design document says which decision is still unresolved, what evidence would resolve it, and which parts of the system are load-bearing on each answer. It means the README names the case the library does not handle rather than staying quiet and letting a user discover it in production. It means a benchmark result reports the regime it did not cover. A programmer who works this way is easier to build on than one whose documents are uniformly confident, because the second kind forces everyone downstream to independently rediscover the boundaries — and they will each find a different, partial version of them.

**Source:** [Recursively Enumerable Sets of Positive Integers and Their Decision Problems](../works/recursively-enumerable-sets-of-positive-integers-and-their-decision-problems.md) — the closing sections, where the paper's motivating question is declared unresolved, the practical consequence of each possible answer is spelled out, and the questions left aside along the way are enumerated as future work.
