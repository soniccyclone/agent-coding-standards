---
type: lesson
title: "A guarantee that only switches on past every real input is not an answer yet — invert it into a reach question"
figure: yao
works: [should-tables-be-sorted]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# A guarantee that only switches on past every real input is not an answer yet — invert it into a reach question

**Lesson:** Results with the shape "for all sizes above some threshold, X holds" are only as useful as the threshold. When the threshold is derived from a combinatorial existence argument it can be astronomically larger than anything that will ever be built, and then the statement is true, important, and irrelevant to any decision — it tells you the shape of the truth without telling you whether the truth applies to you. The failure mode is to report the theorem and stop, letting readers assume the qualifier is a formality. The productive move is to treat the huge threshold as evidence that the question was posed in the direction that hides the interesting information, and to flip it.

The flip is mechanical. A statement parameterized as "above this size, you need at least this much work" inverts into "given a work budget, how large an input can you still handle" — same content, but now the unknown is the reach of the cheap scheme rather than the onset of the expensive regime. This reframing pays three ways. It is answerable in special cases even when the general form is not, so you get exact facts about small budgets instead of asymptotics about unreachable sizes. It puts the practically decisive number in the position of the thing being solved for. And it makes the endpoints of your knowledge visible, so a gap in the middle of the parameter range reads as an open problem rather than being papered over by a theorem whose qualifier nobody checks.

The same alertness applies to counterexamples, which have thresholds too. If a clever scheme beats the conventional one on some tiny instance, the finding is not that the convention is wrong; the finding is that a boundary exists, and the useful work is locating it. Push the parameter up by one and check whether the cleverness survives. Frequently it dies immediately, and then you have learned two things at once — the conventional scheme is optimal from that point on, and the tiny case was a degeneracy rather than a hint. Reporting the counterexample without the boundary, or suppressing it because it looks like noise, both throw away the information. Every claim with a qualifier in it is really a claim about where the qualifier's boundary sits, and the boundary is the part that has consequences.

**Source:** [Should Tables Be Sorted?](../works/should-tables-be-sorted.md) — the section opening that notes the thresholds produced by the Ramsey argument are enormous even for moderate collection sizes, declares the result therefore of little practical use, and recasts the question as the maximum value-space size for which a given probe budget suffices, solving it exactly for a budget of one; together with the earlier treatment of the small cyclic arrangement that beats a sorted table at the smallest nondegenerate size and is shown to stop working one step later.
