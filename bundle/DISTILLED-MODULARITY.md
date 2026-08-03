# The Program You Are Writing Is One Of Several

A set of claims from the people who studied what happens to a system across
versions, variants and years. Their shared move is to treat the thing in front of
you as one member of a set: the releases it will have, the deployments it will
have, the configurations someone will want without you. Nearly every decision
deletes members from that set, and the ones that delete most cost nothing on the
day you make them.

## Decompose by what you had to decide, not by what happens in what order

The default cut names the stages: parse, validate, transform, persist, emit. Those
boundaries coincide with moments in time, and time of execution is not a stable
property of anything. What is stable, or predictably unstable, is the list of
judgement calls: how data is laid out, whether a derived structure is materialized
or recomputed, what the external formats are. Parnas's point is that boundaries
around stages smear each judgement call across everything downstream, since a
representation chosen in one stage must be understood by all the later ones. So the
design act is listing the decisions you do not trust to stay put and giving each
exactly one keeper. Two consequences people resist: the parts will not line up with
phases, so nobody can narrate the system as a sequence; and interface complexity,
not part count, decides how much work proceeds in parallel.

Wirth stops this becoming speculative construction. A separation always looks
disproportionate against the operation it performs today, and that objection wins
unless you can name the change it exists to absorb: another source feeding the same
function, the same service over a different transport. Check both arrangements
against that named change and keep the partition only if the extension slots in
with everything already written untouched.

## Compare candidate structures by what comes out cleanly

Any design can be bent until it works. Parnas draws the deflating consequence:
functional adequacy carries no information when choosing among decompositions,
since every candidate eventually computes the right function. They differ in what
removal costs. Run that test out loud, naming for each part what would have to be
written if this deployment did not want it. Take a stage out of a chain of
transformations and you get a hole plus a shim whose only purpose is the hole you
made. Take an unused facility out of a layered structure and nothing happens.

The fact most casually leaked is cardinality. Presence, absence and number are
information, and a codebase where "there are exactly three of these" lives in
dozens of tables, loop bounds and switch arms taxes removal exactly as hard as
addition: deleting the third buys none of the savings that motivated it until you
rewrite precisely the sites you would have rewritten to add a fourth. Wirth guards
the opposite error. An extension mechanism is a bet that the variant set is still
open, and where the problem is understood and the structure internal you can
usually enumerate the kinds, which makes the tagged union with a documented field
table honest and the type-per-kind hierarchy a purchase nobody will consume.

## A dependency is a claim about correctness, not a record of who calls whom

Parnas defines it exactly: A depends on B when B being present and correct is a
precondition for A meeting its own specification. That cuts the call graph both
ways. You can call without depending, if your specification only obliges you to
issue a well-formed request. You can depend without calling, on the scheduler, the
assumed initialization order, the error handler everyone quietly relies on. Every
structural property you care about follows the correctness relation, and no import
graph shows you the second kind.

So before adding a call, ask whether your correctness now rests on that code or
only on your sending it a legal request; the second answer lets the callee be
absent without breaking anything above it. And when two parts each want to lean on
the other, do not reach for injection or an interface to break the cycle. Parnas
reads mutual dependence as evidence that one of them is really two parts: slice it,
rest A on the lower half and the upper half on A. Check acyclicity and information
hiding separately, too, since a system can be perfectly stratified with every
representational decision baked into the agreements between strata, which is the
usual shape of architectures everybody praises and nobody can change.

## The variants are not branches of the first one

The reflex with a second deployment, tenant or platform is to finish one and cut
the next from it. Parnas names the damage precisely: finishing the first required
settling questions only its circumstances posed, usually about layout, timing and
resource assumptions, and descendants inherit those settlements because undoing
them means rewriting code that already works. Each generation then carries
deficiencies traceable to an environment it never ran in, and nobody can say which
of its properties were intended. The alternative needs the common ancestor to be a
real artifact: a precise, deliberately incomplete design, which is the thing you
hand to colleagues and maintain, so a change is evaluated once for both variants
instead of reconstructed by diffing two codebases.

Liskov adds the timing rule. If you knew about the family before its members
existed, a named shared parent is cheap. If they already exist and somebody now
wants one routine spanning them, retrofitting an ancestor is a tax with no end
date, since every future type must be checked against it too; state the requirement
at the shared routine instead, as a demand on whatever it is handed. Either way the
parent is a budget of permitted variation spent in advance. Dahl's rule for a
general layer you own: publish the holes as a short declared list and keep the
sequencing in the general text, because base-class documentation explaining an
order the subclass must follow is evidence the base gave up control it should have
kept.

## Change is the steady state, and patching wins every individual argument

Lehman's claim is that decay is caused by the property that makes software
attractive. Editing is nearly free, so superimposing a change on what exists beats
re-deriving the structure that would accommodate it, at every individual decision
point, defensibly each time. No per-change discipline fixes an economics like that,
only expenditure that shows nothing in the release notes. And when a program
mechanizes some activity, deploying it moves the activity, so it invalidates its
own requirements by construction; churn there is not a failure of analysis and no
better up-front phase would have stopped it. Booch adds what this does to a
specification: once deployed, observed behavior including defects is the spec, so
fixing a real bug someone's workflow rests on is a regression regardless of
original intent. Brooks names the mechanism, which is that a running system always
answers, so what it does with a case the document never addressed becomes the
operative answer the moment anyone builds on it. Make the mechanism reject what you
declared invalid, because unpoliced permissiveness is a promise made without your
consent.

His batch-size result contradicts what is cheap for you. Size a change by the
re-understanding it forces on everyone attached to the system rather than by the
effort to build it, a cost that grows at least quadratically since each change must
be understood against all the others plus the unchanged remainder. A large sweeping
edit costs you almost nothing and costs its readers superlinearly. Parnas supplies
the matching review criterion: score a change by the exceptions it adds to the
design's organizing idea, not by whether it works. Once a locally correct change
sits where the idea says it does not belong, the system can only be understood as
the rules plus a growing list of places they were broken.

## Be able to say what you have ruled out

Any precise partial design determines a set of programs consistent with it, and
every decision shrinks that set, so Parnas asks that at any point you can state
which programs have been excluded. It is going well if the early exclusions removed
only programs nobody wanted, and if every decision that would exclude a program
someone might want was postponed or sealed where reversing it touches nothing else.
If you cannot say what has been ruled out, you do not know what you have decided,
and that is a claim a colleague can dispute, unlike a claim about elegance. The
same accounting applies to an interface: every guarantee it makes, however true,
subtracts from the set of implementations that stay legal, so enumerate what your
draft forbids and check each exclusion was intended. Royce
generalizes it to structure: characterize any layered arrangement by the distance
between where a class of mistake is introduced and where it becomes visible, and by
how much finished work the correction destroys. Booch's complement is that
architecture is only the decisions whose reversal is expensive, that the set is
small even in enormous systems, and that it moves as volume, platform shifts and
third parties arrive, so it must be re-identified rather than inherited.

## The model is a choice with an author

Nygaard refuses to let "system" name a feature of the world. A stretch of reality
becomes a system when somebody, for a purpose, elects to see a whole made of parts
and picks which properties count. Two competent designers produce incompatible
decompositions of one domain with neither having erred, so read an existing model
as evidence of what its authors cared about rather than as a description of the
domain, and expect it to be locally faithful yet wrong if the properties it
discarded are the ones the problem turns on. His sharper warning is that whoever
supplies the vocabulary has already settled the design: restating someone's problem
in the terms you find natural silently eliminates the alternatives those terms
cannot express.
