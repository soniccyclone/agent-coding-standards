---
type: work
title: "SIMULA 67 Common Base Language"
figure: dahl
description: The formal definition of Simula 67, laying out class, subclass, prefixing, and virtual quantities as concrete syntax and semantics rather than informal proposals. It is the reference document implementers actually built compilers against, distinct from the earlier conference papers that introduced the ideas piecemeal. Several revised editions were issued into the 1980s as the language and its implementations matured.
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
year: 1970
url: https://softwarepreservation.computerhistory.org/ALGOL/manual/Simula-CommonBaseLanguage.pdf
extraction: complete
access: public
host: institutional
tags: [work]
---

# SIMULA 67 Common Base Language

**Author(s):** Ole-Johan Dahl, Bjørn Myhrhaug, Kristen Nygaard
**Venue/year:** Publication No. S-22, Norwegian Computing Center (Norsk Regnesentral), Oslo, October 1970. First edition 1968; a final revision was issued as NR Report 743 in 1984.
**Source:** https://softwarepreservation.computerhistory.org/ALGOL/manual/Simula-CommonBaseLanguage.pdf — scanned PDF hosted at the Computer History Museum's Software Preservation Group archive (title page confirmed: "Common Base Language" by Dahl, Myhrhaug, and Nygaard, Norwegian Computing Center). Verified resolving 2026-07-24 (curl 200, application/pdf).

## Lessons
- [Reach a new paradigm by lifting a restriction off an existing primitive, not by adding one](../lessons/an-object-is-a-block-instance-with-the-stack-discipline-removed.md)
- [Resolve the pull between a general language and a problem-shaped one by making the general language a substrate for dialects](../lessons/make-the-domain-vocabulary-a-dialect-not-a-library.md)
- [Give every entity its own place in its own text, so a life spread over time still reads as one story](../lessons/give-each-entity-its-own-sequence-control.md)
- [Separate the concurrency in your description from the concurrency in your execution, and make the scheduler an inspectable data structure](../lessons/concurrency-as-description-with-scheduling-as-data.md)
- [When a safety rule is too rigid, put an ordering on the things being checked rather than dropping the check](../lessons/order-the-things-you-check-instead-of-abandoning-the-check.md)
- [Define a composition mechanism by reduction to a construct whose rules you already trust](../lessons/define-inheritance-by-reduction-to-a-construct-you-already-trust.md)
- [A general layer earns its generality by naming what it does not define and by keeping control around what fills the gap](../lessons/the-general-layer-names-what-it-does-not-define-and-keeps-the-control.md)
- [An error whose consequences you cannot explain in the language's own terms has destroyed your ability to reason at all](../lessons/errors-must-be-explainable-inside-the-language.md)
- [Aim to be a middle layer: extend a base you refuse to replace, and become a base others need not replace](../lessons/build-a-middle-layer-language.md)
- [Any operation whose misuse escapes into implementation-dependent behavior destroys reasoning everywhere, not just at the fault](../lessons/a-language-must-be-closed-under-its-own-reasoning.md)
- [Build the vocabulary that forces a complete description, then make the description itself the program](../lessons/make-the-description-the-executable-artifact.md)
- [Give each component its own resumption point, and the state machine you would have hand-encoded disappears](../lessons/give-each-component-its-own-sequence-control.md)
- [Judge a proposed primitive by how many existing built-in features it can dissolve into ordinary definitions](../lessons/a-new-primitive-earns-its-place-by-absorbing-the-old-features.md)
- [Make concurrency a nestable construct, so a subsystem's interleaving is invisible from outside it](../lessons/nest-concurrency-so-interleaving-stays-local.md)
- [Specify a derived construct as a rewriting into constructs whose meaning is already settled](../lessons/define-new-constructs-by-rewriting-into-old-ones.md)
- [State the holes: everything a general design leaves to its specializations should be a short declared list, and nothing else should be reachable](../lessons/declare-the-holes-an-abstraction-leaves.md)
- [To get a new kind of thing, take a construct you trust and delete one of its incidental restrictions](../lessons/objects-are-blocks-freed-from-the-stack.md)
- [When safety and flexibility seem to trade off, the fix is more structure in the type space, not a weaker check](../lessons/give-the-checker-a-hierarchy-instead-of-loosening-it.md)
