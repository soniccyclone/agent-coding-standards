---
type: lesson
title: "Two formalisms can reach the same results while differing without bound in the effort to reach them"
figure: godel
works: [on-the-length-of-proofs]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Two formalisms can reach the same results while differing without bound in the effort to reach them

**Lesson:** Take two systems where the stronger one is a conservative-looking extension of the weaker — richer vocabulary, higher-order quantification — and restrict attention to statements *both* can establish. The extra strength is, for these statements, extensionally useless: nothing new becomes reachable. Gödel's short note shows that the extra strength is nevertheless worth an unbounded amount, because infinitely many of those shared statements have derivations in the stronger system that are drastically shorter than anything the weaker system can manage. And the gap is not a constant factor. For any function the weaker system can compute at all, there are statements whose shortest weak derivation exceeds that function applied to their shortest strong derivation. Pick a growth rate and the gap eventually beats it.

Two consequences fall out, and the second is the sharper one. First, equivalence of reachable results tells you nothing about the cost of reaching them, so "these are equally powerful" is not an argument that they are equally good. Every claim that two languages are interchangeable because they compute the same class of functions is committing exactly this error: the class is the same and the effort is not comparable. Second — and this is what makes the situation genuinely uncomfortable — the size of what you are losing cannot be assessed from inside the weaker system, because the speedup outruns every function that system can compute. A formalism cannot measure the economy it is forgoing by not being stronger. You do not get to estimate the cost of your abstraction's poverty using tools built from that abstraction.

For a programmer this is the principled statement of why abstraction earns its keep even when it adds nothing you could not have written by hand, and simultaneously why arguments about it never resolve on the merits from within the weaker position. Everything expressible in a language with a weak type system, no higher-order functions, no macros, or no algebraic data types is still expressible after removing those features — the reachable behaviours are identical — and the code needed to get there can grow by amounts nobody working in the impoverished dialect can predict. The person embedded in the weaker system experiences the extra work as normal, because there is no internal yardstick that shows the loss. That is also why the reverse move, deliberately dropping to a weaker formalism, needs a reason other than "we can still express everything": you can, and the price is unbounded.

The disciplined response is to treat "does this addition let us do anything new?" as the wrong screening question for a language, library, or notation. The right one is what it does to the size of the derivations you actually write, measured by comparison with a system that already has it — not by introspection from inside the system that does not.

**Source:** [On the Length of Proofs](../works/on-the-length-of-proofs.md) — the whole of this two-page note: the definition of proof length as a count of steps, and the theorem that for every function computable in the weaker system there are infinitely many statements provable in both whose shortest weak derivation exceeds that function of their shortest strong one, with the closing observation that the effect is not merely to make new statements provable.
