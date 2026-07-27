---
type: work
title: "Temporal Verification of Reactive Systems: Progress"
figure: manna
description: Draft chapters for what was meant to be the third volume of the Specification (1991) / Safety (1995) book series, covering proof rules for progress and response properties - liveness obligations that must hold under fairness assumptions - for both simple and parameterized reactive programs. The volume was never commercially published, so Manna self-archived the three finished chapters (Response, Response for Parameterized Programs, Response under Fairness) as a standalone draft. Written with Pnueli.
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
year: 1996
url: http://theory.stanford.edu/~zm/apch1.ps
access: public
host: self-archived
tags: [work]
---

# Temporal Verification of Reactive Systems: Progress

**Author(s):** Zohar Manna, Amir Pnueli
**Venue/year:** Unpublished draft, 1996 (intended as the third volume following Specification, 1991, and Safety, 1995).
**Source:** http://theory.stanford.edu/~zm/tvors3.html — self-archived draft-book landing page on Manna's own Stanford CS Theory homepage (theory.stanford.edu/~zm), linking three chapter PDFs/PostScripts, all HTTP 200 verified: Ch.1 Response (http://theory.stanford.edu/~zm/apch1.ps), Ch.2 Response for Parameterized Programs (http://theory.stanford.edu/~zm/apch2.ps), Ch.3 Response under Fairness (http://theory.stanford.edu/~zm/apch3.ps).

## Lessons
- [Reason about a component against an environment allowed to do anything except touch what the component owns](../lessons/reason-against-an-environment-that-may-do-anything-you-do-not-own.md)
- [A progress argument has to track who is responsible, not only how far away the goal is](../lessons/progress-arguments-must-track-who-is-responsible.md)
- [For an unbounded ensemble, the measure is a shrinking set of participants, and it shrinks via the one nobody can block](../lessons/measure-an-unbounded-ensemble-by-a-shrinking-set.md)
- [Somebody progresses and everybody progresses are different guarantees, and which one you can have is decided by your primitive](../lessons/somebody-progresses-and-everybody-progresses-are-different-guarantees.md)
- [A fairness assumption is a debt someone has to implement, not a fact about the world](../lessons/a-fairness-assumption-is-a-debt-someone-must-implement.md)
- [Model unreliability as an extra branch plus a promise, not as a probability](../lessons/model-unreliability-as-a-branch-plus-a-promise.md)
- [Define the shape of a counterexample first; the proof and the checking algorithm are both readings of it](../lessons/the-counterexample-is-the-object-the-proof-is-its-shadow.md)
- also cited by [A rule that appeals to itself is sound exactly when something strictly shrinks](../lessons/circularity-is-legitimate-when-something-strictly-shrinks.md) and [The language your auxiliary constructs are written in caps what you can prove](../lessons/the-annotation-language-is-the-real-ceiling.md)
