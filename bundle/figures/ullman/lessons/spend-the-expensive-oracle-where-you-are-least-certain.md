---
type: lesson
title: "Spend the expensive oracle where you are least certain"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Spend the expensive oracle where you are least certain

**Lesson:** Systems that improve by consuming authoritative answers usually treat the supply of those answers as fixed and exogenous — someone provides them, and the system learns from whatever it gets. When each answer costs real money or real human time, that framing wastes most of the budget, because the majority of cases are ones the system already handles confidently and which therefore teach it nothing. Turn the relationship around: let the system decide which cases to ask about. It is already producing, alongside each decision, some indication of how marginal that decision was — a score near a boundary, a narrow gap between the top two candidates, a low agreement among internal components. Rank by that, and buy answers for the top of the list.

The reason this works is that the information gained from an answer is largest exactly where the current behaviour is least determined. A confirmed answer on a case you were already sure about changes nothing; an answer on a case sitting on the boundary moves the boundary. So the cost per unit of improvement can differ by orders of magnitude between a well-chosen query and a randomly chosen one, and the mechanism needed to exploit that is small — an uncertainty score you probably already compute, a threshold, and a queue.

Two cautions come with it. Because the acquired answers are deliberately not a random sample, they cannot double as an estimate of overall accuracy; a separate, unbiased sample is still needed for measurement, and conflating the two produces a picture heavily skewed toward hard cases. And the oracle is often itself unreliable — a human under time pressure, a crowd worker — so an answer should be treated as evidence rather than truth: ask several independent sources about the same case and take the consensus, spending more on the cases where they disagree, which is the same principle applied one level down.

The general habit is to notice when acquiring information is a controllable cost rather than a fixed input, and to ask what the system would most benefit from knowing. That question has an answer, the answer is usually computable from state you already have, and asking it converts an expensive resource from something consumed uniformly into something aimed.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the discussion of active learning in the machine-learning architecture section, where a classifier that mostly receives unlabelled data can request ground truth at significant cost for examples it is unsure about, particularly those close to the boundary, so that those examples become training data; together with the adjacent note on crowdsourced labelling that asks several people until a clear majority favours one label.
