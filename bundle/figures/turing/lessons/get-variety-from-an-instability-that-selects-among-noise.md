---
type: lesson
title: "Uniform rules cannot produce non-uniform output; build an instability that selects among the noise instead"
figure: turing
works: [the-chemical-basis-of-morphogenesis]
axes: [expressiveness, cognitive-load]
subdomains: [foundations-of-computation, distributed-systems-and-concurrency]
tags: [lesson]
---
# Uniform rules cannot produce non-uniform output; build an instability that selects among the noise instead

**Lesson:** If a system's rules treat every part identically and its starting state is identical everywhere, it stays identical forever — no amount of running it produces structure. This is not a limitation of a particular rule set; it follows from the symmetry itself, and it holds for any local dynamics you might substitute. So whenever you need differentiated output out of undifferentiated machinery, you are not looking for a cleverer rule. You are looking for a place where the equilibrium becomes unstable, because instability is the only thing that lets the tiny unavoidable asymmetries already present in any real system grow into the differences you want.

The second half of the insight is the one people miss. An instability does not merely amplify noise, it filters it: the dynamics decide which components of an arbitrary disturbance grow and which die, so a huge and uncontrolled space of possible perturbations collapses into a small set of possible outcomes. Arbitrary input, few outputs. That means you do not need to specify or control the perturbation at all — only the selection rule — and the perturbation supplies exactly the one thing the rules cannot, which is the choice of orientation or phase among otherwise equivalent outcomes.

A programmer who believes this designs differently around randomness. Randomness stops being a nuisance to be seeded away and becomes the load-bearing source of the choices your deterministic layer is symmetric about: leader election, tie-breaking, jitter that stops synchronized clients from thundering together, hash-based sharding. The design work goes into the selection dynamics — which perturbations get amplified, into how many distinguishable end states — rather than into the perturbation source, which can stay unspecified. And when a system that ought to be producing variety is producing sameness, this lesson tells you where to look: not for a missing rule, but for a stability you failed to break.

**Source:** [The Chemical Basis of Morphogenesis](../works/the-chemical-basis-of-morphogenesis.md) — the section confronting the objection that a spherically symmetric embryo can never become an asymmetric animal, and its resolution via unstable equilibria whose new stable states are far fewer in variety than the disturbances that trigger them.
