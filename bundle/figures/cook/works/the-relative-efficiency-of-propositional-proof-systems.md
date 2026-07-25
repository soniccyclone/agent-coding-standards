---
type: work
title: "The Relative Efficiency of Propositional Proof Systems"
figure: cook
description: With Robert Reckhow, formalizes what a "propositional proof system" is in the abstract (a polynomial-time-checkable relation between proofs and the tautologies they certify) and defines what it means for one such system to simulate another with only polynomial blowup. The paper shows that finding a proof system with no super-polynomial worst-case proof length would settle NP versus co-NP, giving proof-length lower bounds a precise complexity-theoretic payoff. This is the paper that gave proof complexity its standard vocabulary (the "Cook-Reckhow" framework) and is still the reference definition the field cites.
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
year: 1979
url: http://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf
access: public
host: self-archived
tags: [work]
---

# The Relative Efficiency of Propositional Proof Systems

**Author(s):** Stephen A. Cook, Robert A. Reckhow
**Venue/year:** Journal of Symbolic Logic 44(1), 1979, pp. 36-50.
**Source:** http://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf — PDF self-archived on Cook's University of Toronto homepage (verified HTTP 200). Note: Cook's homepage lists a correction to Corollary 4.7 ("if P ≠ NP" should read "if coNP ≠ NP").

## Lessons
- [Abstract a family of artifacts down to the property that makes them useful, then let cheap translation sort out which design choices were ever real](../lessons/define-the-family-by-its-checkable-property.md)
- [The ability to name an intermediate result is not convenience, it is the difference between linear and exponential size](../lessons/the-power-to-name-is-the-power-to-compress.md)
- [Define a hard task by the cheap test that recognizes a good answer](../lessons/the-recognizer-is-the-real-specification.md)
