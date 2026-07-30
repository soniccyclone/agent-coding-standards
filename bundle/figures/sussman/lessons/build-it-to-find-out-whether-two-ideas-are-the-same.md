---
type: lesson
title: "When you cannot tell whether two ideas differ, implement both in one substrate and see whether the artifacts coincide"
figure: sussman
works: [scheme-an-interpreter-for-extended-lambda-calculus]
axes: [cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# When you cannot tell whether two ideas differ, implement both in one substrate and see whether the artifacts coincide

**Lesson:** Two research communities can describe what looks like the same phenomenon in vocabularies so different that no amount of comparing the vocabularies settles whether the phenomena are the same. Arguing about the definitions is unproductive because each side's terms are only defined inside its own framework. The move that works is to build one artifact that supports both, then look at what you built. Scheme exists because its authors could not explain the difference between message-passing agents and procedures, so they implemented an interpreter meant to mix the two cleanly — and on finishing it discovered the two had exactly the same representation. A behavior-defining script paired with a set of known correspondents is a body of code paired with an environment; the agent was a closure with different terminology. The identity was not available by inspection beforehand and became obvious afterward, which is the characteristic signature of a question that construction answers and analysis does not.

The authors are unusually candid that this was not insight arriving whole. They started with one evaluation strategy, found empirically that it wrecked a property they cared about, and rewrote. They describe the whole process as bootstrapping knowledge experimentally rather than deducing a clean design and then coding it. That candor is the methodological content: treat an implementation as an instrument for finding out what you think, not as a transcription of what you already decided. A design you can only defend in prose has not been tested; a design that runs will contradict you, and the contradictions are the payoff.

Two practical consequences. First, when someone claims a new mechanism is fundamentally different from one you already have, the cheapest resolution is often to express both in your existing substrate and compare the results — if they collapse, you have removed a concept from the system rather than added one, which is the best possible outcome for a small core. Second, when a design decision hinges on a property you cannot reason about confidently (what accumulates, what is retained, what breaks under recursion), stop reasoning and build the smallest thing that exhibits the property. The empirical route is not intellectual weakness; here it is what produced the identification that the entire language rests on.

**Source:** [Scheme: An Interpreter for Extended Lambda Calculus](../works/scheme-an-interpreter-for-extended-lambda-calculus.md) — the acknowledgements, describing the attempt to build an interpreter mixing agents and procedures, the discovery on completion that they were identical in implementation, the subsequent empirical discovery that the original evaluation strategy ruined iteration, and the explicit disclaimer that no single flash of understanding was involved; plus the implementation-issues section that argues the identification in detail by matching script to code-body and acquaintances to environment, and rewrites a message-accepting pair constructor as an ordinary closure.
