---
type: lesson
title: "A name nothing was assumed about turns one worked case into the general theorem, and the freshness check runs only over the premises you actually used"
figure: church
works: [introduction-to-mathematical-logic]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# A name nothing was assumed about turns one worked case into the general theorem, and the freshness check runs only over the premises you actually used

Deep in the completeness argument Church has a derivation about one particular individual constant — a specific name, introduced earlier purely to have something to point at while discharging an existential. At the end he replaces that constant by a variable everywhere in the derivation and generalizes over it, and the concrete argument becomes a universal statement without a single step being reworked. That is not a trick applied at the end; it is a fact about what the argument had been all along. Because the name carried no information, the derivation never had any way to depend on which thing it named, so the run over one case was already a proof over all of them. The generalization step only reads out something the text had quietly guaranteed.

The condition that licenses this is the interesting part, and Church is careful about its scope. In a footnote defending exactly this move he does not say the constant is absent from the development; he says it is absent from the hypotheses that were actually used in that subderivation. Freshness is a property relative to the premise set you consumed, not to the ambient world. A symbol can be all over the surrounding chapter and the generalization is still sound, provided no assumption this particular argument leaned on mentions it. Getting that boundary wrong costs you in both directions: draw it too wide and you refuse generalizations you had earned, draw it too narrow and you promote a claim about a constrained object into a claim about every object, which is unsound and leaves no trace on the page.

The engineering version is that the ledger you need is per-argument, not per-scope. A procedure handed an opaque handle it never inspects is polymorphic in that handle whether or not anyone declared it so, and the single case you tested is the general case. The moment any premise you relied on speaks about the concrete instance — a fixture's particular contents, a config value, one tenant's schema — the same code stops being general and no amount of testing it on that instance will tell you. So the discipline is to keep track, for each conclusion you want to export, of which assumptions it actually consumed and which concrete names those assumptions mention. That set, not the surrounding namespace, decides whether your one worked example is already the theorem.

**Source:** [Introduction to Mathematical Logic](../works/introduction-to-mathematical-logic.md) — §45, the construction of a maximal consistent class, where a derivation about a chosen individual constant is converted into a generalized one, and its footnote restricting the non-occurrence condition to the hypotheses actually used in that proof.
