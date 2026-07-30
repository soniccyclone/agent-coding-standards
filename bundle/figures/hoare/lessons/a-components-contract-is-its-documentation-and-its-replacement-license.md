---
type: lesson
title: "A component's stated contract is simultaneously its documentation, its proof obligation, and its licence to be replaced"
figure: hoare
works: [an-axiomatic-basis-for-computer-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# A component's stated contract is simultaneously its documentation, its proof obligation, and its licence to be replaced

**Lesson:** Three activities that are normally staffed and scheduled separately turn out to be one activity performed once. Telling a caller what a component requires of it and what it will get back is documentation. Establishing that the component actually delivers that is verification. Deciding whether some other implementation may be dropped in its place is maintenance. All three are answered by a single statement of the conditions holding before and after — and stating those conditions rigorously is the most precise form the documentation could take anyway, so the rigor is not an extra cost imposed on the other two. This is why writing the contract first is not ceremony: the artifact it produces is needed by everyone downstream regardless of whether anyone ever constructs a formal argument from it.

The compositional payoff is what makes the practice scale past small programs. Once a component's contract is established, an argument about any caller uses the contract and never the component's internals; the established result becomes a step in the caller's argument, and the caller's argument becomes a step in *its* caller's. The consequence is that the shape of the reasoning ends up mirroring the shape of the system, which means decomposition decisions are simultaneously decisions about how the correctness argument decomposes — a good decomposition yields short local arguments, and a decomposition that produces an argument nobody can carry out was a bad decomposition regardless of how the code looked.

Substitutability is the same fact seen from the maintenance side, and it is the only version of "modularity" that has teeth. Any implementation satisfying the same contract may replace the original without re-examining any caller — not as a convention people are asked to honor, but as a consequence of the callers' arguments never having mentioned anything else. Contrast the usual situation, where callers have accreted dependencies on behaviors nobody wrote down, and every replacement is a fresh integration risk. There is a further, less obvious return: the recorded argument tends to explain not just what the component does but why it works, which is the information a person modifying it years later actually needs and the thing that prose documentation almost never manages to preserve.

**Source:** [An Axiomatic Basis for Computer Programming](../works/an-axiomatic-basis-for-computer-programming.md) — the proofs-of-program-correctness section, on assertions before and after a subroutine as the most rigorous statement of its purpose and conditions of use, the proof of a subroutine serving as a lemma in the proof of its callers so that a large program's structure is mirrored in its proof's structure, the validity of replacing any subroutine by another meeting the same criterion, and the observation that the proof explains why rather than merely what.
