---
type: lesson
title: "Wanting to be different is not a design criterion"
figure: stonebraker
works: [the-implementation-of-postgres]
axes: [hardware-affinity, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Wanting to be different is not a design criterion

The most honest admission a builder can make about a project is that a major decision was driven by the wish not to repeat themselves. It sounds harmless — the well-understood approach was already implemented once, nobody learns anything by doing it again — and it quietly corrupts the evaluation, because a designer who wants the novel option to win stops enumerating the conventional option's variants. The conventional approach almost always has a configuration that reaches the same goal, and it goes unexamined precisely because finding it would end the interesting part of the project.

The corruption shows up as an argument that only works under an assumption you did not check. Keeping every prior version in place rather than journaling changes elsewhere gives you instantaneous abandonment of in-flight work and queryable history for free, which is a genuine and attractive gain. But it also means that at commit time you must durably place writes wherever the data happens to live, scattered, while the journaling design places one compact sequential batch — and scattered writes lose to sequential writes badly enough that the comparison is decided before anything else is considered. The novel design only draws level if the hardware provides memory that survives a failure, which was not a property of the machines it ran on. Meanwhile the headline benefit that motivated the whole departure was available the conventional way all along, by writing superseded versions into a history collection under the ordinary journaling protocol. Nobody looked, because looking was not the point.

The same failure repeats at a different scale in the choice of implementation language, picked partly because the previous project used something else, and paid for in a runtime whose central productivity feature — automatic reclamation of memory — had to be suppressed, since a latency-sensitive server cannot afford an unscheduled pause. The general form of the mistake is adopting a tool for advantages your own constraints forbid you from using. So the check is mechanical and worth running every time: state what you are actually trying to achieve, then force yourself to describe how the boring approach would achieve it, including the variants you have not tried. If you cannot make that description, you have not yet earned the right to prefer the interesting one. Novelty is a fine thing to produce and a terrible thing to optimize for.

**Source:** [The Implementation of Postgres](../works/the-implementation-of-postgres.md) — the storage system section, which names the desire to do something unconventional as the guiding motive, works through the durability cost, and then concedes the historical-query capability was reachable by conventional means; the language-choice discussion in the implementation section makes the same admission independently.
