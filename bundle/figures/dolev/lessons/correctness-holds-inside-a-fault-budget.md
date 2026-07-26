---
type: lesson
title: "You will never learn who failed; scope correctness to a budget instead"
figure: dolev
works: [the-byzantine-generals-strike-again, polynomial-algorithms-for-multiple-processor-agreement]
axes: [verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# You will never learn who failed; scope correctness to a budget instead

**Lesson:** Put yourself inside the system rather than above it. You receive a report from a peer, ask everyone else what they received, and find that your copy disagrees with all of theirs. The natural conclusion is that your peer lied. It does not follow: an equally consistent world is one where that peer and you are the only honest parties left and everyone else is coordinating against you. Local evidence underdetermines blame, permanently, and no amount of further inquiry closes the gap. Designs that begin by trying to identify the broken parts are therefore built on something unobtainable, and they fail in the ugliest possible way, by accusing correct participants.

The way out is to stop treating faultiness as a fact to be discovered and start treating it as a quantity to be budgeted. Fix a bound on how many participants may misbehave, admit that misbehaviour inside that bound can be arbitrary and adversarial including collusion, and prove the properties you care about under exactly that hypothesis. Two things follow that feel like giving up but are not. Any behaviour a broken component might exhibit is covered, because nothing was assumed about it; a protocol whose argument never mentions what failures look like cannot be surprised by a failure mode nobody enumerated. And a world with more failures than the budget is explicitly outside the contract, which is the right answer rather than an evasion: if that many parts are gone, no decision the protocol makes was going to matter.

What changes in practice is where certainty is demanded. Identification becomes opportunistic rather than foundational. Sometimes the evidence really is impossible to produce with only the budgeted number of liars, and then a participant genuinely knows something and may exploit it; the rest of the time it does not know and must proceed anyway, which the protocol is built to allow. Systems designed this way have a stated regime of validity, an explicit and auditable numeric assumption, and no dependence on the unavailable ability to tell friend from foe. Systems designed the other way have a heuristic accusation mechanism, an unstated regime, and a failure mode that turns healthy components into casualties.

**Source:** [The Byzantine Generals Strike Again](../works/the-byzantine-generals-strike-again.md) — the introductory passage that constructs the receiver's dilemma from the inside and resolves it by adopting an upper bound on faults, together with its narrow notion of a receiver explicitly knowing a sender is broken. [Polynomial Algorithms for Multiple Processor Agreement](../works/polynomial-algorithms-for-multiple-processor-agreement.md) — the opening statement of the adversarial worst-case stance, that the protocol must survive collusion and must never rely on anticipated behaviour of broken parts.
