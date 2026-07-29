---
type: lesson
title: "Give undefinedness a value instead of a hole"
figure: strachey
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Give undefinedness a value instead of a hole

The natural first instinct when some operation has no answer is to treat that as a missing case: the function simply isn't defined there, and every rule you write about functions now carries an implicit caveat about the places they don't reach. That instinct costs more than it looks like it costs. A partial operation cannot be composed with confidence, cannot be substituted into an equation without checking whether the substitution lands in a gap, and cannot be reasoned about by the same rules as the total operations it sits alongside. Every theorem grows a footnote, and the footnotes are where the errors live.

The alternative is to admit an element that means "no information here" and let every operation be total again. Nothing about the computation changes; what changes is that absence has become a citizen of the value space rather than a defect in the coverage of a mapping. Now composition is unconditional, the algebra has no exceptions, and the structure that carries the undefined element can be reused at every level: over a base domain, over functions between domains, over products and sums built from them, mechanically and by the same rule each time. The reason to prefer this framing is not aesthetic tidiness but that a uniform construction can be lifted; a patchwork of special cases cannot.

A programmer who has internalised this stops writing signatures whose honest reading is "returns a result, except sometimes." Errors, absent lookups, timeouts and nontermination become inhabitants of the result type, so that the caller composes rather than branches, and so that the laws the code is supposed to obey hold without qualification. The same reflex applies well outside language semantics: a protocol with an explicit "unknown" state is easier to reason about than one where silence has to be interpreted, and a schema with an explicit null is easier than one where a missing key means five different things.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the pivot in the recursion and lattice sections, where the authors decline the standard partial-function treatment in favour of adjoining a bottom element so the function spaces become total and their order structure can be derived mechanically at every level.
