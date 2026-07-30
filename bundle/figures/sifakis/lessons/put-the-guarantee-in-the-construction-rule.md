---
type: lesson
title: "Heavy reliance on after-the-fact checking is a symptom of a discipline that lacks construction rules"
figure: sifakis
works: [turing-lecture-2009]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Heavy reliance on after-the-fact checking is a symptom of a discipline that lacks construction rules

**Lesson:** Older engineering fields do not build an artifact and then investigate whether it works. They have laws that constrain how parts may be combined, and an engineer who respects those constraints gets predictable behavior as a consequence of the combining rules, with measurement as confirmation rather than as the source of belief. That computing leans as hard as it does on inspecting finished artifacts is a statement about the immaturity of its composition theory, not a permanent feature of software. The goal is to convert what is currently learned by checking into rules about how components may be assembled.

The bridge between the two is narrower than it looks. Once you have an argument that a particular property holds whenever components with certain local guarantees are wired in a certain shape, you can read that argument in either direction: as a check to run on an existing system, or as a constraint to obey while building one. Read the second way, it is a correct-by-construction rule, and it costs nothing at analysis time because the artifact was never allowed into the bad region. Nor is this all-or-nothing — there is a wide space between fully constructive design and pure after-the-fact checking, and most real systems will live somewhere in it, with some properties guaranteed structurally and others still checked.

The reframe that comes with this is that being checkable is a design property you can aim at, exactly as testability is. Design decisions can be evaluated by whether they keep the system inside the region where your analyses stay cheap, and an architecture that lands outside it has imposed a recurring verification cost that no tool improvement will refund. Practitioners already do half of this instinctively when they apply architectural patterns that are known to work; the missing step is making those patterns carry stated guarantees rather than folklore.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/turing-lecture-2009.md) — Sifakis's section on moving from a posteriori verification to constructivity, the comparison to disciplines with predictive laws, and his proposal to identify verifiability conditions and turn compositionality rules into correct-by-construction techniques.
