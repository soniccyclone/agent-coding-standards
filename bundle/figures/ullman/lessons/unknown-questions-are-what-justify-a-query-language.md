---
type: lesson
title: "Only unknown questions justify paying for a query language"
figure: ullman
works: [a-comparison-between-deductive-and-object-oriented-database-systems]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Only unknown questions justify paying for a query language

The argument most people have about data systems — declarative or procedural,
high-level or hand-tuned — is downstream of a question they skip: are the
questions known in advance? Ullman splits the application space on exactly that
line. Where the interrogations are fixed and the structures stable, a
general-purpose query facility is dead weight; what such a workload wants is a
fast, richly typed store and code written directly against it. Where the
interrogations cannot be enumerated ahead of time — because a scientist is
looking for a relationship nobody has posited, or a trader needs a pattern that
stops paying the moment it is common knowledge — no amount of pre-written access
code helps, because the query that matters is the one nobody thought to write.
Two systems that look like competitors are answering different questions about
the workload, and the cheaper one wins whenever the harder question wasn't being
asked.

What makes the split rigorous rather than a matter of taste is Ullman's figure of
merit for the open-ended case: the cost of an answer is the whole latency of
getting it — conceiving the query, writing it, debugging it, compiling it, and
running it — not the machine time alone. Under that accounting, a language that
executes twice as fast but takes a day to get right loses outright to one that
answers in a minute, and the notorious inefficiency of high-level notation stops
being the decisive objection. It also explains why the argument reverses when
questions are fixed: authoring cost is paid once and amortized to nothing, so
only execution time remains and the specialized path wins on its merits.

A programmer who thinks this way asks about the shape of the question set before
arguing about the technology, and refuses to let one component's needs dictate
another's. It licenses a layered answer rather than a winner: an efficient typed
store underneath, doing what it is good at, with a declarative layer above it for
the traffic that genuinely cannot be anticipated. And it supplies a real
diagnostic for over-engineering. A flexible query interface over a workload whose
every query is known is complexity nobody will ever cash in, while hand-written
access paths over an exploratory workload guarantee that the interesting questions
never get asked, because asking one costs a sprint.

**Source:** [A Comparison Between Deductive and Object-Oriented Database Systems](../works/a-comparison-between-deductive-and-object-oriented-database-systems.md) — the discussion of why declarativeness is needed, which separates applications served by an object store with no query language from those requiring unplanned queries, and which prices a query in total time-to-answer rather than run time.
