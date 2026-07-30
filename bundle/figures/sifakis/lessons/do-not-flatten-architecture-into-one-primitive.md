---
type: lesson
title: "Reasoning at the level where structure is still visible beats translating everything down to one composition primitive"
figure: sifakis
works: [turing-lecture-2009]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Reasoning at the level where structure is still visible beats translating everything down to one composition primitive

**Lesson:** A minimal basis is a virtue in a foundational calculus and a liability in an analysis. Once every protocol, scheduler, and bus in a design has been compiled into a single low-level parallel composition of automata, the semantics is uniform and correct and the structure that would have made the system tractable is gone: what remains is an undifferentiated product with no record of which interleavings the architecture never permitted. Compositional rules should be stated and applied over the high-level coordination constructs the designer actually used, without first flattening them.

This is not an argument against small primitive bases — it is an argument that the layer at which you reason and the layer at which you define meaning are different choices. Reduction to a minimal core is how you establish that a coordination construct means something precise; it is the wrong level for arguing about the resulting system, because reduction is lossy in the specific dimension the argument needs. Keeping a construct's identity intact means keeping the invariants that came with it, and those invariants are the leverage.

Heterogeneity is the reason the temptation to flatten is strong, and also the reason to resist it. Real systems compose parts that differ in how they execute (clocked versus event-driven), in how they interact (locks, monitors, calls, messages), and in the granularity at which their steps are meaningful. Flattening is the easy way to make such parts commensurable, and it makes them commensurable by discarding what distinguished them. The harder and more useful path is a composition framework that expresses the differences directly, so that a scheduler stays a scheduler in the model and the argument can appeal to what schedulers guarantee.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/turing-lecture-2009.md) — Sifakis's discussion of the three sources of heterogeneity in composing components, his call to move beyond a single low-level parallel composition operator, and his insistence that compositional rules apply to high-level coordination mechanisms without translation into automata-based composition.
