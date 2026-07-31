---
type: lesson
title: "A self-referential definition means something only if it commits to an observable step before referring to itself"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# A self-referential definition means something only if it commits to an observable step before referring to itself

**Lesson:** Defining something by an equation that mentions it on both sides is a legitimate and powerful move — it is how you describe behaviour that continues indefinitely without deciding in advance how long it lasts. But it carries a condition that is easy to state and easy to forget: every occurrence of the thing being defined must sit behind at least one committed step. An equation that equates a name with itself, or with something that reaches the recursive occurrence without doing anything first, does not define one thing badly; it defines nothing, because everything satisfies it. The syntactic check is simple enough to apply mechanically, and it is worth applying mechanically, because the failure mode is not an error message but a definition that appears to say something and does not.

The reason the condition works is worth understanding rather than memorizing. When a step must be taken before the recursion is reached, repeated unfolding produces longer and longer descriptions that agree with each other as far as they go, and the object being defined is the limit of that sequence — the same way a real number is pinned down by an unending decimal expansion in which each further digit is forced. Every unfolding is progress that cannot be undone, so successive approximations never contradict one another, and there is exactly one thing they all approximate. Remove the forced step and the unfoldings make no progress, the sequence never narrows, and uniqueness evaporates along with meaning.

Read as a design rule, this says: whenever something is defined in terms of itself, identify the step that guarantees progress and make it explicit. Recursive grammars must consume input before recursing; retry logic must record an attempt before retrying; a rule expressed in terms of itself must reduce something measurable. And note what you get in exchange for the discipline: with progress guaranteed, an implicit definition is as good as an explicit one, and reasoning about it becomes substitution of equals for equals — you may unfold it as many times as an argument requires, and the further unfolding remains available. That is a remarkably cheap way to reason about unbounded behaviour, and it is available only under the guarantee.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the recursion section of the chapter on processes, which derives a clock's defining equation from the observation that a clock preceded by one further tick is indistinguishable from the clock, unfolds it by substituting equals for equals to obtain arbitrarily long behaviours, likens the result to defining a root by the equation it satisfies and to the limit of a decimal expansion, and requires that recursive definitions be guarded — every recursive occurrence prefixed by at least one event — noting that an equation of a name with itself defines nothing because everything solves it, while a guarded equation has a unique solution over a given alphabet.
