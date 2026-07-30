---
type: lesson
title: "The good-default-plus-escape shape is found by failing at both poles, and both failures are necessary"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# The good-default-plus-escape shape is found by failing at both poles, and both failures are necessary

**Lesson:** A mechanism had to pick one of several technically valid options on the user's behalf. The first implementation presented the applicable options and let the user choose, which is the respectful design and the one that survives a design review — and in use it was exceedingly tedious, because the same obvious answer had to be given over and over. The second implementation picked a default automatically, which is the efficient design, and it proved too inflexible. The third picks the default automatically but provides an escape command for choosing any applicable alternative, and that is the one that stayed.

The endpoint is unremarkable; almost every mature tool has this shape. What is worth extracting is that the team needed both failures to get there, and that neither failure was foreseeable from the design. "Always ask" fails on a quantity — the frequency of the question — which is invisible until the thing is in daily use, and asking a user to confirm the obvious reads as careful right up to the moment it becomes an obstacle. "Never ask" fails on a fraction — how often the default is wrong — which is likewise unknowable in advance and, importantly, is never zero for a choice that had multiple valid answers to begin with. Both quantities are properties of usage, so no amount of thought at the design stage substitutes for having shipped each pole and observed which way it hurt.

That gives a diagnostic rather than a slogan. Whenever a system faces a choice that is usually obvious and occasionally not, both pure policies are wrong, and the ratio between "usually" and "occasionally" is exactly what determines the design — which means the design cannot be settled by argument and must be settled by exposure. The corollary is about how to read a tool that already has this shape: the escape hatch is evidence that someone hit the inflexibility, and the automatic default is evidence someone hit the tedium. Removing either because it looks like clutter re-runs an experiment that already has an answer.

A secondary point: the third design is not a compromise between the first two in the sense of doing each half-way. It is the automatic policy plus an affordance, which costs the common case nothing at all — the tedium does not return in diluted form. When the two poles are cheap and expensive rather than symmetric, look for the asymmetric combination instead of the midpoint.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 11 section 11.2's boxed note on selecting the editor: the first Trader implementation presented a list of applicable editors for the user to select from and proved exceedingly tedious, the second automatically selected and instantiated a default and proved too inflexible, and the third and current version normally selects a default automatically but provides an escape command letting the user select any applicable editor.
