---
type: lesson
title: "One pass against the settled state erases the order things arrived in"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# One pass against the settled state erases the order things arrived in

**Lesson:** An online procedure that decides each item against state the item then modifies produces a result that is a function of the input *and its order*. This is rarely intended and is almost never stated. The items processed first were judged against immature state and may be sitting where nothing would put them now; the items processed last were judged against nearly final state and are fine. Nothing distinguishes the two in the output. The cheap and complete remedy is a single extra pass: pin the state at its final value, re-evaluate every item against it, and take the result. The output then depends only on the settled state, which depends on the whole input, so the order in which the input arrived has been divided out.

The economics of that pass are what make it worth arguing for. It costs one sweep, it requires no new machinery — it reuses the same assignment rule the online pass used — and in the overwhelming majority of runs almost nothing changes, because the state moves little once most of the input is in. A step that is cheap, reuses existing code, and is usually a no-op is precisely the profile of a check you should run unconditionally rather than treat as optional. The temptation is to skip it on the grounds that the disagreements are rare; rarity is an argument for it being cheap, not for it being unnecessary, and the rare cases are the ones you would otherwise never find.

The pass also hands you a free diagnostic that nothing else in the procedure provides. Count how many items land somewhere different the second time. A small count says the online run was stable and the state converged early. A large count says the state moved substantially while decisions were being made, which means the online result was substantially an artefact of ordering, and it is a warning worth surfacing even though the corrected output is fine. That number costs nothing to compute and tells you something about the run that no measure of the final state can.

The general shape to look for: any incremental process where a decision consults a value that the decision then changes. Assignment to a group whose centre moves, admission against a budget that the admission consumes, matching against a set the match mutates, caching decisions made against a hit-rate that the caching alters. In all of them the first decisions are made under different conditions from the last, and a re-evaluation against the converged conditions is the difference between a result you can reproduce and a result that depends on which file the loader happened to read first.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 7's outline of the k-means family, which notes that a cluster's centroid migrates as points are assigned to it, and describes as an optional final step fixing the centroids and reassigning every point including the initial k, observing that a point whose original cluster's centroid has since moved far away can end up in a different cluster on the second pass.
