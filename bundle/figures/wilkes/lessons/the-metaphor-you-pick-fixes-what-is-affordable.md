---
type: lesson
title: "The metaphor you adopt for a primitive fixes which operations are cheap and which become impossible"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# The metaphor you adopt for a primitive fixes which operations are cheap and which become impossible

**Lesson:** When you decide what a primitive fundamentally *is*, you are also deciding, usually without noticing, which operations on it will be trivial and which will be unaffordable. Treat a grant of authority as an unforgeable ticket that never loses validity, and you get free copying, free storage, and free delegation — and you have made withdrawal impossible, because a ticket is valid by inspection and there is no register of who holds one. Recovering withdrawal then demands either a central record of every holder, whose upkeep is prohibitive, or permanently unique identifiers so that a discarded grant can never accidentally match a later thing, which loads cost onto every ordinary operation. Neither is an implementation difficulty to be engineered around; both are the price of the metaphor.

The instruction that follows is to examine the metaphor before blaming the mechanism. When a needed operation turns out to be extraordinarily expensive, ask what conception of the object makes it expensive and whether a different conception would make it natural while keeping what you actually depend on. An operation that is hard under every implementation of a design is usually hard because of a decision taken at the level of what the thing means, and no amount of cleverness below that level will fix it.

The other move available is to weaken the requirement along a dimension you had not considered. Withdrawal is expensive; expiry may not be. A grant that cannot be recalled but also cannot be stored — so that it lapses when the session in which it was issued ends, and must be requested afresh each time — gives the grantor a decision point at every renewal without any central bookkeeping. The holder cannot be stripped of what they have, and the grantor is not bound forever. Most demands for revocation are really demands for the ability to reconsider, and reconsideration on a schedule is dramatically cheaper than recall on demand.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's discussion of revocation, which traces the absence of any means of withdrawal to the view that a capability is an unforgeable ticket that does not lose validity, prices the alternatives of a central record and of never-reused unique identifiers as prohibitive, and proposes instead capabilities usable during a session but not preservable, so that a request must be made afresh at each login and the grantor may reconsider the conditions each time.
