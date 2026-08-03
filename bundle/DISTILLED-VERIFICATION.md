# What Counts as Evidence That It Works

A third set of claims, from the people who spent careers on the question of what
actually establishes that a system is right. Their conclusions are mostly
negative and mostly about scope. Every result you obtain is about a model, under
assumptions, of the properties somebody bothered to state, and the engineering
leverage sits in those three qualifiers rather than in the checking.

## A passing check is a claim about a model you built by hand

Sifakis's position is that analysis never touches the running thing, only a
description of it, so every result transfers to the artifact through a relation
some human asserted and nobody verified. That relation is where the errors
concentrate and it is the one part of the pipeline that never gets audited, so
derive the description from the artifact mechanically rather than maintaining it
alongside. A schema kept in a doc, a state machine in a comment, a load test
written against a mock, a policy matrix in a spreadsheet: each is an unverified
transfer relation under whatever confidence you take from it. Where you cannot
generate it, say out loud that the model and the code can disagree without
either looking wrong.

He pairs this with an asymmetry worth internalizing. That a stated requirement
set is consistent can be decided mechanically; that it is complete has no
procedure and no definition. Confidence should scale with how much of what
matters got written down, not with how much of what was written down passed,
because absence from the analysis looks exactly like success.

## Name the edge, then cover outside it with a different blind spot

Abrial's honest formulation is relative correctness: these failures cannot
occur, under these stated assumptions about the environment. The assumptions are
not scaffolding discarded once the check passes, they are part of what you ship,
because they draw the line outside which the guarantee says nothing. Having
drawn it, cover the outside with a mechanism of a different kind, since a second
argument over the same model only re-establishes the same interior. Ask of every
assurance claim what class of fault its mechanism structurally cannot see. Types
cannot see wrong requirements, requirement checks cannot see bit flips, a
verified build cannot see a miscompiled dependency. Two mechanisms with
genuinely different blind spots are worth far more than doubling the strength of
one, which is also Hoare's argument for rival checkers: independence is doing
all the work, and two implementations sharing a library or an author share their
failures.

Abrial's other move is to validate artifacts rather than the machinery that
produced them. When you add a generator, a migration tool, or a codemod, check
its output the way you would check hand-written work rather than trying to
certify the tool.

## Most of the specification is the part nobody writes down

Emerson observed that a stated problem carries the global obligations everyone
argues about, while the bulk of the real content is local structure that a
diagram conveyed and nobody transcribed: each participant is in exactly one
state at a time, the only exit from waiting is inward, one participant's step
cannot relocate another. Local structure is invisible in discussion precisely
because it is shared, which is why it is the reliable source of disagreement. So
the requirements conversation is not finished when the contentious properties
are settled. Ask what everyone in the room already believed about the shape of
each component, and whether a stranger implementing from the document would
believe the same.

The second gap is possibility. A specification made entirely of obligations is
satisfied by a degenerate artifact, since fewer behaviours means fewer chances
to violate anything, and anything that generates or shrinks a system is under
pressure to collapse alternatives. A cache that must always return a correct
value may return one value forever. A retry policy that must eventually succeed
or report failure is satisfied by never trying. Write the reachability claims
next to the safety claims, and check them first whenever you simplify,
serialize, or remove a path, because that is the move that quietly breaks them
while every obligation still passes.

## Check that each decision's evidence had already arrived

Pnueli's sharpest observation is that ordinary specification records that one
thing depends on another and nothing about the moment the dependence is
resolved, which is harmless for a batch computation and fatal for anything
ongoing. Locate the instant each decision is committed, and check that every
quantity the argument leans on had actually arrived by then. Cache eviction,
scheduling, a participant acting on a stale view, a render before the fetch
returns: in each case the tempting analysis is done with the whole trace laid
flat, and the obviousness of the right choice is an artifact of standing outside
time. A failure here is not imprecision, it is impossibility, and the repairs
are structural rather than better code. Delay the commitment, weaken the
requirement to permit a bounded lag, or make the error budget explicit.

The companion is his partition: split every interface into what this component
writes and what is written to it, then re-read each requirement asking whether
the other side can falsify it alone. Anything that constrains the arriving data
is not a requirement you can meet, it is an assumption you owe separately.
Vardi's version applies inside a single process. Keep apart the predicate you
reason with, which may quantify over everything the global state permits, and
the predicate a component can evaluate from what it holds. A guard that would
need to know what other nodes have observed is a correct claim in a vocabulary
that cannot be compiled.

## Discharge the obligation while the decision is the only thing in view

Jones failed to prove a working several-hundred-line program correct, found
redeveloping it from the same specification cheaper, and drew the conclusion
that an argument is a by-product of having built the thing a particular way
rather than a certificate attached later. The finished text presents every
detail at once with no record of which detail discharged which obligation, and
that record only ever existed in the author's head.

His test for any decomposition is worth applying literally. Can you hand
somebody one of these sub-specifications and nothing else, and is there any
circumstance in which their correct work is rejected later? If yes, the
modularity is an illusion that surfaces at integration. Whatever a final
compatibility check would test can instead be written into the pieces'
contracts at the moment of the split, before any piece exists, so that failure
costs one decision rather than a subtree of them. He also supplies the reason
this is affordable: derive the list of what must hold once, then scan rather
than prove, because the great majority of items are settled the instant you look
at them and the cost is dominated by the two or three that resist. An informal
step is safe exactly when you could name the steps that would fill it.

## Where the argument stops is where the code stops

Floyd separates two claims that get conflated: if it returns, the result is
right, and it returns. Jones sharpens this into something you can act on. The
region your case analysis fails to reach is the region the code diverges on,
described twice. When an argument will not close over some slice of the input
space, do not go looking for a cleverer argument, go look at what the code does
there. The corollary is the one people skip: a stated precondition is
simultaneously what makes the descent terminate and what makes the case analysis
exhaustive, so deleting it as redundant documentation removes the only thing
between the function and an infinite regress.

## Eventually is not a bound, and progress needs a named owner

Manna and Pnueli proved a lock starvation-free and then pointed out that nothing
in that guarantee forbids admitting one participant ten times per admission of
the other. An eventuality argument structurally cannot yield a rate, because the
scheduling assumption underneath it is rate-free, so bounded overtaking, a retry
cap before escalation, and a ceiling on queue residency are separate claims
needing counting arguments. Treat every eventually-claim as an invitation to ask
what an adversary can do while honouring it.

Manna's other requirement is that a progress argument name the party responsible
and keep it named. Fairness promises that one continuously-possible action
eventually runs, never that a rotating cast of willing helpers converges. That
rotation is the exact shape of livelock in real systems: every participant is
always ready to do something useful, help is always available from somebody, and
nothing finishes. Any state where responsibility can migrate without progress is
the prime suspect.

## Prefer the tool that hands back a reproducer

McMillan states the epistemics plainly. A positive result is conditional on the
model being faithful, the property being stated correctly, and the property set
being complete, none of which the checker verified. A trace inherits none of
that, because you can walk it against the real artifact. So distrust green
results in proportion to how much modelling stands between you and the thing,
and prefer, wherever you can build it, the tool that returns a witness over the
one that returns a verdict.

Two consequences. First, stop designing interfaces that return booleans. A
checker, solver, or type pass that gives up has necessarily constructed a
reason, and the reason is denser than the answer and automatically fitted to the
instance; ask what yours knows at the moment it fails and make that addressable.
Second, sampling fails structurally rather than weakly against bugs that need a
long coordinated sequence, since the chance of stumbling onto a particular
ordering decays exponentially in the number of events that must line up.
McMillan's case study found a deadlock at depth thirteen that random simulation
would have needed somewhere between years and millennia to hit. When the failure
class has that shape, more fuzzing buys nothing and the method has to change.

## What makes a claim cheap to establish

Manna's cost model is the one to carry into design: the price of an invariant is
proportional to the number of places that write the state it mentions, not to
the size of the program. A claim about state written from one place is nearly
free forever; the same claim about state written from twenty places is twenty
arguments, re-run on every change, and no technique recovers the difference. So
count writers before adding an invariant and read a large write set as a reason
to relocate the state rather than a reasoning problem to brute-force.

Abrial found the same signal from the other end: when an argument gets hard,
two of the three available explanations are diagnoses of your design and only
the third is about the tool. Difficulty is a metric to watch during development
rather than a verdict delivered at the end. Clarke's contribution is upstream of
both, and it applies to code review and test planning as much as to proof: fix
the smallest description that can still answer the question before you start,
because a model that faithfully keeps detail the property cannot observe is both
more expensive and no more trustworthy. And Hoare offers a falsifiable test for
an abstraction, replacing the unfalsifiable ones. It has earned its place when a
second implementation with a genuinely different cost profile would be correct
against the same description. If only one realization makes sense, the
description is a paraphrase of the implementation and will change every time it
does.
