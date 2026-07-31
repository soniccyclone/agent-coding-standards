---
type: lesson
title: "Place a new model inside an established one, and push the containment as tight as it will go"
figure: valiant
works: [evolvability]
axes: [verifiability, expressiveness]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Place a new model inside an established one, and push the containment as tight as it will go

**Lesson:** When you invent a new model of what some process can accomplish, the most valuable early move is not to prove anything about your model directly. It is to show that anything achievable in your model is achievable in some existing, well-studied model. That single containment result converts every impossibility already proved for the older model into an impossibility for yours, at no further cost. You inherit a catalogue of negative results built by other people over years, and you inherit it by writing one short simulation argument: exhibit how a run of your process can be replayed using only the resources the older model provides.

The part that is easy to get wrong is that a loose containment is nearly worthless while a tight one is decisive, and the difference in effort between them can be small. Placing your model inside the broadest available framework yields negative results that are all conditional — they depend on unproven assumptions about hard problems, so they say "this cannot be done unless something surprising is true." Noticing that your model actually fits inside a *narrower* framework, one where the process may only consult aggregate statistics rather than individual cases, yields unconditional separations instead: things provably outside reach with no assumptions attached. So the discipline is to ask, after the first containment lands, whether the simulation really needed everything the container offers. Usually it did not, and the tighter statement is where the sharp results come from.

There is a symmetric payoff that gets less attention. A containment also tells your readers, and you, exactly what is *not* new. Anything your model can do that the container can also do is not evidence that your framing was necessary; the framing earns its keep only where the containment is strict, and pinning down the strictness is therefore the real research question rather than an afterthought. Establishing that your restricted process is genuinely weaker than the general one — exhibiting one target reachable in the container and provably unreachable in your model — is what turns a definition into a result. A new model that turns out to be equivalent to an old one has still taught you something, but it has taught you that the constraint you thought you were imposing was not a constraint at all.

**Source:** [Evolvability](../works/evolvability.md) — the pair of propositions in section 3 showing that evolvability implies PAC learnability by replaying the evolution steps as sampled labelled examples, then strengthening that to containment in the statistical-query model by replacing each comparison of empirical performances with statistical estimates; together with section 4, where the weaker containment yields only a result conditional on an unproven complexity assumption while the tighter one yields the unconditional non-evolvability of parity functions and hence the strictness of the constraint.
