---
type: lesson
title: "When the uniform algorithm fails at one edge, try extending the definition before adding a branch"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# When the uniform algorithm fails at one edge, try extending the definition before adding a branch

**Lesson:** A general method that works everywhere except at one extreme value presents two repairs, and the obvious one is the worse one. The obvious repair is to guard the method with a test and handle the extreme separately, which leaves you with two code paths, two arguments for correctness, and a permanent invitation for the special path to rot because it runs rarely. The other repair is to go back to the mathematical object the method is built on and ask whether its definition can be consistently extended one step past its current boundary, in a way that keeps every equation you were already relying on. If it can, the extended definition swallows the extreme case and the single uniform path becomes correct as written. Computing terms of a recurrence illustrates it: the natural loop cannot start at the very first term, but the recurrence itself extends consistently one index below zero, and once that extra value exists the loop covers the whole range with no test at all.

Notice what the technique is actually exploiting. The special case was never a fact about the problem; it was an artifact of where somebody chose to stop defining things. Definitions are usually written to cover the cases the author had in mind, and the edges of that intention become artificial cliffs later, at which point programs grow branches to compensate for a decision made in a document. So when you are about to write a guard, first ask whether the domain boundary that forced it is essential or merely conventional. Essential boundaries — division by zero, an empty structure with no meaningful answer — genuinely need branches. Conventional ones can be pushed outward, and pushing them is cheaper than defending against them forever.

There is an adjacent warning worth keeping, because it is what makes the situation arise in the first place. It is a reasonable rule of thumb that if a method handles all sufficiently large inputs and the answer is well defined at the smallest one, it will handle the smallest one too, and the rule of thumb is usually right, which is exactly why the exceptions are dangerous. Do not let the general argument stand in for a check at the boundary. Verify the extreme value explicitly against the relation you are maintaining, because the failure mode is not a wrong answer — it is a loop whose entry condition was never satisfiable and which therefore runs forever.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 1.3.6's Fibonacci development, where the natural initialization fails to establish the invariant for the smallest input so the loop would not terminate, the immediate fix is a separate branch, and the exercise following it shows that consistently extending the function one index below zero removes the need for the branch entirely.
