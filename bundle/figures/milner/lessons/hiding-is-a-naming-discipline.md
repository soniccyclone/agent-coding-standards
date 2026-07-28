---
type: lesson
title: "Hiding is a naming discipline, not an annotation you attach"
figure: milner
works: [the-definition-of-standard-ml]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Hiding is a naming discipline, not an annotation you attach

**Lesson:** Most systems express information hiding as a marking: something is declared private, or omitted from a published interface, and the checker refuses references to it. That approach hides the existence of a component. It does not hide the identity of a component, and identity is what leaks. An interface can conceal that a type is implemented as a machine integer and still let a client exploit the fact, because the client can observe that the type is interchangeable with integers wherever both appear. Concealment by omission and concealment of identity are different properties, and the second is the one abstraction actually needs.

The mechanism used here achieves the second by construction. When a module is sealed against an interface opaquely, each type the interface leaves unspecified is bound to a freshly generated name — an identity that appears nowhere else and that no client can write down. Nothing is forbidden; there simply is no expression a client could form that names the same thing, so the desired equations are unprovable rather than prohibited. The distinction between the two available forms of sealing makes this precise and visible: one form hides components but preserves identities, the other hides identities too, and a program can be legal under the first and rejected under the second.

The generativity is uniform, and the consequences are deliberately unforgiving. A parameterized module sealed with an opaque result interface manufactures new names on every application, so two applications produce mutually incompatible abstract types even when the body is a constant with no dependence on the argument at all. That looks like a bug and is a feature: it means the abstraction boundary is a property of the act of sealing rather than of what happens to be behind it, and it cannot be accidentally weakened by an implementation that happens to be simpler than its interface promised. Identities that the interface does propagate — those it names explicitly — do flow through, so the mechanism distinguishes what was shared on purpose from what merely coincided.

The transferable principle is that an abstraction is only as strong as the client's inability to name what is behind it. When you want a boundary to hold, ask what the client can construct that is provably the same as your internals — a shared struct definition, an exposed integer id, a serialization format, a type alias that resolves to a common primitive. Removing the reference is not enough while an equal thing remains constructible. Fresh, unforgeable identity is the enforcement mechanism; visibility rules are only its bookkeeping.

**Source:** [The Definition of Standard ML (Revised)](../works/the-definition-of-standard-ml.md) — the module static semantics rules for the two forms of interface constraint and for application of a parameterized module, with their freshness side conditions, elaborated in the closing appendix's discussion of opaque matching and its worked examples of fresh types arising from repeated application.
