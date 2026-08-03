# What Holds Without Running It

A third set of claims, from people who asked what can be established about a
program without executing it. An abstraction is worth the set of things it lets
you stop checking, and that set is decided by what your system cannot say,
observe, or name.

## Settle what counts as the same before designing the thing

Milner inverts the usual order. Fix indistinguishability first and let the model
be whatever that forces, because nothing in a structure's construction tells you
it is the right one, whereas you do have opinions about whether two
implementations should be interchangeable and can settle a dispute by describing
a situation that tells them apart. So before choosing an interface or a schema,
write down what an adversarial client may notice: timing, partial results,
ordering, whether a retry is visible, whether an intermediate state is readable,
whether it can deadlock. What follows is derived rather than argued, and "is this
abstraction leaky" gets an answer instead of a debate. The relation must also
survive placement inside a larger program: two components behaving alike in
isolation are not thereby interchangeable, since substitutability quantifies over
every surrounding context.

Scott's cheap version for data: could every discriminating mark in a
representation be replaced by a different one throughout, with nothing above the
layer that reads them changing? If not, something upstream has taken a dependency
on the spelling, and a change that should have been local will not be.

## Every capability is paid for out of a law

Landin's test ends the argument about whether an addition is fundamental.
Anything introduced by definition over an existing system inherits that system's
equivalences, so it cannot make a valid interchange invalid. To show an addition
is genuinely primitive, exhibit a law that holds throughout the host plus two
programs the law calls interchangeable that observably are not. The laws that
break are nearly always about aliasing, ordering, identity, or capture of
surrounding context. Run it in reverse when someone insists a feature is
essential: if no law breaks, it is convenience, and convenience belongs in a
layer that cannot complicate the core.

The accounting matters more than the verdict (Reynolds): before adding a
construct, name the theorem that was load-bearing and check it against it.
Landin's own example is one everybody has lived through. Adding mutation costs
the substitution of a name by what it was defined as, so every argument resting
on that must be re-scoped, and the obligation is to draw the region where the law
survives sharply enough that a reader can tell which side they stand on. A rule
with exceptions is a hypothesis, and every use of it carries the checking
machinery around. Strachey's corollary is a
selection criterion: choosing between representations of a state machine, a query
plan, a config format, ask not which describes the domain most faithfully but
which makes the equations you want to prove fall out by calculation.

## A new observer falsifies old refactorings retroactively

Every identity a codebase leans on (this cache is transparent, these two
orderings are equivalent, this retry is unobservable) is quantified over the
surroundings the system can build. Milner's demonstration is that adding an
operator adds surroundings, and previously sound equations go false without
either side changing. Your new surroundings are a metrics endpoint, a debug log,
a second consumer on a queue, an API exposing an intermediate state, a client
sensitive to latency. None touch the refactored code and any can
invalidate the reasoning that justified it, silently, with nothing near the new
observer looking wrong. Treat shipping an externally visible capability as a
re-validation event for the identities that assumed it away, and when one has to
be weakened to survive the new observer, resist special-casing it: the weakened
form was probably the true statement, the strong one an accident of what you had
not yet built.

## An invisible step is not an absent step

Declaring a step internal removes it from every interface and from no contract.
Milner's point is precise: an internal step can consume a choice, so a system
that advances past a branch point without emitting anything has given up options
a client was about to exercise, and getting stuck is observable. An internal
retry, a buffering hop, a background flush, a lazily initialized resource, an
await that yields the scheduler. Each appears nowhere and each can change whether
the system is still willing to do the next thing asked of it. The question is
never whether anyone can see the step but whether it forecloses anything: commits
to a branch, resolves a race, consumes a token. The failures are hangs and lost
liveness rather than wrong answers, so they get found late and blamed on load.

The same hazard voids the cheapest contract available. Reynolds states the
asymmetry plainly: a state-changing procedure's contract is a claim about
behaviour over time that has to be proved from the body, while a value-returning
function's contract is that a call equals the body with the arguments put in,
which is not proved but is what the declaration means. That identity holds only
if calling does nothing else, so one memoization write inside makes every
substitution built on it unsound.

## Buy the guarantee by withholding the capability

A generic operation can be uniform, doing one thing blind to what it was
instantiated at, or a bundle of unrelated behaviours selected by inspecting the
type it was handed. Both satisfy the same signature and only the first supports
reasoning from it alone. Reynolds's move is not a check added to a type system
but a capability deliberately left out: provide no way to branch on a type and
the ad hoc variety becomes inexpressible rather than discouraged, at which point
the signature stops being documentation and becomes a theorem. A
handler that cannot inspect what it was given has a contract you can rely on
without reading the body; one that switches on the runtime class has none.

Girard supplies the failure mode when you skip this. "It works for every type I
tried" is not evidence the generic version is sound, because a generic operation
is not the family of its instances but one thing required to behave the same at
all of them, and no instance-by-instance evidence can test that uniformity. Ask
what the generic version lets a caller do that no single instantiation permits.
The answer is usually self-application, reflection, or comparison across
instantiations, and the break shows up nowhere near the addition, as the loss of
a global property rather than a type error.

## Hiding is about what the client can name

Marking something private hides its existence and not its identity, and identity
is what leaks. Milner's mechanism is unforgeable naming: the hidden thing gets a
fresh identity appearing nowhere else, so the equations a client would need are
unprovable rather than prohibited. The test is to ask what a client can construct
that is provably the same as your internals. A shared struct definition, an
exposed integer id, a serialization format, an alias resolving to a common
primitive. Removing the reference is not enough while an equal thing is
constructible.

Cardelli adds the case where parts point back. A component that can consult the
container it lives in has its meaning stated in terms of the whole, so refining
it stops being a local act and the ordinary rule that improving a part improves
the aggregate goes unsound. Two habits follow. When you want to relax an
invariance restriction, find the back-reference forcing it; there is usually
exactly one. And never detach such a component and offer it standalone, since it
carries an unstated premise about its context that anyone may then violate.

## Build totally, judge separately

Curry rejects making bad terms unformable, on the ground that a discipline which
forbids forming them can never account for them. Construction is made total and
acceptability becomes a further question asked about the thing, not a gate
deciding whether it exists. The consequence cuts against a popular instinct: any
system that makes bad states unrepresentable also makes them undiagnosable, and
when one shows up in production anyway you have no vocabulary for it. Parse into
a total representation and let validity be a predicate you can query, log and
refine, not a constructor that throws and destroys the evidence.

Scott and Strachey do the same for partiality. Rather than treating "no answer
yet" as a defect outside the value space, handled by side conditions and error
channels, enlarge the space with a value meaning no information yet and order
values by how much they tell you rather than by equality. A partially-known
object becomes something you can compute with, and the ordering hands you a
sanity rule: an operation must never retract a commitment when given more input,
which rules out branching on whether something is known. Scott's rider is what
practice gets wrong. Conflict gets its own value, and conflicting is not the same
as merely unrelated.
