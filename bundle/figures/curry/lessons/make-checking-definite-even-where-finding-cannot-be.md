---
type: lesson
title: "Make checking definite even where finding cannot be"
figure: curry
works: [a-theory-of-formal-deducibility]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Make checking definite even where finding cannot be

When Curry sets out what it takes to have a formal system at all, he draws the
decidability line in a place that repays study. Term formation must be decidable.
Whether a candidate is a well-formed statement must be decidable. Whether
something is an axiom must be decidable. But whether a statement is *true* need
not be — and he says so explicitly, adding that a system where truth happens to
be decidable is comparatively trivial. What he demands instead is that whether a
*proposed derivation* is correct must always be decidable. Truth is allowed to be
out of reach; the checking of an offered witness never is.

That split is the whole engineering content of the definition. Search is
permitted to be unbounded, undecidable, cleverness-dependent, even
human-dependent. Adjudication is required to be mechanical and total. Notice how
much this buys: truth becomes objective without becoming computable, because its
objectivity is carried entirely by the definiteness of the checking procedure, not
by any ability to answer the question. Curry says as much — truth is precise and
objective in that the checking of evidence for it is a definite process. He is
willing to let the interesting question be hard so long as the boring question is
easy, and he understands that the boring question being easy is what makes the
hard one meaningful at all.

The design pattern this licenses runs through most systems worth building. A
type checker need not infer your program; it must decide whether an offered
annotation is consistent. A build system need not find the right dependency
graph; it must decide whether a supplied one is acyclic and complete. A consensus
protocol need not compute the correct history; it must decide whether a proposed
certificate is valid. A permissions model need not derive who should have access;
it must decide, totally and without ambiguity, whether a presented grant chain
authorizes an action. In each case the expensive, open-ended, possibly
unsolvable part is pushed to the producer, and the consumer is left with a
decision procedure that always terminates with a yes or a no.

A programmer who takes this seriously reaches for the shape reflexively when
facing something that looks intractable. Rather than weakening the problem until
it becomes computable — the usual reflex, and the one that quietly throws away
what you cared about — you split it: keep the hard question hard, and invest all
your rigor in making the verdict on a candidate answer cheap and total. The
payoff is that the hard part can then be attacked by anything at all, including
heuristics, brute force, a search over a nondeterministic space, or a human with
a hunch, and none of that endangers correctness because none of it is trusted.
The complementary discipline is refusing to let the checker be partial: a
verification step that sometimes says "I don't know" hands the ambiguity straight
back to the caller and destroys the arrangement, which is exactly why Curry
insists on definiteness for derivations and pointedly does not insist on it for
truth.

**Source:** [A Theory of Formal Deducibility](../works/a-theory-of-formal-deducibility.md) — the definition of a formal system in the opening chapter, which enumerates which of the primitive-frame questions must be settleable by a finite process and states directly that truth of an elementary statement need not be while correctness of a proposed derivation must be.
