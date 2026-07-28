---
type: lesson
title: "Individually logical rules compose into a policy nobody chose, so evaluate the composition against the property you wanted"
figure: ritchie
works: [on-the-security-of-unix]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [operating-systems-and-systems-programming, formal-methods-and-verification]
tags: [lesson]
---
# Individually logical rules compose into a policy nobody chose, so evaluate the composition against the property you wanted

The most instructive passage in the memo is the one where Ritchie describes a behaviour as perfectly logical and unfortunate in the same breath. Permission on a container governs the container; permission on an item governs the item; neither rule references the other. Each is defensible in isolation and each is what a reader of the rule would predict. Together they produce two outcomes nobody would have written down as policy: an item can be rewritten or emptied inside a container that forbids writing, and an item can be discarded by anyone with authority over the container regardless of its own protections. No rule is violated. The intended property — that a body of data can be published for reading while being protected from alteration — simply is not implied by the conjunction of the rules that exist.

The thinking move is to stop reviewing a rule set rule by rule and start asking what its closure permits, then compare that against the small list of properties users actually want. Local review is cheap and reassuring and cannot find this class of defect by construction, because there is nothing locally wrong. The gap lives between the rules, in the relation the model declines to express. Ritchie also notes the honest second half: the obvious repair, demanding authority over the container as well as the item, immediately entangles the case where users must be able to modify their own containers while not modifying the one that holds them all. Fixes to compositional defects tend to be compositional themselves, so the difficulty is a property of the model, not a failure of the fixer.

The same logic drives his conclusion about what a user can actually rely on. Rather than advise careful per-item settings, he identifies the one action that is both necessary and near-sufficient — sealing the container — and then names precisely what leaks through even then. That is the useful output of a composition analysis: not a list of knobs, but the smallest configuration that implies the property, plus an explicit statement of the residual holes. He notes as well that the practical rescue for the deletion case came from tooling asking for confirmation, which is worth recognising for what it is: a mitigation living outside the model, protecting people from a policy the model genuinely allows.

A programmer who holds this view writes down the invariants a permission or capability system is supposed to guarantee, separately from the rules that implement it, and then tries to derive each invariant from the rules. Where the derivation fails, they either extend the model or document the hole — rather than assuming that locally sensible rules add up to a sensible system.

**Source:** [On the Security of UNIX](../works/on-the-security-of-unix.md) — the middle section on setting protection modes, where directory-level and file-level permissions are shown to interact in ways that defeat read-only publication and self-protection.
