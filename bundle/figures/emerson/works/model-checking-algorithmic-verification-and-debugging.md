---
type: work
title: "Model Checking: Algorithmic Verification and Debugging"
figure: emerson
description: The shared 2007 ACM Turing Award lecture, written up for a general computing audience, recounting how model checking grew from the early-1980s branching-time temporal-logic work into a widely deployed hardware and software verification technique. Walks through the core method (exhaustive, algorithmic checking of a finite-state model against a temporal-logic spec, with a counterexample trace produced on failure) and the later techniques that made it scale — symbolic (BDD-based) representation, bounded model checking, partial-order reduction, and counterexample-guided abstraction refinement. Serves as both a retrospective on the field Emerson co-founded and a survey of its state as of 2009.
subdomains: [formal-methods-and-verification]
year: 2009
url: https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/Model%20checking%20algorithmic%20verification%20and%20debugging.pdf
access: public
host: self-archived
tags: [work]
---

# Model Checking: Algorithmic Verification and Debugging

**Author(s):** with Edmund M. Clarke and Joseph Sifakis
**Venue/year:** Communications of the ACM 52(11), November 2009, pp. 74-84 (2007 ACM A.M. Turing Award lecture).
**Source:** https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/Model%20checking%20algorithmic%20verification%20and%20debugging.pdf — self-archived PDF on co-author Edmund Clarke's own CMU faculty page, live and directly downloadable (HTTP 200).

## Lessons
- [A correctness method that hands back a failing trace gets adopted; one that only ever says yes does not](../lessons/a-method-that-shows-you-the-bug-is-the-one-that-gets-used.md)
- [When a search space explodes, change how you represent it rather than how you search it](../lessons/attack-blowup-at-the-representation-not-the-search.md)
- [Approximate in a direction whose error you can name, then let each false alarm tell you where to sharpen](../lessons/approximate-in-a-known-direction-and-let-refutations-refine.md)
- [Verifiability is a property of the architecture you chose, so pick structures whose guarantees compose](../lessons/verifiability-is-an-architectural-property-you-design-for.md)
- [When the state space is finite, stop constructing proofs and start deciding truth](../lessons/check-the-model-instead-of-constructing-the-proof.md)
- [Extra expressive power in a specification notation is billed at checking time, so buy the weakest one that says what you mean](../lessons/every-gain-in-what-a-notation-can-say-is-charged-at-checking-time.md)
- [A recursive definition has two solutions, and which one you meant is the difference between an obligation and a constraint](../lessons/two-kinds-of-recurrence.md)
- [Specify what must remain possible, or a generator will hand you the least capable thing that qualifies](../lessons/demand-possibility-or-be-handed-the-least-capable-thing.md)
- [Pick the abstraction from the property you intend to check, then own the claim that it is faithful](../lessons/the-abstraction-you-check-is-a-claim-about-the-real-artifact.md)
- [Expressiveness is a gate, not a dial, and the criterion that decides adoption cannot be formalized](../lessons/expressiveness-is-a-gate-not-a-dial.md)
- [A specification language that cannot state the negation of its own assertions has a blind spot](../lessons/a-language-that-cannot-negate-itself-has-a-blind-spot.md)
