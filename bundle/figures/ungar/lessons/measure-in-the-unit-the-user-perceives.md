---
type: lesson
title: "Report performance in the unit a person actually experiences, or your numbers will flatter you"
figure: ungar
works: [programming-as-an-experience]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Report performance in the unit a person actually experiences, or your numbers will flatter you

**Lesson:** Instruments measure the events a system happens to emit, which is almost never the unit in which a human notices trouble. A runtime that stops to compile emits many small, individually unremarkable delays; the person at the keyboard does not perceive them individually, because delays that land close together fuse into one interruption. Tabulate the raw events and the system looks responsive. Group them the way perception groups them and a different, much worse distribution appears. Both tables are arithmetically correct, and only one of them describes what anyone will complain about.

This generalizes past pause times. Any metric has an implicit aggregation choice — per call, per request, per session, per user-visible action — and that choice, not the measurement precision, determines whether the number means anything. The correct aggregation is not the one that is easiest to collect; it is the one whose boundaries match where a consequence becomes noticeable. Choosing the collectible unit instead is how teams end up defending a green dashboard against users who are certain the thing is slow. Averages over the wrong unit are the most common version of this, but even careful percentiles over the wrong unit inherit the same defect.

There is a design consequence beyond honesty in reporting. Once you commit to the perceptual unit, some optimizations stop looking like wins: work that reduces total time while clustering its cost into a single long stall becomes a regression, and work that smears cost thinly becomes a win even when the total goes up. The goal shifts from minimizing a sum to keeping every fused interval under a threshold. A programmer who has internalized this defines the acceptance criterion in terms of what a person will notice before writing the benchmark harness, because that decision silently determines which improvements the harness will be able to see at all.

**Source:** [Programming as an Experience: The Inspiration for Self](../works/programming-as-an-experience.md) — the responsiveness section, where compilation delays observed over a long interactive session are re-tabulated as clustered rather than individual interruptions, and the order-of-magnitude difference between the two accountings is treated as a statement about evaluation standards rather than about the compiler.
