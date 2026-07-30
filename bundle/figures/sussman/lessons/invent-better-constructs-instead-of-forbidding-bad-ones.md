---
type: lesson
title: "Removing a construct does not remove the practice; supply a better alternative or watch the omission get patched back in"
figure: sussman
works: [lambda-the-ultimate-imperative]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Removing a construct does not remove the practice; supply a better alternative or watch the omission get patched back in

**Lesson:** A designer who deletes a construct in order to prevent a style of thinking has usually not prevented anything. Any language with procedures, procedure values, conditionals, lexical scope and cheap value-free transfer can reconstruct unrestricted jumps, caller-determined variable lookup and lazy parameters as short local idioms, and with a macro facility the reconstruction is comfortable enough for daily use. The prohibition is a speed bump, not a barrier. The historical record the authors assemble bears this out: the language that most conspicuously banned jumps had to grow escape constructs almost immediately, then more of them, because the need the jump had been serving did not disappear when the keyword did. Prohibition converts a legible mechanism into an ad-hoc pile of special cases.

Behind the pragmatic point is a claim about where clarity comes from. A confused program is the image of a confused understanding of the problem, and no vocabulary restriction repairs the understanding. A language helps precisely to the degree that it offers constructs that fit the shape of the problem being solved, which means the design effort should go into finding and inventing such constructs — not into auditing which existing ones might be abused. The right question about a much-criticized feature is not whether to forbid it but whether the language offers alternatives convenient enough that nobody reaches for it. If the alternatives are genuinely better, the feature falls out of use on its own; if they are not, forbidding it produces circumlocution and no gain in clarity.

The rule transfers directly to the smaller design decisions a working programmer makes. Banning a pattern in a style guide, hiding a capability behind a warning, or removing an escape hatch from a library will not stop the need that motivated it; it will relocate the need somewhere less visible, usually as a workaround nobody reviews. Discipline imposed by subtraction is weak because it constrains vocabulary rather than thought. Discipline that comes from a construct so well-fitted that the alternative feels clumsy is strong, because it works with the programmer's judgement instead of against it. Do the harder thing: build the good alternative first, and let the bad practice lose on the merits.

**Source:** [Lambda: The Ultimate Imperative](../works/lambda-the-ultimate-imperative.md) — the conclusions, which argue that any language with the listed features can simulate the supposedly banned constructs straightforwardly, that badly organized programs reflect badly organized conceptions no language design can fix, and that effort should go to discovering helpful constructs rather than eliminating bad ones; plus the note tracing the goto controversy's aftermath, where languages designed without jumps acquired successive escape features as compensation, and reframing Knuth's question as whether a future language will make the construct unnecessary rather than whether it will forbid it.
