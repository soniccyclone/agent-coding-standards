---
type: lesson
title: "Before building the general mechanism, check whether the feature people want is shorthand for something you already have"
figure: ingalls
works: [fabrik-a-visual-programming-environment]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Before building the general mechanism, check whether the feature people want is shorthand for something you already have

**Lesson:** A capability can look incompatible with your model and turn out to be an abbreviation within it. Relations that work in both directions appear to demand cycles, and cycles appear to demand giving up an acyclic, order-free model in favour of a general constraint solver. But look at what people actually build with two-way relations and most of them are not one circular thing: they are several independent one-way computations that happen to share a picture, each with its own entry point and its own outward course. Under that reading nothing circular is required at all — you keep the simple model and let the notation abbreviate the several paths into one drawing. The general machinery would have been built to serve cases that were never really there.

The move that makes this available is refusing to reason about the feature from its surface appearance and instead surveying the uses. The surface says "bidirectional, therefore cyclic, therefore constraints." The uses say "an author wants to write the relationship once and excite it from either end." Those are different requirements, and only the second one has to be met. This is a general discipline for feature requests: the form in which a capability is asked for is usually borrowed from a system where it was implemented some particular way, and adopting the request verbatim imports that system's machinery along with it.

Two obligations come with taking the cheap route. First, name the cases you are giving up: when enough terms of a relation are open to excitation, the direction of causality genuinely becomes ambiguous, and no amount of notation fixes it. Second, decide that trade in the open and record it, along with the escape routes available later — a restriction that forecloses the ambiguous shapes, or the general solver you declined to build. A simplification that is chosen with its failure mode named is engineering; the same simplification adopted because nobody looked is a defect waiting to be discovered by a user. The payoff to weigh against that risk is not only implementation effort saved but library size: a component that runs both ways is one component, not two, and a mechanism that halves the vocabulary a user must learn is worth accepting a stated ambiguity for.

**Source:** [Fabrik: A Visual Programming Environment](../works/fabrik-a-visual-programming-environment.md) — the bidirectionality section, whose central observation is that most uses of two-way connection are a shorthand for multiple independent flow paths that can be treated separately, together with its worked temperature-conversion example, its acknowledgement that a component with too many two-way terminals makes causality genuinely ambiguous, its explicit decision to leave users exposed to that in exchange for the benefits, and its listing of the restrictions or constraint machinery available as remedies.
