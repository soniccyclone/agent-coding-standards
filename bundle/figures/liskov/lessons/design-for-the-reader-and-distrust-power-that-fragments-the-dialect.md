---
type: lesson
title: "Design for the reader, and distrust expressive power that fragments the dialect"
figure: liskov
works: [the-power-of-abstraction]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Design for the reader, and distrust expressive power that fragments the dialect

**Lesson:** A body of code is written once and read continuously — by its author days later, by everyone who has to change it, by whoever inherits it years on. That asymmetry should dominate design decisions about notation and structure, and historically it has not: the reflex has been to make writing convenient, which is optimizing the single cheapest event in a program's life at the expense of the most frequent one. Every convenience that shortens the writing while lengthening the understanding is a bad trade made confidently, because the cost lands on someone who is not in the room.

This is why letting each author invent notation deserves suspicion even though it is undeniably powerful. The moment notation is local, code stops being in a common dialect, and a reader arriving at unfamiliar code must first learn a private language before they can evaluate anything. Scoping the invention helps in principle and does not resolve it in practice, because the reader's problem is not finding where the notation was defined, it is that the text no longer means what a competent reader expects it to mean. The defensible cases are the ones where a genuine community of practitioners shares a domain deeply enough that the specialized notation is common knowledge among all its readers — a real dialect with real speakers, not one author's shorthand.

The underlying criterion is older and broader than notation: whatever appears in the text should let a reader reconstruct what happens when it runs, without tracing paths that the text does not show. That standard is what condemned unconstrained jumps, and the same standard should be applied to every newer mechanism that separates what the text says from what executes — deep chains of inherited behavior, machinery that injects behavior into code that does not mention it. A mechanism that makes the text a poor guide to the execution has taken something valuable in exchange for whatever it gives, and the exchange is rarely priced.

A programmer who believes this evaluates a proposed construct by imagining an unfamiliar reader in front of the resulting code, not an author typing it. They resist private notation absent a real shared audience, and they treat "you can find the definition" as a weak answer to "the code no longer reads as what it does." The habit worth keeping: before adopting a mechanism, ask what a competent reader must know that is not visible in the text, and count that as its price.

**Source:** [The Power of Abstraction](../works/the-power-of-abstraction.md) — the discussion of extensible languages and the era's focus on ease of writing, the stated position that readability matters more than writability, the exchange defending scoped syntactic extension, and the recurring appeal to the code-reading argument against mechanisms whose text poorly predicts execution.
