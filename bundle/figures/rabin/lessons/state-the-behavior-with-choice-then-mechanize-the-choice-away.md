---
type: lesson
title: "State the behavior by allowing choices, then let a mechanical translation remove them"
figure: rabin
works: [finite-automata-and-their-decision-problems]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# State the behavior by allowing choices, then let a mechanical translation remove them

**Lesson:** There are two separate jobs in getting a machine to do something, and confusing them makes both harder. One job is saying what counts as success. The other is arranging a device that decides success by following exactly one path. This work drives a wedge between them: describe the intended behavior by permitting the description to branch freely wherever the choice does not matter, declare an input successful if *some* branch works out, and then apply a fixed transformation that folds all the branches into a single-path device. The transformation is not clever and not creative — it tracks, as one composite state, the whole collection of situations the branching description could be in. It is exactly the kind of tedious bookkeeping a person should never do by hand and a program should always do.

The reason this is not a trick is that the branching form and the single-path form recognize precisely the same behaviors. Choice buys nothing in what can be described and enormous amounts in how compactly and legibly you can describe it. The paper makes the point twice over: allowing the reader to move backward as well as forward also fails to add power, even though backward reference intuitively looks like extra memory, because a bounded state can already carry forward everything a backward scan could recover. Both results share one shape — a feature that appears to extend reach turns out only to extend convenience of statement.

For a programmer this reframes what an abstraction is for. Before building machinery to support a new capability, ask whether the capability enlarges the set of reachable behaviors or merely shortens their expression. If it only shortens expression, the right response is not new runtime machinery but a translation step: keep the convenient form as the thing humans write and reason about, generate the awkward efficient form, and never maintain the generated artifact by hand. The blow-up in the generated form is a real cost, but it is paid in a currency (machine states, memory) that scales far more cheaply than the currency the convenient form saves (human attention).

The same wedge also explains why the convenient form is the better place to prove things. Several closure facts in this work fall out in a few lines when argued over branching descriptions and require lengthy explicit constructions otherwise. If two representations are equivalent, you are free to reason in whichever one makes the argument shortest and let the equivalence carry the conclusion across.

**Source:** [Finite Automata and Their Decision Problems](../works/finite-automata-and-their-decision-problems.md) — the chapter introducing choice-based operation and the subset-of-states translation that eliminates it, plus the later result reducing back-and-forth motion to strictly forward motion.
