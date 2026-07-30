---
type: lesson
title: "Represent ignorance as the set of alternatives you cannot rule out, and let knowledge be what survives across all of them"
figure: vardi
works: [reasoning-about-knowledge]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# Represent ignorance as the set of alternatives you cannot rule out, and let knowledge be what survives across all of them

**Lesson:** The instinct when modelling what a component knows is to store it: a list of facts, a confidence score, a flag. The far more productive representation is the complement — record the set of situations the component's information cannot distinguish, and then define knowing something as that thing being true in every one of them. Nothing is asserted about knowledge directly; it is derived from the shape of the uncertainty. Acquiring information is then a single, uniform operation: shrink the set. Fewer alternatives means more knowledge, and the two notions become the same notion viewed from opposite sides.

Three things follow that make this worth the change of habit. Nested statements become ordinary rather than dizzying: whether one participant knows that another does not know something is just a question about which alternatives are reachable through whose indistinguishability, and the sentence that no human can parse becomes a mechanical check. Ignorance becomes something you can be precise about, since the exact extent of what is not known is written down rather than left as an absence. And because the definition of knowing is uniform, everything downstream — group notions, evolution over time, the interaction with action — is defined once instead of per case.

The move is not confined to reasoning about agents. It is the same reason a set of possible parses beats a single guessed parse, a set of feasible schedules beats a heuristic pick, and a range beats a point estimate: keeping the alternatives explicit lets you answer "is this determined yet" by inspection instead of by argument. And the notion is worth applying to things that obviously do not think — a wire, a buffer, a cache — because "knows" here means nothing more than "its information excludes the alternatives where this is false", which is a perfectly sharp property of a mechanical component.

**Source:** [Reasoning About Knowledge](../works/reasoning-about-knowledge.md) — chapter two's presentation of the possible-worlds model, where a participant knows something exactly when it holds at every world that participant considers possible, with the remark that the fewer worlds considered possible the less the uncertainty and the more is known; and chapter one's framing of the approach as applicable to negotiators, robots, and components such as wires or message buffers alike.
