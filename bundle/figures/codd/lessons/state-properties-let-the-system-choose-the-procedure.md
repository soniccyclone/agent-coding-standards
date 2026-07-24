---
type: lesson
title: "State the properties of the result; let the system choose the procedure"
figure: codd
works: [relational-completeness-of-data-base-sublanguages, relational-database-a-practical-foundation-for-productivity, recent-investigations-in-relational-data-base-systems]
axes: [expressiveness, parallelizability]
subdomains: [programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# State the properties of the result; let the system choose the procedure

**Lesson:** A request phrased as a sequence of steps buries the requester's intent inside one arbitrary member of the family of procedures that would satisfy it, and everything downstream then has to reverse-engineer the intent out of the steps. Codd's comparison of calculus-style and algebra-style query languages makes the case concretely: a description by properties is the ideal input for an optimizer, because the system sees the whole goal at once instead of locally optimizing each step of one operator sequence a user happened to pick; it is the correct basis for authorization, because permission should attach to what data is being asked for, not to which algorithm fetches it; and it sits closest to how people actually ask for things.

The companion principle is operating on whole collections at a time. When one statement processes a set, the iteration disappears from user code and reappears inside the system, which is free to reorder it, batch it across a network to cut per-record round trips, or run it in parallel; when the user writes the loop, that freedom is destroyed one element at a time. Codd treated loop-avoidance as a hard requirement for end users and a productivity multiplier for programmers, and by the Turing lecture he could add the empirical kicker: a compiling optimizer armed with system-maintained statistics generates better access code than the average programmer, precisely because the declarative statement left it room to. The performance objection to high-level interfaces inverts into a performance argument for them.

A programmer who absorbs this designs interfaces where callers describe outcomes and constraints, keeps whole-collection operations primitive rather than exposing element-wise iteration, and treats any API that forces clients to navigate step-by-step as both an intent-destroyer and a parallelism-destroyer. The test of an interface is whether the implementation retains the freedom to satisfy requests in an order and by a method the caller never imagined.

**Source:** [Relational Completeness of Data Base Sublanguages](../works/relational-completeness-of-data-base-sublanguages.md) — Section 5's four-point case for calculus-oriented over algebra-oriented sublanguages (augmentation, search optimization, authorization, closeness to natural language). Also [Relational Database: A Practical Foundation for Productivity](../works/relational-database-a-practical-foundation-for-productivity.md) (the set-processing objective, automatic navigation, and the compiled-optimizer performance argument) and [Recent Investigations in Relational Data Base Systems](../works/recent-investigations-in-relational-data-base-systems.md) (the survey of sublanguage levels and the remote-query argument against element-at-a-time interfaces).
