---
type: lesson
title: "Prefer the measure you can reason about, and say out loud what fidelity you traded for it"
figure: stearns
works: [hierarchies-of-memory-limited-computations]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Prefer the measure you can reason about, and say out loud what fidelity you traded for it

**Lesson:** Between two candidate cost measures, the more faithful one is not automatically the better one to work in. Storage is a less realistic account of what a computation costs than elapsed work, yet reasoning about it yields sharper results and — the decisive point — it is far easier to see *why* a problem inherently needs a given amount of storage than why it needs a given amount of work. A measure whose lower bounds you can actually argue for produces knowledge; a more faithful measure whose lower bounds defeat you produces nothing, and nothing is not more accurate than something. The intuitive accessibility of a measure is a real property of it, on the same footing as its fidelity, because you are the instrument that has to use it.

This does not license picking whatever is convenient. It sits under the prior demand that a model reflect the features that matter, and it survives that demand only because the trade is made explicitly and the loss is named. The pattern is: state that the measure is a proxy, state which direction it distorts, take the sharper results, and expect that insight won in the tractable measure will transfer to the intractable one — not as theorems, but as an understanding of where the difficulty lives. What is not allowed is sliding from "easier to reason in" to "what actually costs money," which is how proxy metrics quietly become targets.

The generalisation is broad and unglamorous. Any time you instrument a system, you are choosing among quantities that differ in how closely they track the thing you care about and in how amenable they are to argument. Counting allocations is coarser than measuring latency and vastly easier to reason about causally; a static structural metric is a worse account of quality than defect rate and gives you something you can act on before defects exist. Take the reasonable proxy, keep the distortion written down beside it, and do not let the choice go unremarked — an unlabelled proxy is the same artifact as a labelled one, minus the only thing that made it safe.

**Source:** [Hierarchies of Memory Limited Computations](../works/hierarchies-of-memory-limited-computations.md) — the second paragraph of the introduction, which concedes that the storage measure is less realistic than the time measure and defends the choice by the sharpness of the results, the insights it yields, and the greater ease of intuiting why a problem inherently needs a given amount of storage rather than a given amount of time.
