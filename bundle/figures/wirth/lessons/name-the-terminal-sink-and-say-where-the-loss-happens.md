---
type: lesson
title: "Name the terminal sink, and say where the loss happens"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Name the terminal sink, and say where the loss happens

**Lesson:** Any system that routes items to destinations must answer what happens when the destination will not take one — no room, no such recipient, no permission. The usual answer is a fallback, which is fine and merely postpones the question, because the fallback can refuse too. Designs go wrong not by having fallbacks but by having a chain of them that is never followed to its end, so the last link is whatever the code happens to do, which is typically to drop the item silently while reporting success to somebody. The fix is not to make the chain longer. It is to follow it to a terminus and write the terminus down.

A well-formed chain has a shape. The first fallback should return the item to whoever produced it, because the producer is the one party guaranteed to be reachable and the one for whom the failure is actionable. The next should route to a designated party whose job is to deal with what nobody else would, and that party is a role in the operating discipline, not a piece of code — which means the design carries an obligation to a human: someone must attend to it often enough that it does not itself fill up. And beyond that there must be an explicit last case, stated plainly as loss. Naming the loss is what makes it engineering rather than accident: it is now a known, bounded, singular circumstance that can be argued about, monitored, and made rare, instead of an unexamined branch.

The reason this matters more than it appears is that undeliverable items are the ones that arrive when the system is already in trouble. A well-behaved chain under normal conditions may be exercised only when everything is full, which is exactly when each fallback is most likely to fail as well, and exactly when a silent drop is most damaging and least visible. So the chain should be evaluated at its worst: assume every stage is at capacity and ask what the last stage does, whether anybody finds out, and whether the producer was told the truth. If the answer to any of those is unsatisfactory, the design does not have a fallback chain, it has a sequence of hopes.

**Source:** [Project Oberon](../works/project-oberon.md) — section 11.2's description of the dispatch procedure, which searches the recipient's mailbox for a free directory slot and then for enough adjacent free blocks, and states that if either no slot exists or no large enough space is found the message is returned to the sender's own mailbox, that if this attempt also fails the message is redirected to the postmaster, that the postmaster is expected to inspect his mailbox sufficiently often that no overflow occurs, and that if the postmaster's mailbox also overflows the message is lost; together with the same section's note that an unregistered recipient name likewise causes return to the sender.
