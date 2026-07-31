---
type: lesson
title: "With no reference answer available, test that two independent routes to the same artifact produce the same artifact"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# With no reference answer available, test that two independent routes to the same artifact produce the same artifact

**Lesson:** Some components have no available oracle. Nobody can write down, for an arbitrary input, what the correct output is, because producing that output is exactly the thing the component is for and the only other way to obtain it is to do the same work by hand. Testing such a component against expected outputs therefore degenerates into testing it against a handful of cases small enough that a person could do them, which is not much of a test. The alternative is to stop asking for a correct answer and ask instead for agreement: find two genuinely different paths that should arrive at the same artifact, and demand that the artifacts be identical. Nothing needs to be known about what the artifact ought to contain. The check is complete and mechanical and it does not care how large the input is.

The cleanest source of such a pair is self-application. When a transformer is written in the language it transforms, you can transform it with itself and then use the result to transform some third thing — and the same third thing can be transformed by the original. Two routes, one destination, and the comparison is a plain equality. What this actually tests is stronger than it looks: it exercises the transformer over an input as complicated as the transformer, which is far more demanding than any input a test author would have thought to write, and it detects any place where the transformer's output disagrees with its own semantics, which is the class of bug that ordinary tests miss because the wrong behaviour is consistent.

The price is that identity is an unforgiving predicate and the failures are miserable to localize. A mismatch tells you two artifacts differ, not which route was wrong or where the divergence began, and the difference propagates so that a single early disagreement shows up as a large diff. Worse, the artifacts can differ for reasons that are not bugs at all — a counter that starts from a different number, an iteration order that depends on where things were allocated, anything at all that varies between the two environments. So the technique imposes a design obligation on the thing being tested: every incidental choice must be made deterministically, derived from the input rather than from the ambient state, or the equality check will be too noisy to run. That obligation is worth incurring for its own sake, and it is the real reason to want such a test even before it catches anything.

Generalized: whenever you cannot state what the output should be, look for a redundancy — the same result reachable two ways, a transformation and its inverse, a value derivable from two independent sources — and assert the agreement. It is the only style of check that scales to components whose whole purpose is to produce something you could not have produced yourself.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 5 section 5.5.7, the footnote attached to the suggestion of compiling the compiler itself and running the result on a new machine: it describes the resulting correctness test as checking whether compiling a program on the new machine using the compiled compiler produces something identical to compiling that program on the original system, and remarks that tracking down the source of any difference is often frustrating because the results are extremely sensitive to minuscule details.
