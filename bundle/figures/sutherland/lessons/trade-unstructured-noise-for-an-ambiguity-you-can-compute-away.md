---
type: lesson
title: "Trade unstructured noise for an ambiguity you can compute away"
figure: sutherland
works: [a-head-mounted-three-dimensional-display]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Trade unstructured noise for an ambiguity you can compute away

Not all uncertainty is equally bad, and the useful distinction is whether it has structure you can exploit. Sutherland's team chose a sensing scheme whose measurements were precise but ambiguous — each reading pinned the answer down tightly within a period while leaving open which period it belonged to — over an alternative whose readings were unambiguous but corruptible by whatever unrelated racket the room happened to produce. The ambiguity was accepted deliberately, because it collapses into a single unknown offset with a known form, and a known form is something extra measurements can pin down. Corruption by arbitrary environmental noise has no such form; there is nothing to solve, only degradation to absorb.

The reasoning generalizes past sensors to any place a design faces a menu of imperfections. Ambiguity with structure is a solvable equation waiting for more constraints. Unstructured error is a permanent tax. So the right move is often to select the component that is wrong in a describable way and then buy back the certainty elsewhere, by over-determining the system — Sutherland's rig took roughly twice as many readings as the degrees of freedom it needed, precisely so the redundancy could adjudicate what any single reading could not. Redundancy here is not belt-and-braces duplication; it is the mechanism that converts a well-shaped unknown into a determined one.

There is a second lesson folded in: the residual uncertainty was traced back to one identifiable quantity, the initial guess about a starting condition, and named as such. Uncertainty that has been localized to a specific unknown with a specific origin is tractable — you can measure it, bound it, attack it, or decide to live with it knowingly. Uncertainty spread diffusely across a system is none of those things.

A programmer who believes this changes how they evaluate imperfect dependencies and inputs. Faced with a choice between a component that fails cleanly in a characterized way and one that mostly works but fails arbitrarily, they take the characterized failure and design the resolution around it, rather than taking the one that looks better in the median case. They add redundant observations not as a safety blanket but as the specific instrument that resolves a specific ambiguity, and they can say in one sentence which unknown each redundant observation is there to eliminate. And when uncertainty remains, they push to name it as a quantity rather than tolerating it as a mood about the system's reliability.

**Source:** [A Head-Mounted Three Dimensional Display](../works/a-head-mounted-three-dimensional-display.md) — the head-position sensing section, which weighs continuous versus pulsed acoustic measurement, accepts periodic ambiguity to gain noise immunity and cheap transducers, and proposes geometric over-determination as the way to resolve it.
