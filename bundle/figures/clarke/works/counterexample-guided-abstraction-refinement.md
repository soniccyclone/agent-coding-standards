---
type: work
title: "Counterexample-Guided Abstraction Refinement"
figure: clarke
description: Introduces the CEGAR loop, co-authored with Grumberg, Jha, Lu, and Veith. A system is checked against a coarse, automatically-built abstraction; if the checker returns a counterexample, that trace is tested against the real (concrete) system, and if it turns out to be spurious the information in it is used to automatically refine the abstraction and try again. This closed-loop automation of abstraction became the dominant technique for scaling model checking to industrial-size software without a human hand-crafting the abstraction, and underlies tools such as Microsoft's SLAM.
subdomains: [formal-methods-and-verification]
year: 2000
url: https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/Counterexample-guided%20abstraction%20refinement.pdf
access: public
host: self-archived
tags: [work]
---

# Counterexample-Guided Abstraction Refinement

**Author(s):** Edmund M. Clarke, Orna Grumberg, Somesh Jha, Yuan Lu, Helmut Veith
**Venue/year:** Originally presented at CAV 2000 (Chicago, IL); extended version published as "Counterexample-Guided Abstraction Refinement for Symbolic Model Checking," Journal of the ACM 50(5), pp. 752-794, 2003.
**Source:** https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/Counterexample-guided%20abstraction%20refinement.pdf — self-archived scan (the extended JACM version) on Clarke's own CMU faculty page, live and directly downloadable (HTTP 200), resolving the uncertain flag from the prior pass. Also independently mirrored on a Stanford course reading page (web.stanford.edu/class/cs357/cegar.pdf), corroborating the text.

## Lessons
- [Let the false answer locate the imprecision](../lessons/let-the-lie-locate-the-imprecision.md)
- [Engineer your information loss so the errors all point one way](../lessons/make-your-information-loss-fail-one-way.md)
- [Guarantee the loop, guess the step](../lessons/guarantee-the-loop-guess-the-step.md)
- [An abstraction is only exact where it respects the operations it abstracts over](../lessons/an-abstraction-must-respect-the-operations.md)
- [A verifier that can only say yes is half a verifier](../lessons/a-verifier-that-only-says-yes-is-half-a-verifier.md)
