# Growing a Language Toward the Problem

A second set of claims, from the people who treated a program, an API and a
language as the same kind of artifact. Almost all code is Algol-descended, and
that lineage's instincts arrive feeling like neutral judgement rather than one
tradition's answers. These are the moves it does not make by default.

## You are designing a language whether or not you admit it

Steele's claim is that anyone writing a large program is constructing a language
on top of the one they started in, hundreds of terms deep with its own rules for
how those terms combine, and that there is no other way to do it. The gap between
your conceptual vocabulary and your medium's is the volume of definitions you
must write before starting on the problem, and it belongs in the estimate. Review
that vocabulary as a designed artifact: is each term paying its definition cost,
do the terms compose, is the rule for coining new ones written anywhere.

Ingalls supplies a measurement cheap enough to run on code you have. What
fraction of the text is about the subject matter, and what fraction about
machinery: allocating, threading context, announcing ownership, converting
between two shapes of the same thing? Recurring bookkeeping names an obligation
some layer below should discharge once instead of a thousand times.

This does not license a config layer or plugin system beside your code. It is the
opposite move: extend the vocabulary you are already writing in, so the new term
is used exactly as everything else is.

## "You could already express that" settles nothing

Any sufficiently general system encodes any feature, so the existence of an
encoding is evidence of nothing (Church, Sussman). Steele's replacement test is
locality: write the encoding and see how far it spreads. If each construct maps
to a corresponding piece with the program's shape and size roughly intact, the
feature was notation over mechanism you already had. If adding it means every
caller gains a parameter, every return convention changes, or the control flow
turns inside out, it is a missing primitive you are paying for in complexity
smeared across unrelated files. Threading a context object through a whole
codebase feels wrong because that is the visible cost of simulating what the
substrate does not provide.

McCarthy's version applies to representations, and is the one to run before
adopting a config format, schema, wire format or intermediate form. Write down
three changes you expect to want within a year and check the size and locality of
each in the candidate. A weaker representation where all three are one-line
additions beats a more expressive one where all three are refactors. "We can
build anything on top of this" is not an argument in a representation's favour;
ask for the diff.

## The line between describing and computing is yours to move

Whether a description counts as a program is a fact about the evaluator, not the
description (Sussman). Faced with a specification that will not run, the reflex
is to enrich it with steps until it stops being a specification, at which point
what was wanted survives only in a comment. The other move is to leave the
description as written and ask what capability one level down would let it stand
as code. That is often narrower than it looks: a constraint runs once something
can generate candidates and be told a branch is dead; a relation runs once
something pushes information in whichever direction has enough inputs. The first
move costs once per specification, the second once.

Keep that layer ignorant of your subject matter (McCarthy). The exhaustive part
earns its keep by blindness, which lets you state its guarantee without naming
any application; the part choosing what to feed it earns its keep by being
unashamedly domain-specific and revisable. The two collapse into each other one
special case at a time until nobody can say what the engine promises, and when
such a system is slow, nearly all the waste is selection error rather than engine
cost.

## Reify the mechanism you cannot control, then hide it again

Every system runs on machinery its users never name: where a result is delivered,
what happens next, who handles the failure. Take one and make it an ordinary
argument every procedure receives and passes along (Steele, Landin, Strachey).
Once the rest of the computation is a parameter, an early exit is handing the
result to a different destination rather than a new control construct, and
jumping out, breaking, cancelling and resuming become one mechanism used
differently (Strachey). Once the failure path is a parameter, the callee cannot
tell whether what it was handed returns normally or unwinds past six frames, so
policy is fixed at the outermost caller and every layer between becomes
indifferent to it (Landin). Steele's second half is the part people drop: reify
to understand a mechanism and settle what it means, then push it back under
notation. Make hidden machinery explicit to debug it, not to live in it.

Reynolds makes the behaviour/data boundary crossable in either direction by rote.
Any callback can be replaced by a tagged record holding exactly the free
variables its body uses plus one dispatcher branching on the tag, and the number
of record kinds is bounded by the places that create it, finite even though the
runtime instances are not. That buys inspection, logging, equality, serialization
and replay for something previously opaque. Run the transformation blind and
interpret afterwards: the records you are forced to invent are the ones you would
otherwise have designed by hand, which makes them consequences you check rather
than choices you defend.

## The seam is what kills extensibility

Steele compares two languages, each with one brilliant designer and an extension
facility, that diverged completely in whether users grew them. In one, built-ins
had special notation and user definitions got ordinary names, so user work was
visibly second class, growth stayed with the few holding the source, and
promoting a contribution into the core meant rewriting its call sites. In the
other, user definitions looked like primitives and, the half people forget,
primitives looked like user definitions. So evaluate any extension point by what
the extension cannot do that the built-in equivalent can: same syntax, same
tooling, same error messages, same performance story, same place in the docs.
Every privilege your framework reserves for itself is a ceiling on how far anyone
will carry it. Kay adds that exempting the small and fast from a uniform scheme
yields a two-tier system whose special-case reasoning propagates upward.

Ingalls supplies the number: judge by the marginal cost of the Nth addition, not
the first, since a demo only ever shows the first. Count how many existing
working definitions you must edit to add the next kind of thing. Zero means the
mechanism carries the extension; anything else means the case matrix still lives
in your code.

## What a model states, and what it merely inherits

An explanation that uses the feature it explains says nothing to the audience
that needs it, and silently forwards every misconception about the medium into
the subject (Reynolds). Apply his test to any model, embedded language or
generated artifact: which properties does it state, and which does it merely
inherit? A rules engine that evaluates by calling the host's eval has not defined
evaluation order, truthiness, numeric behaviour or error semantics; it exports
the host's quirks and will inherit the host's next release. Define the thing in a
medium strictly weaker than itself, and treat every failure of that attempt as
the finding.

Sussman's companion claim is that a notation resembling a more powerful one gets
used as though it were that one, and the predictable error is composition:
someone feeds one operation's result into another because the host allows it, and
your restricted version cannot express that at all. The restriction is not
discoverable from examples, so state it where the notation is introduced and have
the checker reject violations with a message naming the rule. In a borrowed
notation, every rule not enforced is assumed absent.

## Build it to find out, and remember that whatever runs first wins

When you cannot tell whether two ideas differ, stop comparing vocabularies and
implement both in one substrate (Sussman, Steele). Scheme exists because its
authors could not say how message-passing agents differed from procedures, built
one thing holding both, and found on finishing that they were the same object. If
two concepts collapse you have removed a concept, which is the best outcome
available. Hand a proposal over running rather than described: describing
surfaces the consequences you already saw, running surfaces the rest.

McCarthy's warning is why the model must not quietly become the product: whatever
runs first becomes the specification. Lisp's parenthesised form was an encoding
invented so an evaluator could be printed in a paper; someone hand-coded that
evaluator, and the language stopped moving. Spend disproportionate care on what
is hardest to change later, meaning data formats, wire protocols, public names
and sentinel values, and schedule a placeholder's replacement before it acquires
users, because afterwards the cost falls on other people and is never paid.
