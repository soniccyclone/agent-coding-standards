---
type: lesson
title: "When users can define new things, axiomatize the forms of definition, not the things"
figure: hoare
works: [notes-on-data-structuring]
axes: [verifiability, primitive-count, expressiveness]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# When users can define new things, axiomatize the forms of definition, not the things

**Lesson:** A fixed catalogue of concepts can be pinned down by a fixed list of rules — this is what the classical treatment of the natural numbers looks like. That approach is unavailable the moment your system lets people introduce concepts you have never seen: there is no list to write, because the things to be described do not exist yet. The way out is to move up one level and give rules for each *way of defining*, as a pattern with the definition's own parts standing in it. A user writes a definition; the pattern instantiates against it; out comes the rule set for that particular thing. You have specified an unbounded family by writing down a handful of schemes, one per construction form, and the count of construction forms is small precisely because you chose it to be.

This reframes what the design of a construction form costs. Each one you admit obliges you to say, in general, what any instance of it means: which values it brings into existence, that there are no others, how its parts are recovered, and — where the form permits an optional property such as an ordering — how that property is induced from the parts. If you cannot write the scheme, the form is not understood well enough to ship, whatever the examples suggest. This is a much sharper test than asking whether the form seems useful, and it is the reason a small set of composition rules is worth more than a large set of built-in structures: the small set is fully described, and it describes everything anybody builds from it.

Be honest, finally, about how such a foundation gets used. It is not the instrument for checking a real program; a proof conducted directly against the underlying rules for anything non-trivial is unbearable. Its job is to underwrite a modest number of familiar working properties — that two things are equal when they agree everywhere, that membership distributes over the combining operations, that the ordering behaves as ordering should — which are established once and thereafter used informally, at speed, by people who never look at the rules again. That is the correct economy of a formal layer: capital, spent once to buy facts, not currency handled in every transaction. It also explains why the foundation still matters to someone who will never write a proof, since it is what circumscribes exactly how much freedom an implementer has when choosing a representation.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the axiomatisation chapter, which lists the intended roles of the axioms (including stating the necessary properties of any representation while granting circumscribed freedom in choosing one), explains that a fixed axiom set of the kind available for integers is impossible because the applicable axioms depend on how each type was defined, gives instead a schema per structuring method from which a particular type's axioms are derived, and states that these are not meant for direct use in proving non-trivial programs but for establishing familiar properties of the data spaces which are then used informally.
