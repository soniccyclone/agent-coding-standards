---
type: lesson
title: "The argument for generic operations is organizational, not aesthetic: nobody can agree in advance"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# The argument for generic operations is organizational, not aesthetic: nobody can agree in advance

**Lesson:** Ordinary data abstraction puts a barrier between how a thing is used and how it is represented, which divides one design problem into two that can be solved separately. The authors then say plainly that this is not enough, and the reason they give is not a technical one. Programs are built by many people over long periods against requirements that change, so it is simply not possible for everyone to settle a representation in advance. The need for a second kind of barrier — one that separates competing design choices from *each other*, rather than separating use from implementation — follows from facts about how software gets made, not from any property of the computation.

That is a more useful justification than the one usually offered for polymorphism, because it tells you when you need it. If one person owns a data type and its lifetime is short, a single representation behind a barrier is complete and correct engineering; adding a dispatch layer buys nothing. The second barrier earns its cost exactly when the situation contains the conditions named: multiple independent authors, a long horizon, requirements that will move, or components that were written in isolation and must now be combined. Those are observable properties of a project, so the decision stops being a matter of taste.

The criterion attached is the sharp part. What is required is that modules can be incorporated into a larger system *additively* — without redesigning or reimplementing what already exists. Additivity is a strong and checkable standard, much stronger than "extensible" or "modular," and it is the thing to hold a design against. Ask concretely: when the next representation shows up, what has to be edited? If the answer includes anything already written and working, the barrier is not doing the job, whatever it is called. A structure passes only when the new case is new text.

The geometry the authors use makes the two barriers easy to keep distinct. The horizontal ones stack layers, isolating higher-level operations from lower-level representations, and they are what you get from ordinary information hiding. The vertical one runs the other way, partitioning the layer itself so alternative implementations can sit side by side and be developed separately. Most designs have plenty of the first and none of the second, which is exactly why adding a new variant so often means touching every layer at once.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - the introduction to chapter 2 section 2.4, which recaps the abstraction barrier of the rational-number package, argues that this is not yet powerful enough because it may not always make sense to speak of the underlying representation, observes that programming systems are often designed by many people over extended periods under changing requirements so that agreeing in advance on representation is not possible, calls for barriers that isolate different design choices from each other and conventions permitting modules to be incorporated additively without redesign or reimplementation, and introduces the horizontal and vertical abstraction barriers of the complex-number system.
