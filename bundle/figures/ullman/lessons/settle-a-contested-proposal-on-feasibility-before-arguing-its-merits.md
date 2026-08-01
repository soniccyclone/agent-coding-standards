---
type: lesson
title: "Settle a contested proposal on feasibility before anyone argues its merits"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Settle a contested proposal on feasibility before anyone argues its merits

**Lesson:** When a system is proposed and immediately becomes a fight, the fight almost always runs along the axis of whether it *should* exist: what it costs the people it touches, what it is worth, who decides. That argument is expensive, it recruits people's priors, and it rarely converges. There is a second and usually unasked question sitting underneath it — whether the thing can do what it is being defended for at all — and answering that one is often cheap, often decisive, and does not depend on anybody's values. A proposal justified entirely by an outcome it cannot produce is disposed of without ever adjudicating whether the outcome would have been worth having.

The discipline has two halves and both matter. The first is to state plainly what you are declining to arbitrate. Announcing that you will not settle the tradeoff between competing goods, and then proceeding to a technical verdict, is what keeps the verdict readable as a technical verdict. Skip that step and the same arithmetic reads as a preference wearing a lab coat, which is exactly how it will be received and dismissed by whoever the arithmetic went against. The second half is to pick the feasibility question the proposal's own justification depends on, not a convenient adjacent one. If the case for a system is that it will find rare cases hidden in bulk data, the question is what its yield actually looks like at that ratio, and the answer will be a number rather than a position.

What makes this worth building into how you evaluate anything is the asymmetry in what the two questions cost to answer. The values question requires agreement among people who disagree. The feasibility question requires an afternoon and some arithmetic on volumes you can look up. If the feasibility answer comes back negative, everything downstream of it evaporates, including the entire values debate, because there is nothing left to weigh against anything. If it comes back positive, you have lost almost nothing and you have made the values debate a real one, conducted over a system that would work rather than over a promise.

The same move applies far below the level of policy. A team arguing over whether to take on a piece of surveillance-shaped instrumentation, a fraud rule, an alerting heuristic, or an automated enforcement action is usually arguing about whether it is acceptable, when a ten-minute estimate of how many of its firings would be spurious would end the discussion. The general habit: whenever a proposal is defended by an outcome, compute whether the mechanism produces that outcome before you let anyone argue about the outcome's worth. Note that the negative answer is not "this needs tuning." A mechanism whose spurious yield exceeds its genuine yield by orders of magnitude is not a system with a threshold problem, and the people who will bear its output are not the people who will be tuning it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 1's Total Information Awareness discussion, where the authors note the program was killed after objections from privacy advocates, explicitly decline to take up the privacy-versus-security tradeoff as outside the book's purpose, and instead redirect to the technical feasibility question of whether searching broadly for suspicious activity yields anything but artifacts, with the cost of the artifacts counted both as investigative work and as intrusion into the lives of the innocent people flagged.
