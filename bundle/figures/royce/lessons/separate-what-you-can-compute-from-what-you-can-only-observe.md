---
type: lesson
title: "Separate what you can compute from what you can only observe"
figure: royce
works: [managing-the-development-of-large-software-systems]
axes: [verifiability, hardware-affinity]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Separate what you can compute from what you can only observe

**Lesson:** Royce splits a system's properties into two epistemic classes and organizes his whole argument around the split. Some properties yield to analysis in advance: the orbital mechanics, the attitude determination, the payload optimization, work that occupies entire departments on paper and then reduces to a few lines of arithmetic in the program. Others do not yield to analysis at all. How long the thing actually takes, how much memory it actually occupies, what the input/output channels actually sustain: none of these are the solution to an equation you can write down beforehand. They are found by running the artifact and watching. The consequence is unforgiving. Whatever moment holds the first real execution is the moment you learn whether the design was feasible, and everything scheduled before that moment was built on an unchecked assumption.

That reframes the risk in a project from "did we reason correctly" to "when do we first get to look." A programmer who takes the split seriously stops treating first execution as a downstream milestone and treats it as the point of maximum information gain, then drags it as early in the work as physical possibility allows. Royce's remedy is to build the system twice on purpose: a small version, scoped to the parts nobody can reason about confidently, produced on a fraction of the schedule and expected to be thrown away. The disposable version is not a rehearsal for the real one, it is an instrument. Its only job is to convert a quantity that was a matter of opinion into a number, while there is still time to act on the number.

He is also specific about why careful thinking cannot substitute for the measurement. Estimates of resource consumption are not merely uncertain, they are biased, and biased in a known direction: reliably optimistic, in the same family as guesses about takeoff weight or cost to complete. Uncertainty with a direction does not wash out by being conscientious about it. Only an observation corrects it, which is why the argument lands on building an experiment rather than on estimating more rigorously.

The practical discipline is to sort every load-bearing assumption in a design into derivable or observable, and for each observable one, name the cheapest artifact that would produce the observation and the earliest date it could exist. Assumptions that stay in the observable column without a scheduled observation are the ones that will move the whole project backward when they finally break.

**Source:** [Managing the Development of Large Software Systems](../works/managing-the-development-of-large-software-systems.md) — the argument for why the naive phase sequence invites failure (timing, storage and transfer behavior being experienced rather than analyzed), together with the "do it twice" corrective and its remarks on the optimism of unaided human judgment.
