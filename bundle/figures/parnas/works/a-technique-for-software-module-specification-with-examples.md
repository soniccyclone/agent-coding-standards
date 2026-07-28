---
type: work
title: "A Technique for Software Module Specification with Examples"
figure: parnas
description: Companion piece to the decomposition paper, working out what a module's specification should actually contain: enough for a client to use it correctly without seeing the implementation, and no more. Demonstrates the technique on a small tutorial-system example, specifying modules by the externally visible effects of their functions rather than by internal state or algorithm. Laid groundwork for later formal interface-specification methods built on the same hiding principle.
subdomains: [software-engineering-and-architecture]
year: 1972
url: http://www.laputan.org/pub/papers/p330-parnas.pdf
extraction: complete
survey_pages: 7
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# A Technique for Software Module Specification with Examples

**Venue/year:** Communications of the ACM 15(5), May 1972, pp. 330-336.
**Source:** http://www.laputan.org/pub/papers/p330-parnas.pdf — self-hosted paper archive on laputan.org (Brian Foote's long-running software-patterns resource site). Verified live.

## Lessons
- [Describe a component as an observable device, not as a sequence of steps](../lessons/describe-a-component-as-an-observable-device-not-a-sequence-of-steps.md)
- [Treat a specification as an object to be tested, and test it before any program exists](../lessons/test-the-specification-before-the-program-exists.md)
- [Close the side channels through which knowledge reaches a client without passing through the specification](../lessons/close-the-side-channels-that-leak-information-past-the-spec.md)
- [Misuse is the caller's problem, and a refused operation must leave no trace](../lessons/misuse-is-the-callers-problem-and-a-refused-call-must-leave-no-trace.md)
