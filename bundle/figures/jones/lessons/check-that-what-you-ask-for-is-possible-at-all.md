---
type: lesson
title: "Check that what you are asking for is possible at all, and demote the check when it costs as much as building"
figure: jones
works: [systematic-software-development-using-vdm]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Check that what you are asking for is possible at all, and demote the check when it costs as much as building

**Lesson:** A description of desired behaviour can be perfectly well-formed, perfectly readable, agreed by everybody, and impossible to satisfy. Ask for the largest prime, or for a number such that both it and its successor are even, and nothing is wrong with the request except that nothing meets it. The failure is invisible on inspection because each clause is sensible; only the conjunction is empty. So the first question to ask of any specification is not whether it says what you meant but whether anything at all could satisfy it: for every input you have declared acceptable, does some acceptable output exist. Asking this before anyone starts building is one of the cheapest possible interventions, and it catches a defect that would otherwise surface as an implementer who cannot finish and cannot say why.

Two things make the question sharper than it first appears. It is not decided by the conditions alone — the declared types of results participate, so the same requirement can be satisfiable over one number type and impossible over another, and a request that a value decrease by two is fine until you also insist the value never go negative. And it is not decided by each operation in isolation either: whatever legality condition governs the shared structure is implicitly demanded of every operation's result, so an operation which is satisfiable in the abstract may be impossible once you require it to leave the structure legal. This is exactly why it pays to have established, in advance, that the basic ways of altering your structures preserve their legality — those small facts are what make the possibility check a two-line argument instead of a research problem.

The pragmatic rule for when the check is hard is the part most easily missed, and it is what separates a usable discipline from a ceremony. Sometimes establishing that something is achievable is no easier than achieving it — the argument amounts to constructing the answer. In that case do not stall. Put the question on the review checklist, let a competent reader say whether they believe it, and proceed on the strength of that belief. The value of naming the obligation was never that it always gets discharged formally; it is that it stops being overlooked, and that there is somewhere to apply more rigour if doubt arises later.

**Source:** [Systematic Software Development Using VDM](../works/systematic-software-development-using-vdm.md) — the states-and-proof-obligations section: the satisfiability obligation requiring that some result exist for each valid input, the unsatisfiable examples of a largest prime and a number whose successor is also even, the observation that type information interacts with the conditions so that the same operation is satisfiable over integers but not naturals, the extension of the obligation to state invariants with its reliance on the earlier invariant-preservation lemmas, and the explicit advice that where the obligation is no easier to prove than creating the implementation it should be used as an item on a review checklist while work proceeds.
