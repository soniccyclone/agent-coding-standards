---
type: lesson
title: "Define correctness against the inputs that actually occur, and buy the remaining accuracy with runtime"
figure: valiant
works: [a-theory-of-the-learnable]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Define correctness against the inputs that actually occur, and buy the remaining accuracy with runtime

**Lesson:** Demanding that an artifact agree with its specification on every conceivable input is often the reason no feasible artifact exists. The productive weakening is not to lower the bar vaguely but to move it onto a distribution: fix whatever probability law governs which inputs arrive in practice, leave that law entirely unknown and unconstrained, and require only that the total probability mass on which the artifact disagrees stay below a bound the user chooses. The bound then becomes a parameter, and the cost of meeting it enters the running time — tighten the requirement and you pay for it in work performed, on a schedule you can compute in advance. A specification with a knob on it is a very different object from one without: it converts an all-or-nothing feasibility question into an engineering trade you can actually sit on either side of.

Two properties make this respectable rather than a dodge. First, the distribution must be arbitrary and unmodelled — the guarantee holds whatever nature is doing — because the moment you assume a convenient distribution you are proving something about your assumption instead of about the world. What you are entitled to assume is only that the same law generates the samples you learn from and the cases you will later face. Second, the error should be one-sided wherever the problem permits: arrange that the artifact never asserts something false, only that it sometimes fails to assert something true. Asymmetric error is far easier to compose and to reason about downstream, because a caller can trust every positive answer unconditionally and needs to hedge only against silence.

The stance has a consequence worth sitting with. If agreement is only ever required on inputs that occur, then behavior on inputs that never occur has no content at all — two artifacts that differ wildly on the unreachable part of the space are, for every purpose that matters, the same artifact. Arguments constructed out of hypothetical situations the system will never encounter are then not merely low-priority; they are arguments about nothing. This is a sharp filter to apply to design debate: before spending effort on a discrepancy, ask what probability mass sits under it.

**Source:** [A Theory of the Learnable](../works/a-theory-of-the-learnable.md) — the definition of learnability in section 3, where the adjustable parameter governs both the failure probability and the permitted error mass under an arbitrary distribution, the remark there on one-sided versus two-sided error, and the closing discussion of agreement on natural inputs and the emptiness of reasoning about unnatural ones.
