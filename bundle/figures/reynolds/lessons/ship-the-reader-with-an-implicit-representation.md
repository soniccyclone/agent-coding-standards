---
type: lesson
title: "Ship the reader alongside an implicit representation, and expect its direction to dictate the reader's shape"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Ship the reader alongside an implicit representation, and expect its direction to dictate the reader's shape

**Lesson:** A compact encoding does not merely save space; it relocates work. What used to be present in the data is now implied by the data, and somebody has to do the implying. If that encoding is the output of your program, then leaving the reconstruction to your consumer means every consumer independently rediscovers a scheme you designed, and the first one to get it slightly wrong produces plausible garbage. The output of a program that emits an implicit representation is not the representation — it is the representation together with a means of interrogating it. Publish them as one thing, in the same place, so that the encoding's invariant has exactly one implementation that depends on it.

The interesting constraint is that you do not get to choose the reader's structure freely. The encoding was designed around the producer's access pattern, which pointed one way; the consumer usually wants the other way. Chains built backwards from each item to its predecessor are ideal to write, because the predecessor is exactly what you have in hand at the moment you write. They are useless to walk forwards, because there is no forwards. So the reader cannot be a simple loop — it has to descend to the far end first and do its work on the way back out, which is to say the direction of the links has forced the reader to be recursive. That is not a stylistic accident; it is the encoding's asymmetry surfacing in the only place it can.

Two things follow. First, when evaluating a compact encoding, cost the reader too — an encoding that halves your storage and forces every consumer into a stack-depth proportional to the data may not be the trade you wanted, and you will not notice if you only look at the writer. Second, if the reader's shape is awkward, that is information about the encoding rather than about the reader: an asymmetry you introduced for the producer's convenience is being paid for on the other side, and it is worth checking whether it is being paid for more often than it is being collected.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.1.7's closing, which notes that because the link array is an output and the way it represents paths is rather implicit, it is useful to supply a procedure making any particular path explicit; gives that procedure as a higher-order one applying a supplied action to each node of the path in order; and observes that it is difficult to formulate iteratively because the links lead from the target back towards the source rather than forwards, so the problem is solved by a straightforward use of recursion.
