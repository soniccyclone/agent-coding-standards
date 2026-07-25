---
type: lesson
title: "The verification problem worth solving is establishing properties of assemblies whose parts are known to fail"
figure: booch
works: [the-future-of-software-engineering, the-promise-the-limits-and-the-beauty-of-software]
axes: [verifiability]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# The verification problem worth solving is establishing properties of assemblies whose parts are known to fail

**Lesson:** Rigorous proof of program properties works, and where it is applied to devices that can kill people it is worth every hour it costs. It is also, measured against the total volume of software that civilization now depends on, almost absent. The honest diagnosis of that gap is not that practitioners are lazy. It is that the techniques were developed for a situation that most systems are not in: a bounded artifact, under one team's control, whose components behave as specified. Real systems are assembled largely from parts nobody present wrote, running on infrastructure nobody present operates, and the characteristic failure is one in which a component you did not know existed takes your system down. Proving the parts you wrote does not address that.

So the interesting question is inverted from the classical one. Not how to establish correctness of a component in isolation, but how to establish properties of a composition whose constituents are guaranteed to be unreliable, whose set of constituents is not fully known, and whose failures include modes that arise only from interaction. Concurrency is the small-scale version of the same difficulty and is already beyond most practitioners: a defect can live entirely in the interference between two independently correct pieces of work, invisible to either team because neither piece was wrong. Scale that up across organizational and network boundaries and the reasoning unit can no longer be the module. It has to be the assembly, with unreliability of parts as a premise rather than an exception.

This is a demand on both directions of the field. Formal work that stays inside the bounded-component assumption will keep being correct and keep being irrelevant to most of what gets built, and its practitioners should regard reaching the unbounded case as the ambition rather than a compromise. Practitioners, for their part, should stop treating unreliability as an operational surprise handled by retries after the fact and start treating it as a stated assumption their design has to be argued against. A programmer who thinks this way asks what property their system still guarantees when an arbitrary dependency is unavailable or wrong, and treats an answer of "we would notice" as no answer.

**Source:** [The Future of Software Engineering](../works/the-future-of-software-engineering.md) — the direct challenge to the formal methods community, acknowledging its value in life-critical devices while noting its near-absence from the bulk of software built, and framing the open problem as proving things in an environment whose components are reliably unreliable. Also [The Promise, the Limits, and the Beauty of Software](../works/the-promise-the-limits-and-the-beauty-of-software.md) — the treatment of concurrency and distribution as a limit most developers cannot clear, illustrated by a public system whose data leak arose purely from the interaction between two independently reasonable pieces of work.
