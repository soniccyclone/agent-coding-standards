---
type: lesson
title: "Make every surprise consume a bounded budget, and a counting argument finishes the proof"
figure: valiant
works: [a-theory-of-the-learnable]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Make every surprise consume a bounded budget, and a counting argument finishes the proof

**Lesson:** The hard part of any procedure that refines a guess against incoming evidence is showing it converges. The reliable way to get that is structural: arrange the state so that any observation which is *not* already consistent with the current guess forces an irreversible change, and so that the number of such changes possible in total is bounded by the size of the representation. Then the procedure has a budget of surprises. Either it stops being surprised — which is exactly the statement that the guess now covers what arrives — or it burns through the budget, and the budget is finite. Nothing about the order of observations, or about which ones arrive, enters the argument.

Once that structure is in place the convergence proof is a counting exercise rather than an analysis. Running long enough gives you many independent trials; each trial either falls in the already-covered region or triggers a budget-consuming step; and failing to converge means having made many trials while consuming few budget units, which is precisely the event a repeated-trial tail bound says is unlikely. The whole probabilistic content collapses into one reusable lemma about how many trials are needed before rare events stop being missed, provable once and applied everywhere. This is the right way to organize such a result: isolate the sampling argument into a standalone bound with no reference to the problem domain, so that each application only has to exhibit its budget and its progress measure.

Notice that the same skeleton supports opposite-looking strategies. You can start maximally restrictive — assume every possible constraint holds — and delete constraints as evidence contradicts them; or start maximally permissive and add covering cases as evidence demands. In one the guess grows toward the target from below, in the other it shrinks toward it from above, but both work for the identical reason, and both are safe in the same one-sided way: everything the current guess asserts remains sound at every intermediate step, so a run stopped early is degraded rather than wrong. When choosing between the two, the deciding question is not elegance but which direction gives you the smaller budget and the cheaper consistency test.

**Source:** [A Theory of the Learnable](../works/a-theory-of-the-learnable.md) — the combinatorial bound isolated in section 4 with its urn illustration, and its two applications: the section 5 procedure that initializes with every short clause and deletes those contradicted by examples, and the section 6 procedure that starts from nothing and adds one new term per uncovered example, each bounded by the number of clauses or terms available.
