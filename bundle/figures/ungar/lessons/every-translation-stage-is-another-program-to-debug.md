---
type: lesson
title: "Each stage that rewrites your source is another program you are on the hook for understanding"
figure: ungar
works: [debugging-and-the-experience-of-immediacy]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Each stage that rewrites your source is another program you are on the hook for understanding

**Lesson:** Any mechanism that transforms what you wrote into something else before it runs — expansion, generation, a checking pass that alters what is admissible, a translation step in the build — creates a second artifact with its own behavior. Most of the time the second artifact is invisible and everything is fine. It becomes visible exactly when something goes wrong, and at that moment the programmer is debugging two programs at once: the one they wrote and reason about, and the one that actually executed. The second one they did not write, may never have read, and have no mental model of. Whatever the transformation bought in expressiveness is repaid, with interest, in the worst possible circumstances.

The accounting most people do is wrong because it prices the transformation only in the good case. The honest price is the good case discounted by how often you land in the bad one, plus the standing cost of a program you cannot see. Two properties make the difference between a transformation that pays and one that does not. First, whether the identity between what you wrote and what runs is preserved well enough that failures are reported in your terms rather than the derived artifact's. Second, whether engaging with the transformation is optional — something you reason about when you choose to — or mandatory, imposed on every program whether it helps or not. Machinery that is both invisible in the good case and terms-preserving in the bad case is nearly free. Machinery that forces indirect reasoning about a derived form on every program charges everyone, continuously, to benefit the cases that needed it.

The practical discipline is to notice each such stage in your own systems and ask what a failure inside it looks like from the outside. If the answer is that someone reads generated output to understand behavior they did not intend, that stage is not a convenience, it is a debt with a due date. This does not condemn transformation — it argues for keeping the count low, keeping each one traceable back to the source it came from, and being suspicious of any stage whose benefit accrues to a minority of code while its reasoning cost is charged to all of it.

**Source:** [Debugging and the Experience of Immediacy](../works/debugging-and-the-experience-of-immediacy.md) — the closing section on language design, where static translation stages, including macro expansion and mandatory static checking, are assessed by how far they push what runs away from what the programmer wrote and can see.
