---
type: lesson
title: "Treat a specification as an object to be tested, and test it before any program exists"
figure: parnas
works: [a-technique-for-software-module-specification-with-examples]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Treat a specification as an object to be tested, and test it before any program exists

**Lesson:** The unexamined assumption behind most process is that specifications are the safe part of a project and code is the risky part. That is backwards in a specific way: a specification precise enough to be worth writing is about as demanding of exactness as a program and can be comparably intricate, so it is about as likely to be wrong. What it lacks is the one thing that makes program errors surface — it cannot be executed. So the same defect density arrives with none of the feedback, and the natural response is to postpone judgment until there is running code to try, at which point the specification's errors are being paid for at implementation prices.

The way out is to notice that a sufficiently formal description is a set of axioms, and that a set of axioms supports derivation. You can then interrogate it the way you would interrogate any theory: does it ever apply an operation outside the range where that operation is defined; is this predicate true exactly when that value exists; can this quantity ever exceed its stated bound; is there any call sequence at all that reaches this state; is this failure path reachable; can two distinct inputs collide in a way that was supposed to be impossible. Every one of those is answerable from the description alone, and every "no" you were expecting and do not get is a design defect found before anyone wrote a line. This is also why the description must be formal enough to be mechanically checkable in principle — not because you will necessarily automate it, but because a description you could not automate is one you cannot derive from, which means it cannot be wrong in any detectable way, which means it is not really saying anything. Prose descriptions fail this test, though prose remains indispensable for conveying what the formalism is meant to mean.

The subtle point is that this makes correctness a chosen notion rather than a given one. There is no universal list of theorems; you pick the questions, and the questions you pick are what "correct" means for this component. Choosing them well is design work requiring knowledge of what the thing is for, and a specification signed off without anyone having chosen them has not been reviewed in any meaningful sense. The same derivation habit answers a second class of question that has nothing to do with correctness: given the description, which components would have to be touched if a particular restriction were lifted later? That is change-impact analysis performed on documents, before the cost of being wrong has been incurred.

A programmer who takes this on stops treating "the spec is done" as a milestone and starts treating it as a hypothesis with an outstanding test suite. Tooling that answers questions over specifications is welcome but not the point; the habit of asking is the point.

**Source:** [A Technique for Software Module Specification with Examples](../works/a-technique-for-software-module-specification-with-examples.md) — the goal requiring formality sufficient for conceivable machine checking, and the "Using the Specifications" section with its list of sample theorems and its argument against deferring specification testing until programs can be run.
