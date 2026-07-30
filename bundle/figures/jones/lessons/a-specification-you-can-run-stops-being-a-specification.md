---
type: lesson
title: "A specification you can run stops being a specification"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A specification you can run stops being a specification

**Lesson:** Once a specification is written precisely enough, someone will notice it could be executed, and building the machinery to do so looks like pure gain. It is not. A specification earns its power by being allowed to say what must be true without saying how, which routinely means describing an outcome by a property that no sane implementation would compute the way the description reads. Make execution the goal and that freedom quietly disappears: the description drifts toward things that run acceptably, then toward things that run well, and what you have is a slow implementation with a misleading name. No amount of cleverness in choosing representations turns a description phrased for clarity into a viable implementation, and the attempt corrupts the description long before it produces a usable program.

The deeper cost is to the reader. A specification's job is to be a model you think in — the thing you argue about, the thing you check a design against, the thing whose statements you can hold in mind. Executability pulls the artifact toward being a program, and programs are not thinking models; they are optimized for a machine's needs. When the same file is meant to serve both purposes, the machine's needs win, because they are the ones that produce visible failures.

The same discipline applies to tooling built around any rigorous practice. Useful support is a collection of things you can invoke — check the syntax, check the types, find where this is used, apply a substitution, instantiate the relevant obligations, trace what a change affects, help accumulate the reusable results — rather than an environment that owns the process and dictates the form of what you write. Tools that assist are adopted; tools that take control get worked around, and the workarounds distort the practice they were meant to support. The rigid notation any tool needs is itself a cost to be paid deliberately, not a benefit.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the bringing-into-practice section of the conclusions, which states that the temptation to provide a system for executing specifications should be resisted because it leads users away from the proper goal of a specification as an abstract thinking model, lists the support functions that would be worthwhile instead, and argues for a series of invokable functions rather than a controlling environment; together with the alternatives section of the data-refinement chapter, which calls the interpretation of model-oriented specifications as very-high-level implementations dangerous and notes that no clever choice of representation would make one of its own set-based specifications efficient.
