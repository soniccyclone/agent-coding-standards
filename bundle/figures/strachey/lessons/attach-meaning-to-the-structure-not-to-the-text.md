---
type: lesson
title: "Attach meaning to the structure, not to the text"
figure: strachey
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Attach meaning to the structure, not to the text

Scott and Strachey write grammars that are frankly ambiguous, then raise the obvious objection against themselves: if one string can be read two ways, a function from strings to meanings is not well defined, so their whole apparatus is ill-formed. Their answer is to relocate the domain. The meaning function was never really defined on strings; it is defined on the derivation — the structure that records how a phrase was built out of smaller phrases. A string that admits two derivations simply has two structures behind it, each with a perfectly determinate meaning, and there is no defect in the semantics at all. What there is, is a separate question about which structure a reader or a parser should recover from that string, and that question belongs to a different layer and a different day.

This is worth more than the technical repair suggests, because it tells you where to spend precision. Once meaning attaches to structure, the surface can be as convenient as you like: they note that a fully parenthesised form would remove every ambiguity and that no human will write it, so they use the loose form and keep their clauses in exact correspondence with the grammar's, so the abbreviation is mechanically undoable. The imprecision is deliberate, stated, and reversible, which is what separates it from sloppiness — the reader is told what the equations really range over, and could reconstruct the pedantic version if they cared to. Unstated abbreviation is a defect; announced abbreviation is a saving.

The same reasoning licenses a stronger move. When the natural way to state a construct requires two of its parts to agree in a way no context-free rule can express, they break out of the grammar class without apology and remark that the class was never something they owed loyalty to. Grammar formalisms are instruments for building parsers; they are not a standard the design has to satisfy, and contorting a construct so it fits inside one is paying for tidiness at the layer where tidiness buys the least. The invitation they extend — bring us a better definition system and we will use it — is the right posture: dogmatic about the mathematics of meaning, indifferent about the machinery of surface description.

Practically this argues for keeping every rule that matters — evaluation, validation, typing, transformation — defined over the internal structure, and treating the text as one of several possible ways to arrive at that structure. Systems that instead pin semantics to the written form end up with meaning that depends on formatting, rules that cannot be stated without talking about characters, and a permanent inability to add a second surface syntax. The order to insist on is structure first, meaning attached to structure, text as a lossy convenience on top.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the end of the section on states and commands, which concedes the grammars' ambiguity and answers it by defining the semantic mappings on annotated derivation trees rather than on expressions as such, noting that a fully bracketed form is available but intolerable to write; together with the recursion section's remark that the extended command syntax is no longer context-free and its refusal to treat that as a problem.
