---
type: lesson
title: "Keep the plausible assumption out of the load path, even when everyone believes it"
figure: strassen
works: [relative-bilinear-complexity-and-matrix-multiplication]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Keep the plausible assumption out of the load path, even when everyone believes it

**Lesson:** Every mature field accumulates a few regularity assumptions that everyone expects to be true, that nobody has proved, and that make a great deal of theory fall out immediately if granted — combining two independent instances costs exactly the sum of their individual costs, an optimization is never worth more than the sum of its parts, a shared resource behaves like private resources added up. These are the most dangerous premises available, precisely because they are so productive: a result derived from one is cheap, publishable, and structurally worthless if the premise fails. The discipline is to treat the plausible assumption as a hint about where to look, and then to pay whatever the harder proof costs to obtain the result without it. Doing the extra work when the assumption seems obviously true is the point, not a formality.

The payoff is not just insurance, though the insurance is real: in the case that motivates this, the natural additivity assumption turned out to be false, and it was falsified in the same work that had just proved the key theorem without needing it — so the entire edifice built on the unconditional proof survived intact while anything that had leaned on the conjecture would have collapsed. The deeper payoff is that removing an assumption from a proof tells you which weakened form of the assumption is actually true. A theorem that was expected to require exact additivity but in fact only needs an asymptotic version is, read from the other side, a proof of asymptotic additivity: the false conjecture had a true residue, and the unconditional argument is what isolates it. You do not learn that by assuming the conjecture, because the assumption hides exactly the seam where it fails.

Applied engineering-side, the rule is to notice which of your invariants are proved, which are enforced, and which are merely expected, and to know exactly which conclusions depend on the third category. Systems accumulate these silently — clocks are roughly monotonic, this queue is roughly FIFO, retries are roughly independent. Each is fine as a heuristic and lethal as a premise. When a conclusion you care about rests on one, the productive response is not to argue that the assumption is surely fine but to find out what survives without it, because that residue is both what you can safely rely on and, usually, a sharper statement than the one you set out to prove.

**Source:** [Relative Bilinear Complexity and Matrix Multiplication](../works/relative-bilinear-complexity-and-matrix-multiplication.md) — the introduction's account of the additivity conjecture: the key theorem for bounding the exponent would follow at once if additivity for border rank were granted, Schönhage instead proved it unconditionally by a recursion argument and in the same work exhibited a counterexample to the conjecture itself, and the unconditional theorem can therefore be reread as an asymptotic confirmation of the very statement that is false exactly.
