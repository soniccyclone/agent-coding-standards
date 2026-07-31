---
type: lesson
title: "Most obligations are vacuous, which is exactly what makes checking every one of them affordable"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Most obligations are vacuous, which is exactly what makes checking every one of them affordable

**Lesson:** People resist systematic checking because they picture the worst case: every item requiring real work, multiplied by the number of items, multiplied by the number of steps. That picture is wrong about the distribution. In practice the great majority of the things you are obliged to check are settled the instant you look at them — the assumption you have to establish is one that nothing constrains, so the requirement is satisfied trivially and there is literally nothing to write. A handful of items in a whole development need actual thought, and one or two need a real argument. The cost of a complete pass is dominated by the few hard cases, not by the count.

That distribution is what converts a formal system into something usable, and the conversion is worth naming as a technique rather than a compromise. Derive, once and carefully, the exhaustive list of what must hold for each way of putting pieces together. Then, thereafter, do not prove — *scan*. The list becomes a checklist that reminds you of the failure modes of each construct, and you go down it noting which items are immediate and stopping only where one is not. What you have bought is coverage: you know the enumeration is complete because it was derived rather than remembered, so nothing can be forgotten, which is the actual failure mode of experienced people. What you have not paid for is proof, because you only pay where the check resists.

Two conditions make this honest rather than self-deception, and both matter. The list must have been derived from something — a real account of what the constructs mean — rather than assembled from experience, or it is just a code review with pretensions and will have holes exactly where your intuitions do. And the scanner must know what the full argument would look like for each item, because that knowledge is what lets them recognise a case that is not immediate. Someone applying the checklist without that background will wave through the interesting ones, which are the only ones that were ever going to be wrong.

The residue is the payoff. When a scan stalls, you have localized the difficulty to a single named item of a single step, and it is completely clear what a full argument for that one item would have to establish. That is a much better position than a general uneasiness about whether the design is right, and it is reached without having formalized anything you did not need to.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 5's framing of its lists of properties for programming constructs as checklists reminding the programmer of potential errors, with only particularly difficult items proved formally; the worked sequential-composition example in which the domain rules come out vacuously true because the component operations are total and are therefore stated to require no proof, and the associated convention of marking a condition "immediate" when it follows from arithmetic alone; the remark following the multiplication development that the recorded arguments are no more than notes towards a proof but that, because a standard list of properties is being used, what is recorded is an adequate basis for constructing a more formal proof and it is clear what must be done if a step is called into doubt; and the note that the rules were themselves justified against a definition of the language given in the appendices rather than asserted.
