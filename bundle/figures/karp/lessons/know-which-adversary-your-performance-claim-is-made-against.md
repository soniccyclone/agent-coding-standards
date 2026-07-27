---
type: lesson
title: "Every performance claim names an adversary; know which one yours assumed"
figure: karp
works: [combinatorics-complexity-and-randomness]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Every performance claim names an adversary; know which one yours assumed

**Lesson:** Behind every statement about how fast something runs sits an unstated assumption about where the inputs come from, and the two standard assumptions give violently different verdicts on the same code. The conventional one imagines an infinitely clever opponent who has read your implementation and hands you the input engineered to humiliate it. That framing is what makes a bound trustworthy, because it holds no matter what happens. It is also what makes the framing occasionally useless: judged that way, the simplex method and the best practical tour-improvement heuristics of the era were failures, even though they were the tools that actually solved the field's real problems every day. A verdict that condemns your most reliable instrument is a verdict about your model, not about your instrument.

The alternative assumption is that inputs arrive from someone drawing them out of a plausible distribution, neither malicious nor helpful. Under that assumption you can often prove what practitioners already observed: that the algorithm's execution is predictable and its output nearly optimal with overwhelming probability, because large numbers of random events aggregate into regularity. Karp is scrupulous about the price of this move, and the honesty is the instructive part. Such a result means something only if the assumed distribution resembles the instances that actually occur, and there is no way to establish that from inside the analysis. He judged the whole program only partly successful for exactly this reason, and observed that designing these algorithms in practice stayed closer to a craft than to a science.

The habit for a programmer is to make the input model explicit every single time a performance claim is made, yours or someone else's. "This is fast" is not a statement until you say fast on what, drawn from where. Benchmarks quietly encode a distribution and then get cited as though they encoded a guarantee. Worst-case bounds get cited as though the worst case were reachable in your deployment, which decides whether a hostile user is in your threat model, an entirely different question from whether the code is good. Neither model is correct in general; using one while believing you are using the other is how teams both ship fragile systems and reject good ones.

**Source:** [Combinatorics, Complexity, and Randomness](../works/combinatorics-complexity-and-randomness.md) — the passage contrasting worst-case analysis, framed as an omniscient adversary constructing embarrassing inputs, with the probabilistic analysis of algorithms Karp turned to in the mid-1970s, along with his own accounting of that program's limits.
