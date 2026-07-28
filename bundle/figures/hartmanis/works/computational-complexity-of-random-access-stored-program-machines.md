---
type: work
title: "Computational Complexity of Random Access Stored Program Machines"
figure: hartmanis
description: Works out a complexity measure based on running time for random access stored-program machines (RASPs) rather than Turing machines, aiming for a model closer to how real computers are organized. Shows, via an argument about the size of computed functions rather than diagonalization, that arbitrarily complex functions exist whose optimal RASP running time can't be improved by any constant factor, and that such optimal programs can't be self-modifying. Also compares machines with and without built-in multiplication and briefly considers associative-memory and distributed-logic machines.
subdomains: [algorithms-and-complexity]
year: 1970
url: https://ecommons.cornell.edu/handle/1813/5929
extraction: complete
access: public
host: institutional
tags: [work]
---

# Computational Complexity of Random Access Stored Program Machines

**Venue/year:** Cornell University Department of Computer Science, Technical Report TR70-70, August 1970. A revised version was later published as "Computational Complexity of Random Access Stored Program Machines," Mathematical Systems Theory 5 (1971), pp. 232-245 — that Springer-published journal version is paywalled (confirmed: link.springer.com/article/10.1007/BF01694180 redirects to a Springer login gate) and is excluded; this technical report is the same work made public by Cornell.
**Source:** https://ecommons.cornell.edu/handle/1813/5929 — Cornell's own DSpace-CRIS institutional repository (eCommons). Verified via the repository's REST API that the item resolves and its PDF bitstream downloads cleanly (HTTP 200, valid 38-page PDF, 1,698,680 bytes matching the recorded metadata) at https://ecommons.cornell.edu/server/api/core/bitstreams/072d9316-ddeb-4e51-b87a-e289f65ad21b/content — the handle page itself is a JS-rendered front end for automated tools but resolves normally in a browser.
**Host:** institutional — Cornell University eCommons repository, sole author of record Juris Hartmanis.

## Lessons
- [Whether a constant factor is noise is a fact about your machine model, not about computation](../lessons/whether-a-constant-factor-is-noise-depends-on-the-machine.md)
- [Bound the size of the answer and you have bounded every algorithm at once](../lessons/bound-the-answer-before-bounding-the-algorithm.md)
- [Code that writes code buys a constant — unless it can manufacture primitives you did not have](../lessons/self-modification-buys-a-constant-unless-it-manufactures-primitives.md)
- [Judge a hardware feature by what it costs to fake it, and distinguish faster lookup from faster construction](../lessons/ask-what-it-costs-to-fake-the-feature.md)
