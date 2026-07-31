---
type: lesson
title: "Index the invariant by the set of work already done, not by the counter"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Index the invariant by the set of work already done, not by the counter

**Lesson:** The reflex when describing what a loop maintains is to write a condition on the loop counter: the counter is somewhere in range, and the accumulated result corresponds to everything below it. That formulation drags the counter's arithmetic into every claim, and it forces a case split as soon as the range can be empty, because the counter's value in the empty case does not mean what it means otherwise. The better parameter is the *set of items already processed*. State what is true of the accumulated result as a function of that set, and the loop's job becomes: start with the empty set, and each step move one item across.

Three things improve at once. The range condition disappears from the invariant entirely, because which items have been processed is now the subject rather than something you have to constrain — the construct's own structure supplies it. Degenerate cases stop needing separate treatment: an empty range is just the empty set, the invariant holds of it trivially, and the conclusion you infer covers that case with no extra argument, where a counter-based version would have demanded its own analysis. And the invariant becomes about the problem rather than about the mechanism, so it survives changing the order of traversal or the shape of the iteration.

There is a discipline that makes it work and a diagnostic that comes free. The discipline: the counter must not appear in the invariant except inside the description of the processed set, since otherwise you have not actually parameterized by progress and the degenerate cases come back. The diagnostic: when an invariant resists being written this way — when the natural statement genuinely needs the counter itself — that awkwardness is real information. It usually means the code behaves oddly in exactly the degenerate case, and the contorted invariant is reporting that oddity rather than inventing it. A formulation that refuses to be stated cleanly is telling you something about the program, not about the notation.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 4.1.2, which rejects taking the invariant as a function of the control identifier because it forces separate lines of reasoning for the regular and irregular interval cases, adopts Hoare's approach of treating it as a function of the interval of integers processed so far, notes that unlike the while case the invariant then carries no range information since that is built into the construct, points out that the restriction forbidding the control identifier to occur free in the invariant except within the processed-interval expression is what ensures the invariant really is a function of that interval, exhibits factorial and exponentiation examples where the negative-bound case is included without extra analysis, and closes with a maximum-finding example whose natural invariant must be rewritten in terms of the processed interval, remarking that the resulting reasoning seems unnatural but correctly reflects the procedure's unnatural behaviour on an empty range.
