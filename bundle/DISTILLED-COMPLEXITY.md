# What It Costs, and Which Resource You Are Spending

A third set of claims, from the people whose subject was cost rather than
structure. Their finding in common is that a program's cost is a separate artifact
from its behaviour, with its own specification and its own ways of being silently
wrong. Most of what follows is what the correctness-first instinct does not do.

## Correctness leaves the cost unspecified, and something fills the gap

A soundness condition carves out a space of programs and does not pick one out of
it, so cost is the free parameter you are choosing whether or not you notice
(Knuth). Karp and Edmonds sharpen that into a rule you can apply today: wherever a
method says choose any, which pending item to process, which candidate to try,
what order a set iterates in, you have a family sharing a correctness proof and
nothing else, and you will eventually get its worst member. With the choice free,
the classical flow method's cost tracks the numbers in the data and on real-valued
input need not terminate at all; fix it to shortest-first and the bound depends on
the graph alone. The rule that buys the good bound amounts to servicing pending
work in arrival order, which you get for free if you happened to use a queue. So
performance routinely rests on a container choice nobody documented, no test
covers, and the next tidying refactor deletes. Where a cost claim depends on an
unspecified step, write the rule down next to the reason it works.

## Name the resource before touching the implementation

The measure decides the ranking, so it is a design decision, not a reporting
format; when a well-formed analysis contradicts what practitioners observe,
suspect the input model before the practitioners (Tarjan). Whatever you decline to
charge for sets the resolution of everything you can see, because a large fixed
term in every reading drowns the variable term that distinguishes the cases
(Stearns), so a metric reporting that a whole range behaves identically is a
hypothesis about the metric first. And a tight bound on one resource says nothing
about the resource that decides feasibility: fault-tolerant agreement sat at its
proven round floor for years while every protocol achieving it sent exponentially
many messages, so the problem was closed by the accepted measure and
unimplementable in fact (Dolev). Enumerate every resource whose exhaustion stops
the system, not the one the benchmark rewards. Yao's corollary for a changed
deployment shape: re-derive which quantity to count before re-tuning anything, and
accept that this is a new theory rather than a new constant.

## Input size is usually the wrong parameter

Cost that scales with the magnitude of numbers rather than the size of data is
exponential in disguise, since a value written in digits grows exponentially in
its digit count (Karp). The test takes ten minutes and nobody runs it: hold the
shape of the input fixed and scale only the magnitudes, larger prices, longer
timeouts, bigger quantities, more decimal places. If the runtime moves, your cost
is tied to values rather than structure, and someone will hand you a legitimate
input with big numbers in it. Edmonds adds that the precision the data is written
to belongs in the size measure, and that saying which of the three kinds of bound
you have (independent of the data, growing with precision, growing with magnitude)
is as much of the result as the number.

Valiant's version governs accumulated context: one local operation must not cost in
proportion to everything in scope, the whole registry, the whole config, all
previously defined things, or the system cannot go on accumulating context. A cost
parameter that describes the environment rather than the task is a defect to
engineer out, usually by making irrelevance expressible so unmentioned things are
absent rather than present with a default. And when a benchmark holds the
parameter that actually drives the work fixed, the benchmark is measuring the
fixture (Cook).

## Growth rate is categorical, but locate where it bites

Karp's own first defeat is the standard one: a synthesizer full of shortcuts each
shaving a constant fraction off a workload that multiplied per input variable, so
it solved toys forever. Small inputs are precisely where two growth curves are
indistinguishable, which is why the demo works and the fatal property is invisible
in the only evidence anyone gathered. Measure across a range of sizes and read the
shape rather than the numbers; when the shape is wrong the options are a different
mechanism, a different problem, or an approximate answer, and polishing is not
among them.

Hartmanis supplies the cheapest lower bound available, and it is not asymptotic
reasoning. Look at the output before the code: how much must this emit, and what
is the most any one primitive can produce per step? That ratio is a floor under
every implementation in every language, and knowing it early is the difference
between renegotiating a requirement and burning a quarter on optimization. Read it
backwards too, since a small required output with a large measured cost is
somebody's waste and worth hunting. His second counting argument settles anything
that answers queries from a summary instead of the full history: count how many
distinct pasts the summary must tell apart against how many it can encode, and
when the first number wins, the design is wrong at the level of information and
the discussion about caches and indexes is already over.

Two counterweights stop this becoming asymptotics worship, both Tarjan's. A bad
bound usually lives in a region of parameter space rather than everywhere, so keep
distinct parameters distinct through the analysis and ask where your workload sits;
union-find is superlinear only when merges and lookups are of comparable count and
plainly linear when either dominates. And a worst case counts only if it is
reachable through legal operations and pays for its own setup. A state reached by
hand-writing a corrupt file or poking past the API proves nothing; the real
question is the cheapest sequence of permitted operations that gets there, and
whether that cost is small next to the damage claimed.

## The kind of guarantee is part of the contract

Interchangeable at the interface is not interchangeable at the guarantee (Tarjan).
An amortized bound is a claim about a sum, funding cheap steps from surplus banked
earlier, and a caller with a per-operation obligation will call at moments where no
surplus exists, so worst-case promises can only be assembled from worst-case parts.
A container with constant average lookup, an allocator with amortized reclamation,
a rate limiter with burst smoothing, a map that occasionally rehashes: each is a
legal substitution under a throughput obligation and an illegal one under a
tail-latency or deadline obligation, and neither the types nor the tests will say
so. Record which kind of bound a component has, and treat "amortized" as a
rejection rather than a footnote when you owe a per-operation number.

Adaptivity converts reads into writes, which is the bill no complexity analysis
mentions (Tarjan). Anything reorganizing on access, caches reordering on hit,
indexes rebuilding on query, JIT tiering, trees rebalancing on lookup, turns a pure
query into a mutation and costs you concurrent readers, shareable copies, clean
pages and snapshot stability while leaving the asymptotic bound untouched. Free if
one thread touches the data, a serialization point otherwise. Decide on that axis.

Every performance claim names an adversary, and the worst-case and distributional
assumptions give opposed verdicts on the same code, so state fast on what, drawn
from where, every time (Karp). Two from Dolev. A worst-case bound is not a licence
to charge for it on every run: keep the provisioned parameter and the observed one
apart, and ask of every retry budget, quorum wait, timeout ladder and
reconciliation pass whether it pays full price when nothing is wrong, which a
surprising amount of software does because the bound was compiled into a constant
early. And optimal is always optimal-within-a-class, the class being unnoticed
structural commitments such as work batched per round or decisions taken from the
current snapshot. Naming it turns a closed result into a list of assumptions worth
attacking.

## Moves worth reaching for before cleverness

When two methods have crossing cost profiles, do not characterize the crossover and
dispatch on it. Run both and take whichever answers first: the combined cost is the
pointwise minimum for a constant factor, with no dispatch logic to get wrong
(Stearns). Commitment is forced only when the methods contend for something that
cannot be duplicated, so the questions that matter are whether the loser is
abandonable without visible effects and whether the racers contend for cache,
bandwidth or locks, since the constant is a constant only if they do not.

Before adopting a heavier mechanism because your data is awkward, reshape the data
back inside the cheap tool's precondition (Karp, Edmonds). The move is licensed by
an invariance and finding the invariance is the whole content: work out which
transformations leave the output you care about fixed, and that set is exactly your
freedom to normalize, shift, rescale, canonicalize or partition into the fast
regime. A reshaping that helps but is not covered by such an argument is a bug with
good luck.

Where randomness sits matters more than how much there is (Karp). A fresh draw per
decision, random replica, random shard, random eviction victim, random tiebreak, is
what everyone writes first and is often worth no more than no randomness at all,
because the decisions accumulate no structure across time. One random ordering
fixed at startup and followed deterministically thereafter can be provably optimal,
collapses the system's entire nondeterminism to a seed you can log and replay, and
costs less. It holds only while the order stays hidden, so an adversary who watches
your decisions and adapts the load destroys the guarantee.

Classify candidate mitigations by which failure mechanism they close rather than by
how much each helped alone, and measure the cross terms (Tarjan): union-find's two
refinements each buy a log factor separately and something of a different order
together, because one prevents depth from being built and the other repairs depth
already traversed. Two mitigations attacking the same mechanism are worth about one.

When a cost can neither be derived nor measured by running the thing to completion,
sample it (Knuth). Walk one random path down the space, record how many
alternatives existed at each step, and weight what you see by the reciprocal of the
probability you saw it; the expectation is the true total, nothing is materialized,
and the probe can be built before the system it prices. Applies to query planning,
crawl sizing, migration sizing, any total that is a sum over a space too large to
enumerate.

## When the wall is real

"This cannot be done" is at least four statements and only some admit engineering
(Valiant). The information barrier says the evidence cannot pin down what you want.
The representation barrier says the goal is reachable but not while you insist on
describing candidates this way. The intrinsic barrier says no description helps.
The channel barrier says the feedback you agreed to accept, aggregate scores rather
than labelled cases, cannot separate what must be separated. Only the second
invites a change of representation, and a team reading a channel limitation as a
representation one will cycle through encodings forever with nothing in the
failures to explain why. Record also whether a barrier is unconditional or rests on
an unproven assumption, since the second kind has an escape clause.

Once the wall is real, refinement is not the answer. Change the specification
deliberately, dropping exactness, generality, or the assumption that inputs are
adversarial, and then prove something exact about what remains (Karp). Dolev's
finding is that the requirement is usually the biggest lever in the system:
"everyone agrees" is a family whose members differ discontinuously in price along
exactness, simultaneity and universality, so pin it at the weakest point the
application tolerates and solve that problem natively rather than wrapping the
strong mechanism.

One constraint on how anything complicated can get built at all (Valiant). Where
the process carrying the work cannot bank a loss against a future gain, a team
judged quarterly, an optimizer scored per iteration, a migration that must ship at
every commit, no step can be justified by a payoff three stages out, because the
mechanism cannot represent that argument. A plan whose early steps only make sense
in light of the final architecture will not survive contact with such a process and
must be re-cut into stages that each pay on arrival. If no such re-cutting exists,
that is not a communication problem, it is information that the end state is not
reachable this way.
