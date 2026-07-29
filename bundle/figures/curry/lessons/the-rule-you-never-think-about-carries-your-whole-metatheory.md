---
type: lesson
title: "The step you never think about is carrying your whole metatheory"
figure: curry
works: [a-theory-of-formal-deducibility]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# The step you never think about is carrying your whole metatheory

Curry singles out one step in his system for special treatment: the one that
takes a derived fact from one place and splices it in as an assumption
somewhere else. It is the step nobody notices, because chaining results is what
reasoning *is*. Every other rule he has is an explanation — it says how a
construct enters discourse and what it licenses. This one explains nothing. It
is a property you *want*, and his verdict is that it therefore has no business
being assumed. It must be proved redundant, and he spends the longest and most
delicate argument in the book proving exactly that: any derivation that uses the
splice can be rewritten into one that does not.

Two things make the effort worth understanding rather than admiring. First, the
redundancy was *predictable in advance* from how he built the rules. Each rule
had explained a complex construct in terms of simpler pieces, so nothing was
left over to need a general chaining principle — the intuition that it "ought to
be" a consequence came from the design, not from experiment. That is the shape
of a well-founded system: the conveniences you rely on are consequences you can
see coming. Second, and more usefully, the proof *fails* for systems whose base
rules do not have the right form — those with induction, for instance. Curry
notes flatly that in such systems the splice cannot be derived, and that
assuming it anyway *is* the non-constructive moment in ordinary arithmetic. The
convenience everyone uses without thought is not merely unproven there; it is
precisely where the extra strength is hiding, and it hides so well that people
spent decades attributing the strength somewhere else.

He then shows the same thing from the failure side. When he tries to add a modal
operator, the chaining proof stops working, and he identifies why in one
sentence: the proof had depended throughout on being able to carry extra
surrounding context through every rule untouched, and the new operator's rule
inspects and restricts its context. One rule that is not uniform in its
surroundings costs every theorem that had leaned on uniformity. Curry does not
paper over this. He stops, publishes the chapter as unfinished, and says the
question is open.

For a programmer the pattern is exact and constant. The operation your codebase
performs everywhere without comment — retry, cache read-through, config merge,
implicit transaction join, cross-service call substituted for a local one — is
carrying invariants nobody has stated. Two consequences follow. When you want
to know where a system's real strength or real fragility lives, do not audit the
features; audit the step so ubiquitous it has become invisible, and try to derive
it from the others. If it derives, you have a clean system and a genuinely
optional convenience. If it does not, you have just located your load-bearing
assumption, and it is almost certainly the thing that will break under a new
requirement. And when you add a feature, the question is never whether the
feature works — it is which uniformity the rest of the system was silently
assuming, and whether the new thing respects it. A single construct that reads
its own context turns local reasoning into global reasoning everywhere at once.

**Source:** [A Theory of Formal Deducibility](../works/a-theory-of-formal-deducibility.md) — the argument for the elimination theorem and the surrounding discussion of why that step is a desired property rather than an explanatory rule, the concluding remark identifying its tacit assumption as the non-constructive moment in arithmetic, and the modalities chapter's account of how one context-sensitive rule invalidates the proof.
