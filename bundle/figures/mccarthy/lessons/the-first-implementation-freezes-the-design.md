---
type: lesson
title: "Whatever runs first becomes the specification, so treat every provisional notation as a candidate permanent one"
figure: mccarthy
works: [history-of-lisp]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Whatever runs first becomes the specification, so treat every provisional notation as a candidate permanent one

**Lesson:** Design intent has no authority over a design that already executes. McCarthy's retrospective is unusually honest on this point: the intended human-facing notation for Lisp was a bracketed, Fortran-flavoured surface syntax, and the parenthesized list encoding of programs was invented only so that a universal evaluating function could be written down in a paper. Nobody expected people to program in the encoding. Then someone realized the paper's evaluator could simply be hand-coded, and once an interpreter existed the language stopped moving. The surface notation was never defined precisely, never compiled, and never formally abandoned either; it just drifted out of the future while a generation of programmers grew up preferring the encoding that happened to be running.

The consequences were not cosmetic. Choices made offhandedly for expository convenience — the shape of the conditional form, which piles up parentheses, and the decision to let a single machine address serve as the empty list, the false value, and zero — outlived every justification they ever had and complicated implementations for decades. The mechanism is worth naming precisely: an executing artifact acquires users, users acquire code, and code converts arbitrary conventions into compatibility constraints. There is no later moment at which the accidental parts get separated back out from the deliberate ones, because from the outside they are indistinguishable. Static friction against purely notational change, as McCarthy puts it in his conclusions, is exactly what keeps a core in place once it is good enough.

The practical inversion is that prototype quality should be judged on its conventions, not only on whether it works. A demonstration built to prove a concept viable will be the thing that ships if it succeeds, so any interface, encoding, or naming scheme you would be embarrassed to defend in five years should not be in it. Conversely, if you genuinely intend to replace a placeholder, the replacement has to be scheduled before the placeholder gets users, because afterwards the cost of change is paid by other people and will therefore never be paid at all.

A programmer who believes this spends disproportionate care on the parts of an early system that are hardest to change later — data formats, wire protocols, public names, sentinel values — and comparatively little on the parts that are cheap to revisit. They are suspicious of the sentence "we'll fix the syntax later." And when they inherit an odd convention, they ask whether it was reasoned or merely first, because knowing which one it is tells you whether there is an argument to engage or only a migration to plan.

**Source:** [History of Lisp](../works/history-of-lisp.md) — the account of the implementation period, where the evaluator's unexpected appearance as a working interpreter fixes the language's form, together with the list of choices McCarthy identifies as having been made lightly for a paper and regretted afterwards, and the discussion of the never-finalized, never-cancelled surface notation.
