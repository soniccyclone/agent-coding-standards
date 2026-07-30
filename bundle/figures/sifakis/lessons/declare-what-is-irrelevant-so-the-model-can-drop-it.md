---
type: lesson
title: "Let the author declare what carries no meaning, so abstraction becomes a deletion rather than a guess"
figure: sifakis
works: [cesar-1982]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Let the author declare what carries no meaning, so abstraction becomes a deletion rather than a guess

**Lesson:** Analysis of a concurrent design drowns in data. Most of that data has nothing to do with the question: whether a transmission protocol recovers from loss depends on the control bit attached to a message and not at all on the payload it carries. The usual response is to build machinery that infers which state is irrelevant. The cheaper response is to give the description language a way for the author to say so up front — a type introduced by name whose operations are deliberately left unspecified — and then have the extraction step simply delete variables of those types. Nothing was inferred, so nothing can be inferred wrongly, and the person best placed to know what the argument depends on is the one who said it.

The generalizable idea is to put the abstraction boundary in the source rather than in the tool. A declaration of ignorance is a strong statement: it promises that no property under consideration examines the internals, which means that whatever behavior the system exhibits is independent of them. Once made, the promise is enforced structurally, because there are no operations available to violate it. Compare this to reconstructing the same fact by static analysis after the fact, which is more work, weaker, and silently degrades when the code is written in a way the analysis cannot follow.

The design pressure this creates on a notation is worth noticing. A language whose only types are fully specified forces everything to be modeled in full detail; a language that admits opaque types lets a description carry exactly the detail its intended arguments need, and no more. The same instinct applies far outside verification: whenever you find a tool guessing at what matters in your data, ask what small declaration would let you tell it instead.

**Source:** [Specification and Verification of Concurrent Systems in CESAR](../works/cesar-1982.md) — the description language's non-specified types in section 2.1, the translator's deletion of internal variables of those types in section 2.2, and the conclusion's remark on abstracting from details irrelevant to behavioral verification.
