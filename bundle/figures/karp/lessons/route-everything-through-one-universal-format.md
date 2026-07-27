---
type: lesson
title: "Route many problems through one universal format instead of building translators between every pair"
figure: karp
works: [reducibility-among-combinatorial-problems, combinatorics-complexity-and-randomness]
axes: [primitive-count, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Route many problems through one universal format instead of building translators between every pair

**Lesson:** Once you accept that problems can be translated into each other, an architectural question follows immediately: which translations should you actually build? Connecting every pair directly grows quadratically and nobody maintains it. Karp's answer, and the structural insight that made his catalogue an organizing principle rather than a list, is to elect a single hub problem and translate everything to and from that. Each new problem costs one translation, not one per existing problem, and because translations compose, connecting to the hub connects you to everything else transitively. The hub earns its position by being simple enough to reason about and expressive enough that anything can be phrased in it, which is a real tension: too weak and the encodings become impossible, too rich and the hub is as hard to study as the mess it replaced.

This is the same shape as a compiler's intermediate representation, a database query plan, a wire protocol, a common data model behind a dozen integrations. The engineering payoff compounds in one specific way that is worth naming: all the optimization effort concentrates on the hub. Every hour spent making the central solver faster benefits every problem routed through it, whereas an hour spent on a bespoke solver benefits one caller. This is precisely why industrial satisfiability solvers became infrastructure that verification, scheduling, and configuration tools all sit on top of, rather than each field growing its own search engine.

The habit for a programmer is to notice when you are on the verge of writing your third pairwise converter and stop. Ask what canonical form all of these could pass through, pay the one-time cost of defining it well, and accept encoding overhead in exchange for the collapse in the number of moving parts. The cost of the hub is honest and worth stating: encodings inflate problem sizes and can obscure structure the bespoke path would have exploited. That trade is usually worth it, and when it is not, you at least know which specific problem earned its own path.

**Source:** [Reducibility Among Combinatorial Problems](../works/reducibility-among-combinatorial-problems.md) — the choice to make satisfiability the single source of all the reductions in the paper's figure, and Karp's own note that he was influenced by Dantzig's suggestion that integer programming could act as a universal format for combinatorial problems.
