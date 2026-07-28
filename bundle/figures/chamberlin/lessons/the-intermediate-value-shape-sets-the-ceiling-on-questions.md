---
type: lesson
title: "What a language can ask is capped by what its intermediate values can hold"
figure: chamberlin
works: [quilt-an-xml-query-language]
axes: [expressiveness, primitive-count]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# What a language can ask is capped by what its intermediate values can hold

When a query language cannot express some question, the reflex is to blame the surface syntax and propose new clauses. That diagnosis is usually wrong. The binding form of the language — the type of thing a variable is allowed to hold between the matching step and the output step — is what actually fixes the ceiling. If the intermediate value is a flat record of scalar values, then everything the input had beyond scalars is gone by the time the output clause runs, and no amount of syntactic invention downstream can recover it. Questions about position, containment, or the order two things appeared in are then unaskable, not because nobody thought of the syntax but because the information stopped existing one stage earlier.

The design response is to widen the intermediate type until it is at least as rich as the structure you claim to support, and only then argue about notation. If your data model is hierarchical and ordered, a variable should be able to name a subtree with its descendants and its position intact, and a set-valued variable should carry an ordered collection rather than a bag. Once that holds, whole categories of query become sayable with the operators you already have, and features that looked like they needed dedicated machinery turn out to be ordinary expressions. The failing language and the working language in this comparison had similar levels of syntactic ambition; they differed in what a bound variable was permitted to be.

A programmer who believes this audits pipelines at their narrowest point rather than at their interface. Before adding an option to an API, ask what the internal representation between stages discards — the serialization format, the row type, the event payload, the AST node. Lossy intermediates are the reason feature requests keep arriving that all sound unrelated and all turn out to be the same bug. Conversely, this is a warning against over-normalizing early: flattening structure at the entrance because the first few use cases were flat is how you make the later use cases impossible.

**Source:** [Quilt: An XML Query Language for Heterogeneous Data Sources](../works/quilt-an-xml-query-language.md) — the paper's opening comparison of the candidate languages it drew from, where it locates the failure of the variable-binding approach it inherits in the scalar-relation result of that language's matching clause rather than in its verbosity, and then defines its own tuples of bindings over trees and ordered forests.
