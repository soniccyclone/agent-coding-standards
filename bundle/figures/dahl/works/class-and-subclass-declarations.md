---
type: work
title: "Class and Subclass Declarations"
figure: dahl
description: The paper that first presents the class/subclass mechanism as a remodeling of Hoare's record-class idea, using prefixing to organize classes into a hierarchical tree and letting subclass objects carry a prefix part plus a main part. It works through the syntax for class and prefix declarations and shows how the mechanism gives compile-time-checked structuring of data without the rigidity of Hoare's original records. This is the specific paper where the class/subclass vocabulary that the later OO lineage inherits first appears in print.
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
year: 1967
url: https://www.ub.uio.no/fag/informatikk/faglig/dns/dokumenter/classandsubclass1968.pdf
access: public
host: institutional
tags: [work]
---

# Class and Subclass Declarations

**Author(s):** Ole-Johan Dahl, Kristen Nygaard
**Venue/year:** Presented at the IFIP Working Conference on Simulation Programming Languages, Lysebu, Oslo, May 1967. Published in J.N. Buxton (ed.), "Simulation Programming Languages," North-Holland, Amsterdam, 1968, pp. 158-174.
**Source:** https://www.ub.uio.no/fag/informatikk/faglig/dns/dokumenter/classandsubclass1968.pdf — scanned PDF hosted by the University of Oslo Library (Universitetsbiblioteket i Oslo). Verified by fetching and visually confirming the scanned title page matches (curl 200, application/pdf; page 1 reads "SIMULATION PROGRAMMING LANGUAGES - NORTH-HOLLAND (1968) / CLASS AND SUBCLASS DECLARATIONS / OLE-JOHAN DAHL and KRISTEN NYGAARD"). Resolves as of 2026-07-24. Originally flagged `uncertain` in the Phase 1 pass; resolved to public/institutional here.

## Lessons
- [When a safety rule is too rigid, put an ordering on the things being checked rather than dropping the check](../lessons/order-the-things-you-check-instead-of-abandoning-the-check.md)
- [Define a composition mechanism by reduction to a construct whose rules you already trust](../lessons/define-inheritance-by-reduction-to-a-construct-you-already-trust.md)
- [A general layer earns its generality by naming what it does not define and by keeping control around what fills the gap](../lessons/the-general-layer-names-what-it-does-not-define-and-keeps-the-control.md)
- [An error whose consequences you cannot explain in the language's own terms has destroyed your ability to reason at all](../lessons/errors-must-be-explainable-inside-the-language.md)
- [Treat 'undefined' as a decision you have deferred, and know that every plausible default you supply destroys the evidence you would have needed](../lessons/a-plausible-default-for-a-case-you-do-not-understand-deletes-evidence.md)
- [Let the machine's cost model set the grain of your abstractions, and refuse any mechanism whose expense is invisible to whoever uses it](../lessons/let-the-machines-cost-model-set-the-grain-of-your-abstractions.md)
- [Reach a new paradigm by lifting a restriction off an existing primitive, not by adding one](../lessons/an-object-is-a-block-instance-with-the-stack-discipline-removed.md)
- [Resolve the pull between a general language and a problem-shaped one by making the general language a substrate for dialects](../lessons/make-the-domain-vocabulary-a-dialect-not-a-library.md)
- [Aim to be a middle layer: extend a base you refuse to replace, and become a base others need not replace](../lessons/build-a-middle-layer-language.md)
- [Any operation whose misuse escapes into implementation-dependent behavior destroys reasoning everywhere, not just at the fault](../lessons/a-language-must-be-closed-under-its-own-reasoning.md)
- [For every partial operation, decide consciously whether to trap or to default, and know that a default spends your ability to detect the unforeseen](../lessons/choose-between-a-diagnostic-and-a-default-deliberately.md)
- [Judge a proposed primitive by how many existing built-in features it can dissolve into ordinary definitions](../lessons/a-new-primitive-earns-its-place-by-absorbing-the-old-features.md)
- [Refuse expressive power whose cost is invisible at the point where it is used](../lessons/refuse-power-whose-cost-is-invisible.md)
- [Specify a derived construct as a rewriting into constructs whose meaning is already settled](../lessons/define-new-constructs-by-rewriting-into-old-ones.md)
- [State the holes: everything a general design leaves to its specializations should be a short declared list, and nothing else should be reachable](../lessons/declare-the-holes-an-abstraction-leaves.md)
- [To get a new kind of thing, take a construct you trust and delete one of its incidental restrictions](../lessons/objects-are-blocks-freed-from-the-stack.md)
- [When safety and flexibility seem to trade off, the fix is more structure in the type space, not a weaker check](../lessons/give-the-checker-a-hierarchy-instead-of-loosening-it.md)
