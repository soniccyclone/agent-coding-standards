---
type: lesson
title: "Modularity comes from agreeing on one interchange representation, not from splitting code into modules"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Modularity comes from agreeing on one interchange representation, not from splitting code into modules

**Lesson:** Once four processing stages are separated into named operations that all consume and produce the same kind of thing, something happens that mere separation would not have produced: the pieces recombine. The same components rearrange into a program computing squares of a generated series, into one multiplying selected elements, into one finding the highest salary among filtered personnel records. Nobody planned those combinations. They are available because every stage speaks the same interchange format.

That is the actual content of modularity, and it is worth distinguishing from the thing usually called by that name. Splitting a program into separate files, classes or services divides the code without necessarily making any two pieces composable -- if each piece takes and returns its own bespoke shapes, you have partitioned the work and gained nothing recombinable. Composability requires a *conventional interface*: one agreed representation flowing between stages, so that the output of any component is a legal input to any other. The analogy the authors draw is to signal-processing hardware, where designers cascade parts from standardized families precisely because the connections are standardized.

The empirical support is striking and easy to overlook -- an analysis of a widely used scientific subroutine library found roughly ninety percent of its code fitting the produce-filter-transform-combine pattern. What looked like hundreds of distinct specialized routines was mostly one shape, written out repeatedly because the language offered no common medium in which to express it once.

There is a second, delayed payoff. Because all structural dependence is now concentrated in a handful of sequence operations, the representation underneath can be replaced without touching the programs built above -- which is exactly what the book later exploits to extend the same pipeline vocabulary to infinite sequences. Choosing a conventional interface is therefore not only about the recombinations available today; it is what keeps the door open to changing the substrate later.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.2.3, which reformulates both example procedures as compositions of map, filter, accumulate and enumerate, states that the value of expressing programs as sequence operations is designs constructed by combining relatively independent pieces, draws the analogy to cascading standardized filters and transducers in signal processing, demonstrates reuse by recombining the same components into three further programs including one over personnel records, notes in a footnote Waters's finding that ninety percent of the Fortran Scientific Subroutine Package fits the map-filter-accumulate paradigm, and observes that uniform representation localizes data-structure dependencies to a few operations so alternative representations can be substituted while leaving the overall design intact.
