# What Counts as Evidence That It Works

A third set of claims, from the people who spent careers on what establishes
that a system is right. Their conclusions are largely negative and about scope:
any result you get is about a model, under assumptions, of the properties
somebody bothered to state. The leverage lives in those three qualifiers rather
than in the checking.

## A passing check is a claim about a model you built by hand

Analysis never touches the running thing, only a description of it, so every
result reaches the artifact through a relation some human asserted and nobody
verified. Sifakis's point is that this relation is where errors concentrate and
is the one part of the pipeline never audited, so derive the description from
the artifact mechanically rather than maintaining it alongside. A state machine
in a comment or a load test written against a mock is an unverified transfer
relation under whatever confidence you take from it, and where you cannot
generate it, say out loud that model and code can drift apart without either
looking wrong. Clarke narrows the same job from the other side, which bears on
review and test planning as much as on proof: model only what the claim can see,
since keeping detail the property cannot observe costs more and buys no trust.

Sifakis pairs this with an asymmetry. That a requirement set is consistent can
be decided mechanically; that it is complete has no procedure and no definition.
So confidence should scale with how much of what matters got written down, not
with how much of what was written down passed. Absence from the analysis looks
exactly like success.

## Name the edge, then cover outside it with a different blind spot

Abrial's honest formulation is relative correctness: these failures cannot
occur, under these stated assumptions about the environment. The assumptions are
part of what you ship rather than scaffolding to discard, because they draw the
line outside which the guarantee says nothing. Cover that outside with a
mechanism of a different kind, since another argument over the same model only
re-establishes the same interior. Ask of every assurance claim what class of
fault its mechanism structurally cannot see: types cannot see wrong
requirements, requirement checks cannot see bit flips. Two mechanisms with
genuinely different blind spots beat doubling the strength of one, which is
Hoare's argument for rival checkers: independence does all the work, and two
implementations sharing a library or an author share their failures.
Abrial's other move: validate artifacts, not the machinery that made them. Check
a generator's output the way you would check hand-written work.

## Most of the specification is the part nobody writes down

Emerson observed that a stated problem carries the global obligations everyone
argues about, while the bulk of the content is local structure a diagram
conveyed and nobody transcribed: each participant is in exactly one state, the
only exit from waiting is inward, one participant's step cannot relocate
another. Ask what a stranger implementing from your document would fail to
already believe.

The second gap is possibility. A specification made only of obligations is
satisfied by a degenerate artifact, since fewer behaviours means fewer chances
to violate anything, and anything that generates or shrinks a system is under
pressure to collapse alternatives. A cache that must always return a correct
value may return one value forever; a retry policy that must eventually succeed
or report failure is satisfied by never trying. Write the reachability claims
beside the safety claims and check them first whenever you simplify, serialize,
or delete a path, since that is the move that breaks them while every obligation
still passes.

## Check that each decision's evidence had already arrived

Pnueli's sharpest observation is that ordinary specification records that one
thing depends on another and nothing about when the dependence resolves: fine
for a batch computation, fatal for anything ongoing. Locate the instant each
decision is committed and check that every quantity the argument leans on had
arrived by then. For eviction, scheduling, or any participant acting on a stale
view, the tempting analysis lays the whole trace flat, and the obviousness of
the right choice is an artifact of standing outside time. A failure here is
impossibility rather than imprecision, and the repairs are structural: delay the
commitment, permit a bounded lag, or make the error budget explicit.

His companion move is to split every interface into what this component writes
and what is written to it, then ask of each requirement whether the other side
can falsify it alone. Anything constraining the arriving data is an assumption
you owe separately, not a requirement you can meet. Vardi adds the version
inside one process: keep the predicate you reason with, which may quantify over
anything the global state permits, apart from the one a component can evaluate
from what it holds. A guard needing to know what other nodes have observed is a
correct claim in a vocabulary that cannot be compiled.

## Discharge the obligation while the decision is the only thing in view

Jones, having failed to prove a working several-hundred-line program correct and
found redevelopment cheaper, concluded that an argument is a by-product of
having built the thing a particular way rather than a certificate attached
afterwards. His test for a decomposition applies literally: can you hand
somebody one sub-specification and nothing else, and is there any circumstance
in which their correct work gets rejected later? If yes, the modularity is an
illusion that surfaces at integration. Whatever a final compatibility check
would test can instead go into the pieces' contracts at the moment of the split,
before any piece exists, so failure costs one decision rather than a subtree.
What keeps this affordable is that most obligations are vacuous: derive the list
of what must hold once, then scan rather than prove, stopping only where an item
resists.

Floyd's separation of "if it returns the result is right" from "it returns" gets
its usable form from Jones. The region your case analysis fails to reach and the
region the code diverges on are one set described twice, so when an argument
will not close over some slice of the input space, look at what the code does
there rather than for a cleverer argument.

## Eventually is not a bound, and progress needs a named owner

Manna and Pnueli proved a lock starvation-free, then pointed out that nothing in
that guarantee forbids admitting one participant ten times per admission of the
other. An eventuality argument structurally cannot yield a rate, because the
scheduling assumption underneath it is rate-free, so bounded overtaking, a retry
cap before escalation, and a ceiling on queue residency are separate claims
needing counting arguments, reached by asking what an adversary could still do
while honouring the eventually-claim.

Manna also requires a progress argument to name the responsible party and keep
it named, since fairness promises that one continuously-possible action
eventually runs and never that a rotating cast of willing helpers converges.
That rotation is the exact shape of livelock: everybody is always ready to do
something useful, help is always available from somebody, nothing finishes.

## Prefer the tool that hands back a reproducer

McMillan states the epistemics plainly. A positive result is conditional on the
model being faithful, the property stated right, and the property set complete,
none of which the checker verified. A trace inherits none of that, since you can
walk it against the real artifact. Distrust green results in proportion to how
much modelling stands between you and the thing.

So stop designing interfaces that return booleans. A checker, solver, or
analysis pass that gives up has necessarily constructed a reason denser than its
answer; ask what yours knows at the moment it fails and make that addressable.
And sampling fails structurally rather than weakly against bugs needing a long
coordinated sequence, because the chance of hitting a particular ordering decays
exponentially in the events that must line up. McMillan's case study found a
deadlock at depth thirteen that random simulation would have needed millennia to
reach; against that class more fuzzing buys nothing.

## What makes a claim cheap to establish

Manna's cost model belongs in design: the price of an invariant is proportional
to the number of places that write the state it mentions, not to the size of the
program. A claim about state written from one place is nearly
free forever; the same claim over twenty writers is twenty arguments, re-run on
every change, and no technique recovers the difference. Count writers before
adding an invariant, and read a large write set as a reason to relocate the
state rather than a reasoning problem to brute-force.

Abrial found the same signal from the other end. When an argument gets hard, two
of the three available explanations are diagnoses of your design and only the
third is about the tool, so difficulty is a metric to watch during development
rather than a verdict at the end.
