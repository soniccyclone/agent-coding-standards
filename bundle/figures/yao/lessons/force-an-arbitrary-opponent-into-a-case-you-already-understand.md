---
type: lesson
title: "You cannot analyze an arbitrary implementation, so force it onto inputs where it must behave uniformly"
figure: yao
works: [should-tables-be-sorted]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# You cannot analyze an arbitrary implementation, so force it onto inputs where it must behave uniformly

**Lesson:** Claims of the form "no scheme can do better" are hard because the quantifier ranges over schemes nobody has thought of, and an unthought-of scheme has no structure to attack. The way through is not to reason about the arbitrary scheme at all. Instead, prove the bound once for a single well-behaved family — one whose layout is fixed and predictable — and then show that any scheme whatever, however inventive, is *forced* to look like a member of that family somewhere. The bound then transfers, because a scheme that is inventive on most inputs and conventional on a few is still beaten on the few.

The mechanism is a coloring argument. Enumerate the finitely many behaviors the scheme could exhibit on an input of a given size — for a storage layout, which slot each rank of item lands in, and which slots hold bookkeeping rather than items — and treat each behavior as a color painted on that input. There are only finitely many colors, so if the space of possible inputs is large enough, some sizeable region of it must be painted a single color: on every input drawn from that region, the scheme commits to exactly one behavior. Inside the region the scheme is no longer arbitrary; it is a fixed layout, and a fixed layout is something you can run an adversary against. Two details make it work. The known bound must be robust to relabeling, so that "one fixed behavior" is as good as "the conventional behavior" — if the bound only held for the canonical arrangement and not for every renaming of it, the monochromatic region would be worthless. And the region must be big enough to contain a hard instance, which is why the argument needs a region roughly twice the working size rather than merely one instance's worth.

The transferable habit is to stop trying to bound cleverness directly. Cleverness has to be expressed as a finite choice at some point — a layout, a schedule, a dispatch decision, an encoding — and once you name the choice space, the pigeonhole does the work of ruling out all the strategies you never imagined. The cost is honesty about the price: this style of argument needs the input space to be enormous before the uniform region appears, so it tells you the bound is real without telling you it bites at any size you will meet. That is a separate question, and conflating the two is how a correct impossibility proof gets misread as practical advice.

**Source:** [Should Tables Be Sorted?](../works/should-tables-be-sorted.md) — the proof of the main optimality theorem, which first establishes the bound by adversary induction for layouts that follow any fixed permutation, then partitions all item-subsets by the permutation the arbitrary layout imposes on them and applies Ramsey's theorem to extract a subspace on which that permutation is constant; and the generalized restatement, where the colors additionally record which cells hold pointers.
