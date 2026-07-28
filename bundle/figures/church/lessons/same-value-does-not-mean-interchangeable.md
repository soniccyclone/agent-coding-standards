---
type: lesson
title: "Denoting the same thing does not make two expressions interchangeable; substitution has a scope and you must know where it ends"
figure: church
works: [introduction-to-mathematical-logic]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Denoting the same thing does not make two expressions interchangeable; substitution has a scope and you must know where it ends

Church builds his account of meaning on a split he takes from Frege: an expression both picks out a thing and carries a way of picking it out. Two expressions can land on the same object while differing in how they get there, and he separates the consequences precisely. Replacing a constituent by one with the same way-of-picking-out leaves the whole expression's way-of-picking-out unchanged. Replacing it by one that merely lands on the same object leaves only the object unchanged — the way-of-picking-out may shift, and where that shift matters, truth can change with it.

He then shows where it matters, with an example that has become standard: a sentence reporting that someone once demanded to know whether one name's bearer was the other's is true, while the sentence obtained by substituting the equally-referring name is false. Contexts of asking, believing, wishing, and seeking take an expression's manner of reference as their subject, so inside them a co-referring swap is not a no-op. His response is not to declare such contexts illegitimate but to identify them as a distinct mode of use — and to note that a well-built language should either eliminate the mode or provide separate machinery to refer to the manners of reference directly, rather than leaving the two uses of the same expression to collide silently.

The general principle is that substitutability is licensed by an equivalence *plus* a claim about which contexts respect it, and the second half is where the errors live. Everyone learns the first half — equal things may replace each other — and then applies it under a construct that was never covered. Church's discipline is to state, as explicit assumptions of the theory of meaning, exactly which replacements preserve exactly what. He extends the same treatment to expressions with free variables, defining when two of them agree everywhere including where both are undefined, so that the substitution principle has a stated domain rather than an assumed one.

A programmer who holds this distinction stops treating "equal" as a single notion and asks equal-for-what: two values may be interchangeable for arithmetic and not as cache keys, interchangeable for a comparison and not for identity, interchangeable in a computation and not inside a quoted form, a macro, a log line, a serialized record, or anything that reflects on how the value was written. Any construct that consumes the expression rather than its value — templating, memoization on structure, code generation, symbolic differentiation, an error message that echoes source — is an oblique context, and substitutions that are valid everywhere else are simply not valid there.

**Source:** [Introduction to Mathematical Logic](../works/introduction-to-mathematical-logic.md) — the section on names, which distinguishes sense from denotation, states the assumptions governing substitution of constituents, and identifies oblique occurrences where a co-referring substitution changes truth; extended in the following section to forms and their agreement in value.
