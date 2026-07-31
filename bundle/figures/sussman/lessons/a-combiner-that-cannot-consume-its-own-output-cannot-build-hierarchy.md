---
type: lesson
title: "A means of combination that cannot consume its own output cannot build hierarchy"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A means of combination that cannot consume its own output cannot build hierarchy

**Lesson:** An operation for combining things has the closure property when whatever it produces can itself be fed back in as an input. Stated that way it sounds like a technicality. It is the entire reason hierarchical structure is possible: parts made of parts made of parts exist only if the combiner accepts its own results, and a combiner lacking that property can build exactly one level and then stops.

The diagnostic value comes from applying it to real tools, and the authors do. Some languages combine data by assembling it into arrays but cannot form arrays whose elements are arrays. Others permit nesting but require the programmer to manage pointers explicitly and to declare in advance the form each field may hold. In each case combination exists and closure does not, or is available only at a cost that discourages using it. The consequence is not that certain programs become impossible but that every recursive shape in the problem domain must be encoded by hand, differently each time, with the language unable to help.

The follow-on effect is what Perlis's aphorism records: better a hundred operations on one data structure than ten on ten. Where a single closed combiner supplies universal glue, one uniform representation carries every compound thing, and an operation written once applies everywhere. Where each compound shape is its own declared type, operations specialize to those types, and functions that would otherwise cooperate cannot, because each speaks a different structural dialect. The proliferation of data structures is what fragments the function library, and the fragmentation is the real cost of the missing closure.

The habit worth taking: when adopting or designing any combining mechanism -- a data format, a query composition rule, a pipeline operator, a configuration language -- check first whether its output is a legal input to itself. That one question predicts whether users will be able to build depth, and whether the operations they write will compose or merely accumulate.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.2's introduction of the closure property: an operation for combining data objects satisfies closure if the results of combining things with it can themselves be combined by the same operation, and closure is the key to power in any means of combination because it permits hierarchical structures -- with the footnote observing that many popular languages' data combiners do not satisfy closure or make it cumbersome, that arrays of arrays are unavailable in some and nested structures require explicit pointer manipulation and prespecified field forms in others, and quoting Perlis that it is better to have 100 functions operate on one data structure than 10 functions on 10 data structures.
