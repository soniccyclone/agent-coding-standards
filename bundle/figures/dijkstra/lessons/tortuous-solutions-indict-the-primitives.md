---
type: lesson
title: "When a simple requirement needs an intricate solution, the fault is in your primitives, so change them"
figure: dijkstra
works: [cooperating-sequential-processes]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# When a simple requirement needs an intricate solution, the fault is in your primitives, so change them

**Lesson:** Mutual exclusion over bare shared variables is achievable, and the achievement is a mystification: pages of subtle spinning code whose relation to the one-line requirement it implements is opaque, burning resources to wait busily when sleeping is what the situation calls for. The correct reading of that mismatch is diagnostic. When a conceptually trivial requirement demands heroic implementation, the primitive vocabulary is wrong for the problem, and the productive move is not to polish the heroic solution but to identify the missing capability and introduce it as a new primitive. Here the root deficiency is precise: reading a shared variable leaves no trace, so another process can invalidate what you learned before you act on it; the world may change between look and leap. An operation that atomically combines the test with the consequence (and lets a process be dormant until the condition it awaits is made true by another's signal) dissolves the entire tangle, and the notorious problem becomes a one-liner.

The judgment call is what to canonize. A primitive earns its place by what it makes expressible and cheap, not by irreducibility: even when a richer operation is demonstrably encodable in a poorer one, the encoding's clumsiness can justify keeping the richer form, because the primitive set is a vocabulary for thinking, not a minimal basis to be admired. Superfluous in theory and adequate in practice is a legitimate, stated trade-off.

The lesson generalizes far beyond synchronization. Layer boundaries are vocabulary decisions, and each one deserves the same interrogation: is the complexity in my code essential to the problem, or is it compensating for an operation the layer below should have offered? Programmers who never ask this ship mystifications; programmers who ask it too eagerly mint primitives for every inconvenience. The test is the gap: when difficulty of expression vastly exceeds difficulty of concept, the interface, not the program, is the thing to fix.

**Source:** [Cooperating Sequential Processes](../works/cooperating-sequential-processes.md) — the transition sections where the shared-variable solution is condemned as economically and intellectually misleading, the trace-free one-way nature of plain reads is identified as the root cause, the synchronization primitives are introduced, and the general form is kept despite a demonstration it could be encoded with the binary form alone.
