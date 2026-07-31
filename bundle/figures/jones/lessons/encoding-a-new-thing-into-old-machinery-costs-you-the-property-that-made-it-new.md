---
type: lesson
title: "Encoding a new kind of thing into machinery you already have costs you exactly the property that made it a new kind of thing"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Encoding a new kind of thing into machinery you already have costs you exactly the property that made it a new kind of thing

**Lesson:** When something genuinely new turns up in a design, there is nearly always a way to avoid admitting it: represent it inside the machinery you already have. A stream of results going out to the world can be held as another piece of mutable state, and then writing to it is just another assignment, and every rule you already wrote for assignments applies unchanged. This is attractive for good reasons — no new notation, no new rules, no new cases in anything downstream — and it is the reflex a preference for small vocabularies trains into you. It is also, often, a mistake, and the reason is specific enough to be a test.

An output stream is not just state that changes; it is state that only ever grows, and each thing put into it is beyond recall. That monotone, append-only character is the whole nature of the thing. Model it as an ordinary assignable component and the model permits what reality does not: the value can shrink, can be replaced wholesale, can be rewritten. Nothing in the encoding is *false* — every real behaviour is representable — but the encoding is strictly looser than the truth, and the surplus freedom it grants is invisible. So the reasoning apparatus can no longer exploit growth, which was the one property that made statements about the stream easy; and it can no longer catch you violating growth, because in the encoded world violating it is legal. You gave up both the leverage and the guardrail in exchange for not adding a construct.

The general test is worth carrying: before folding a new concept into an existing mechanism, name the structural property that distinguishes it — monotone, single-assignment, ordered, unique, once-only, irreversible — and ask whether the host mechanism can still state that property. If it can, the encoding is a genuine simplification and you should take it. If it cannot, you have not simplified anything; you have moved a real constraint out of the notation and into the heads of the people using it, where it will be maintained by discipline and eventually not maintained at all. Adding a construct is a one-time cost paid by the designer. Losing a property is a recurring cost paid by everyone who reasons about the system afterwards.

This also sharpens what a minimal vocabulary is actually for. A small basis is valuable because it makes the foundations arguable, not because every later concept must be expressed in it. The right move when a new kind of thing appears is usually to add the construct, define it against the basis, and derive its rules — keeping the foundation small while letting the working vocabulary say what is true.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 19's parenthetical rejection of the alternative treatment of input/output: the observation that new notation for input/output statements could be avoided by adding components holding the files to the state, so that the statements become like assignment statements over the extended state, together with the stated reason for not recommending it, namely that this fails to model the essential growing property of the output file; read against the chapter's own rules for sequential and iterative composition of output-producing operations, which are framed throughout in terms of extending the output list and appending the lists produced by the parts.
