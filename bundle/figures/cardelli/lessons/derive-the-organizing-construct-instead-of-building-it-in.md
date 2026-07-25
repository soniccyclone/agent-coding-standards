---
type: lesson
title: "Derive the organizing construct from what you already have, and its preconditions become visible instead of built in"
figure: cardelli
works: [an-imperative-object-calculus, a-language-with-distributed-scope]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Derive the organizing construct from what you already have, and its preconditions become visible instead of built in

**Lesson:** The structure a system uses to organize itself, whether a class, a hierarchy, a registry, or a plugin framework, is usually built in as a primitive with special rules. Built in, it is inflexible in one specific way: its side conditions are implicit in the mechanism, so nobody can state them, argue about them, or discover that a particular case violates them until something breaks. Derive it instead, from abstraction over the eventual whole plus the existing notion of refinement, and the conditions surface as ordinary requirements you can read off. A class becomes a collection of routines each parameterized over whatever refinement it will end up serving, together with one uniform assembly step, and the question of whether a given routine may be reused by a refinement turns into a checkable relation between two descriptions rather than a property of a keyword.

The immediate benefit is that you learn things the built-in version was hiding. Reuse is unconditional for slots used in both directions and for slots only written; it can fail for slots only read, where a refinement may legitimately need its own version. That is a real design constraint about inheritance, and it is invisible in a language where inheritance is a primitive. A second benefit is coverage: a kernel with no built-in hierarchy models both the class-shaped world and the world where behaviour is shared by cloning and redirecting prototypes, because neither is favoured by the primitives. Committing to one in the kernel would have made the other a hack.

The same reasoning shows up in a language design that omits hierarchies and lookup strategies entirely, keeping only four operations on self-contained objects, and then recovers the sharing idioms as combinations of them. The consequence is that a lookup is one step rather than a search up a chain, which matters when the chain might cross a network. In general, when a construct is primitive its cost model and its side conditions are both opaque; when it is derived, both are just properties of the derivation.

**Source:** [An Imperative Object Calculus](../works/an-imperative-object-calculus.md) — the section representing classes as collections of routines parameterized over eventual refinements, with a uniform construction step, and the derivation of the inheritability condition together with the observation that only one variance case restricts reuse. Also [A Language with Distributed Scope](../works/a-language-with-distributed-scope.md) — the object model section, which rejects hierarchies and lookup strategies in favour of four operations on self-contained objects, and recovers single and multiple inheritance idioms from cloning.
