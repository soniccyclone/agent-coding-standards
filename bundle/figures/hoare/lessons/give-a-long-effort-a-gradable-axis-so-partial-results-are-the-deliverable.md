---
type: lesson
title: "Give a long effort a gradable axis, so partial results are the deliverable and not consolation"
figure: hoare
works: [the-verifying-compiler-a-grand-challenge-for-computing-research]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Give a long effort a gradable axis, so partial results are the deliverable and not consolation

**Lesson:** An objective stated as a single binary — the thing works or it does not — is unmanageable over any horizon longer than a few months, because for almost the entire duration the only honest status report is "not yet." The fix is not to lower the ambition but to decompose the goal along axes that admit degrees, so that at any moment the state of the work is a coordinate rather than a verdict. Two independent axes do more work here than one long list of milestones: how much has been said about the artifact, and how strongly what was said has been established. A component can carry nothing, or a claim about its structural well-formedness, or a partial description of its behavior, or a complete one; and each of those claims can rest on nothing but testing, on a human argument, on a machine-assisted argument, or on a fully mechanical one. Every unit of work moves something along one of those axes, and the position is legible to someone outside the project.

Grading this way changes what "failure" means. If the top-right corner is never reached, the effort still leaves behind a large body of artifacts annotated with what they are supposed to do and checked to some stated degree, which is worth having on its own terms. That is a design requirement on the plan, not a comforting afterthought: structure the work so that the intermediate states are independently useful, and you have removed most of the risk of a long bet without shortening it. A plan whose value is concentrated entirely at the finish line is a plan that will be cancelled before the finish line.

The same decomposition solves the coordination problem for free. Because the axes are orthogonal and the artifacts are separable, independent groups can work on describing components, on the checking machinery, and on the underlying reasoning engines without a central schedule, and their outputs meet later. It also makes competition legible — with a shared measure, rival efforts can be compared rather than merely advocated for. A goal you cannot grade is a goal you cannot parcel out, and a goal you cannot parcel out will only ever be as large as one team.

**Source:** [The Verifying Compiler: A Grand Challenge for Computing Research](../works/the-verifying-compiler-a-grand-challenge-for-computing-research.md) — the Incremental, Useful, Cooperative and Competitive criteria, which define separate scales for level of annotation and level of verification, require that partial work bring benefit even if the whole project fails, and use the shared scales to parcel work out and to compare rival teams.
