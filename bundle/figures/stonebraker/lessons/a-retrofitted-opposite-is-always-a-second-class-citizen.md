---
type: lesson
title: "A retrofitted opposite is always a second-class citizen"
figure: stonebraker
works: [one-size-fits-all]
axes: [expressiveness, hardware-affinity]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A retrofitted opposite is always a second-class citizen

Some design decisions are not features but polarities: the system commits to a direction of flow, and everything above that commitment is shaped by it. A store-then-ask engine puts durability first and treats a question as something that arrives later, against settled state. An ask-then-let-it-flow engine puts the question first and treats each arriving item as something that must find its way through standing interrogation. Both are coherent. Neither can be turned into the other by adding a feature, because the polarity is not a component you can swap — it is the assumption the scheduler, the cost model, the recovery story, and the programming interface were all built on top of.

This is why the compatibility features that promise the missing direction stay stunted for decades. Bolting reactive rules onto a store-first engine produces something hedged with arbitrary limits, invisible to the tooling that manages everything else, unsupported by the abstraction machinery the native constructs enjoy, and slow enough that the workaround loses to a purpose-built engine by two orders of magnitude. That is not an implementation failure to be fixed in the next release. It is the predictable result of asking a foundation to serve a load it was oriented against. The tell is always the same: the retrofitted mechanism cannot participate in the system's own abstractions.

The programmer who believes this changes what they audit first. Before comparing feature checklists, they identify the polarity — which direction does the data actually move, and which side of the arrow is the thing being stored? — and check whether it matches the problem. If it does not, the honest options are to build on a foundation with the right orientation or to accept the constant-factor penalty knowingly, not to hunt for the extension that will finally make the wrong polarity behave. It also changes how they judge their own work: when a request keeps forcing them to write the mechanism that runs against the grain, the request is telling them the grain is wrong, and no amount of local cleverness converts that signal into a fix.

**Source:** ["One Size Fits All": An Idea Whose Time Has Come and Gone](../works/one-size-fits-all.md) — the argument distinguishing outbound from inbound processing models, and its assessment of why the trigger mechanism grafted onto conventional engines never became a real substitute for a natively push-oriented one.
