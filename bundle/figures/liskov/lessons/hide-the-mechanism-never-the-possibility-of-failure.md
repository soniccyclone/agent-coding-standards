---
type: lesson
title: "Hide the mechanism and the location; never hide the possibility of failure or the cost"
figure: liskov
works: [guardians-and-actions]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# Hide the mechanism and the location; never hide the possibility of failure or the cost

**Lesson:** Designing an abstraction over a network is mostly a series of decisions about what to conceal, and the decisions divide cleanly if you ask who is better positioned to handle each fact. Fragmenting data into packets, retrying transmission, tracking duplicates, deciding how long to wait before declaring the network hopeless — the caller has no basis for any of these judgments, and would make them badly. Conceal them. Whether the operation succeeded at all, and how much it costs relative to a local one — the caller absolutely has a basis for handling these, and often the only basis, because the right recovery depends on what the application is for. Do not conceal them.

The failure half is the one people get wrong, in both directions. Exposing raw failure with unclear consequences is useless: a caller told only that something went wrong must assume the operation may have half-happened, and coping with that is brutal. Concealing failure entirely is worse, because the abstraction then either blocks forever or lies. The productive middle is to expose the failure while sharply constraining what it can mean: guarantee that the operation either took effect completely or not at all, and report which. Now the caller's recovery is short — try elsewhere, take a different path, give up cleanly — because a failure carries no residue to clean up.

The cost half is quieter but shapes whole programs. If a remote interaction is made to look exactly like a local one, programmers will write code whose performance is unpredictable from reading it. Making the boundary visible in what may cross it — data by value, never a live reference into someone else's state — has two effects at once: it keeps each module in actual control of its own state, since nobody outside can touch it directly, and it gives the programmer a reliable intuition about which operations are cheap. Note that this is compatible with hiding location entirely: where a peer runs can stay unknown and even change, because location is exactly the kind of fact the caller cannot use.

A programmer who believes this sorts every detail an interface could expose into "the caller can act on this" and "the caller can only be confused by this," and hides only the second. When tempted to make a remote thing indistinguishable from a local one, they stop: the useful goal is to make the remote thing easy to use, not to make it a convincing forgery.

**Source:** [Guardians and Actions: Linguistic Support for Robust, Distributed Programs](../works/guardians-and-actions.md) — the remote-procedure-call section, which argues for masking packetization and retransmission while refusing to mask ultimate communication failure and for the system rather than the programmer choosing timeouts, together with the rule that arguments cross module boundaries by value.
