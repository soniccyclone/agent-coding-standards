---
type: lesson
title: "Put Only Suspend-And-Resume In The Machine; Keep Scheduling Policy In Libraries"
figure: nygaard
works: [simula-67-common-base-language]
axes: [parallelizability, primitive-count, verifiability]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Put Only Suspend-And-Resume In The Machine; Keep Scheduling Policy In Libraries

**Lesson:** The base language's entire concurrency story is that an instance can step out of the flow of control while keeping a private marker of where it stopped, and that some other instance can hand control back to it so it continues from that marker. There is no clock, no queue, no priority, no notion of simultaneity, and at any moment exactly one component of a given system holds control. Everything a simulation actually needs — a time axis, notices scheduled at future times, ranking among events sharing a timestamp, waiting for an indefinite period, being cancelled — is built in ordinary declarations layered on top of that pair of operations, and the report tells users of the higher layer to stop calling the lower one directly.

The separation earns two things at once. First, the primitive is small enough to reason about: with a single active component and an explicit handoff there is no interleaving the programmer did not write, so control flow remains inspectable in a way that genuine preemption is not. Second, scheduling becomes an ordinary program rather than a fixed feature. Time-ordered discrete-event scheduling is only one policy expressible over suspend-and-resume; a different domain can write a different one without asking the language to change, and both can coexist because the layering mechanism is the same one used for every other extension.

The transferable habit is to keep the mechanism of yielding control strictly apart from the policy that decides who runs next, and to resist the temptation to fuse them because one policy happens to be the first requirement. A programmer who does this ships a scheduler as replaceable code rather than as an unmovable feature of the runtime, and gains the ability to reason about a concurrent program by reading its handoffs. The honest naming matters too: what the report offers is not parallel execution but disciplined interleaving, and refusing to blur that distinction is what keeps the reasoning sound when someone later needs true parallelism and must confront the differences deliberately.

**Source:** [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the sequencing chapter defining detached and attached states with per-component sequence control, contrasted with the later system-class chapter where the event notices, time axis, and scheduling statements are defined as library-level declarations over those primitives.
