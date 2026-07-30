---
type: lesson
title: "Put the degenerate case inside the operation, and postpone the optimization that moves it out"
figure: wirth
works: [algorithms-and-data-structures]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Put the degenerate case inside the operation, and postpone the optimization that moves it out

**Lesson:** An operation should accept the boundary case where there is nothing to do and handle it correctly itself, in the same way arithmetic is defined so that the zero case needs no special treatment from anyone who uses it. Wrap the body in the test for the non-degenerate case and give the degenerate one its own answer, and every caller is thereby relieved of a check. The accounting is what makes this more than a style preference: with the test inside, it is written once and verified once; with the test outside, it must appear at every call site, and every call site that omits it now owes an argument for why the omission is safe in that particular context. Those arguments are individually plausible, collectively unverifiable, and silently invalidated by the next caller somebody adds. One guard in the shared operation is smaller than n guards outside it and is the only version that stays true.

There is a real efficiency argument on the other side — the caller often does know the case cannot arise, and the test is then wasted — and the point is not to deny it but to sequence it. Get the correct version built first, with the case handled inside, and only then consider hoisting the check out where the surrounding code demonstrably makes it redundant. Doing it in the other order introduces the complication before you know whether it is needed, at the moment when you understand the algorithm least and are most likely to be wrong about which cases can occur. The general rule this belongs to is that structural simplifications justified by context should be applied to a program that already works, since the context you are appealing to is only established by the working program.

Notice that the same reasoning also settles a smaller question that recurs constantly: where a guard is a conjunction of tests and one of them is only meaningful when the others hold — a bounds check followed by an access using those bounds — the order of the terms is load-bearing and the meaningful-only term must come last. That is the same principle at the scale of an expression. A condition that is undefined outside its guard belongs inside the guard's protection, whether the guard is a preceding term in a conjunction or a surrounding conditional around a procedure body.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 3.4's remark that the conditional encompassing the procedure body ensures the degenerate case of a full board is handled correctly, that this is a general device similar to how arithmetic operations are defined to handle the zero case for convenience and robustness, that performing such checks outside the procedure as an optimization obliges each call to carry the check or justify its absence, and that introducing such complications is best postponed until a correct algorithm is constructed; together with the same section's requirement that the term testing the board contents appear last in the acceptability conjunction because the variable it inspects exists only when the preceding range tests hold.
