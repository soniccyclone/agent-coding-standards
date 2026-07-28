---
type: lesson
title: "A total model answers questions the original left open and attaches checks that may never run; audit both its inventions and its idle guarantees"
figure: landin
works: [correspondence-algol-60-church-lambda-notation-part-i]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# A total model answers questions the original left open and attaches checks that may never run; audit both its inventions and its idle guarantees

**Lesson:** A formal model of an existing system drifts away from it in two opposite directions at once, and both drifts are invisible unless you go looking. It over-decides: because a mechanical account has to be total, it produces an answer in every situation, including the situations the original deliberately or accidentally declined to specify. Give every declared name a starting value and you have just decided what reading an uninitialised variable means — a question the thing you were modelling left open on purpose. Your model is now more generous than the system it describes, and programs that were meaningless have become meaningful by accident, courtesy of a convenience you chose for uniformity.

It also under-enforces. A distinction the source document asserts but your mechanism does not represent is not enforced at all, however firmly the prose insists on it; if nothing in the machinery separates the immutable from the mutable, then nothing stops the immutable being overwritten. Worse, a check expressed as a condition on the value something produces is only as strong as the guarantee that it produces one. Attach validation to results and every path that yields no result — the routine never called, the one that escapes through a jump before returning — slips past unexamined. The model looks like it is checking; it is checking conditionally on control flow it does not control.

The habit worth taking is to treat a finished model as a thing to be interrogated about its edges rather than merely tested on its centre. For each place where you made the model total, ask whether the original was silent there, and record the imputation instead of enjoying the tidiness. For each guarantee, ask what has to happen for it to be evaluated at all, and treat a guarantee that can be skipped as absent rather than present. Both audits are cheap and both catch a class of error that ordinary example-based checking never will, because on every example you would think to write the model and the system agree exactly.

**Source:** [A Correspondence Between ALGOL 60 and Church's Lambda-Notation: Part I](../works/correspondence-algol-60-church-lambda-notation-part-i.md) — the treatment of declarations, where Landin notes his uniform initialisation confers meaning on programs the source report leaves undefined, together with the discussion of type transfer, where he calls the model over-tolerant because a mismatch modifies the offending object rather than rejecting it, so the rejection never occurs unless a result is actually produced.
