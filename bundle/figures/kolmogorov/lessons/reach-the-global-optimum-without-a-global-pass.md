---
type: lesson
title: "Before assuming you need a global pass, check whether local adaptation reaches the same bound"
figure: kolmogorov
works: [three-approaches-to-the-quantitative-definition-of-information]
axes: [parallelizability, hardware-affinity]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Before assuming you need a global pass, check whether local adaptation reaches the same bound

**Lesson:** A theoretical optimum is usually derived from a global property of the whole input, and the derivation is then silently read as a procedure: to hit the bound, first survey everything, compute the property, then act. That reading is an assumption, not a theorem, and it is frequently false. Cut the input into segments, act optimally on each with only local knowledge, and the aggregate can meet the same bound to within a negligible margin — because the global property was itself an aggregate of the local ones, and the cost of learning it separately was pure overhead.

The reason this matters far beyond coding schemes is that the two-pass reading imposes architecture. It says the whole input must exist before work begins, which rules out streaming, rules out starting before the end has arrived, rules out doing the segments concurrently, and forces you to hold or re-read everything. Those constraints get accepted as the price of optimality when nobody has checked whether optimality actually required them. The check is worth doing every time: state what the bound depends on, then ask whether that dependence is genuinely global or merely a convenient way to write the derivation.

The general shape is that a quantity defined over a whole often decomposes, and where it decomposes, so does the algorithm. When it does, you get an approach that needs no prior survey, degrades gracefully on inputs whose character shifts partway through, and parallelizes for free — properties the globally-informed version had to give up. When it genuinely does not decompose, you have learned something sharp about the problem, and you pay the two passes knowing why. What you want to avoid is paying for global knowledge out of habit, and building an entire pipeline around a survey step that the mathematics never asked for.

**Source:** [Three Approaches to the Quantitative Definition of Information](../works/three-approaches-to-the-quantitative-definition-of-information.md) — §1's observation that a universal coding method reaching the entropy bound need not be excessively complex and in particular need not begin by determining the letter frequencies of the entire message, since splitting the message into segments and handling each yields the requisite inequality.
