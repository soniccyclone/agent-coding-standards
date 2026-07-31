---
type: lesson
title: "A surprising result is usually a faithful reading of your trade-off"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A surprising result is usually a faithful reading of your trade-off

**Lesson:** When an optimiser settles somewhere that looks obviously wrong — a solution exists that you can see by eye and it did not find it — the instinct is to suspect the search: bad initialisation, wrong step size, stopped too early, a bug. Check the objective first. Almost always the returned answer is the correct optimum of the function you wrote, and what you wrote is not what you meant. The gap is in the weighting between competing terms, where a constant was set to a value nobody thought hard about, and that constant is a quantitative statement of preference the optimiser is faithfully honouring.

The specific failure is that these constants are usually introduced as a technical necessity — two terms need combining, so a coefficient appears — rather than as the policy decision they are. Set it low and you have declared that violations of the requirement barely matter compared with the other objective, so a solution that violates the requirement on several cases while doing well on the other axis is genuinely better by your stated criterion. The obvious-by-eye solution scores worse. Nothing is broken; you asked for one thing and are unhappy to receive it because you were picturing the other.

Two habits follow. Whenever you introduce a coefficient balancing two terms, write down in words what its magnitude asserts — "at this value, I am saying one violated case is worth this much margin" — because that sentence is checkable against intent in a way the number is not. And when a result surprises you, evaluate your preferred solution under the objective before touching the search. If your solution scores worse, the objective is the problem and tuning the optimiser is wasted effort; if it scores better, then and only then do you have a search problem.

The general form is that an optimiser is a very literal reader of a specification, which makes it an excellent detector of specifications that do not say what their author meant. Treat a surprising optimum as free information about your own stated preferences rather than as a malfunction, and the surprise becomes the most useful output of the run.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the closing remark of the gradient-descent worked example in the support-vector-machine chapter, which asks why the process converges on a solution with points inside the margin when an obvious separating hyperplane with a clear margin exists, and answers that choosing the small regularisation constant was itself the statement that misclassified or margin-violating points did not matter much compared with obtaining a large margin.
