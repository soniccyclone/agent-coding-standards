---
type: lesson
title: "Ask what a construct is forbidden to do"
figure: strachey
works: [fundamental-concepts-in-programming-languages]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics]
tags: [lesson]
---
# Ask what a construct is forbidden to do

Take any kind of thing a language deals in and ask, systematically, whether it can do everything the most ordinary kind of thing can: be denoted by an expression, be stored, be passed in, be produced as a result, be selected between by a conditional. Where a kind of thing can do only some of these, it holds a lesser status than the numbers do, and Strachey's point is that this asymmetry is almost never a considered decision. It is inherited — from a tradition in which functions were constants with recognisable names rather than values you compute — and it survives because nobody asked the question.

The test is powerful because it converts a vague sense that a language is awkward into a checklist that produces specific, actionable gaps. It also predicts where a language will feel arbitrary: if you can choose between two numbers with a conditional but not between two procedures, every program that needs the latter has to encode it some other way, and the encodings proliferate as ad hoc conventions. Notably, Strachey argues that resistance to this idea is mostly a failure of imagination about representation — the reason practitioners find higher-order values unreal is that they cannot picture what one is. He removes the obstacle by exhibiting the representation: a function value is a pair, code plus a handle on the environment its free names come from, and once that is on the table passing a function, storing one, or returning one from another function all reduce to moving a pair around. He then shows that the same shape covers the harder cases, including self-reference, which becomes a representation that points back into itself.

The consequence is a preference for removing restrictions over adding features. Where a designer's instinct is to add a special mechanism for the case a second-class construct cannot handle — a distinct facility for separately compiled program pieces, say — the discipline says look for the restriction whose removal makes that case ordinary. Strachey's own demonstration is exactly this: separate compilation stops needing special machinery once functions may return functions, since a piece of program parameterised by its external names is just a function you apply later. Each restriction lifted retires a family of workarounds, and the language gets smaller rather than larger.

**Source:** [Fundamental Concepts in Programming Languages](../works/fundamental-concepts-in-programming-languages.md) — the section contrasting first- and second-class status, the account of function values as closures that follows it, and the treatment of program segmentation as an application of functions returning functions.
