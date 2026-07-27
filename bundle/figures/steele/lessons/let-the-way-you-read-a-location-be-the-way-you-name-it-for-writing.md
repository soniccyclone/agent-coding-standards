---
type: lesson
title: "Let the expression that reads a location be the name of that location, and derive the writer from it"
figure: steele
works: [common-lisp-the-language-2nd-edition]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Let the expression that reads a location be the name of that location, and derive the writer from it

**Lesson:** A system with many kinds of mutable storage normally accumulates two parallel vocabularies: one operation to read each kind of location and a differently-named operation to write it. The vocabularies grow together, must be memorised in pairs, and there is nothing in either name that tells you the other. This specification eliminates the second vocabulary by a change of viewpoint. Instead of treating a read as a function that computes a value from arguments, it treats the whole read expression as a *name* for the storage it reached — so the expression that extracts a field is the field's name, the expression that indexes an array is that slot's name — and then provides a single assignment construct that takes such a name and mechanically derives how to store into it. The consequence is stated bluntly: the individual writer operations become redundant, and most of them were removed from the language, the historical few surviving only out of deference to habit.

What makes this a design method rather than a syntactic trick is what the mechanism has to guarantee to be trustworthy, and the specification is unusually explicit about it. A single assignment construct that expands into read-modify-write code must preserve exactly the number and the order of evaluations that the source text implies, because the subexpressions inside the location's name may have side effects and may themselves be locations. The document walks through nested cases where a naive expansion would duplicate a subexpression and change the program's meaning, then defines the extension interface as a small tuple of parts — temporaries, the forms to bind them to, the variable receiving the new value, a storing form, an accessing form — from which correct expansions can be generated mechanically. It then gives the reason this machinery is in the language rather than left to users: even experts get this wrong, so the invariant belongs in the mechanism where it can be established once.

The generalisation is that if two operations are always introduced in pairs, one of them is probably not a separate concept but a derived view of the other, and the right fix is to find the shared notion that names them both. That collapses an O(N) vocabulary to O(1) plus a per-kind extension, and it makes the extension point the thing you document. The invariant that must be maintained across the collapse — here, evaluation order and count — is the real design work, and the specification's willingness to spend pages on it is what makes the collapse safe rather than merely tidy.

A programmer with this instinct resists adding a setter alongside every getter and asks instead whether the getter's expression can serve as the address. More broadly, they treat every pair of mirror-image APIs as a smell: serialise/deserialise, encode/decode, subscribe/unsubscribe, migrate-up/migrate-down. Sometimes both halves are genuinely irreducible; often one is derivable from a single richer description, and deriving it eliminates the whole class of bugs where the two halves drift out of agreement.

**Source:** [Common Lisp the Language, 2nd Edition](../works/common-lisp-the-language-2nd-edition.md) — the generalized-variables section of the control-structure chapter: the reframing of an access form as a name for a storage location, the argument that the separate update functions become redundant, and the specification of the extension interface together with its evaluation-order obligations.
