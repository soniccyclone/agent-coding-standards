---
type: lesson
title: "When the same construct is forced on you in unrelated settings, you have found structure — factor it out"
figure: reynolds
works: [the-discoveries-of-continuations]
axes: [primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# When the same construct is forced on you in unrelated settings, you have found structure — factor it out

**Lesson:** One concept here was arrived at independently by at least seven people working on visibly unrelated problems: how a compiler must represent a label so that jumping out of a nested body works, what a state-transition evaluator has to keep on the side once its current work is exhausted, how to give an equation-style meaning to a jump, how to strip a construct out of a language by rewriting, and how a pattern-matching routine can report failure to something several levels up. None of these people were looking for the same thing, and the concept was not a convenience any of them chose — it was forced. That pattern of forced convergence is the most reliable evidence available that you are looking at real structure rather than a trick, and the right response is to name and factor out the common entity rather than to maintain a separate ad hoc treatment in each setting. The rediscoveries were not caused by researchers failing to read each other; they were caused by the concept genuinely being what each of those problems needed.

Two practical readings follow. First, you need a problem hard enough to force the abstraction into view. One of the near-misses in this story was formulated over a flat, unstructured model with no nesting at all; in that setting the construct is present but indistinguishable from ordinary iteration, and nothing in the formulation reveals what it is generally for — there is not even any syntactic thing whose meaning has to consume it. If a candidate abstraction looks unmotivated, suspect that the example is too small rather than that the abstraction is worthless, and try it against a setting with hierarchy in it.

Second, an abstraction is often easier to see in its plural form than in its degenerate one. The person who reached the concept via failure handling used two of them at once, one for success and one for failure, and said afterward that having two was what made the pattern recognizable — with a single instance there is nothing to compare against and the thing reads as an incidental extra argument. This suggests a deliberate tactic when you suspect a concept is hiding: instantiate it twice in the same program and see whether the two instances are the same shape. If they are, the shape is the abstraction, and the single-instance case you started from was simply too impoverished to display it.

**Source:** [The Discoveries of Continuations](../works/the-discoveries-of-continuations.md) — the opening claim that the repetition of discovery reflected the variety of settings rather than poor communication, the survey of the compiler, interpreter, program-transformation and denotational routes to the same concept, the assessment of Mazurkiewicz's unstructured automaton model as too limited to reveal the general nature of the idea, and F. L. Morris's recollection that a success-and-failure pair was easier to recognize than a single instance.
