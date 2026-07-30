---
type: lesson
title: "An argument cannot be retrofitted onto a finished artifact, so redevelop rather than reason backwards"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# An argument cannot be retrofitted onto a finished artifact, so redevelop rather than reason backwards

**Lesson:** Take a working program of a few hundred lines, written competently, in service for a while, and try to establish after the fact that it meets its specification. The attempt drowns. Not because the program is wrong and not because the technique is weak, but because the finished text presents every detail at once and at the same level, with no record of which details were consequences of which decisions. The structure that would have made the argument tractable — this piece was introduced to discharge that obligation, under those assumptions — existed only in the author's head and evaporated when the code compiled. Redeveloping the same program from the same specification is the cheaper move, and it is not merely cheaper: the redevelopment exposes errors in the original that nobody had found by running it.

The general form of this is a warning about a plausible three-phase plan: write a precise specification, do the development, then prove the result. The middle phase gets no help from either of the others. Errors introduced there are not detected until the last phase, by which point everything built on top of the faulty step has to be discarded with it, and that rework is exactly the cost the precision was supposed to eliminate. A failed proof is also a poor debugger; it tells you that something does not follow, not which decision was the wrong one. So the argument has to move into the development, one obligation per step, discharged while the step is still the only thing you are looking at and the parts underneath are still nothing but named promises. That is the moment when there is least to reason about — and it never gets better later.

The corollary worth internalizing is that an argument is not a certificate you attach to a product. It is a by-product of having built the thing a particular way. Where a project treats the reasoning as a separable deliverable, to be produced afterwards by someone other than the designer, the reasoning will be either impossible or worthless, because the person doing it lacks the one thing that made the artifact comprehensible: knowledge of what each part was for.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — the account in the introduction of the 1970 challenge to prove an existing several-hundred-line PL/I program correct, its failure under the sheer quantity of detailed information, and the substitute experiment in which the same specification was redeveloped by the method, ran without testing, and revealed errors in the original; the accompanying remark that proofs can show the absence of bugs but not prevent their insertion; and the "fatal flaw" argument opening the chapter on proofs in program development, that a specify-develop-prove sequence leaves the development phase unassisted, that late-detected early errors force reconstruction of everything built on them, and that proof attempts are an inefficient way to debug an incorrect program.
