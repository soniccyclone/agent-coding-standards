---
type: tension
title: "Whether a type can be a part of one universal domain, or must be a rule about what may be said"
figures: [scott, reynolds]
lessons: [scott/put-everything-in-one-universal-domain-and-define-the-rest-as-subspaces, reynolds/a-type-restricts-what-you-may-say-not-what-values-exist]
status: resolved-by-llm
tags: [tension]
---
# Whether a type can be a part of one universal domain, or must be a rule about what may be said

## The decision
You need a mathematical setting in which to say what a language with data types
means. The economical move is to build one domain large enough to contain
everything the language can produce and identify each type with a distinguished
part of it. The question is whether that construction is a free simplification
or whether it silently licenses conclusions the types were introduced to
forbid, in which case the setting has to be chosen differently no matter what it
costs in machinery.

## Scott: one domain, and the parts you need are cheap to pick out
[Put everything in one universal domain and recover the specific types as subspaces of it](../figures/scott/lessons/put-everything-in-one-universal-domain-and-define-the-rest-as-subspaces.md)
argues the move on two independent grounds and insists on both. Structurally,
nothing is lost: every reasonable space embeds in the universal one and every
function on a part extends to the whole, so working inside its subspaces
excludes nothing you wanted. Practically, the subspaces you actually need are
easy to define, in the same language as ordinary values. The specific choice
matters more than the size. Taking sets of integers as the ground gives a
lattice and a topology by inspection, so the heavy apparatus arrives later as
analysis of what was already done rather than as a prerequisite, and the link to
computability needs no translation. Because it is one space and not a hierarchy,
you can prove theorems before settling which category you are working in or
whether to restrict to the computable. Self-application stops being paradoxical
because one object is simply being used two ways. Scott names the hazard
himself: an element is an integer, a set, a relation or a functional depending
only on how the surrounding expression treats it, nothing prevents mixing
interpretations, and the discipline he asks for is that you owe an account
whenever you do.

## Reynolds: a type is what you may not say, and a subset of a universe cannot forbid anything
[A type is a restriction on what you are allowed to say, not a description of which values exist](../figures/reynolds/lessons/a-type-restricts-what-you-may-say-not-what-values-exist.md)
starts from two lecturers who build the same abstraction on incompatible
representations, talk past each other all term, and never contradict each other,
because both stayed inside the sentences that hold under either construction.
The test that falls out is adversarial: could someone swap your representation
for another legitimate one overnight and leave everything you wrote still true?
A discipline like that earns its keep entirely through what it forbids, and the
forbidden things are meaningful at the representation level. Whether two types
overlap, and what their common members are, has to become unaskable rather than
merely false, because the underlying sets certainly do intersect and a different
valid representation gives a different intersection. Make a type a subset of one
big universe and those questions come back well defined, which is the opacity
you were modelling, gone. Hence the methodological rule: use the weakest setting
that supports the phenomenon, and do not import machinery from an unrelated
difficulty, because abstraction was practiced correctly for centuries by people
who would not have understood a partial value.

## Resolution
**LLM DECISION — Nathan may overturn.**

Both claims are true because they are about different things, and the seam is
that an abstraction boundary is not a value and therefore cannot survive or fail
to survive an embedding of values. Scott's losslessness is a statement about
denotation, quantified inside one model: everything the language can compute has
a meaning in the universal domain, and no function you wanted has gone missing.
Reynolds's loss is a statement about a family of models: an abstraction boundary
is the set of claims invariant under change of representation, so it is a
relation between interpretations, not an object in any one of them. Nothing in
the value structure of a single domain was ever going to encode it, which is why
Scott can be entirely right that nothing is lost and Reynolds entirely right
that the boundary is not there. The mapping is that you build Scott's domain to
say what a program means, and state abstraction one level up, as preservation of
relations across the domains that different implementations induce. The error
Reynolds is attacking is answering a question about the abstraction by looking
inside the model, and Scott bans that too, both in this lesson's demand for an
account whenever interpretations get mixed and directly in
[keep the apparatus you reason with out of the domain you model](../figures/scott/lessons/keep-the-apparatus-you-reason-with-out-of-the-domain-you-model.md).
He would accept the rule and deny that his construction is what violates it.

That leaves the case the seam was supposed to cover: one language with both
general recursion and data abstraction, where you cannot keep the two settings
apart. It does not force a choice. The resolution the technical history actually
produced is one domain-theoretic model with a layer of logical relations over
it, and the price of Scott's apparatus shows up there and only there, as the
admissibility conditions the relations must satisfy to survive the limits that
recursion introduces. That is a real cost and Reynolds is right to have named
it, but it is a cost paid in the relational layer, not a reason to refuse the
domain underneath.

On the narrower question Reynolds actually poses, which setting to use when
explaining an abstraction boundary, he wins outright and Scott's own
methodological rule agrees with him. Explaining opacity in a setting rich enough
to make intersections well defined means every reader must be told which
available conclusions not to draw, and a setting whose correctness depends on
readers declining to use it is the wrong setting.

The shape here recurs in
[when a construct is provably redundant](simulability-kills-a-construct-vs-simulability-proves-nothing.md).
An argument of the form "X embeds into Y, so nothing is lost" only ever
establishes losslessness for the property the embedding was built to preserve.
Behavior survives a simulation and intent does not; values survive an embedding
and opacity does not. The person holding the theorem is entitled to a narrower
conclusion than the one they reach for.

**Strongest counter-argument:** the claim that the boundary lives above the
model is fine for metatheory and possibly useless for enforcement, which is what
a working type system is for. If the model licenses an intersection, something
in a real implementation will eventually ask for it, through reflection, a
debugger, a foreign function interface, a serialization format or an unsafe
cast, and the quantify-over-representations move protects only the reader who
was already being careful. Reynolds may be making an operational point rather
than an aesthetic one: choose a setting in which the illegal question cannot be
formed and the enforcement comes free, choose the permissive one and you are
relying on convention that the first pragmatic feature will breach. If that is
right, then for the design of a language whose types must actually hold, as
opposed to the semantics of one already designed, Reynolds governs the modelling
question too and the layering proposed here is a comfortable evasion.
