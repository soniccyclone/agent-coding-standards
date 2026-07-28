---
type: lesson
title: "The nouns are the design; build a theory of them before defining any behavior"
figure: milner
works: [the-definition-of-standard-ml]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# The nouns are the design; build a theory of them before defining any behavior

**Lesson:** Ask what a system is and the usual answer describes its syntax or its operations. The claim made here is that neither is the system's character. What distinguishes one language from another is the collection of abstract entities its users actually think in — the things its keywords are names for. Two systems with near-identical surfaces and different underlying entities are different systems; two with different surfaces over the same entities are notational variants. So the first task, before any rule about behavior is written, is to say precisely what those entities are.

Two constraints on how you say it are worth taking seriously. First, the notation must be independent of the thing being defined; describing a language in terms of another language is deferring the problem rather than solving it, and the choice made here is ordinary mathematics. Second — and this is the part usually skipped — it is not enough to write down definitions. The definer must develop a small theory of the entities: state and check properties that establish they are worth studying at all, the way a mathematician does after introducing a structure. Objects with nice properties are tractable; objects merely stipulated are not. A definition that skips this step, the preface warns, may be entirely formal and still yield no insight.

The book practises what it prescribes. Before any rule appears, there are pages establishing what it means for a type to admit equality, when a type structure is well-formed, what it means for one environment to enrich another and separately for one to be an instance of another, and how those two combine into a single matching relation. Each is a property of the entities, provable and reusable, and the rules that follow are short because they can lean on them. The development history records that the crucial insight in the module system was exactly the separation of enrichment from instantiation — that is, getting the theory of the nouns right — not any decision about syntax.

For anyone building a system rather than a language, the translation is direct: the domain model is the design, and a model is not finished when the types compile. It is finished when you can state and defend the invariants relating its parts — which values are interchangeable, which are more specific than others, what it means for one to satisfy another's interface. Do that first and the behavioral logic gets short. Skip it and every operation carries its own private, unexamined, and eventually inconsistent notion of what those relationships are.

**Source:** [The Definition of Standard ML (Revised)](../works/the-definition-of-standard-ml.md) — the preface's account of the language-definer's twofold job, and the sections defining semantic objects and their properties in advance of the inference rules, notably the treatment of equality, well-formedness, enrichment, instantiation, and matching.
