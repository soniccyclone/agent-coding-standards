---
type: lesson
title: "When a safety rule is too rigid, put an ordering on the things being checked rather than dropping the check"
figure: dahl
works: [class-and-subclass-declarations, simula-67-common-base-language]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# When a safety rule is too rigid, put an ordering on the things being checked rather than dropping the check

**Lesson:** The class hierarchy arrives as the resolution of a stated dilemma, and the shape of that resolution is the transferable idea. One prior approach pinned every reference variable to exactly one record class, which gave complete static checking at the price of a rigidity the authors judged unusable: nothing could hold a mixture, and a collection of related-but-varying things had no expressible type. The other approach, already in the earlier Simula, deferred the whole question to a runtime discrimination the programmer was syntactically forced to perform, which restored flexibility but moved the cost into every access site. Both treated the set of classes as unrelated points. The move that dissolves the problem is to give that set a structure: arrange classes into a tree by prefixing, let a reference's declared class stand for that class together with everything below it, and replace the equality test on classes with a test for one class including another.

The economics change completely once the check is an inclusion test on a partial order. Assignment in the safe direction, from a more specific class to a variable declared at a more general one, is statically decidable and needs no runtime work at all. Only the narrowing direction retains a residual question, and it is answerable by a single discrimination at one place, after which the compiler again knows exactly which attributes are legitimately reachable. Flexibility and static checking stopped competing because the ordering absorbed the variation that used to have to be handled dynamically. This is a general pattern rather than a fact about types: a check that is too strict is often a check performed against the wrong algebraic structure, and finding the order, lattice, or subtyping relation that the domain already has converts a rejected program into an accepted one without weakening anything.

The discipline required to make it work is worth naming. The order must be a genuine order, so prefix chains are required to be finite and no class may appear twice in one, and if two classes share an ancestor they share the entire chain up to it. Without those constraints the inclusion test is not a decision procedure and the whole benefit evaporates. Structures bought for reasoning have to satisfy their laws.

A programmer holding this lesson responds to "the type system won't let me express this" by looking for the missing relation rather than by reaching for a cast or an untyped escape hatch. The question to ask is what ordering, sum, or interface relation among the cases would make the intended program well-typed, and whether the domain actually satisfies it. The failure mode this guards against is the habit of buying flexibility by deleting information, which trades a compile-time error you can see for a runtime error you cannot predict.

**Source:** [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the introduction's comparison of the fully-static record approach against Simula's forced runtime connection check, and the reference-operations section, where legality of assignment is decided by which inclusion relation holds between the qualifying classes, with the ambiguous case singled out for separate treatment. Also [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md), whose introduction states qualification as permitting the named class or any of its subclasses.
