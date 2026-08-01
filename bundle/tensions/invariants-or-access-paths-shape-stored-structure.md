---
type: tension
title: "Whether expected access is a legitimate input to the structure of stored data"
figures: [codd, bachman, ullman]
lessons: [codd/let-invariants-not-access-patterns-shape-structure, bachman/access-cost-as-designed-artifact, ullman/how-you-group-data-is-an-access-plan-in-disguise]
status: resolved-by-llm
tags: [tension]
---
# Whether expected access is a legitimate input to the structure of stored data

## The decision
You are about to fix the structure of data that will outlive the program reading
it: a schema, a file format, a shard key, a class's fields, a directory layout.
Two candidate inputs are on the table. One is the set of time-independent facts
about the domain, which attributes determine which others. The other is the set
of traversals the system will actually run. The question is whether the second
is admissible at all, or whether letting it touch the structure is the mistake
that produces every subsequent integrity problem.

## Codd: only the invariants may shape it, because reads are recoverable and integrity is not
[Let invariants, not access patterns, shape the structure of data](../figures/codd/lessons/let-invariants-not-access-patterns-shape-structure.md)
makes neutrality to query statistics a stated design goal rather than an
accident. The argument is about differing rates of change: functional
dependencies are properties of the domain and mostly hold still, while traffic
shifts with every new feature and every new customer, so a structure derived
from dependencies survives changes that a structure derived from traffic does
not. The evaluation procedure follows from that. You judge a candidate structure
by which update sequences it makes dangerous, not by which reads it makes
convenient, because the two failure modes are not symmetric: convenience lost to
an awkward layout is recoverable later by joining or by defining a view, whereas
a fact stored in two places has already made a class of update anomalies
expressible, and no amount of later work makes them inexpressible again.

## Bachman: the placement question gets answered either way, so answer it deliberately
[The cost of reaching data is a designed artifact, not an inherited accident](../figures/bachman/lessons/access-cost-as-designed-artifact.md)
starts from an observation that no logical argument can retire: bytes sit
somewhere, and the distance between two of them is set by whoever laid them out,
including the designer who declined to think about it. A layout chosen by
neutral logic has not abstained from the access question; it has answered it
with whatever falls out, and in Bachman's era the answer cost a seek. His
positive program is that a relationship should be a declared, materialized path
with related records placed together, so that following it is cheap by
construction, and that the aging of a layout against drifting access patterns
should be a standing design question rather than an emergency. The lesson
concedes the logical argument to the relational tradition and then says the
thinking survives underneath it: someone still does it, and pretending otherwise
relocates the cost to where nobody can see it.

## Ullman: your grouping was already a retrieval plan, and it has a breaking point
[How you group data is a search strategy in disguise](../figures/ullman/lessons/how-you-group-data-is-an-access-plan-in-disguise.md)
supplies the fact that decides between them. Partitioning the world into named
collections looks descriptive and is functional: the collection name is the
first step of every retrieval, the decision about where to look, and when it can
be made statically its cost vanishes into compile time. This is why deriving
reads from a neutral structure is affordable at all. It is also why the
affordability has a limit. Push into a domain where entities differ in which
attributes apply rather than in their values, so the honest count of categories
approaches the count of entities, and the static structure a planner would route
through stops existing, indexing every attribute is unaffordable at that width,
and the retrieval plan the schema used to hand you for free has to be rebuilt
deliberately.

## Resolution
**LLM DECISION — Nathan may overturn.**

The two govern different objects and the mapping between them is a
maintainability test: an access-shaped structure is legitimate exactly when it
is a derived function of the invariant-shaped one, recomputable from it,
discardable without loss, and maintained by the system rather than by the
application. Indexes, clustering, materialized views, sort orders, caches and
replicas all satisfy that and are pure Bachman, and none of them touches Codd's
rule, because none of them is authoritative for any fact. Codd's rule governs
which facts exist and where the single copy of each one lives. Bachman's governs
the arrangement and duplication of those copies. Design in that order:
dependencies decide the units, expected traversals decide the geometry, and a
proposed geometry that cannot be derived automatically is a request for an
engine feature rather than a reason to reopen the units.

What made this look like a contradiction is that Bachman's setting had no seam
to exploit. The declared path was the only copy, so choosing it was
simultaneously an access decision and an integrity decision, which is precisely
what Codd was attacking. The relational engine did not refute Bachman, it gave
his discipline somewhere to stand that could not corrupt anything.

The interesting part is where that seam is absent, because Codd's guarantee that
reads are recoverable by derivation is conditional on there being a level below
your structure that is free to be re-derived without changing it. When the
structure you are choosing is itself the bottom, there is no such level and the
two decisions land in the same artifact again. A file format, a wire format, an
on-disk record, a shard key, a directory layout: here the access decision is the
structure, and Bachman governs. Codd's own lesson overreaches when it extends to
a cache, since a cache has no invariants of its own to derive from. It is
nothing but a bet on access, and derived by construction. It is Bachman's object
sitting in Codd's list.

Ullman marks the other place the seam fails, from the opposite direction. Note
first that his admission criterion is Codd-compatible: the count of meaningful
categories in a domain is a time-independent fact about that domain, not a query
statistic, so checking a grouping against it is not the forbidden input. What he
shows is that Codd's derivability guarantee is underwritten by a property of the
domain rather than by anything in the relational model, namely that categories
are few and broad enough to route through. When they are not, derivation stops
being cheap, and the retrieval plan has to be authored. The same fact appears
one floor up in
[when a construct is provably redundant](simulability-kills-a-construct-vs-simulability-proves-nothing.md):
a proof that something is recoverable in principle prices capability and leaves
the cost unmeasured.

**Strongest counter-argument:** the derived-and-discardable test may be too
generous about what modern systems actually do, in which case Bachman deserves a
place inside the schema rather than beneath it. The redundancy Codd banned
returned as denormalized read models, event-sourced projections and search
indexes, and most of those are maintained asynchronously by application code.
Calling them non-authoritative does not make them safe; a projection that drifts
is Codd's update anomaly with an extra hop and a worse debugging story, and it
fails in a way normalization theory has nothing to say about. If asynchronous
derivation is the normal case rather than the degenerate one, then the honest
design records each access-shaped structure explicitly, with its derivation rule
and its staleness bound stated as part of the schema, which is much closer to
Bachman's declared materialized path than to an optimization the designer is
entitled to ignore.
