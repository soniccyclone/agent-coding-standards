---
type: lesson
title: "Carry provenance in the value, because an error of interpretation produces results outside your model entirely"
figure: hoare
works: [notes-on-data-structuring]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Carry provenance in the value, because an error of interpretation produces results outside your model entirely

**Lesson:** When one slot can hold things of several different kinds, there are two ways to know which kind is in it: the value can say so, or the surrounding code can be relied upon to remember. The second is cheaper by a few bits and is the common practice, and it is a bad trade for a reason that has nothing to do with the bits. If the value carries no mark of its origin, a mistaken belief about what it holds cannot be caught by anything — not by the compiler, which sees only a slot, and not at runtime, which has nothing to compare against. The mistake is then resolved by whatever the bit pattern happens to mean under the wrong reading, and the consequences are unpredictable *in the terms the programmer was working in*. That is the real damage: not a wrong answer, but an answer produced outside the abstraction entirely, so every piece of reasoning conducted at the abstract level stops applying to the running system.

Marking origin also forces you to be honest about identity. If a value drawn from one source and a value drawn from another are indistinguishable once inside the combined type, then the combined type is a plain set union, and set union loses information wherever the sources overlap. Keeping them distinct means that two values with identical payloads but different origins are not equal, and that a source contributing the same shape twice still yields two separable cases. This is often exactly what the domain wants — two decks with identical cards, two channels carrying the same message format, two subsystems reporting the same numeric code — and it is invariably what the *code* wants, because provenance is what determines which operations are legitimate. Equality has to take the mark into account for any of this to hold.

Treat the mark, then, as part of the value's meaning rather than as bookkeeping overhead to be optimized away. Space pressure is a real argument and there are honest answers to it — pack the mark into a few bits, fold it into the encoding arithmetically, drop the padding when the value sits inside a larger structure. Those keep the discrimination and pay less for it. Omitting the mark is a different thing: it does not make the distinction cheap, it moves the distinction into the heads of everyone who touches the data and removes the only mechanism that could ever detect their being wrong. Reserve that for the exceptional case, and know that you have left the checkable world when you do it.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the chapter on discriminated unions: the insistence that a union's values be wholly distinct from those of its constituent types and that origin remain recoverable even when the same type appears twice (the two-pack patience example), together with the representation section's remarks on packed, minimal and padding-free encodings of the tag and its closing judgement on the then-common practice of omitting the tag and relying on the programmer's knowledge of what a value ought to be.
