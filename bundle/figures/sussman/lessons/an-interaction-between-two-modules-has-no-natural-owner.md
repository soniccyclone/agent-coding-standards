---
type: lesson
title: "An interaction between two modules has no natural owner, and that is the cost, not the code"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# An interaction between two modules has no natural owner, and that is the cost, not the code

**Lesson:** Independent packages behind a common interface work beautifully until an operation has to span two of them. The obvious answer is to write the mixed case explicitly and register it, which works. The authors then count the cost, and the interesting part of the count is not the quantity. Yes, adding a type now means writing every cross-combination as well, easily more code than the type itself. The part that actually breaks the design is the question of *whose job it is*. Mixing complex with ordinary numbers plausibly belongs to the complex package. Mixing rational with complex could belong to either, or to some third package built on both — and there is no argument from the structure that settles it.

That is worth stating as a general property rather than a quirk of arithmetic. A module can own its own behaviour. Nobody owns the relationship between two modules, because by construction each was written not knowing about the other. So every cross-module operation forces a decision that is not derivable from the decomposition, and with many packages and many pairings, the meta-problem — a coherent policy for dividing that responsibility — becomes, in the authors' word, overwhelming. The load that sinks such a system is not lines of code but a growing body of conventions about where things go, held by people rather than by the structure.

The practical consequence is that when you evaluate a decomposition, you must evaluate the interactions, not just the parts. A decomposition can look clean under the test "is each piece coherent and self-contained" and still be unworkable, because that test never asks what happens where two pieces meet. The better test: enumerate the pairs that will need to interact, and for each one ask whether the design tells you where the code lives. If the answer is a convention or a judgement call, you have found the part of the system that will rot, and it will rot in the seams where nobody is looking.

The escape, when one exists, is to stop putting the interaction anywhere. The authors get out of it by finding structure among the types themselves — relations that let one thing be viewed as another, so the mixed case is transformed into a same-type case that an existing owner already handles. Note the shape of that move: not "assign the orphan to somebody" but "arrange things so the orphan does not exist." When you meet the ownership question and no answer feels right, treat that as evidence that the question should be dissolved rather than answered, and go looking for the structure that dissolves it.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.5.2's opening on combining data of different types, which shows an explicit add-complex-to-schemenum installed under a mixed type key, observes that the cost of a new type then includes constructing and installing all its cross-type operations and can easily exceed the code for the type itself, argues that this undermines additivity, and points out that while mixed complex/ordinary operations plausibly belong to the complex package, complex/rational operations might belong to either package or a third, so that formulating coherent policies on the division of responsibility among packages becomes an overwhelming task; followed by the introduction of coercion as the way out.
