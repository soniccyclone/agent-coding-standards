---
type: lesson
title: "Climbing a hierarchy buys simplicity, never power — so say convenience and mean it"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [cognitive-load, expressiveness, primitive-count]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Climbing a hierarchy buys simplicity, never power — so say convenience and mean it

Designers are embarrassed to justify a placement decision by saying a facility belongs at some level because it is convenient there. It sounds unrigorous, so they reach for language suggesting the higher level can do things the lower one could not. Parnas argues the embarrassment is misplaced and the substitute is false. Assume the bare machine can already perform everything the system will ever need to perform — it must, since everything above it is built from it. Then going up the structure cannot add capability. It can only spend it: resources get consumed by the levels below, so strictly speaking capability is lost on the way up. What the upper levels supply is that new functions can be written as much shorter, much simpler programs, because more is already available to lean on.

Once that is admitted, level assignment gets a real criterion instead of a vague sense of altitude. For each function, find the lowest level at which the facilities that make it simple to write are already present, and put it there. The test that you have gone too low is concrete rather than aesthetic: if you implement it a level down, you will find yourself writing code that duplicates what the next level up was about to provide. Duplication is the symptom of misplacement, not an unavoidable cost of layering. And the test that you have gone too high is equally concrete: look at the next level up and check whether anything there would have helped. If nothing would, you are at the right height.

The word matters because it keeps a fact visible that grander language hides — every one of these placements was optional. Any function could have been written lower down at greater cost in program complexity, which means each level in the structure is a deliberate purchase of simplicity paid for in resources and in ordering constraints, not a discovery about what is possible. A designer who talks this way can be asked what each level bought and answer; a designer who talks about levels of abstraction as if they conferred new powers has no way to price anything, and tends to end up with strata that exist because the diagram wanted them.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — the subsection defending the use of the word "convenience," including the assumption that the hardware can perform all necessary functions, the observation that capability is lost rather than gained going up, and the rule of assigning each function to the lowest level whose available programs make it simple.
