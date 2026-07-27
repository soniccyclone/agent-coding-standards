---
type: lesson
title: "A correctness criterion earns its keep by being true of everything you can build, not by being cheap to check"
figure: girard
works: [linear-logic]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# A correctness criterion earns its keep by being true of everything you can build, not by being cheap to check

**Lesson:** It is tempting to insist that any property you rely on must be decidable at reasonable cost, and to reject a criterion that would require exponentially many checks. That instinct conflates two different jobs. The criterion's job is to say precisely what it means for an artifact to be well-formed. Establishing that a particular artifact satisfies it is a separate job, and the good answer to that job is almost never validation — it is closure. Prove that your generators produce only well-formed artifacts and that your combinators preserve well-formedness, and every object you can actually construct satisfies the criterion without anyone ever running the check.

The framing that makes this comfortable is to notice you already accept it elsewhere. That a polymorphically typed function from integers to integers really does yield an integer when applied to one is a deep property of the system, and nobody proposes verifying it per-application; it is guaranteed by how the term was built. A structural soundness condition on a concurrent proof object is the same kind of thing. It is stated as an abstract property, deliberately not as an algorithm, and it is discharged by construction: compile from a sequential source, or combine two objects already known to be sound, or rewrite one by a transformation proved to preserve soundness. The unbuildable pathologies — the self-referential configurations that would loop forever consuming themselves — are excluded not by detection but by never being reachable.

Two design consequences follow. First, the interesting engineering question shifts from "how do I check this?" to "what is my complete set of admissible construction routes?" That question is finite, answerable, and something you can enumerate in a document; it also tells you exactly where to invest, because a *feasible* alternative characterization of soundness is valuable specifically for the case where an artifact arrives from outside your construction paths — hand-authored, edited on a screen, or received across a trust boundary. Second, closure arguments compose in a way validation never does: a component whose internals you cannot inspect can still be admitted, provided its interface is declared and it is itself known to be well-formed. Correctness of the whole then depends only on the interface, and the opaque interior can be swapped for any other object with the same interface.

The lesson for a programmer is to stop treating undecidability or expense as a reason to weaken an invariant. Weakening it to something checkable usually means asserting less than you actually need. State the invariant you actually need, then make it unfalsifiable by construction.

**Source:** [Linear Logic](../works/linear-logic.md) — the discussion of proof-net soundness, which explicitly declines to treat an exponentially expensive condition as something to be checked and instead enumerates the soundness-preserving ways of producing such objects, together with the black-box treatment of opaque enclosures whose interiors need not be known.
