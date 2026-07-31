---
type: lesson
title: "When the deployment shape changes, re-pick the resource you count before re-tuning anything"
figure: yao
works: [a-journey-through-computer-science]
axes: [hardware-affinity, parallelizability]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# When the deployment shape changes, re-pick the resource you count before re-tuning anything

**Lesson:** Every cost model is a bet about which resource is scarce, and that bet is inherited from the machine shape the model was invented on rather than derived from anything permanent. A model that counts steps encodes the assumption that one processor with cheap access to all the data is doing the work. Move the same computation onto participants who each hold part of the data and must talk to reach an answer, and the expensive thing is no longer the work — it is moving the data to where work can happen. Optimizing the inherited quantity in the new setting produces designs that look excellent on the old metric while being dominated by a cost the metric does not mention. So the first response to a change in deployment shape is not to re-tune the implementation; it is to re-derive which quantity to count, and to accept that this makes a new theory rather than a new constant factor.

Defining the new measure is a modeling act with two obligations. It must name exactly what is being charged for — bits crossing between parties, holding nothing else against the participants, so that their local effort is free and only the interaction is scored — and it must be sharp enough that different problems separate under it. That separation is the evidence the measure is real: some joint questions are answerable with a trace of interaction because each side needs only a digest of the other's data, while others force one side to ship essentially everything, and a measure that cannot tell those two apart is not measuring anything. Note where the intellectual weight sits. Showing that a cheap protocol exists is the easy half; showing that no protocol can do better is where the substance is, and it is also the only half that tells an engineer to stop looking.

The transferable discipline is to keep the accounting unit under active review, because the scarcity that justified it is a fact about a moment in hardware and topology, not about the problem. When batch gave way to interaction, when one machine gave way to many, when memory hierarchies made locality dominate arithmetic, each shift invalidated a metric that everyone was still optimizing. A measure chosen this way pays out well beyond its motivating setting: an abstraction that charges for information crossing a boundary applies wherever a boundary exists, from parts of a chip to stages of a pipeline, because the underlying question — how much must one side learn about the other's data to produce this answer — was never really about networks.

**Source:** [A Journey Through Computer Science](../works/a-journey-through-computer-science.md) — the communication-complexity section: its account of why the measure was introduced (the late-1970s shift from mainframe to networked, collaborative computing, where moving data became the dominant expense), the contrast between a joint question answerable with a couple of bits and one requiring an entire operand to be sent, the remark that proving no better protocol exists is the deep part, and the closing note on the measure's reach from chip design to data streaming.
