---
type: lesson
title: "Rate a convenience by what retreating from it would cost, and ship the restrictive version first"
figure: hoare
works: [communicating-sequential-processes-paper]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Rate a convenience by what retreating from it would cost, and ship the restrictive version first

**Lesson:** Some features are pure sugar and some only look like it. The test that separates them is not how much typing they save but what happens when you have to withdraw them: write out the program you would need if the feature did not exist, and see how far the edit reaches. If the fallback is a local rewrite inside one component, the feature was sugar and you can adopt it cheaply. If the fallback obliges every participant to exchange extra messages, honor an extra protocol, or agree on a new shutdown handshake, then the feature was never sugar — it was silently supplying part of the interface contract between components, and removing it is a redesign. The dangerous case is precisely the attractive one: an implicit rule that makes the common arrangement work with no code at all, where the explicit equivalent is merely inconvenient rather than impossible, so nobody notices the feature is load-bearing until it has to go.

There is a second cost, subtler and worse. A convenience that handles a hard question automatically removes the occasion on which a designer would have thought about that question. Automatic handling of orderly shutdown means nobody plans shutdown; when the automatic behavior turns out not to fit some particular system, the plan that should have existed from the start has to be invented late, against interfaces already frozen around its absence. So a convenience should be suspected in proportion to the importance of the decision it is making on your behalf. Saving keystrokes is fine. Answering a design question you never asked is a debt whose size you learn only when it comes due.

The practical discipline for a designer proposing something new follows from this asymmetry: publish the restrictive version. Restrictions can be relaxed later without invalidating any existing program, whereas a facility that turns out to be a mistake cannot be withdrawn from the programs that have already leaned on it. And be especially strict when the claim is that the new thing is *primitive*, since anything reconstructible from the rest of the language is by definition not primitive and its presence is an argument about convenience masquerading as an argument about foundations. Keeping those two claims apart is what lets you evaluate each on its own evidence.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-paper.md) — the closing restriction discussion, which flags automatic termination of a repetitive command when its input sources have all terminated as powerful, convenient, demonstrably non-primitive, and hazardous: the explicit alternative requires end-signal exchange, so if the automatic behavior proves unsatisfactory the reprogramming reaches the interfaces between processes, and the feature tempts programmers to omit termination planning in the first place. Also the stated preference for specifying a highly restrictive version of an unfamiliar feature rather than proposing extensions.
