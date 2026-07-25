---
type: work
title: "Monitors and Concurrent Pascal: A Personal History"
figure: brinch-hansen
description: Brinch Hansen's own retrospective account, written for the ACM Second History of Programming Languages conference, of how he arrived at the monitor concept and built Concurrent Pascal, including where his approach agreed and disagreed with Hoare's parallel formulation of monitors. It's a first-person record of the design decisions and dead ends behind the earlier technical papers, useful for the reasoning that doesn't show up in the polished CACM/TSE write-ups. Written with the benefit of nearly two decades of hindsight.
subdomains: [distributed-systems-and-concurrency]
year: 1993
url: http://www.brinch-hansen.net/papers/1993a.pdf
access: public
host: self-archived
tags: [work]
---

# Monitors and Concurrent Pascal: A Personal History

**Venue/year:** ACM Second History of Programming Languages Conference (HOPL-II), 1993; also published in ACM SIGPLAN Notices 28(3).
**Source:** http://www.brinch-hansen.net/papers/1993a.pdf — author's self-archived papers site (brinch-hansen.net/papers), verified resolving 2026-07-24. Note: the site's HTTPS certificate is currently expired; the HTTP URL above resolves cleanly.

## Lessons
- [A shared intuition is not yet a concept; force it into a definition and then allow yourself no other tool](../lessons/a-shared-intuition-is-not-yet-a-concept.md)
- [Count your special-case rules: a pile of ad hoc restrictions means the underlying concept has not been found yet](../lessons/count-your-special-case-rules.md)
- [Cut module boundaries where simultaneity demands them, not where the data would suggest](../lessons/cut-boundaries-where-simultaneity-demands.md)
- [Design concurrent code for reproducible behavior, because the errors that matter are the ones testing can never reach](../lessons/design-for-reproducibility-because-testing-cannot-reach.md)
- [Design the machine you wish you had been given, then hold the layer above it to explaining itself without ever mentioning it](../lessons/design-the-machine-under-the-language.md)
- [If writing a module is hard, the real work has not been done — choosing the modules is the design](../lessons/the-work-is-choosing-the-modules.md)
- [Put the permitted operations next to the data they touch, and give up language power until the compiler can enforce it](../lessons/put-the-operations-where-the-data-lives.md)
- [Settle design arguments by building whole systems, not with exercises or with objections nobody has tested](../lessons/settle-design-arguments-by-building-systems.md)
- [Systems code earns no exemption from the disciplines you would demand of any other program](../lessons/systems-code-earns-no-exemption.md)
- [Trade generality for tractability on purpose, and keep a ledger of what the trade cost you](../lessons/trade-generality-for-tractability-on-purpose.md)
- [When a class of mistakes needs a name to happen, remove the ability to name it](../lessons/remove-the-name-remove-the-error.md)
