---
type: lesson
title: "Every impossibility result is somebody's guarantee — go find the field where it is good news"
figure: valiant
works: [a-theory-of-the-learnable]
axes: [verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Every impossibility result is somebody's guarantee — go find the field where it is good news

**Lesson:** When you cannot prove the negative result your framework needs, look for a neighbouring discipline whose working assumptions are the same statement with the sign flipped. The two directions are often literally identical propositions: a function nobody can reconstruct from polynomially many input-output pairs of their choosing is exactly a function that survives a chosen-plaintext attack, so the entire practice of an adjacent field betting its security on the existence of such functions is simultaneously a bet that a broad class of easily computable things cannot be acquired from examples. You inherit their evidence for free, and — since they have been trying hard to break their own constructions — their failure is stronger evidence than anything you were likely to produce unaided.

The move generalizes past this one pairing. Hardness results are the load-bearing beams of cryptography, of lower-bound theory, and of every argument that some optimization cannot exist; anywhere a discipline is built on things being difficult, it has accumulated evidence usable by anyone who wants to conclude that those things are difficult. So before mounting a direct assault on "no efficient procedure can do X," spend an hour asking who benefits from that sentence being true and what they already believe. The reverse holds too, and is the more uncomfortable direction: if you find yourself designing a system whose usefulness requires that some behavior be inferrable from observed data, check whether the security community would call that same inference an attack they consider infeasible.

The two kinds of evidence should be kept honestly separated. Circumstantial evidence borrowed this way is exactly as strong as the assumption it rests on, and no stronger; it says which conjecture your problem is equivalent to, not that the problem is settled. That is still a substantial gain — knowing your obstacle is the same obstacle as some well-studied hardness conjecture tells you where to stop pushing — but a result conditional on a widely believed assumption should be labelled as such rather than promoted to a theorem in the retelling.

**Source:** [A Theory of the Learnable](../works/a-theory-of-the-learnable.md) — the introduction's argument that a cryptographic scheme immune to chosen-plaintext attack is precisely a non-learnable easily computed function, and the note in section 3 that a subsequent unconditional-looking result still rests on the intractability of factoring, both offered as circumstantial rather than settled evidence.
