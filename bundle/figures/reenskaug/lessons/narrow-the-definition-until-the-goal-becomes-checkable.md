---
type: lesson
title: "Narrow a word deliberately until the goal stated with it becomes checkable"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Narrow a word deliberately until the goal stated with it becomes checkable

**Lesson:** The stated objective was to specify a large class of systems without programming, motivated bluntly: writing programs is expensive, slow, and error-prone. The obvious objection arrives immediately, and the author raises it against himself. Programming can reasonably be defined as the specification of a computation — under which definition setting parameters on general components, driving generation from a table, and using a domain-specific visual tool are all programming, and the goal is either vacuous or false. Rather than argue the philosophy, he restricts the word by fiat: here *programming* means writing in a programming language, and nothing else.

The move is worth studying because it looks like evasion and is the opposite. Under the broad definition the objective cannot be assessed at all — every act of specifying anything qualifies, so no design could ever satisfy it and no design could ever fail it. Under the narrow definition the objective becomes a question about the world with a checkable answer: at which layers does someone open a text editor and write code in a general-purpose language? Their answer was two of six, and that claim can be inspected, disputed, and falsified. A goal you cannot fail is not a goal, and the usual fix — arguing for a truer definition — is the wrong one, because the broad definition is not incorrect; it is merely useless for deciding anything.

The condition that keeps this honest is that the narrowing is declared, in a labelled aside, alongside the broader sense it rejects. That is the difference between defining a term and equivocating with one. A stipulated definition stated openly lets a reader recompute your claims under their own definition and see exactly where they would differ. A narrowing left implicit produces the familiar bad argument in which "no code" turns out to mean "code in a place I have decided not to count."

The reflex generalizes to any objective built on a contested word — serverless, no-ops, zero-config, typed, declarative, automated. Before evaluating the claim, find the definition the claimant is using and ask whether the claim is falsifiable under it. If it is not, the useful contribution is not to reject the goal but to propose the narrowing that makes it measurable, and then to see whether the goal is still worth having once it means something specific.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 12 section 12.1, which observes that specifying a computation is traditionally considered programming but that programming is notoriously expensive, time consuming and error prone, so they actively search for ways to specify services that avoid it; and the boxed aside "What is programming?", which concedes that under the definition "specification of a computation" parameterization, table-driven generation and application-specific visual tools would all count, and then restricts the term to mean specifying a program in a programming language such as Eiffel, C++ or Smalltalk — against which the claim that only two of the six layers involve programming can actually be checked.
