---
type: lesson
title: "A budget nothing can lay out inside itself is not a budget"
figure: stearns
works: [hierarchies-of-memory-limited-computations, on-the-computational-complexity-of-algorithms]
axes: [verifiability, primitive-count]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# A budget nothing can lay out inside itself is not a budget

**Lesson:** A limit is only usable if something can mark it out using resources that fit inside the limit. That self-referential condition is not a technicality invented to make proofs go through; it is what separates a budget from a wish. If determining how much you are allowed to spend itself costs more than the allowance, then no process can enforce the allowance, no process can be constructed that exactly saturates it, and the allowance names no real capability level. So the interesting resource functions are precisely those that can be measured out from within — and the whole structure of results has to be stated over that restricted family rather than over all conceivable functions.

The right response to discovering such a restriction is neither to hide it nor to apologise for it, but to go and populate it. A restriction that admits only trivial cases is fatal; a restriction that admits every growth rate you would ever write down is a formality. Showing that the well-behaved family already contains everything reachable from multiplication, exponentiation and composition — and that it is closed under composing anything in it with the threshold function itself, so the family stays rich all the way up from the floor — converts an apparent weakness into a demonstration that the theory covers the practical ground. The general form: whenever your result needs a side condition, your next obligation is to characterise how much of the space the condition keeps, because a side condition of unknown extent is indistinguishable from a hole.

This transfers directly to anything that enforces its own limits. A quota, a rate limit, a timeout, a memory cap, a deadline in a scheduler: each is only meaningful if the bookkeeping needed to track it fits inside the budget it tracks, and the failure mode when it does not is not a small inefficiency but total loss of the guarantee. The same reasoning explains why the accounting in a self-limiting construction is usually done in an encoding chosen so the counter provably fits — the choice of base or representation is not an aesthetic detail but the thing that makes the limit self-supporting. Design the meter before you design the policy, and if the meter does not fit under the ceiling, the ceiling is fictional.

**Source:** [Hierarchies of Memory Limited Computations](../works/hierarchies-of-memory-limited-computations.md) — the definitions of constructability preceding the two hierarchy theorems, which require a machine that stays within the bound while marking out exactly that bound, together with the surrounding discussion showing the constructable family contains the real-time countable functions, is closed under composition with the model's threshold function, and is therefore very rich above it.
