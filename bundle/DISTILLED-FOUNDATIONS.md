# Choosing Which Questions Stay Answerable

A third set of claims, from the people who worked out which questions about a
system have answers at all. Their results are remembered as a fence around what
software can do. The useful half is the opposite: a way of deciding, before you
build, which properties you will still be able to establish afterwards.
Analyzability is bought, and it is spent.

## Every capability is paid for in questions you can no longer answer

Rabin's automata work extends a formalism one notch at a time and watches what
breaks. Give the device a second input and the basic questions survive, but the
describable relations stop being closed under conjunction, so two requirements
can no longer be combined into an artifact of the same kind. One notch further
and even "does this ever succeed" becomes unanswerable. The ordering is the
instructive part: compositionality goes first, decidability second. So the
earliest symptom of an over-powerful config language, query dialect or policy
engine is not that verification became impossible. It is that you can express
each rule and cannot express their conjunction. Gödel sharpens the diagnosis:
decidability is usually lost to feature interaction rather than to any single
feature's power, which is why reviewing extensions one at a time never catches
it.

Price each capability in lost questions. Name what you rely on being able to
establish, such as whether a rule can ever fire or whether two policies combine
into a policy, and check what the extension invalidates. One that costs
compositionality belongs at the edge rather than in the core vocabulary. One that
costs decidability has converted your artifact into something you can only run
and observe, and everything above it inherits that.

## Bounded state is a verification asset, not just a performance property

Rabin's case for deliberate weakening is that a finite configuration count
generates the proofs: run longer than the number of distinguishable situations
and one must recur, so any witness can be cut down. Bounding a queue, fixing a
retry count, forbidding unbounded recursion, replacing user-supplied logic with a
restricted vocabulary, each trades expressive reach for claims that hold over all
inputs rather than the ones you tried.

Kleene makes the count constructive. A machine with finitely many finite parts
distinguishes only finitely many pasts, and the number is fixed before any input
arrives, so what a component knows is a partition over histories rather than a
recording of one. Ask what decisions it must make, derive the coarsest
classification of history sufficient to make them, and make that the state. If
the classification grows with runtime, no bounded implementation exists, and you
have learned it before writing code instead of after enlarging the state and
hoping. Hartmanis turns the count into a lower bound: compare how many pasts must
stay distinguishable against how many the budget can represent, and when the
first outgrows the second no ingenuity closes the gap, because the shortfall is
carrying capacity rather than strategy. A streaming system that cannot answer its
query in bounded memory is not badly written, and profiling will never show why.

## Read the hypotheses before you quote the impossibility

Gödel, who proved the two most famous limitative theorems in logic, spent a
conference talk arguing that limitative theorems are routinely over-read. They
are conditionals, their hypotheses are load-bearing, and transmission drops the
hypotheses first. Is your rule set actually fixed, or extended by hand every
release? Do you need the property for all inputs, or the ones you receive? Do you
need a decision procedure, or one that answers correctly when it answers and says
"unknown" otherwise? When you loosen a hypothesis, name which one and say you are
solving a nearby problem. The move is legitimate because it is stated.

Post shows the payoff inside the paper proving his correspondence problem
unsolvable. Before the proof he disposes of whole families of instances by
inspection: if each string on one side is longer than its partner the lengths
cannot match, and if each pair disagrees on its first letter no sequence can
begin. Cheap partial procedures come from finding the conserved or monotone
quantity, and the instances forcing undecidability are constructed adversarially
rather than encountered. Halting is undecidable and every serious compiler still
warns about a great many infinite loops. Hartmanis supplies the failure from the
other side: a barrier to a technique gets upgraded by repetition into a property
of the problem, then into a reason not to try, while counterexamples sit in a
well-known journal filed as contrived. A wrong pessimistic belief is load-bearing
in a way an optimistic one is not, since the optimistic one is refuted by the
first attempt and the pessimistic one prevents that attempt.

## Ask where the difficulty went, and what each guarantee consumes

Turing constructs a system satisfying a strong completeness property and then
dismisses it himself, because determining which input to hand it is exactly as
hard as the original problem. A formalism does not measure the difficulty of its
own preconditions. A type system that proves anything given the right annotation,
a verifier needing an invariant nobody can find, a cache always correct given
correct invalidation: each is a true guarantee resting on an obligation that may
carry the whole original difficulty. Leaving non-mechanical steps is legitimate;
leaving them unmeasured is not.

Church states the matching requirement before presenting any decidable special
case. A solution in a special case is two procedures, one deciding membership in
the class and one deciding the question for members, and he states the first
explicitly rather than leaving it a courtesy. Write the restriction down as a
decision procedure and price it, instead of leaving it an adjective in the
surrounding prose. A fast path guarded by a sortedness check on every call, or by
a residency test costing the miss it avoids, is not a fast path.

The same accounting runs over what a result rests on. Hilbert organized a book
around naming, for each theorem, which assumptions the derivation used and no
more, withholding continuity to show the area theory never needed it. An
assumption you did not know you were using cannot be removed or replaced, and it
narrows where the result can travel. Péter fixes the trusted base narrowly and
rebuilds every borrowed convenience inside it, because a result holding "given
this library" is weaker than one holding given a handful of primitives, and the
difference only appears when someone writes the base down. Kolmogorov adds the
placement rule: put the assumption you cannot justify in one named place,
introduced only where it is needed. When a module's correctness quietly relies on
messages arriving in order, that assumption is part of the module whether or not
anyone wrote it down.

## Quantifier order is the entire guarantee

Church stops mid-introduction to make this unmissable, choosing an example where
the two orders differ in truth value and pointing at continuity against uniform
continuity. Inner existentials may depend on the universals preceding them;
existentials placed outward cannot depend on anything to their right. For every
request there is a worker that can serve it, against there is a worker that can
serve every request: the first is a scheduling property, the second a capacity
claim, and one sentence in a design document gets read both ways by two people in
the same meeting. For each input there is a timeout under which it completes,
against there is a timeout under which every input completes: the first is
compatible with unbounded latency, and it is what most systems provide. Rewrite
any guarantee with its quantifiers explicit and in order, then check each
existential against what it may depend on.

Rabin supplies the adversarial half. A construct expensive to break on average is
worthless if a small minority of cases is easy, because an opponent is not
obliged to accept the inputs you hand him and can retry until he lands in the
easy fraction. Averaging assumes a sampler with no stake in the outcome. Name the
population a bound is quoted over and ask who can steer inputs out of it; treat a
mean as capacity planning, never as a safety property.

## An equivalence is scoped to the operations you had in mind

Hartmanis found that two characterizations provably equal in the base system come
apart the instant it is extended, because the extension is not a passive
addition. It magnifies exactly the structural differences the equivalence proof
was allowed to ignore. Two libraries interchangeable under normal use diverge
under cancellation, or introspection, or when something must observe intermediate
state. Two storage layers with identical query semantics diverge the moment
replication or a change feed appears.

Church makes the same observation about his own work, in a footnote, having just
proved two formulations of the propositional calculus equivalent in the strongest
sense available. They have exactly the same theorems, and yet one is complete in
three senses and the other in none, because moving the substitution rule into the
shape of the axioms dropped a constraint no theorem exercises. A test suite
measures the theorem set. It cannot measure how a system responds to being
extended, because that response is a property of the rules and the tests see only
consequences. So when you replace a mechanism with an equivalent one, the
equivalence you established is the weak one, and what is left over is what the
old mechanism ruled out that the new one does not.

## What a specification can pin down at all

Chaitin's result is a conservation law. Treat a set of assumptions as a program
grinding out its consequences and measure it by that program's size; no
conclusion whose content exceeds the assumptions' content by more than a fixed
amount is reachable, however long the derivation runs. The bound is stated in
terms of the size of the reasoning system, so it covers a specification or a type
discipline as much as arithmetic. A specification small enough to hold in your
head does not determine a system carrying orders of magnitude more content, and
no verification technology repairs that, because the gap is informational rather
than technological. Either shrink the system's content until the specification
covers it, or accept that the uncovered part gets handled some way other than by
reasoning.

The counting argument underneath explains why so much material refuses to
compress. There are far fewer short descriptions than things to describe, so
incompressibility is the normal condition and compact form the rare find. When
tax rules, protocol quirks, hardware errata or accumulated business policy resist
folding into a general mechanism, the default explanation is not that the search
was insufficiently clever. Budget that search and then stop, and store the
irreducible material rather than building a generator larger than the table it
replaces. Because incompressibility is the background condition, every real
compression is evidence of a constraint in the domain that was not obvious, worth
real effort to find and worth protecting once found.
