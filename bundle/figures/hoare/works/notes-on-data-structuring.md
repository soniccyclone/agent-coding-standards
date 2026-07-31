---
type: work
title: "Notes on Data Structuring"
figure: hoare
description: A long expository chapter working through how to reason formally about data types and their representations, covering enumerations, arrays, records, discriminated unions, and pointer-based structures, and building toward the correctness-of-representation ideas Hoare formalized separately the same year. Written as a companion to Dijkstra's and Dahl's essays in the same volume, aimed at showing that data structuring deserves the same disciplined treatment as control-flow structuring. Its terminology and worked examples influenced how type systems and abstract data types were later taught.
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
year: 1972
url: https://www.cs.cornell.edu/courses/cs4860/2018fa/lectures/Notes-on-Data-Structuring_Hoare.pdf
survey_pages: 92
survey_text_layer: full
survey_fetch_mb: 4
access: public
host: third-party-rehost
tags: [work]
---

# Notes on Data Structuring

**Author(s):** C. A. R. Hoare
**Venue/year:** Chapter II in O.-J. Dahl, E. W. Dijkstra, and C. A. R. Hoare, *Structured Programming* (Academic Press, 1972), pp. 83-174.
**Source:** https://www.cs.cornell.edu/courses/cs4860/2018fa/lectures/Notes-on-Data-Structuring_Hoare.pdf — course-reading mirror hosted by Cornell University (CS4860, Fall 2018). Content verified directly by decompressing the PDF's text streams: opening text reads "II. Notes on Data Structuring".

## Lessons
- [Keep the notation you design in deliberately unimplemented, so its expensive conveniences must be spent rather than tolerated](../lessons/keep-the-design-notation-deliberately-unimplemented.md)
- [An operation belongs in the primitive set exactly when its efficiency depends on the representation](../lessons/an-operation-is-primitive-when-its-cost-depends-on-the-representation.md)
- [Claim only the structure your problem actually has: unasserted properties are freedom the implementer gets to spend](../lessons/claim-only-the-structure-your-problem-has.md)
- [Choose a modelling apparatus for the cost profile of the models it yields, then write down the fidelity gap](../lessons/choose-the-modelling-apparatus-for-its-cost-profile-not-its-fidelity.md)
- [If safety demands a check at every use, redesign the notation so the fact is established once and carried by scope](../lessons/establish-a-fact-once-and-let-scope-carry-it.md)
- [Carry provenance in the value, because an error of interpretation produces results outside your model entirely](../lessons/carry-provenance-in-the-value-not-in-the-readers-head.md)
- [Sharing one copy is an optimization licensed only by immutability, and the licence must travel with the technique](../lessons/sharing-is-an-optimization-licensed-only-by-immutability.md)
- [Get full machine efficiency without machine dependence by naming the machine's parameter and computing from it](../lessons/parameterize-on-the-machine-property-not-the-machine.md)
- [Write the unaffordable version first and keep it: the abstract program is the frame the efficient one is built on](../lessons/keep-the-abstract-version-as-the-frame-of-the-concrete-one.md)
- [Going from bounded to unbounded is a cliff, not a gradient: stay on the cheap side until the application forces you off](../lessons/the-finite-to-unbounded-step-is-a-cliff-not-a-gradient.md)
- [The shape of the data dictates the shape of the program: each way of composing data has exactly one matching control structure](../lessons/the-shape-of-the-data-dictates-the-shape-of-the-program.md)
- [Buffering absorbs variance, never a rate deficit — past two or three, extra buffers only delay the diagnosis](../lessons/buffers-absorb-variance-not-a-rate-deficit.md)
- [Name a structure by what it forbids: the restriction is the asset, and it must be fixed before the data is written](../lessons/name-a-structure-by-what-it-forbids.md)
- [Give a value one representation for processing and another for transport, and make the conversion an explicit phase](../lessons/one-value-two-representations-processing-and-transport.md)
