---
type: lesson
title: "Modularity bought by removing a proof rule must be paid back by hand"
figure: liskov
works: [a-behavioral-notion-of-subtyping]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Modularity bought by removing a proof rule must be paid back by hand

**Lesson:** Flexibility in a description is usually purchased by leaving something out, and what gets left out is rarely just detail — it is often the foothold some reasoning technique depended on. Detach the creation of objects from the description of their behavior and you gain real freedom: multiple implementations, new ways of constructing added later, children that build differently from their parent. You also lose the base case of the induction that let anyone establish a property holds of every object of the type, because there is no longer any point in the description where objects are known to start out legal. The freedom and the loss are the same act.

The disciplined response is not to reverse the trade but to name the debt and settle it. What induction used to derive gets asserted outright, as an explicit statement of which states are legal, checked separately against every operation. The same pattern repeats a level up: a description can either carry an explicit account of how an object may evolve over its lifetime, in which case clients reason only from that account and never from the operations themselves, or it can let clients derive evolution from the operations, in which case every added operation has to be justified against what was already possible. Each option removes a reasoning route and compensates with an obligation. Neither is free, and choosing without noticing which route you closed produces descriptions that look adequate and quietly are not.

The uncomfortable part is that the replacement is only as good as the person writing it. An induction rule is mechanical; an asserted invariant is a judgment call, and one that is too weak stays too weak forever — the clients who needed the missing consequence have no legitimate way to recover it, since the route that would have let them derive it is exactly the route the trade closed off. So the substituted assertion has to be strong enough not merely for today's clients but for every property anyone will later want, which is a genuinely harder discipline than the mechanical rule it replaced.

A programmer who believes this reads every simplification of an interface as a question about what proof or check it just disabled. Removing a constructor from the contract, widening a return type, admitting a new implementation path — each may be right, but each demands an explicit answer to "what could someone conclude before that they cannot conclude now, and where is that conclusion now written down?" The answer belongs in the artifact, stated strongly, not in the head of whoever made the trade.

**Source:** [A Behavioral Notion of Subtyping](../works/a-behavioral-notion-of-subtyping.md) — the specification sections arguing that omitting creators forfeits data type induction and must be compensated by an explicit invariant clause, and the comparison section weighing the loss of the history rule against stating evolution constraints declaratively.
