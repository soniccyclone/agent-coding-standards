---
type: lesson
title: "Add permissiveness as a later phase that only runs when the strict phase found nothing"
figure: steele
works: [the-java-language-specification]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Add permissiveness as a later phase that only runs when the strict phase found nothing

**Lesson:** When a language gains the ability to slide silently between two representations of the same number, every existing call site where more than one candidate procedure could match acquires a new set of possible matches, and the risk is not that old programs stop compiling but that they quietly start calling something else. This specification's answer is not a tie-breaking rule bolted onto the selection algorithm; it is a split of the argument-passing situation into two distinct situations with two distinct permission sets. The conservative one admits only transformations that existed before the feature did. The permissive one admits those plus the new ones. The crucial clause is the ordering: the permissive situation is consulted only if the conservative one yields no applicable candidate at all. A program that resolved before the feature existed resolves identically after, because the second phase never gets a turn on that program.

This is a general and underused device. Backward compatibility is usually attempted by making the new rule narrow enough that it cannot collide with the old one, which fails because collisions are discovered later, by users, in code nobody was thinking about. Phasing sidesteps the problem entirely: instead of proving no collision exists, you arrange the search so the old answer is always found first. The cost is real and worth naming — a reader must know two rule sets and know that one is subordinate, and diagnostics have to explain which phase spoke — but that cost is bounded and local, whereas silent re-resolution is unbounded and remote.

The same chapter shows the other half of the discipline: an accommodation that was available and was refused. Assignment permits a value known at compile time to shrink into a smaller type when it demonstrably fits, which is why an ordinary small integer literal can initialise a small integer variable without ceremony. Argument passing does not permit this, and the reason recorded is not safety but the added complexity it would inject into candidate selection — followed by a concrete case that would need extra tie-breaking rules to resolve. So a rule is priced by what it does to the algorithm that must consult it, not merely by whether it is individually sound. Two rules that are each obviously correct can be jointly unaffordable, and the place that cost shows up is in the resolution procedure a human has to simulate to predict which code runs.

A programmer who works this way, faced with "make the matching smarter," builds the smarter matcher as a fallback tier behind the existing one rather than as an improvement to it — in overload and dispatch logic, in routing tables, in config lookup, in dependency resolution. And when asked to add a convenience coercion, they ask what it does to every ambiguity the system already has to resolve, and are willing to refuse a locally pleasant rule on the grounds that it makes the global procedure unpredictable.

**Source:** [The Java Language Specification](../works/the-java-language-specification.md) — the conversions chapter's split of argument-passing into a strict and a loose context with the loose one used only when the strict one finds no applicable declaration, together with its note explaining why compile-time narrowing of constant expressions was deliberately excluded from argument passing while remaining available in assignment.
