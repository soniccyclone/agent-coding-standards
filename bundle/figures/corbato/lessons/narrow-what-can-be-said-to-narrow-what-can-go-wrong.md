---
type: lesson
title: "Narrow What Can Be Said to Narrow What Can Go Wrong"
figure: corbato
works: [on-building-systems-that-will-fail, multics-the-first-seven-years, introduction-and-overview-of-the-multics-system]
axes: [primitive-count, expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Narrow What Can Be Said to Narrow What Can Go Wrong

**Lesson:** Having spent most of his Turing lecture arguing that mistakes in ambitious systems are unavoidable, Corbató owes his audience something to do about it, and the short list he offers is mostly about restricting expression rather than adding checks. The load-bearing item is that a notation which refuses to let you state irrelevant things shrinks the space of errors you are capable of committing. That is a different move from testing or proving. Testing samples the error space and proof searches it; a constrained language deletes regions of it before anyone writes a line. His measure of elegance points the same direction — capability obtained per unit of machinery spent, with clarity as the gate rather than an afterthought — and so does his defence of metaphor, which he treats as a way of buying agreement about behavior in advance so that fewer things have to be said, learned, or coordinated at all.

The Multics record puts a useful dent in the naive version of this. The 1965 paper commits the system to PL/I; the retrospective reports that the language contained constructs complicated enough that programmers had to learn to steer around them, and that nobody yet knew how to compile it well. Yet the eventual verdict was that moving from an early subset compiler to one handling nearly the whole language improved performance in almost every module converted, and that a language does not have to be cut down to a simple subset to be usable for building a system — provided it is genuinely understood. They even specified a smaller, easily compilable systems language and then never implemented it, because the need evaporated. So the constraint does not have to live in the grammar. It can live in the grammar, or in a compiler that rejects things, or in a discipline the team has actually internalized about which constructs are off the table. What it cannot do is live nowhere.

The two halves resolve into a single test. For any capability a notation offers, ask what class of mistakes it admits and whether anything else in your setup is going to catch them. Where nothing will, the expressive power is a liability you are paying for in defect probability, and the right response is to remove the ability rather than to promise vigilance. Vigilance is the mechanism that fails first, as the CTSS password episode in the same lecture demonstrates — the system programmers there sincerely undertook to be careful, and were.

A programmer who thinks this way values a facility partly by what it forbids, prefers the dialect or subset that cannot express the thing they must not do, and reads "we all know not to do that" as an unenforced invariant rather than a safeguard. The same instinct explains why Corbató wanted one calling sequence rather than several and no separate vocabulary for supervisor code: every alternative way of saying something is another way of saying it wrong.

**Source:** [On Building Systems That Will Fail](../works/on-building-systems-that-will-fail.md) — the closing set of recommendations, particularly the items on simplicity and elegance, on metaphor, and on constrained languages for design and synthesis. The countervailing evidence is the system-programming-language discussion under insights in [Multics: The First Seven Years](../works/multics-the-first-seven-years.md), and the language choice argued for in the 1965 kickoff paper.
