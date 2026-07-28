---
type: work
title: "An Introduction to Input/Output Automata"
figure: lynch
description: Introduces the I/O automaton, a state-machine model for a single component of a distributed or concurrent system that interacts with its environment purely through labeled input and output actions. Defines composition (how automata combine into larger systems) and a simulation-based notion of one automaton implementing another, giving a rigorous way to prove a low-level algorithm correctly implements a high-level specification. Became the standard formal substrate for the specification and correctness proofs collected in Lynch's later textbook and in *Atomic Transactions*.
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
year: 1989
url: http://groups.csail.mit.edu/tds/papers/Lynch/CWI89.pdf
survey_pages: 30
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: institutional
tags: [work]
---

# An Introduction to Input/Output Automata

**Author(s):** with Mark R. Tuttle
**Venue/year:** CWI Quarterly 2(3), September 1989
**Source:** http://groups.csail.mit.edu/tds/papers/Lynch/CWI89.pdf — submitted-version PDF hosted on MIT CSAIL's Theory of Distributed Systems group publications page (university-hosted), live and directly downloadable (HTTP 200). A publisher-hosted copy is also live at the CWI institutional repository: https://ir.cwi.nl/pub/18164/18164A.pdf.

## Lessons
- [A component's interface is defined by what it cannot refuse, not by what it chooses to accept](../lessons/an-interface-is-defined-by-what-you-cannot-refuse.md)
- [Make a specification the same kind of object as an implementation, so correctness is just containment](../lessons/a-specification-is-a-more-permissive-program.md)
- [The right obligation on an open component is never to be the first to break the invariant](../lessons/never-be-the-first-to-break-the-invariant.md)
- [Judge a composition operator by whether your reasoning survives it in both directions](../lessons/an-abstraction-operator-must-preserve-the-properties-you-reason-with.md)
