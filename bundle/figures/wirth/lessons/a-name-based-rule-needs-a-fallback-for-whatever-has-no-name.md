---
type: lesson
title: "A name-based rule needs a fallback for whatever has no name"
figure: wirth
works: [project-oberon]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A name-based rule needs a fallback for whatever has no name

**Lesson:** Deciding identity or compatibility by name is a powerful simplification: it makes the question a comparison of tokens, it makes the answer independent of how deeply nested the things are, and it lets an author state that two things are different even when they happen to look the same. It also carries an assumption that is easy to leave unexamined — that everything needing an identity was introduced by a declaration that gave it one. Some categories are constructed anonymously, appearing inline at the point of use and never named anywhere, and for those the name-based rule has nothing to compare. The rule does not fail loudly; it simply has no input, and something must take over.

What takes over is the structural comparison the name rule was adopted to avoid: walk both descriptions in parallel, matching component by component, and decide compatibility from the shapes. So the honest description of a name-based system is that it has two rules, and the expensive one is still present, confined to the anonymous categories. Knowing this in advance changes two decisions. It tells you the real cost of the design, which is not zero. And it tells you where to look when adding a new kind of construct: if the new kind can be written without being declared, it needs the structural rule too, and this is much cheaper to notice at design time than after the fact.

There is a compensating move worth taking. Once the structural comparison exists for the anonymous case, look for the other places in the system that need exactly the same question answered — reconciling a promise made earlier against the definition that arrives later is the same comparison of two descriptions for compatibility — and route them through the same routine. A mechanism forced on you by one requirement is at its cheapest when it is the only implementation of that question in the system, and at its most expensive when a second, subtly different version of the same comparison grows up beside it.

**Source:** [Project Oberon](../works/project-oberon.md) — the discussion of module OCH in section 12.7, which states that assigning procedures to variables of a procedural type requires a fairly complex compatibility check because the language admits structural equivalence rather than name equivalence in this case, that this is necessary because the type of a declared procedure bears no name, that both the result type and the parameter types must therefore be checked, and that the routine performing the comparison is also invoked for forward declarations.
