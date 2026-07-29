---
type: lesson
title: "Give a construct a meaning, not another notation"
figure: strachey
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Give a construct a meaning, not another notation

The standard way to explain what a program means is to say what it turns into: machine code, an intermediate form, the transitions of some hypothetical machine. Scott and Strachey's objection is that this never terminates the question. A translation explains one notation by another notation, so you are always left asking what the target means, and the explanation of any individual construct gets entangled with the bookkeeping of the target — symbol tables, identifier lists, state vectors of an invented machine — none of which was part of the construct you wanted to understand. Their alternative is to make each construct denote a mathematical object that exists independently of any notation, and to say what that object is.

The distinction they use to make this vivid is between the marks that name a number and the number itself. Many strings name the same number, in one notation or several, and the interesting question — which expressions are equivalent — is not answerable at the level of the strings. Once each expression is assigned an object, equivalence has a definition, and a claim like "this symbolic procedure computes addition" becomes a theorem with a proof rather than an appeal to intuition. Their sharpest observation is that before the meaning function existed, such a question could not even be posed. The same holds for programs: making the denotation explicit turns "is this implementation correct?" from a matter of taste into a comparison against a stated standard.

The independence has a second payoff. Since the semantic equations are stated relative to whatever the primitive operations and the state space happen to be, the same equations describe a whole family of interpretations, and you can ask whether two programs are equivalent under one interpretation but not another. Committing early to a single concrete representation forfeits that, and Scott and Strachey treat any needless restriction of generality as a habit that will mislead you later even where it seems harmless now.

A programmer who takes this seriously stops accepting "it compiles to this" as an explanation of a feature. Where a construct's behaviour is defined only by what the implementation does, there is no way to say the implementation is wrong, and every question about equivalence, refactoring, or optimisation reduces to reading the compiler. The remedy is to state independently what the construct denotes, and then treat the implementation as something answerable to it.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the introductory contrast between expressions and the objects they denote, the discussion of models and program equivalence in the section on identifiers and environments, and the concluding claim that the mathematics supplies the standard an implementation must meet.
