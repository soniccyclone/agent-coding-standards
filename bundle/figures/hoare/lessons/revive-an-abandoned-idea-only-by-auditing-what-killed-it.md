---
type: lesson
title: "Revive an abandoned idea only when you can name what killed it and show each cause is gone"
figure: hoare
works: [the-verifying-compiler-a-grand-challenge-for-computing-research]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Revive an abandoned idea only when you can name what killed it and show each cause is gone

**Lesson:** Old ideas come back around constantly, and the usual argument for retrying one is that the field has moved on and machines are faster now. That argument is worthless because it is unfalsifiable: it names no specific obstacle, so it cannot be checked, and it will sound equally plausible the next time the attempt fails. The disciplined version of the same move is to treat feasibility as a claim with an itemized proof. Enumerate the concrete reasons the earlier attempt collapsed — not "it was too hard," but the particular missing capability, the particular economics, the particular property of the material being worked on — and then, for each item on that list, state what has changed and why the change removes it. If an item has no answer, the revival is premature and you now know exactly what to go build first.

The value of the audit is that it converts nostalgia into a work plan. Some of the original obstacles turn out to have dissolved for reasons unrelated to the idea itself: the artifacts you would apply the method to used to be secret, short-lived and written at the wrong level of abstraction, and are now public, durable and shared by millions, which changes the payoff of any effort spent on them without anyone having solved a technical problem. Others were solved incidentally by neighboring work aimed elsewhere — the analyses a compiler needs to optimize code are largely the analyses a checker needs to reason about it, so a decade of optimization research delivered infrastructure the verification effort never had to fund. Noticing that the enabling advance came from an adjacent field is the difference between a plan and a wish.

Run the audit honestly and it also tells you what has gotten *worse*. In the same interval that proof technology matured, the programs to be checked acquired concurrency, dynamic dispatch, inheritance and decades of accumulated legacy — features that were explored in clean experimental settings precisely because they are hostile to the reasoning you now want to do at scale. An honest revival states both columns and shows the balance has actually tipped. A pitch that lists only the improvements is not an argument; it is advertising.

**Source:** [The Verifying Compiler: A Grand Challenge for Computing Research](../works/the-verifying-compiler-a-grand-challenge-for-computing-research.md) — the Historical and Feasible criteria, which reconstruct why the 1970s attempt was abandoned (weak proof support, ephemeral secret assembler-level code) and then itemize the eight specific conditions that have since changed, alongside the admission that modern language features added new difficulties.
