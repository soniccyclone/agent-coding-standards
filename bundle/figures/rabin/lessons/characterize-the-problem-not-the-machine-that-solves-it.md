---
type: lesson
title: "Characterize the problem intrinsically, not by the machine that solves it"
figure: rabin
works: [finite-automata-and-their-decision-problems]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Characterize the problem intrinsically, not by the machine that solves it

**Lesson:** Asking whether some machine exists that handles a given task is an awkward question, because the space of candidate machines is unbounded and a failed search proves nothing. This work replaces that question with one about the task alone. Group inputs together when no continuation can ever tell them apart; the task is machine-solvable exactly when this grouping leaves finitely many groups. No machine appears in the statement. The property being tested belongs to the problem, and the machine's existence follows as a consequence rather than being the thing under investigation.

Two things follow that no machine-side search could give you. First, negative results become as easy as positive ones — to show something is out of reach you exhibit an infinite family of inputs that pairwise differ in what they can still accept, which is often a couple of lines. Second, the grouping is not merely a decision procedure but the optimal implementation itself: the number of groups is the least number of internal configurations any solution can have. You get impossibility proofs and minimality from a single construction, because the grouping is measuring the actual information content of the task rather than any particular encoding of a solution.

The generalizable habit here is to look for the equivalence that your problem itself induces on its inputs — which distinctions in the input genuinely change what may happen later, and which are noise you are only carrying because your current representation happens to carry them. Any state a component keeps that does not separate futures is state you are paying for and can delete. Any two situations your code treats differently while no downstream behavior differs are a candidate merge. Running that analysis on a problem before writing the component is how you arrive at the minimal design instead of discovering it by successive deletion later.

There is a discipline lesson underneath. The intrinsic characterization was worth building even though direct constructions were already available, because it changed which arguments were short. A well-chosen invariant is not documentation of a solution you already have; it is the instrument that decides which solutions are possible at all, and it earns its keep by making a family of questions cheap rather than answering one.

**Source:** [Finite Automata and Their Decision Problems](../works/finite-automata-and-their-decision-problems.md) — the section developing the equivalence-relation characterization of recognizable sets (attributed there to Myhill and Nerode), its corollary identifying the minimal machine, and the short impossibility argument it enables immediately afterward.
