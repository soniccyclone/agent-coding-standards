---
type: lesson
title: "An extension point is only as open as the invariants it makes you learn"
figure: stonebraker
works: [the-implementation-of-postgres]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# An extension point is only as open as the invariants it makes you learn

Two extension mechanisms in the same system can look equally open — both documented, both pluggable, both loadable without stopping the system — and have audiences that differ by orders of magnitude in skill. The difference is not the plumbing. It is how many of the system's internal contracts the extender has to hold in their head to write a correct implementation. Supplying a new value type means writing conversions and knowing nothing about the engine. Supplying a new indexing strategy means participating in the locking protocol, driving the buffer pool by hand, understanding how execution state is threaded through, and getting a dozen interlocking entry points right. The first is a weekend; the second is a specialist's project, and no amount of interface polish changes that, because the cost is the invariants, not the signatures.

There is a blunt proxy for this that costs nothing to compute: the length of the document a person needs to read before they can succeed. Two pages and fifty pages are not two points on a continuum, they are two different populations. Measuring it early matters because the mechanism you build should match the audience, and the audience determines what is worth paying for. Making extensions installable into a running system is expensive machinery — caches of loaded code, catalogs consulted at plan time, aging policies — and it earns its cost only if extensions arrive from people who cannot be asked to rebuild and restart. If in reality every extension of that kind will be written by someone who is already comfortable rebuilding the system, you have bought dynamism for an audience that did not need it, and paid in permanent internal complexity.

So the discipline runs in both directions. Before building an extension point, name the person who will use it and count the invariants they must respect; if that count is high, either flatten it by giving the extension a narrower contract that the engine mediates, or accept the specialist audience and stop paying for conveniences aimed at amateurs. And when an existing extension point turns out to be far harder to use than intended, treat that as a specification error rather than a documentation gap — the honest fix is a different, smaller contract, not fifty better-written pages.

**Source:** [The Implementation of Postgres](../works/the-implementation-of-postgres.md) — the critique of the access method interface, which contrasts the effort of adding a new type against adding a new access method and separately regrets designing for runtime extension by end users who never existed.
