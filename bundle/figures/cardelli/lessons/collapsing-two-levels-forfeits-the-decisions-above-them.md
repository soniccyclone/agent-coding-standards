---
type: lesson
title: "Collapsing two levels to save concepts also destroys the questions those levels let you answer"
figure: cardelli
works: [structural-subtyping-and-the-notion-of-power-type]
axes: [cognitive-load, hardware-affinity, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Collapsing two levels to save concepts also destroys the questions those levels let you answer

**Lesson:** Identifying two levels of a system with each other is a seductive economy. One less category to explain, one less set of rules, a shorter presentation. The hidden cost is that the distinction was doing work you had not enumerated, and afterwards there are ordinary questions you can no longer ask. Once descriptions are themselves things described by the same machinery, it stops being answerable whether a given expression produces a value or a description, because the very same expression can legitimately do either depending on what it is handed. That is tolerable in a purely interpreted, applicative setting where the answer never has to be decided. It is fatal wherever the system must commit some work to one stage and some to another, because staging is exactly the decision the collapse made unanswerable.

The general principle is that a level distinction usually encodes a phase, resource, or authority boundary that someone downstream depends on. Ask, before merging, which decisions the boundary currently lets you make: what gets computed early versus late, what may be discarded before running, what is permitted to depend on data that does not exist yet. If any of those matter, the collapse is not a simplification, it is a deferral of complexity onto whoever must reintroduce a stratification later, and reintroducing one while preserving the good properties that motivated the merge is much harder than never merging.

It is worth noting the honest way the trade can still be taken. Collapse deliberately, for exposition or for a setting that provably does not need the distinction, say so, and record that a stratified variant is required for the settings that do. That leaves the economy available where it is safe and prevents it from being mistaken for a general result. The failure to avoid is discovering, late, that a feature you need is not expressible because two things you merged for elegance had to be told apart all along.

**Source:** [Structural Subtyping and the Notion of Power Type](../works/structural-subtyping-and-the-notion-of-power-type.md) — the discussion of kind and phase distinctions, which adopts the self-describing collapse for simplicity of presentation, works out the consequent inability to say whether a term is a value or a description, and identifies phase separation rather than the collapse itself as the real requirement for compiled and stateful languages.
