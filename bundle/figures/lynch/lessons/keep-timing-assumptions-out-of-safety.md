---
type: lesson
title: "Let timing assumptions buy you progress and nothing else, so safety never depends on the clock"
figure: lynch
works: [consensus-in-the-presence-of-partial-synchrony]
axes: [verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Let timing assumptions buy you progress and nothing else, so safety never depends on the clock

Correctness for a fault-tolerant protocol splits cleanly in two. There are the obligations that must never be broken at any instant — no two participants settling on different answers, nobody settling on an answer that was never legitimately available — and there is the obligation to eventually finish. The discipline worth extracting is that timing assumptions may be spent only on the second kind. Whatever you assume about message delay or relative process speed should determine *when* the system makes progress and never *whether* what it did was right. A protocol built this way is unconditionally safe: hand it an arbitrarily hostile network and it stalls rather than corrupts.

There is an argument for why this split is not merely tidy but forced. Suppose you state your assumption in the weak, realistic form that the timing bound holds from some unknown point onward. Any protocol correct under that assumption is automatically safe even against a network that never settles down at all — because a safety violation is by definition observable at a finite moment, and any finite prefix ending in a violation can be extended into a run where timing does eventually stabilize, which would contradict the protocol's correctness in the assumed model. So the eventual-stabilization assumption and the safety-always / termination-when-timely formulation are the same requirement wearing different clothes. Designing against eventual synchrony gets you unconditional safety whether you asked for it or not, and conversely any protocol whose safety leans on a timing bound was never correct in the model you thought you were in.

For someone building systems this reverses the usual instinct about timeouts. A timeout is not a mechanism for deciding what is true; it is a mechanism for deciding to try something else. Once you accept that, the design questions get concrete: which state must survive an arbitrarily long stall without becoming wrong, and which state exists purely to trigger retries and can be discarded freely? The protocols in this work make the distinction structural — a value once locked by enough participants stays locked regardless of how long the network misbehaves, and the timing assumption enters only in the claim that eventually some coordinator's turn comes around during a calm stretch and finishes the job. Systems that instead let a fired timeout mutate authoritative state have made the clock part of their trusted computing base, which is where most of the ugliest distributed bugs live.

**Source:** [Consensus in the Presence of Partial Synchrony](../works/consensus-in-the-presence-of-partial-synchrony.md) — the reasoning appears in the introduction's discussion of whether to state the model as a global-stabilization-time assumption or as separated safety and termination requirements, and is then embodied in the lock/lock-release structure of the basic-round protocols, whose consistency proofs never invoke a timing bound.
