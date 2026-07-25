---
type: lesson
title: "A description only explains what it is smaller than"
figure: chaitin
works: [on-the-length-of-programs-for-computing-finite-binary-sequences, meta-math-the-quest-for-omega]
axes: [primitive-count, cognitive-load]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# A description only explains what it is smaller than

**Lesson:** Some rule can always be fitted to any finite body of observations, so the mere existence of a rule proves nothing about whether the observations have structure. What separates an explanation from bookkeeping is the ratio of two sizes: how much it takes to state the rule against how much it takes to state the data the rule accounts for. A rule as long as the data it covers is the data wearing a costume. The degree to which the statement is shorter is the degree to which something has actually been understood, and this is a quantity, not a matter of taste.

The reason this holds is that the space of short descriptions is small and the space of things to describe is large, so brevity is scarce and therefore informative. Fitting a curve through arbitrary points costs about as many coefficients as there are points; the fit consumes exactly the freedom the data supplied and returns nothing. A genuinely short rule, by contrast, has spent almost none of that freedom and still reaches all the cases, which is only possible if the cases were not independent. Compression is not a proxy for insight, it is the same thing measured in symbols.

The same shape shows up wherever anything gets generated from something more compact: assumptions producing conclusions, a genome producing an organism, a program producing output. Each is a claim that the left side is smaller than the right, and each can be audited by measuring both. A programmer who takes this seriously prices every abstraction, framework, and configuration layer against the enumeration it replaces. If the general mechanism plus its call sites is no smaller than writing out the cases, the generality is decorative and the honest move is to write out the cases. And when a body of rules genuinely cannot be shortened, that is a finding about the domain rather than a failure of the programmer.

**Source:** [On the Length of Programs for Computing Finite Binary Sequences](../works/on-the-length-of-programs-for-computing-finite-binary-sequences.md) - the closing part, where an observer recording a sequence of events is asked what would count as having found a law, and a lookup table of the whole sequence is rejected as a theory. Also [Meta Math! The Quest for Omega](../works/meta-math-the-quest-for-omega.md) - the chapter drawing this out of Leibniz and restating scientific method, axiomatics, and heredity as one diagram of a compact input driving a large output.
