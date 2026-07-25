---
type: work
title: "The Functional Abstract Machine"
figure: cardelli
description: Describes the FAM, an abstract machine (a compilation target and evaluator, in the tradition of Landin's SECD machine) designed specifically for efficiently executing ML-family functional languages. It shaped how curried functions, closures, and pattern matching got compiled down to a small instruction set rather than interpreted directly over syntax trees. An early example of Cardelli's recurring move: take an informal implementation technique and give it a precise, checkable machine model.
subdomains: [programming-languages-and-semantics]
year: 1983
url: http://lucacardelli.name/Papers/FAM.pdf
access: public
host: self-archived
tags: [work]
---

# The Functional Abstract Machine

**Venue/year:** AT&T Bell Laboratories Technical Report TR-107, April 1983 (reprinted in Polymorphism, the ML/LCF/Hope Newsletter, Vol. I, No. 1, 1983).
**Source:** http://lucacardelli.name/Papers/FAM.pdf — self-archived on Cardelli's own site (verified 200, application/pdf). Resolves the Phase 1/2 `uncertain` flag.

## Lessons
- [Identify the operation your programs perform constantly, make it cheap, and factor it so common sequences cancel](../lessons/make-the-hot-operation-cheap-and-let-composites-cancel.md)
- [Buy performance with an invariant your own semantics guarantees, and quarantine the exceptions rather than generalizing](../lessons/buy-speed-with-an-invariant-the-semantics-guarantees.md)
- [Minimality is owed by the layer you reason in, speed by the layer you run on, and neither should be asked of the other](../lessons/each-layer-owes-a-different-virtue.md)
- [State the semantics over the mechanism you will actually run, so the theorem covers the thing you ship](../lessons/prove-it-about-the-machine-you-will-actually-run.md)
