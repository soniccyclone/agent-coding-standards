---
type: lesson
title: "Ask how well the model fits before asking how hard the theorem was"
figure: stearns
works: [its-time-to-reconsider-time]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Ask how well the model fits before asking how hard the theorem was

**Lesson:** The first question to put to any formal apparatus is whether it preserves the features of the thing it claims to describe that actually matter — not whether it is elegant, and emphatically not whether its results were difficult to obtain. The worth of a result tracks how much it tells you about the real object, and an intricate derivation over a badly chosen abstraction tells you nothing while looking authoritative, because the machinery is visibly hard and the mismatch is invisible. What software people call garbage in, garbage out is exactly as true of theory, and worse there: a program with wrong assumptions eventually misbehaves in front of you, whereas a theorem with wrong assumptions stays true forever and simply fails to be about anything. Difficulty of proof is a seductive proxy for significance precisely because it is the one thing a specialist can always assess.

That puts model construction, not theorem proving, at the center of the work. When a domain concerns something real but intangible — the structure of competition, the nature of computing — no existing mathematics fits, and the honest response is to build new models rather than force the phenomenon into a formalism that happens to be available. The choice of model deserves at least as much explicit argument as the results derived from it, which is why the good early literature on such subjects spends its energy on defending the abstraction and comparatively little on proofs. A corollary about careers, incidentally: someone who follows the problems that genuinely interest them will find the field reorganize itself around them rather than needing to pick one, because a discipline is a downstream consequence of a cluster of problems that turned out to need the same new models.

The working habit is a two-column audit for every abstraction you adopt: which salient features it keeps, and which it discards. Both columns must be written down, because the discarded column is where every later surprise comes from. And when handed a result, run the question in reverse — what would have to be true for this theorem to hold and the real system still be broken? If the answer is easy to construct, the result is about the model and not the world, however hard it was to prove.

**Source:** [It's Time to Reconsider Time](../works/its-time-to-reconsider-time.md) — the closing of the personal-history section, where the question of how well models reflect the salient features of what they describe is named the first question for both mathematicians and computer scientists, significance is tied to information conveyed rather than difficulty of proof, and the garbage-in analogy is extended from software to theory; together with the preceding account of game theory and computation as two subjects that each required new mathematics for something intangible yet real.
