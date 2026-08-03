# Small Mechanisms and the Paths Nobody Walks

A third set of claims, from people who built operating systems and judged a design by
what it costs everyone downstream rather than by what it can do. Two questions run under
all of it: what does this mechanism force every caller to reconstruct, and which of its
paths does anybody actually walk. Both have answers you can go and find.

## Start from the failures, not the structure

Reading a codebase to understand it produces a shallow model, because nothing forces you
to separate the parts you understand from the parts you have merely accepted. Cutler's
route is the inverse: take the failures and build an account that explains them, since
every gap in the account announces itself as the place the trace goes cold. In an
unfamiliar repository that means the bug tracker, the commits whose messages say "fix",
and the code around them, before the architecture document. Look for the pattern across
many failures rather than reasoning hard about one.

Cutler's second half is the expensive one: the fault need not live at the layer you are
searching. Months spent hunting a bug in software that was never in the software leave a
person willing to entertain "the abstraction is lying to me" as a hypothesis rather than
an excuse. Budget how long you will keep interrogating your own code before you start
questioning what sits underneath it.

## A path that is not walked is not correct

Any system with several configurations has one it treats as normal, and everything else
is reached by a path labelled remote, cross, foreign, or legacy. That path rots at a rate
set by how rarely it is taken. Thompson's response is to abolish the privileged case
rather than test it harder: in Plan 9 there is no plain compiler command, every build is
a cross-build, so the general path is the one everyone is already on. In ordinary service
code the move is to delete the in-process shortcut beside the RPC path, the "if local,
skip serialization" branch, the dev-only auth bypass, and pay the small uniform tax
instead of defending a branch most contributors will never run. Where a fast case must be
kept for cost, keep it as an implementation of the general interface, never as a second
interface.

Ritchie supplies the counting rule. Take every general-purpose mechanism you own and
count its distinct callers. One caller means the abstraction is a disguised special case
and should be renamed as one. Two callers using it obliquely to its stated meaning means
replacing it with what they were really asking for. His example is a general
message-passing facility with exactly two users, both abusing it, which carried a real
bug for years precisely because nothing exercised the paths that would have exposed it.
Unexercised generality is not capability held in reserve, it is a claim nobody has
checked, and a client that does not exist cannot find the bug waiting in the part nobody
runs.

Corbató points the same instinct inward: build the system out of what you hand the user.
Refuse to maintain a second, inward-facing copy of a facility, and read a request for an
internal-only path as evidence that the public one is wrong. A mechanism you are willing
to build your own internals out of is one whose defects you will find, because you are
its heaviest user.

## Capability belongs low, shape belongs high

Ritchie designed the substrate by subtraction. Before adding a concept to a foundational
interface, ask whether some layer above could supply it; if it could, it does not belong
below, because structure imposed at the bottom is structure every client must either
accept or work around, and the workarounds are the real cost. Accept that the naive
caller then pays overhead a structured design would have avoided, and answer with a small
helper on top rather than a richer interface underneath.

Pike gives the test in a line: when you add a facility, are you adding a capability or
standardizing a shape? Capabilities belong low where everything can reach them; shapes
belong high where they can be replaced without anyone's permission. A pattern implemented
low down is a pattern everyone above must adopt, which is how a system acquires a
mechanism that covers eighty percent of cases and blocks the rest.

Thompson prices the other direction. A primitive that carries no state has handed that
state to every caller, separately, forever. The cheap memoryless version is frequently
right, but its correctness now rests on facts outside itself, so when you choose it record
in the same breath which external assumption just became load-bearing, and treat that
assumption as part of the interface.

Pike also inverts the usual instinct about errors. If you find yourself writing the same
check at every call site and then doing nothing with it, the error return was the mistake.
An error signal is a request for a choice and is worth its cost only when callers have
different useful answers; when the honest answer is the same everywhere, encode it in the
operation and make the operation total. Keep the substituted value distinct from any
pre-existing "unknown", and write down what the totality lost.

## Audit the property, not the change

Ritchie's sharpest observation concerns rules that are each perfectly logical. Unix
directory and file permissions never reference one another, so together they let a file be
emptied inside a directory that forbids writing. No rule is violated; the property anyone
wanted simply is not implied by the conjunction. Review a permission model, a feature-flag
precedence order, or a set of retry rules by asking what its closure permits and comparing
that against the short list of properties you actually want. Rule-by-rule review cannot
find this class of defect, because nothing is locally wrong.

Wilkes generalizes it across time. A structural property decays through additions that
individually violate nothing, so the property has to be recomputed from scratch,
mechanically, against the whole. He also names the trap: the drift becomes visible at
exactly the moment the code starts working and its clients depend on it, when the
incentive to repair has fallen to nearly zero. "We will clean up the structure once it
works" is a plan not to clean it up.

Rashid turns the same instinct on defect lists. For each symptom, ask what would have to
be true of the representation for that symptom to be impossible. If the answers converge,
four scheduled fixes collapse into one change that also repairs things nobody had noticed.
His recurring culprit is structure inside a name: an identifier assembled from the pieces
that locate its referent is a schema, exactly as hard to change later as a database
schema, and forgeable besides.

## Meter the quantity nobody is metering

Corbató's example is the telephone plant. Replacing copper with fiber was justified purely
on capacity per dollar, and the redundancy that vanished had never been a line item
because it was a side effect of the old technology's inefficiency. Treat every
consolidation as a change to the failure model and not only to the cost model, whether
that is merging two services, collapsing two regions into one, or replacing several modest
components with a single excellent one. Ask which correlated failure just became possible,
and what would reveal it before the day it happens.

Denning supplies the calculation to run before any argument about eviction, pooling, or
admission. Differentiate throughput with respect to miss rate. When a miss costs orders of
magnitude more than a hit, which is what a network round trip against local memory amounts
to, efficiency near the good operating point is a cliff rather than a slope, and a policy
that observes degradation and reacts is too late by construction. Where the derivative is
that steep, stop tuning the rule and build the precomputed admission bound with a reserve
held back. His related rule: a shortage in one resource announces itself as surplus in
another, so never tune a resource because its own meter looks bad.

Judge every eager fetch by whether its trigger is independent of whatever makes the
prediction stale, rather than by average hit rate (Denning again). Cache warming,
connection pre-establishment and eager initialization tend to fire at exactly the moment
the thing they predicted has changed. Average-case accuracy is the wrong statistic;
conditional accuracy at the instant you would act is the right one.

## Trust is a property of construction, not of text

Thompson's compiler argument generalizes to anything whose current state was produced by
an earlier version of itself: package managers, CI, code generators, models. Reading the
source stops being a trust-establishing activity and becomes one input among several. The
questions that move are about provenance, and two independently derived build paths
arriving at the same artifact is evidence that reading cannot supply. His companion claim
is about depth: order your worry by how far down a defect could sit before you order it by
how clever it is, because detection probability is dominated by how few people ever look
at that layer. Stating the assumption underneath the layer you checked is usually worth
more than strengthening the layer you checked. Saltzer's terminus is that no system
bootstraps its own trust, so the honest output is a named stopping point rather than a
claim of coverage.

Torvalds draws the reader-facing version of the same line. An abstraction may hide data;
it may never hide control flow. Anyone scanning code commits without thinking to the
belief that a name followed by parentheses returns to the next statement, and a construct
that violates this invalidates every inference drawn downstream of it, which documentation
cannot repair because nobody consulted documentation. Apply the category test to
decorators, context managers, macros and middleware: what will a reader assume from the
shape alone, and is every one of those assumptions true?

## The counterweight

Cutler is worth holding against everything above. A small design wins because it is cheap
to get right under scarcity, which is an instrumental justification, and it expires when
the constraint does. Whoever spends the surplus on outcomes collects the advantage, and a
competitor who accepts a more complicated design and has the budget to verify it is not
making an error. The corollary bites hardest: the complete version of a mechanism is
sometimes less total work than the trimmed one, because the trimmed one forces every
consumer above it to change. Check the reflex to strip against total cost including
dependents.

Wilkes gives the discipline that keeps this honest. Take an instinct you hold, such as
uniformity or minimality or regularity, and name the multiple you would pay for it when
other things are not equal: how much extra total material buys making everything the same,
and at what scale. An instinct you can price becomes an engineering constraint. One you
cannot price was never doing any work; it was vocabulary for approving decisions already
taken on other grounds.
