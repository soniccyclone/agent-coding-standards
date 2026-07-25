---
type: lesson
title: "When your understanding of the problem compresses, rewrite the artifact to match"
figure: chaitin
works: [meta-math-the-quest-for-omega]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# When your understanding of the problem compresses, rewrite the artifact to match

**Lesson:** Chaitin's rule for his own long-running project was to rewrite the code from scratch each time his understanding of the problem advanced. The justification is the compression thesis applied to the artifact rather than to the domain. If a program is a compact statement of the structure of a problem, then a program that grew by patching is a statement of a structure you no longer believe, with the superseded model still load-bearing underneath and the new understanding layered on top as corrections. The size grows while the understanding shrinks, which is the wrong direction on both counts.

He notes that accretion is the normal outcome when rewriting is impossible. Inherited biological code keeps ancient subroutines and re-runs its own history during development because too much is built on top of it to start over, and human codebases behave the same way for the same reason. That is a description of a constraint, not an endorsement. The distinguishing feature of software is that the option to start over sometimes exists, and the moment it is most valuable is the moment your model of the problem got simpler, because that is exactly when the existing artifact encodes the largest amount of obsolete theory.

The test he applies is conceptual integrity: can you state the single idea the code embodies, and does the code look like that statement? A codebase where the answer is no has stopped being a compression of the problem and become a record of the path taken to understand it. Those are both useful artifacts, but only one of them should be the thing you maintain. In practice this means treating a genuine simplification of your model as an event that triggers work, not as a satisfying thought to be noted and deferred.

**Source:** [Meta Math! The Quest for Omega](../works/meta-math-the-quest-for-omega.md) - the concluding chapter, where he describes rewriting his own code from scratch at each advance in understanding, refusing ad hoc code, and naming faithfulness to a single idea as what matters most in a design. The contrast with accretion is drawn in the earlier chapter comparing inherited biological code to long-lived software.
