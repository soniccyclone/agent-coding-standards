---
type: lesson
title: "Model unreliability as an extra branch plus a promise, not as a probability"
figure: manna
works: [temporal-verification-of-reactive-systems-progress]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Model unreliability as an extra branch plus a promise, not as a probability

**Lesson:** Faced with a channel that drops or garbles messages, Manna and Pnueli decline both of the obvious approaches. They do not attach a probability to it, and they do not redefine what a send operation means. Instead they rewrite the program: where it used to send, it now chooses nondeterministically between sending correctly, doing nothing at all, and sending a corrupted value. The primitive keeps its original semantics, the reasoning apparatus is untouched, and the fault is expressed in the same language as everything else — one more branch a scheduler may take. Faults become program structure rather than a special theory.

Applying a fairness assumption to the good branch is what makes the model usable, and it is the substantive move. If the correct-send branch is one that must eventually be taken when repeatedly available, the channel is not reliable but it is eventually reliable: it may lose any particular message and may lose arbitrarily many, but it cannot lose all of them from some point onward. That is exactly the qualitative residue of a quantitative claim. Manna and Pnueli make the translation explicit, replacing an assumption that a message arrives nine times out of ten with the assumption that a message submitted infinitely often eventually arrives. The probability is discarded and the correctness argument survives, because a retransmission protocol's correctness never depended on the rate — it depended only on not being starved forever. You give up throughput and latency conclusions, which the qualitative model was never going to give you anyway, and in exchange the whole apparatus for reasoning about progress applies unchanged.

They are honest about the price, and the honesty is instructive. Making the faulty branch subject to the same fairness treatment means the model also insists that faults keep happening — the corrupted send is not merely permitted but eventually required. The abstraction is not a neutral relaxation; it constrains the fault behavior in both directions, and knowing which direction you have over-constrained is part of knowing what your proof means. Their alternating-bit-protocol analysis then lands in exactly the shape you would hope: the protocol cycles through retry states, and the argument that it makes progress is precisely that each pass through the cycle re-enables the good branch, so fairness eventually fires it.

A programmer who reasons this way models a flaky dependency as a branch in the state machine plus a named promise about what cannot be withheld forever — timeouts, partial writes, dropped packets, transient failures, a cache that may or may not have the entry. They write the promise down as an assumption rather than a probability, because the promise is what their retry logic actually needs to be correct, and because a promise can be checked against the dependency's contract while a made-up probability cannot.

**Source:** [Temporal Verification of Reactive Systems: Progress](../works/temporal-verification-of-reactive-systems-progress.md) — the Response Under Fairness chapter's sections on modeling faulty channels: the substitution of probabilistic characterization by a strong-fairness assumption, the program transformations introducing loss and corruption branches, the argument that strong fairness on the good branch yields eventual reliability, the remark that this modeling also forces faults to recur, and the alternating-bit-protocol progress argument built on retry cycles.
