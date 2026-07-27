---
type: lesson
title: "Stratify a reasoning system so its general part knows nothing about your program"
figure: pnueli
works: [the-anchored-version-of-the-temporal-framework]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---

# Stratify a reasoning system so its general part knows nothing about your program

**Lesson:** A proof system for real programs has to talk about three unrelated things: how time and sequencing behave, how the data behaves, and what this particular program does. Fusing them produces a system where nothing can be reused and nothing can be checked in isolation. Splitting them into layers — one that establishes facts true of every conceivable run regardless of data or program, one that supplies the arithmetic or list or string reasoning the program and its specification happen to need, and one whose rules narrow attention to the runs this specific program can produce — gives each layer a self-contained job and a self-contained soundness argument. The layering runs strictly one way: the sequencing layer never mentions integers, and neither of the lower layers mentions the program.

The structural payoff is the usual one for correct dependency direction, and it is concrete here. The general layer is provable once, complete on its own terms, and reusable across every program and data domain forever. Swapping the data domain touches only the middle layer. Changing the program touches only the top. Better, the interface between layers can be made deliberately thin: a single rule that lifts a fact valid of all individual states into a fact valid at every position of every run is enough to let arbitrary machinery — a hand proof, a decision procedure, whatever is available — be used for the data reasoning without the sequencing layer knowing or caring which. That is an abstraction boundary in the strict sense: the upper layer is stated entirely in terms of what it needs from below, not in terms of how the below is implemented.

It also makes the costs visible instead of ambient. Accepting arbitrary valid state facts as inputs keeps the upper layer independent of any particular assertion prover, and the price is that the combined system is no longer mechanically enumerable, since validity in a rich data theory is not. Restricting the state language buys recursiveness back. That trade is only statable because the layers were separated; in a fused system, the same fact would show up as a vague sense that the method is hard to automate. A programmer who works this way builds reasoning tools and domain models the same way — sequencing and coordination logic that has no idea what data it moves, domain rules that have no idea what program invokes them, and program-specific glue confined to a layer that everything else is independent of — and expects the boundaries to reveal where the real costs sit.

**Source:** [The Anchored Version of the Temporal Framework](../works/the-anchored-version-of-the-temporal-framework.md) — the introduction's decomposition of the proof system into general, domain, and program parts with each part's role and the completeness claims attached to them; and the general-part section's instantiation rule, which takes validity of a state formula rather than provability as its premise, together with the accompanying note that this independence from any assertional prover is what makes the combined system non-recursive unless the state language is restricted.
