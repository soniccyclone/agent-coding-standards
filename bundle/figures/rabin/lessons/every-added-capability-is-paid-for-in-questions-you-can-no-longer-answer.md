---
type: lesson
title: "Every capability you add is paid for in questions you can no longer answer"
figure: rabin
works: [finite-automata-and-their-decision-problems]
axes: [expressiveness, verifiability]
subdomains: [foundations-of-computation, formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Every capability you add is paid for in questions you can no longer answer

**Lesson:** The second half of this work is an experiment in extending a formalism one notch at a time and watching what breaks. Give the device a second input to read, alternating between them, and the basic questions about a single input survive — you can still decide whether it ever succeeds, whether it succeeds on infinitely many inputs. But the pleasant algebra is gone: the describable relations are closed under negation and not under conjunction, so you can no longer combine two specifications by requiring both. Push one notch further, letting the two-input device also move backward, and even the most elementary question — does this ever succeed at all? — becomes unanswerable by any procedure, because deciding it would decide a problem already known to be undecidable.

The ordering of these losses is the instructive part. Closure under composition goes first, before decidability does. That means the earliest symptom of an over-powerful formalism is not that verification becomes impossible but that specifications stop composing: you can express each requirement individually and cannot express their conjunction as an artifact of the same kind. Anyone who has watched a configuration language, a query dialect, or a policy engine grow features has seen this exact failure, usually without recognizing it as a boundary being crossed.

So the discipline is to treat each proposed extension as a purchase with a price tag denominated in lost questions. Before adding a capability, name the properties you currently rely on being able to establish — can I tell whether this rule ever fires, whether two rule sets agree, whether the combination of two policies is itself a policy — and check which of them the extension invalidates. An extension that preserves all of them is free. One that costs you compositionality is expensive and should be pushed to the edge of the system rather than into its core vocabulary. One that costs you decidability of the basic questions has converted your artifact from something analyzable into something you can only run and observe, and that conversion is irreversible for everything built on top.

Notice also how the impossibility is established: by encoding a known-hard combinatorial problem into the formalism. The general move is to look for a way to smuggle an already-understood hard problem into your system. If you can, you have learned the boundary of your own analysis tools, and further effort at building a checker is wasted.

**Source:** [Finite Automata and Their Decision Problems](../works/finite-automata-and-their-decision-problems.md) — the multi-input chapters: the loss of closure under intersection and union for two-input devices, the reduction from Post's correspondence problem showing the joint-acceptance question unsolvable, and the final result that even the emptiness question fails for two-input devices allowed to move both directions.
