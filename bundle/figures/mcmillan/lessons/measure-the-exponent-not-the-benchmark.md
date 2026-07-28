---
type: lesson
title: "Measure the exponent of a parameterised family, not the runtime of a benchmark"
figure: mcmillan
works: [symbolic-model-checking-for-sequential-circuit-verification]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Measure the exponent of a parameterised family, not the runtime of a benchmark

The evaluation in this paper is built on a methodological conviction stated outright: the meaningful comparison between verification methods is not how fast each one handles some example, but how each one's cost *grows* as the examples get bigger. Everything else follows from that. Rather than presenting one impressive circuit, the authors build circuits with knobs — register count, register width, pipeline stages, operation count — and then report the slope on a log-log plot for each knob independently. The claim they end up defending is about a growth rate, which is a claim a single measurement is structurally incapable of supporting.

The reason this matters is spelled out at the end: making a tool usable on bigger problems is not a constant-factor exercise. A method whose cost climbs exponentially in the number of parts stays useless no matter how much you tune it, while a method that climbs polynomially becomes usable as machines improve. Those two situations look identical on any fixed benchmark, and they are the only distinction that actually predicts whether a technique will still be relevant. A benchmark number tells you about today's machine and today's example; a slope tells you about the method.

There is a second, subtler discipline here that is easy to miss. The authors do not merely measure the slopes — they instrument the internal representation, tabulate how many nodes are attributed to each variable, and use those distributions to *account for* the growth they observe, deriving the expected exponent from the structure of the circuit and then checking it against the timing. Measurement that arrives with an explanation is worth far more than measurement alone, because an unexplained exponent is a coincidence that will not survive the next example while an explained one predicts.

A programmer who works this way builds a parameterised family before running anything, sweeps each parameter separately so the exponents are attributable, and refuses to claim a scalability improvement on the strength of a faster wall-clock time. They also add enough introspection to the implementation that a surprising curve can be traced to a structural cause, since the aim is a story about why the cost grows the way it does rather than a table of numbers.

**Source:** [Symbolic Model Checking for Sequential Circuit Verification](../works/symbolic-model-checking-for-sequential-circuit-verification.md) — the stated comparison methodology in the related-work discussion, the parameter sweeps over the pipeline and asynchronous examples, and the closing argument that growth-rate reduction is the only meaningful notion of scalability.
