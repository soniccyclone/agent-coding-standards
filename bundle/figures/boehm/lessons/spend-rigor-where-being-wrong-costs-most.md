---
type: lesson
title: "Rigor is a budget to allocate, not a standard to apply uniformly"
figure: boehm
works: [a-spiral-model-of-software-development-and-enhancement]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Rigor is a budget to allocate, not a standard to apply uniformly

**Lesson:** The default instinct about precision is that more is better and evenly distributed is fairest: every module documented to the same depth, every interface specified with the same formality, every component reviewed with the same ceremony. Boehm's argument is that uniform depth is a mistake in both directions at once. It over-invests in the parts everybody already understands, and it under-invests in the parts where a wrong guess will force expensive demolition later, because those are exactly the parts hardest to write about early. Precision costs money and delays commitment, so it should be spent where the consequence of being wrong is largest and withheld where the consequence is small. Elements whose failure mode is cheap can be left deliberately vague until later, when knowing more makes the description almost free.

There is a second cost to uniformity that is easy to miss. Detail is not neutral: it consumes the attention of the few people capable of spotting the real problem. A specification that elaborates everything equally buries its dangerous claims inside a mass of harmless ones, and the scarce expert who could have caught the bad assumption spends their review budget confirming that the trivial parts are still trivial. Graded depth is therefore not just an economy of writing effort, it is an attention-shaping device: the shape of the document tells the reader where to look hard.

The same allocation logic extends past documents to every quality activity. How much testing, how much configuration discipline, how much formal verification is enough? The question has no fixed answer, only a per-project one, obtained by asking what it costs to be wrong in each area. That reframing is what makes "how much process is enough" a tractable engineering question instead of a culture war.

A programmer who believes this writes uneven artifacts on purpose and can defend the unevenness. They will push a risky subsystem down to executable detail while leaving its low-stakes neighbor at one paragraph, and they read a colleague's design the same way, checking whether the depth tracks the danger rather than whether every box is filled in.

**Source:** [A Spiral Model of Software Development and Enhancement](../works/a-spiral-model-of-software-development-and-enhancement.md) — the risk-driven specification discussion illustrated by the design of the traceability tool, plus the evaluation section's treatment of "how much is enough" for planning, quality assurance, verification, and testing.
