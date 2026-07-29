---
type: lesson
title: "When every intermediate result is the same kind of thing, composition rules replace case analysis"
figure: thompson
works: [regular-expression-search-algorithm]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# When every intermediate result is the same kind of thing, composition rules replace case analysis

Thompson's translator for regular expressions is startlingly small — a stack, a handful of cases, one pass over the operators in postfix order — and the reason is not cleverness in any individual case. It is that every operand and every result of every operation is the same kind of object: a reference to a fragment of already-emitted code with a known way in. A binary operator consumes two of these and produces one. A unary operator consumes one and produces one. When the operators run out, exactly one such object remains, and it is the answer. No operator needs to know what its operands were built from, and no case has to consider what might be nested inside another.

This closure property is what collapses the combinatorics. Without it, a translator must reason about the pairing of constructs — how a repetition inside an alternation inside a concatenation behaves — and the number of situations to handle grows with the product of the construct kinds. With it, each construct is defined only against the uniform representation, so the number of situations to handle equals the number of constructs. The algebra of the input language then maps directly onto emission: a repetition is realized by observing that repeating something is equivalent to either matching nothing or matching it once and repeating again, and that identity becomes a fixed, constant-size piece of structure wired around whatever fragment the operand happened to be. The law in the notation and the wiring in the output are the same fact stated twice.

The consequence Thompson draws at the end of the paper is the practical test of whether you have achieved this: new operators and new atoms can be added without disturbing anything, because they only have to produce and consume the uniform representation. An extension point you do not have to design is the signature of a representation that closed properly. Conversely, if adding a construct to your translator, evaluator, or query builder requires touching the handling of existing constructs, the intermediate representation is not closed and you are paying for that in every future change.

A programmer who believes this designs the intermediate form before the operations. The question they ask first is not "how do I handle each syntactic case" but "what single kind of value can every case both accept and yield" — and they treat any operation whose result is a different kind of thing from its inputs as a joint that will have to be special-cased forever.

**Source:** [Regular Expression Search Algorithm](../works/regular-expression-search-algorithm.md) — the compiler section, where a stack of pointers to compiled operands lets each operator combine its inputs into a replacement operand, including the identity used to realize closure, plus the closing note that new operators and special atoms extend the scheme freely.
