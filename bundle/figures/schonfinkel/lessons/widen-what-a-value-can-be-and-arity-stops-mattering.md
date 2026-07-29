---
type: lesson
title: "Widen what a value can be and arity stops mattering"
figure: schonfinkel
works: [bausteine-der-mathematischen-logik]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Widen what a value can be and arity stops mattering

Faced with functions of several arguments, the obvious response is to add machinery that handles them: tuples, argument lists, a notion of arity attached to every function. Schönfinkel does the opposite. He enlarges the notion of function so that a function's result may itself be a function, and with that single change the multi-argument case evaporates. Supplying the first argument no longer produces an answer; it produces another function still waiting for the rest. Every function in the calculus takes exactly one argument, and a call on several is a chain of one-argument calls.

The technique is famous, but the reusable insight is the direction of the fix. The complexity of the n-ary case was not intrinsic to the problem — it was an artifact of an unnecessarily narrow answer to the question "what may a value be?" Relaxing the domain of values eliminated a whole class of special cases rather than accommodating them. That is the opposite of the usual reflex, which is to leave the value domain alone and grow the operator set to cope. When a formalism sprouts parallel machinery for the one-of-these and the several-of-these cases, the narrowness is often in what it lets you hold, not in what it lets you do.

Schönfinkel is careful about a point that gets lost when this is taught as syntax. The intermediate object is genuinely a function whose *shape* depends on the argument already supplied, not merely a value depending on it, and he flags the distinction explicitly with an arithmetic illustration: fixing the first argument yields a new function, and only then is the second substitution meaningful. That staging is the substance. It is why partial application is a semantic fact rather than a convenience, and why a language whose functions are ordinary values gets it for free while one with a separate calling convention for multi-argument procedures must bolt it on.

The practical consequence is a preference for uniformity in what can be passed around and returned. If functions, and by extension whatever else the system traffics in, are first-class values, then combination, staging, and specialization all reduce to application, and you stop writing distinct mechanisms for each. If they are not, every one of those becomes its own feature with its own edge cases — and the deficit shows up not as a missing capability but as a growing pile of near-duplicate machinery.

**Source:** [Über die Bausteine der mathematischen Logik](../works/bausteine-der-mathematischen-logik.md) — the second section, where the function concept is extended to admit functions as both arguments and results, and multi-argument functions are recast as nested single-argument application under a left-associating convention.
