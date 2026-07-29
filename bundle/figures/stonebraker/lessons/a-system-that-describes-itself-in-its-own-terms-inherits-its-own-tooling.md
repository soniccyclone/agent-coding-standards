---
type: lesson
title: "A system that describes itself in its own terms inherits its own tooling"
figure: stonebraker
works: [the-design-and-implementation-of-ingres]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A system that describes itself in its own terms inherits its own tooling

A data manager needs somewhere to record what data it is managing — names, layouts, widths, which keys exist, which files are involved. The lazy instinct is a bespoke format for this, on the grounds that it is internal, small, and performance-critical. The better instinct is to notice that the description of the data is itself data, and to store it in exactly the structures the system already knows how to store, retrieve, key, and rearrange. The catalogs become ordinary collections, and everything the system can do to user data it can now do to its own self-description without a line of new code.

The returns compound in three directions. Accessing metadata reuses the same access path as accessing anything else, so there is one implementation to make correct and fast rather than two. Whatever tuning applies to real collections applies here too, so if metadata lookups turn out to dominate under some workload mix you have the whole existing repertoire available instead of a special-case optimization project. And the ordinary query facility becomes an inspection and repair tool, which means the system can be interrogated about its own state by anyone who already knows how to ask it questions. The quiet fourth return is evolvability: adding a new field to the description of things — a value range, a statistic, a flag that lets a later stage skip a lookup — is a routine schema change rather than a format migration, so the metadata can grow at the speed the rest of the design demands.

The generalization is that the internal bookkeeping of a system is the highest-leverage place to apply its own abstraction, and it is also where designers most often refuse to. A programmer who takes this seriously asks, of every internal registry and configuration store, why it is not expressed in the system's primary data model, and treats a bespoke answer as needing justification rather than being the obvious default. The self-application is also an honesty check: an abstraction too clumsy or too slow to describe its own implementation is telling you something about how it will feel to the people using it for their problems.

**Source:** [The Design and Implementation of INGRES](../works/the-design-and-implementation-of-ingres.md) — the treatment of system catalogs in the data structures section, which states the reasons for representing the system's own bookkeeping as ordinary relations and notes how that choice made later restructuring cheap.
