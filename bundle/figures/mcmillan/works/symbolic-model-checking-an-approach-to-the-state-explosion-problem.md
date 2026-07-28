---
type: work
title: "Symbolic Model Checking: An Approach to the State Explosion Problem"
figure: mcmillan
description: McMillan's 1992 CMU PhD thesis, the founding document of symbolic model checking. It shows how to represent a system's entire state space as a Boolean function encoded in a Binary Decision Diagram rather than as an explicit list of states, turning fixed-point computations over the mu-calculus into BDD operations. This let verification scale to state spaces many orders of magnitude larger than explicit-state model checkers of the time could handle, and the thesis works through a synchronous pipeline circuit as a worked example.
subdomains: [formal-methods-and-verification]
year: 1992
url: https://mcmil.net/pubs/thesis.pdf
extraction: complete
survey_pages: 214
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: self-archived
tags: [work]
---

# Symbolic Model Checking: An Approach to the State Explosion Problem

**Venue/year:** PhD thesis, Carnegie Mellon University (CMU-CS-92-131), May 1992.
**Source:** https://mcmil.net/pubs/thesis.pdf — self-archived PDF on McMillan's own site, live and directly downloadable (HTTP 200, title page confirmed: "Symbolic Model Checking: An approach to the state explosion problem," Kenneth L. McMillan, May 1992, CMU-CS-92-131).

## Lessons
- [Change the representation underneath your algorithms, not the algorithms](../lessons/change-the-representation-under-the-algorithms-not-the-algorithms.md)
- [Systems are only well behaved where they can actually go](../lessons/systems-are-only-well-behaved-where-they-can-actually-go.md)
- [Separate the structure that is in the system from the structure your model imposes on it](../lessons/separate-structure-in-the-system-from-structure-your-model-imposes.md)
- [Put the guarantee in the notation, and make the escape hatch visibly worse](../lessons/put-the-guarantee-in-the-notation.md)
- [A concrete witness outranks a proof, because it does not inherit your assumptions](../lessons/a-witness-outranks-a-proof.md)
- [To generalise over sizes, compare with an ordering rather than an equivalence](../lessons/pick-an-ordering-not-an-equivalence.md)
- [Refuse to decide what nobody asked you to decide](../lessons/refuse-to-decide-what-you-were-not-asked.md)

_Note: mcmil.net thesis.pdf has Type-3 bitmap fonts with no Unicode map (pdftotext -layout and -raw both yield garbage). Extraction used the host-provided text derivative at archive.org item DTIC_ADA250924 (`DTIC_ADA250924_djvu.txt`), same work, full 214 pages._
