---
type: lesson
title: "Independent-looking knobs with an arithmetic relation are not independent"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Independent-looking knobs with an arithmetic relation are not independent

**Lesson:** A component that exposes several settings invites the reader to treat them as separate choices, each with its own sensible range. Often they are not separate at all: an expression relating them has to come out a whole number, or fit within a bound, or divide exactly, and the legal configurations are therefore a sparse lattice inside the box that the individual ranges describe. Every setting can be individually reasonable and the combination still be impossible. This is a class of defect that no amount of per-setting validation catches, because per-setting validation is looking at the wrong thing.

The obligation is to write the relation down and put it somewhere the user of the component will meet it. Documenting each setting separately, however carefully, does not communicate a constraint that only exists between them. Better still is to remove the freedom: derive one of the settings from the others so the constraint holds by construction, or expose a single parameter that names the intended outcome and computes a consistent assignment behind it. A setting that can only take one value given the others is not a setting, and offering it as one is an invitation to a failure that occurs late, in an unrelated place, with a message about dimensions rather than about configuration.

There is a second-order version of this that shows up whenever the constraint has to hold repeatedly. If a quantity is reduced by a fixed factor at each of several stages, and each stage requires the division to be exact, then the constraint is not on one stage but on the original value — it must be divisible by that factor as many times as there are stages. That is a real requirement on an input that nothing in any individual stage's interface mentions, and the practical form of the advice is to choose the starting size to have generous headroom in that factor, rather than to discover at the fourth stage that it does not. Rules of thumb of this shape ("pick sizes that halve cleanly several times") look like superstition until you locate the arithmetic they are protecting.

The general habit: when you meet a component with several numeric settings, do not stop at what each one means. Find the formula that connects them to the output size or the resource bound, and ask what it requires. If nobody can produce that formula, the component has a validity condition that exists but is not known, which is worse than a documented restriction and is where the confusing failures come from.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the convolutional-layers section, which gives the output size as a formula in the input size, filter size, padding and stride, warns that these must be chosen so the stride divides the combined quantity evenly or the layer is invalid and implementations will raise an exception, and later lists among its architecture rules of thumb that it is very useful for the input size to be evenly divisible by two many times over.
