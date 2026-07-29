---
type: lesson
title: "Make the expected cost part of the request"
figure: strachey
works: [time-sharing-in-large-fast-computers]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Make the expected cost part of the request

**Lesson:** Some failures are undetectable from the inside. A computation stuck in a cycle that produces nothing is, moment by moment, doing exactly what a healthy computation does — consuming the machine and making progress by its own lights. No local test distinguishes the two, so a shared system that watches only for illegal actions will happily let a broken job absorb everything while never once misbehaving. The failure has no signature of its own; it only shows up as a discrepancy against an expectation, and if nobody wrote the expectation down there is nothing for reality to disagree with.

So require the expectation as part of the submission. Whoever asks for work to be done states what it should cost, and the supervising layer treats a large overshoot as a fault of the same kind as an illegal reference — not a warning, not a log line, but grounds for eviction. This turns an unobservable liveness property into an ordinary observable one, and it does so without any analysis of the program's structure. The declaration also has to be mandatory, with a default supplied when it is omitted, because an optional budget is a budget nobody sets. The one detail worth copying is the tolerance factor: judgement against a stated estimate needs slack, since the point is to catch divergence, not to punish imprecision.

The wider principle is that a system should ask its clients for the small pieces of intent that make misbehaviour visible, rather than trying to infer intent from behaviour after the fact. Timeouts on requests, expected row counts, declared memory ceilings, asserted invariants at boundaries — all are the same move, and all fail in the same way when treated as advisory. A programmer who has absorbed this stops asking "how would I detect that this hung?" and starts asking "what would the caller have had to tell me for hanging to be detectable at all?"

**Source:** [Time Sharing in Large Fast Computers](../works/time-sharing-in-large-fast-computers.md) — the treatment of loop stops in the description of how programs are checked and removed, where a required running-time estimate becomes the basis for the supervising program declaring an error.
