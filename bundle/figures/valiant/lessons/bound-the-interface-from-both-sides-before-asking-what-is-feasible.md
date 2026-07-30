---
type: lesson
title: "Fix the information channel before asking what is achievable, and bound its power from both sides"
figure: valiant
works: [a-theory-of-the-learnable]
axes: [expressiveness, primitive-count]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Fix the information channel before asking what is achievable, and bound its power from both sides

**Lesson:** Questions of the form "can a system acquire X on its own" are unanswerable until you pin down exactly what it is allowed to receive from outside. The method is to specify the channel first — the precise set of calls the system may make to its environment and what each returns — and only then ask which targets are reachable through that channel within a resource bound. The channel is the real design object; the feasibility result is downstream of it. This reorders the usual investigation, in which people argue about what a mechanism can do while the assumptions about its inputs stay implicit and keep shifting under the argument.

The interesting part is that the channel has to be squeezed from both directions, and both failures look like success at first glance. Give the supplying side too much power and the answer gets smuggled across: if the environment can hand over a premeditated sequence of inputs rather than samples it does not control, two distinguishable messages are enough to encode an arbitrary program in binary, and the system has been programmed while everyone congratulates it on having figured things out. Give the supplying side too little and the target becomes findable only by exhaustive search, so the negative result you prove is about your own impoverished interface rather than about the problem. A channel worth studying sits in the band between smuggling and starvation, and locating that band is most of the intellectual work.

Once the channel is explicit it becomes a dial rather than a fixture, and comparing settings is where the structure shows up. Different targets need different channels: some classes fall out from passive samples alone with no questions asked; others need the ability to pose constructed queries the samples would never have supplied; the strongest need queries so pointed that whether they are legitimate at all becomes debatable. Reading a result therefore means reading its channel — a capability that is cheap under one interface and impossible under another has told you where the difficulty really lives, and the boundary between reasonable and unreasonable interfaces is a genuine open question rather than a technicality to wave through.

**Source:** [A Theory of the Learnable](../works/a-theory-of-the-learnable.md) — section 2, which motivates the choice of protocol by rejecting both a teacher powerful enough to encode a program in a sequence of examples and a protocol too weak to avoid exponential search, and the later sections where progressively stronger oracles are traded against the classes they render deducible.
