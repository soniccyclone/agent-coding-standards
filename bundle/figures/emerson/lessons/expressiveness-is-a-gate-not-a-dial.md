---
type: lesson
title: "Expressiveness is a gate, not a dial, and the criterion that decides adoption cannot be formalized"
figure: emerson
works: [model-checking-algorithmic-verification-and-debugging]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Expressiveness is a gate, not a dial, and the criterion that decides adoption cannot be formalized

**Lesson:** When choosing a notation to state requirements in, the ordering of concerns is counterintuitive. Speed of checking looks like the practical concern and reach of the notation looks like the academic one, but the reach comes first and it is not negotiable. If the property you actually need to assert falls outside what the notation can say, no amount of algorithmic cleverness rescues you; there was never any reason to adopt the method in the first place. Efficiency is a dial you turn after the gate opens. Emerson states this ordering plainly and it is worth taking as a general rule for any declarative layer a programmer commits to: constraint languages, type systems, query languages, policy engines, schema validators. Ask first what you cannot say, not how fast it runs.

Past the gate, three criteria pull apart that are usually conflated. Reach is whether a property can be stated at all. Compactness is how much text the statement costs, and it can differ exponentially between notations that are otherwise equally capable, since a single formula in a richer logic can require a blowup of cases when rewritten in a poorer one. Ergonomics is whether the person writing the requirement can produce a correct statement of the thing they actually meant. The first two admit mathematical treatment. The third does not, and Emerson's judgment is that in real use it dominates. That is an uncomfortable claim from someone whose career was spent on the formalizable half, and the evidence he offers is that industry spent person-years building specification languages whose distinguishing feature was not additional reach but compact high-level operators expanding into the same underlying vocabulary.

The trade-offs run against each other in a way that makes a single best answer impossible. A richer notation costs checking time. A more compact notation usually reads better and costs even more checking time. There is no dominant point, only positions that suit particular jobs, and finding a good one takes experience rather than derivation. Emerson also makes an efficiency observation in the same spirit: an algorithm with a bad worst case that is repeatedly observed to behave well on real inputs will beat one with a better bound and worse measured behavior, so the criterion is observed performance on the workloads that exist rather than the bound on the workloads that could.

A programmer holding this view evaluates a DSL, schema language, or assertion library by first writing down the three hardest things they will need to express and checking whether the notation can express them, before benchmarking anything. They treat abbreviation layers over an existing core as real engineering rather than sugar, because ergonomics is where adoption is won and it cannot be argued for from the semantics. And they stay suspicious of a notation whose selling point is a complexity bound, since a bound says nothing about whether anyone can write a correct specification in it.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/model-checking-algorithmic-verification-and-debugging.md) — Emerson's own opening part of the shared lecture, in the sections where he ranks expressive power above efficiency as the primary criterion for a specification logic, separates reach from compactness from convenience while conceding the last is informal, and then discusses the trade-offs and the preference for observed over worst-case algorithmic behavior.
