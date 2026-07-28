---
type: lesson
title: "A freshly created private name buys atomicity and isolation without a new primitive"
figure: milner
works: [a-calculus-of-mobile-processes]
axes: [expressiveness, primitive-count, parallelizability]
subdomains: [distributed-systems-and-concurrency]
tags: [lesson]
---
# A freshly created private name buys atomicity and isolation without a new primitive

**Lesson:** Suppose a sender must deliver two related items to exactly one of several willing receivers. Sending them one after another over a shared channel fails, and fails in the worst way: one receiver takes the first item, another takes the second, and no participant sees anything locally wrong. The instinctive remedy is a new primitive — a compound message form, a transaction, a lock over the channel. The remedy used here needs nothing new. The sender creates a name nobody else has, sends that one name, and spawns a small helper that will deliver the two items over it. Whoever received the name is now the only party who can reach the helper, so the pair arrives whole, at one recipient, and interleaving with competitors is impossible.

The mechanism doing the work is uniqueness, not synchronization. A name that has never existed before cannot be guessed or held by anyone else, so possessing it is by itself an exclusive right; the atomic step is the single act of handing that right over, and everything sequenced behind it inherits the exclusivity. Nothing had to be locked because nothing else could contend. This is why the trick composes rather than degrading: the items delivered over the private name may themselves be delivered by the same device, so arbitrarily deep structures transfer as one indivisible grant, and a component that repeatedly announces itself to several parties can hand each a separately-named conversation so that no two parties read fragments of the same announcement.

The same device is then reused as the answer to a different question — how to represent structured data at all when messages carry only single names. A compound value becomes a process reachable by a private name that dispenses its parts on request, so exploring a structure and following a chain of exclusive conversations are the same activity. One idea, deployed for atomicity, isolation, and data representation.

The engineering translation is direct: a fresh unguessable identifier, a per-request channel, a session established for one exchange and then discarded. Reach for one of those before reaching for a lock or a transaction, and ask whether the exclusivity you need is already available as a consequence of newness. Many problems phrased as mutual exclusion are really problems of having addressed a shared endpoint when a private one would have done.

**Source:** [A Calculus of Mobile Processes, I and II](../works/a-calculus-of-mobile-processes.md) — Part I's example where a pair of names cannot be delivered safely over a shared port and the private-name construction that repairs it, then reused to encode list structures as processes and to keep separate parents from reading fragments of the same message in the combinator-graph model.
