---
type: lesson
title: "Plan the variation at the top, or the family cannot exist at all"
figure: liskov
works: [a-behavioral-notion-of-subtyping]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Plan the variation at the top, or the family cannot exist at all

**Lesson:** Families of related types are normally discovered from the bottom: several concrete things look similar, so a general parent is retrofitted over them. Once substitutability is held to a strict standard, that direction stops working. A parent that pins down a detail has thereby promised it to every client, and no child may then vary that detail — so the parent's tightness, not the children's differences, is what forbids the relation. The way to get a family is to decide in advance where the members are allowed to differ and to leave exactly those points deliberately loose in the parent, while pinning everything else. The looseness is not sloppiness; it is the only channel through which specialization can happen.

Two shapes of specialization fall out of this. A child can add abilities and internal state the parent never mentioned, which is the case everyone already imagines. But the more interesting case is a child that adds nothing and instead resolves slack the parent left open — choosing a specific behavior where the parent permitted a range, or narrowing the set of legal states. Both are specializations under the same criterion, and the second one only exists if somebody thought about the slack ahead of time. Where the members genuinely conflict rather than merely differ, the honest fix is a parent that nobody instantiates: a purely descriptive node whose whole job is to name what the members really do share, letting them be siblings instead of forcing one to pretend it is a version of another.

There is a sharp consequence for anyone drawing a hierarchy: the shape of the tree is determined by the descriptions, not chosen by the designer. If two things ought to be related and the criterion refuses, that is information about the descriptions — usually that one of them promised more than the domain warranted. Reworking the parent so it promises less is the fix; wedging the relation in anyway just relocates the eventual breakage into client code that trusted a promise the tree no longer keeps.

A programmer who believes this treats a general type as a budget of permitted variation, spent in advance. Before adding a second member to a family, they ask which promises the parent must give up, and they accept that giving them up makes the parent less useful to reason about — that is the actual price of the family, paid honestly rather than hidden. They also stop being surprised when an appealing hierarchy turns out to be illegal, and read the refusal as a design result rather than an obstacle.

**Source:** [A Behavioral Notion of Subtyping](../works/a-behavioral-notion-of-subtyping.md) — the type-hierarchies section, which separates specializations that extend from specializations that reduce permitted variation, and works through families of bounded collections, counters, and integer sizes where an uninstantiated general type is required.
