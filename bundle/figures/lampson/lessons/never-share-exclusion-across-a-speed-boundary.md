---
type: lesson
title: "Mutual exclusion between participants of very different speeds destroys the fast one's worst-case guarantee, so a speed boundary is where a coordination model has to change"
figure: lampson
works: [experience-with-processes-and-monitors-in-mesa]
axes: [hardware-affinity, parallelizability, verifiability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Mutual exclusion between participants of very different speeds destroys the fast one's worst-case guarantee, so a speed boundary is where a coordination model has to change

**Lesson:** The tempting move when a fast participant and a slow participant must share state is to make them play by identical rules: both acquire the same lock, both respect the same discipline, one uniform model all the way down. It is a clean design and it is wrong, for a reason that has nothing to do with elegance. Once the fast participant can be made to wait behind the slow one's critical region, its worst-case response time is bounded below by however long the slow one needs to finish — permanently, by construction. Higher throughput on the fast side is still available, but the real-time guarantee is gone and no amount of tuning brings it back. This is a structural loss, not a performance regression, and it is invisible in any measurement of average behavior.

The correct response is to accept that the coordination model must change somewhere along the path from the physical device to the application, and then to choose the crossing point deliberately rather than letting it land wherever the layering happens to break. Below the crossing there is no shared lock at all: the only mutual exclusion available is whatever the memory itself provides on a single indivisible access, and the shared structure must therefore be designed so that every update it needs is expressible in those terms. Producer-and-consumer shapes over a list or an array fit inside that budget. Above the crossing, ordinary disciplined exclusion resumes. The rule is that the amount of code living below the crossing must be small and sealed off, because it is code that no invariant argument protects.

Sealing it off is not the same as making it safe, and the honest version of this design admits the residual hazard rather than papering over it. Removing the lock reintroduces exactly the race that the lock existed to prevent: one side can observe that there is nothing to do and be on its way to waiting when the other side changes the world and announces it, and the announcement lands on nobody. That has to be closed by a remembered-wakeup flag on the condition itself, which turns it into a counting device rather than a pure notification, and only for the conditions that a device can announce. And the deeper cost is one of illusion — dressing unsynchronized code in the same syntax as synchronized code invites everyone to reason about it as if the exclusion were real. Timing bugs at that boundary are reported as a recurring annoyance in the resulting system even though the authors still judged the economy of a single mechanism worth it.

A programmer who believes this stops looking for the one uniform concurrency model that covers the whole stack, and starts looking for the place where the speed ratio makes uniformity indefensible. They then ask a different question at that seam: not "how do I lock this?" but "what update pattern can I express using only the atomicity the hardware already gives me, and how little code can I confine to that regime?"

**Source:** [Experience with Processes and Monitors in Mesa](../works/experience-with-processes-and-monitors-in-mesa.md) — the discussion of device-originated notification outside the lock, including the rejected alternative in which devices acquire locks like ordinary participants and the worst-case-response argument against it.
