---
type: lesson
title: "Restate an impossibility as a size limit and it turns into an instrument"
figure: chaitin
works: [the-limits-of-mathematics, algorithmic-information-theory-some-recollections]
axes: [verifiability, primitive-count]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Restate an impossibility as a size limit and it turns into an instrument

**Lesson:** There are two ways to establish that a formal system cannot do everything. The classical route runs through a self-referential sentence and yields one strange statement that is true and unreachable. The result is decisive and also easy to quarantine, because the exhibited statement is visibly a contrived artifact, unlike anything encountered in ordinary work. Chaitin took the other route. He built on the paradox of the smallest thing that cannot be named briefly, which is about description length rather than self-reference, and got limits stated as inequalities in bits, parameterised by the size of the system doing the reasoning.

The gain is not only strength. A limit with a size in it has a dial on it. You can ask how much assumed content buys how much reach, compare two systems by their content, and locate a specific claim relative to the boundary. The limitation stops being a curiosity about one weird sentence and becomes a budget that applies to whatever you are actually doing. Chaitin pushed this all the way to naming the constants, so that the statement of a limitation includes a number a reader can check.

The transferable move is to look, whenever you hit an impossibility, for the version of it that names a resource. Undecidability restated as a bound on how much a given amount of specification can determine is something you can plan around. Unpredictability restated as a bound on how much a model of a given size can capture is something you can budget for. Impossibility results without quantities tend to be either ignored or over-generalised, because there is nothing in them to measure against; the same result with a size attached tells you where you stand.

**Source:** [The Limits of Mathematics](../works/the-limits-of-mathematics.md) - the lecture transcript contrasting the liar-paradox route with the naming-paradox route step by step, and deriving a bound in bits parameterised by the reasoning system's own complexity. The path from the early appearance of that argument to the mature incompleteness results is traced in [Algorithmic Information Theory: Some Recollections](../works/algorithmic-information-theory-some-recollections.md).
