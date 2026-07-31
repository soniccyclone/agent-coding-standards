---
type: lesson
title: "When what you actually want is a quantity passing through, add a variable whose whole job is to keep it unmerged"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# When what you actually want is a quantity passing through, add a variable whose whole job is to keep it unmerged

**Lesson:** Some procedures have a worthless postcondition. Run a traversal over every starting point and the final state says only that everything got visited, which nobody needed to be told. The value of such a procedure is in the states it passes through: at one specific moment inside each call, the accumulated state describes precisely the part of the structure attributable to that call, and that is the fact everything built on top of the traversal will depend on. Treat that intermediate assertion as the contract. A specification written only at the boundary will be trivially true and will constrain nothing, so any later modification that destroys the interior property will pass every check you wrote.

The complication is that the interesting quantity usually is not present in any variable. A single accumulator merges what this call contributed with what was already there, and subtraction is not available — by the time the call ends, the two are indistinguishable. The fix is to stop trying to recover it and instead pay for a second variable whose only purpose is to hold it separately. That variable buys nothing at the boundary; it exists so that a property you want to talk about has somewhere to be true.

The idiom that makes such a variable behave correctly under recursion is worth recognising on its own, because it is how a shared global gets the dynamic extent of a call without becoming a parameter. On entry, stash the incoming value in a local, reset the global to just this call's own starting contribution, let the recursion run so that the global ends up holding exactly what this subtree produced, then recombine the stashed value with the current one on the way out. Every level does the same, so each level sees its own subtotal at the moment between the reset and the recombine, and the caller still sees a correctly accumulated whole. The local stash is what makes the global per-call; the recombination is what makes it still an accumulator.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.4.1, where the depth-first search procedure's final assertion is noted to be trivial and the point of the program is identified as producing a sequence of states satisfying the assertion that holds inside the body after the loop over successors; the set of nodes reached by this particular call is observed to be unobtainable from the accumulated visited set, which combines it with the prior contents, so a second global set is introduced and the procedure extended to save the incoming value in a local, reset the global to the singleton of the current node, run the recursion, and finally reassign the union of the saved and current values.
