---
type: lesson
title: "Put a number on how much extra you would pay for uniformity, so the trade stops being a matter of taste"
figure: wilkes
works: [best-way-to-design-an-automatic-calculating-machine]
axes: [cognitive-load, hardware-affinity, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Put a number on how much extra you would pay for uniformity, so the trade stops being a matter of taste

**Lesson:** Nearly everyone prefers a design built from repeated identical parts over one built from an equal number of different parts; the preference is cheap because nothing is being given up. The interesting question begins where the uniform version is *larger*: how many copies of one standard part would you accept in place of a given number of bespoke parts? Turning the preference into a ratio — the multiple of total material you are willing to spend to make everything the same — converts an aesthetic instinct into a claim someone can dispute, price out, and check against the finished artifact.

Committing to a specific figure, and to the scale at which it applies, is what makes the claim real. A ratio well above one says out loud that regularity is not a tidiness bonus but a primary objective worth substantial waste, and it forces the designer to notice when a proposed non-uniform optimization is asking for more than the stated budget. Naming the scale matters just as much, because the answer is not scale-free: what you would pay for uniformity across a handful of parts is not what you would pay across a whole system's worth of them, and a ratio stated without its context is not a usable rule.

The general move is to take every "obviously preferable, other things being equal" instinct in your design vocabulary and ask what it is worth when other things are *not* equal. Instincts that survive that question become engineering constraints. Instincts that cannot be priced at all were never doing any work; they were vocabulary for approving decisions already taken on other grounds.

**Source:** [The Best Way to Design an Automatic Calculating Machine](../works/best-way-to-design-an-automatic-calculating-machine.md) — the passage on degree of repetition, which sets up the comparison between a group of distinct units and a larger group of identical ones, conjectures a specific lower bound on the acceptable multiple, and states the machine scale the conjecture is meant for.
