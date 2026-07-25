---
type: lesson
title: "Treat guaranteed termination of your own tooling as a budget you may knowingly overspend"
figure: cardelli
works: [structural-subtyping-and-the-notion-of-power-type, on-understanding-types-data-abstraction-and-polymorphism, basic-polymorphic-typechecking]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Treat guaranteed termination of your own tooling as a budget you may knowingly overspend

**Lesson:** Expressiveness in a description language is not free, and the currency it is bought with is the tractability of checking. Push far enough and the checker can no longer be guaranteed to terminate at all. The instinct is to treat that boundary as sacred, but the more useful stance is to treat it as a budget with an exchange rate you should know. Three positions appear across this work and all three are argued rather than assumed. One accepts a checker that may diverge, on the grounds that divergence occurs only for degenerate constructions or for uses beyond what any conventional language can express, and that ordinary programs check quickly. One stops deliberately below a boundary, noting what the next level up would buy and that the cost has not yet been shown to be worth paying. One notes that an incomplete procedure which sometimes gives up is a legitimate option, because a program's meaning gets beyond human comprehension well before it reaches the limits of the heuristic.

The common structure is that the question is never merely whether a property holds but who pays when it fails, and how often the failing case occurs in the population of things you actually write. A theoretical worst case that no realistic input hits is a different kind of problem from one that shows up in the second week of use. Making that judgement requires knowing which sublanguage carries the weight; here it is structural checking that keeps things practical even when the full system does not terminate, so the safe region is identifiable rather than a matter of luck.

What this rules out is not ambition but silence. The failure mode is a design that quietly ends up undecidable, or exponential, because nobody tracked what each added construct cost, and whose users discover the limit as an unexplained hang. Stating the position, including where you stopped and what you would have gained by continuing, converts a hazard into a documented trade and leaves the next person able to revisit it with evidence.

**Source:** [Structural Subtyping and the Notion of Power Type](../works/structural-subtyping-and-the-notion-of-power-type.md) — the discussion of undecidable checking, which lays out the choice between limiting expressive power and living with possible divergence, and explains why divergent cases stay degenerate in practice. Also [On Understanding Types, Data Abstraction, and Polymorphism](../works/on-understanding-types-data-abstraction-and-polymorphism.md) — the hierarchical classification of type systems and its closing judgement about stopping at a particular level pending experience with the extra complications. Also [Basic Polymorphic Typechecking](../works/basic-polymorphic-typechecking.md) — the digression noting that undecidable or exponential systems can be served by incomplete heuristics, given limits on how complex a program can usefully be.
