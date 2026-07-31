---
type: lesson
title: "Don't widen a domain to house machinery its definition excluded"
figure: strachey
works: [continuations-a-mathematical-semantics-for-handling-full-jumps]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Don't widen a domain to house machinery its definition excluded

Describing an early-exit construct requires stashing something for the exit to reinstate later, and that something has to live somewhere. The obvious place is the existing table of name-to-meaning bindings, since the thing being stashed is looked up in exactly the way a name is looked up and scopes in exactly the way a name scopes. Taking that route costs one reserved name and nothing else structurally. Strachey and Wadsworth decline it, and the reason is worth extracting, because the trade they made looks like the wrong one on any local accounting.

The table of bindings maps names to a particular collection of values, and that collection is not an arbitrary grab-bag: it is characterised, in their other work, as precisely the things a programmer can attach a name to in that language. Putting the saved exit-target in the table would force the collection to be enlarged to contain something no programmer can ever name, and the characterisation would silently stop being true. So instead of widening the collection they complicated the container, making the context a pair — the ordinary bindings alongside a separate compartment holding the saved exit-target — and paid for that in extra notation on every rule that touches context. A structural cost, taken deliberately, to keep a definition saying what it said.

The general shape is that certain sets in a design carry a claim, not just a membership list. "These are the values a user can construct." "These are the states an external client can observe." "These are the errors a caller is expected to handle." Internal machinery always needs somewhere to sit, and the cheapest somewhere is always inside one of those sets, because adding a member is a small edit and building a separate compartment is not. But the claim is what everything else was reasoning from, and there is no mechanism that will warn you when it quietly weakens. Afterwards every statement about the set needs a caveat, and the caveat is invisible in the type.

So the discipline is to notice when a container's definition is load-bearing before you extend it, and to ask whether the thing you are about to add is the kind of thing the definition described. If it is not, give it its own compartment even when the compartment is uglier than the extension would have been. It is also worth noticing what made the cost visible here at all: they had committed to the same characterisation across several documents, so an inconsistency was something they could detect. An invariant only stated once, in the place it is convenient, is an invariant nobody can catch you breaking.

**Source:** [Continuations: A Mathematical Semantics for Handling Full Jumps](../works/continuations-a-mathematical-semantics-for-handling-full-jumps.md) — the treatment of the value-yielding block and its result command, where the expression continuation is saved into an extended notion of environment, together with the footnote weighing and rejecting the simpler alternative of a hidden reserved identifier on the grounds that it would require the domain of denotations to admit something no program identifier can denote.
