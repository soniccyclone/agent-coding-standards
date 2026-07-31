---
type: lesson
title: "The decisions that actually decide performance are only visible once the detail is stripped away"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# The decisions that actually decide performance are only visible once the detail is stripped away

**Lesson:** Abstraction and speed are usually presented as opponents: you work in clean high-level terms and pay for it, or you get close to the machine and give up the clarity. That framing survives because it is true of one narrow activity — squeezing a finished system — and false of the activity that determines the outcome. The changes available at the end are marginal by construction: the structure is fixed, so all that is left is local trickery. The changes that decide whether a system is fast were made much earlier and are structural, and they are choices you can only see if you are looking at something small enough to hold in your head.

That is the whole argument, and it inverts the usual conclusion. What makes a high-level decision visible is the absence of detail. A description in terms of what information is held and what operations act on it lets you see the entire operation set at once, ask which are frequent, and compare candidate structures against that profile — an exercise which is a page of thinking and which decides orders of magnitude. The same problem described at implementation level is too large to survey, so the structural question never gets asked at all; you optimize what is in front of you, and what is in front of you is the consequence of a decision nobody consciously made.

The pleasing part is that this is the same property, not a second one. Removing detail is what makes an argument about correctness tractable, and it is what makes the performance question tractable, for the identical reason: both are questions about the whole, and you cannot reason about a whole you cannot see. So the abstraction you introduced to be able to check the design is the instrument that also lets you choose the representation — and it is precisely in data structure design, where the range of possible representations of the same abstract content is widest, that the payoff is largest.

The practical instruction: when a system is too slow, resist the reflex to profile-and-patch as the first move. Ask instead whether you can state, in a paragraph free of implementation detail, what the system holds and what it does to it. If you can, the structural options usually become obvious and one of them is worth more than every local fix combined. If you cannot, that inability is the finding — you have no vantage point from which the important decisions are even visible, and acquiring one is the work.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 17's introductory argument that, apart from greater accuracy, implementations with better performance are created by a rigorous design method: the observation that a completed system's performance can be improved only marginally by tricky techniques while the really important performance decisions lie at a much higher level, the claim that bringing those decisions within intellectual grasp requires shearing them of detail, the conclusion that precisely the use of abstractions which makes proofs manageable is what makes performance questions handleable, and the note that this holds particularly in data structure design because of the wide range of possible representations of an abstract data type. Chapter 11's opening remark that separating the decisions is likely to increase the efficiency of the final program, for the same reason, states the same claim from the development-process side.
