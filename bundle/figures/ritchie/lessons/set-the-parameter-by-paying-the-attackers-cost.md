---
type: lesson
title: "Set a defensive parameter by paying the attacker's cost yourself, not by arguing about it"
figure: ritchie
works: [on-the-security-of-unix]
axes: [verifiability, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, algorithms-and-complexity]
tags: [lesson]
---
# Set a defensive parameter by paying the attacker's cost yourself, not by arguing about it

When Ritchie reaches the question of how long and how varied a password should be, he does not reason about it. He gathers a real sample of stored credentials from a spread of installations, runs the search an opponent would run — short combinations, then the contents of a large dictionary — records how many fall and how much machine time it took, and reads the recommendation off the result. The parameter is chosen because the experiment showed where the search became unaffordable on the hardware of the day, not because a number felt prudent.

Why this is the right shape of reasoning: a defence built on computational cost is a claim about an adversary's budget, and budgets are measurable quantities, not matters of opinion. Arguing about whether some length is "enough" substitutes intuition for an experiment that is usually cheaper to run than the argument is to settle. Running it also converts a vague worry into two hard numbers — the fraction of secrets that fell and the time it consumed — and only those numbers can tell you which direction to move the parameter, or that moving it will not help. Ritchie's framing is careful in a way that matters here: he says the scheme appears reasonably secure provided its limitations are understood, and then makes the limitation concrete by exercising it. Understanding a limitation means knowing its price.

The measurement also has a boundary he marks explicitly. Immediately after reporting it he describes a way to obtain a secret that ignores the mathematics entirely: imitate the login prompt and collect what a user types. The cost of the cryptanalytic path constrains one route only; a cheaper non-computational route can sit beside it and make the whole calculation moot. So an empirical result licences a parameter, never a conclusion about the system.

A programmer who believes this treats any security constant — key size, iteration count, rate limit, token length — as an unfinished measurement rather than a value inherited from custom, and re-runs it as hardware changes, since the number that justified the choice is a hardware-relative one. They also state what the measurement does not cover, so nobody mistakes a well-calibrated cost for an absent path around it.

**Source:** [On the Security of UNIX](../works/on-the-security-of-unix.md) — the password-security discussion, in which a cracking experiment against a collected sample of real encrypted passwords yields the length and alphabet recommendation, followed immediately by the non-cryptanalytic prompt-imitation attack.
