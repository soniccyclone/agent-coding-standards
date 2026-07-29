---
type: lesson
title: "Postulate the capability you lack as a primitive, then re-run your impossibility argument against the enlarged machine"
figure: turing
works: [systems-of-logic-based-on-ordinals]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Postulate the capability you lack as a primitive, then re-run your impossibility argument against the enlarged machine

**Lesson:** When you hit something your system provably cannot do, there are two very different follow-up questions, and conflating them wastes years. The first is: what else is blocked by this same obstruction — that is, how much of what I want falls out for free if this one thing were somehow given to me? The second is: would having it actually finish the job, or would the same obstruction reappear one level up? The way to answer both is to stop treating the missing capability as an absence and start treating it as a hypothetical primitive: extend the machine with an operation that just answers the hard question, define exactly what that operation is allowed to be asked, and then reason about the extended machine as a first-class object of study.

Doing this converts a dead end into a measuring instrument. Everything that becomes reachable once the primitive is assumed is, in a precise sense, "no harder than" that primitive, which gives you a way to compare difficulties rather than merely sorting problems into possible and impossible. More striking is what happens when you re-apply the original impossibility argument inside the extended system. If the argument was structural — a self-reference that turns any total decision procedure against itself — it does not care that the machine got stronger. It reproduces, and yields a fresh question the enlarged machine cannot answer either. The consequence is a ladder rather than a cliff: difficulty is layered, unbounded upward, and adding power relocates the frontier instead of removing it.

The engineering discipline that follows is to name your oracles. Any component whose behaviour you have assumed rather than built — a perfect classifier, a human reviewer, an external service treated as always-correct, a solver assumed to terminate — should be modelled explicitly as a primitive with a stated interface, and everything downstream should be understood as conditional on it. Then ask the second question, which almost nobody asks: if this assumed component were perfect, would the system actually be finished? If the same class of failure reappears just above the oracle, the assumption was never the bottleneck, and buying a better one is money spent on the wrong layer.

**Source:** [Systems of Logic Based on Ordinals](../works/systems-of-logic-based-on-ordinals.md) — the short section on problems that are not number-theoretic, where a machine is granted an unspecified external answer-source as one of its fundamental operations and the earlier diagonal argument is then applied to the extended machines themselves.
