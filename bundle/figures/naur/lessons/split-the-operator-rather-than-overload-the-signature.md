---
type: lesson
title: "Enumerate every case an operation can be in, and split the operator when the cases disagree"
figure: naur
works: [revised-report-on-the-algorithmic-language-algol-60]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Enumerate every case an operation can be in, and split the operator when the cases disagree

**Lesson:** Wherever you genuinely can pin an operation down, pin down every case of it, including the ones with no answer. Write the result kind as a function of the argument kinds for each combination, and where the combination has no meaning, say undefined rather than saying nothing. A table of cases is not verbose; it is the only form in which a reader or an implementer can tell the difference between a case you decided and a case you never thought about. Silence reads as permission, and two implementers reading the same silence will choose differently. This is the mirror image of deliberately declining to fix a behaviour: declining is legitimate only when you name the decline, and everything you have not named you owe a case for.

The discipline of writing the table out is what exposes the design error. If one symbol turns out to need two different result kinds depending on its operands, you are looking at two operations sharing a name, and the honest fix is two symbols. Give division that always yields an approximate result one symbol, defined over every mixture of argument kinds; give truncating division on whole numbers a different symbol, admitted only for whole-number arguments, and define its value by an expression built from operations already in the system rather than by prose about rounding. The reader now knows which one they wrote by looking at it, and no case analysis at the call site is needed to know the result kind. The same test applies anywhere: an operation whose signature depends on its arguments is a pun, and puns are where the ambiguity in a system lives.

The two supporting habits matter as much as the table itself. First, define the awkward cases by reduction to named operations you have already introduced, so a conversion has a specified value rather than a specified intent — a rounding on assignment given as an explicit expression, not as the word "converts". Second, when the case analysis has genuinely open cells, keep them visible as cells: a base-and-exponent operation with several undefined combinations is more trustworthy written as a full table with holes than as a rule with an escape clause, because the holes are then countable, and someone can later close them one at a time without reopening the whole definition.

**Source:** [Revised Report on the Algorithmic Language ALGOL 60](../works/revised-report-on-the-algorithmic-language-algol-60.md) — section 3.3.4's rules relating operator and operand types to result types, in particular 3.3.4.2's separation of the always-approximate division from the whole-number-only division whose value is given by an expression in the already-defined sign and truncation functions, and 3.3.4.3's exhaustive base-and-exponent case analysis with its explicitly undefined combinations; together with section 4.2.4, which specifies the conversion applied on assignment across types as a named expression rather than as an intent.
