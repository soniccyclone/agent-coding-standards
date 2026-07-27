---
type: lesson
title: "A release is not a delivery event; it is the act of manufacturing an authoritative version to reason from"
figure: lehman
works: [on-understanding-laws-evolution-and-conservation-in-the-large-program-life-cycle]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A release is not a delivery event; it is the act of manufacturing an authoritative version to reason from

**Lesson:** Between releases, a widely used system does not have a single state. The same fault is patched one way at one site, differently at another, and not at all at a third. Local adaptations accumulate. Code gets edited without the documentation following, and documentation gets edited to match observed behavior without anyone having worked out what the code actually means across the whole system under every condition it can meet. In that condition there is no artifact you can point at and call the system, which means there is nothing stable enough to reason about, measure, or hold anyone to.

Release is what ends that condition. Its deep function is not shipping but establishing, at one instant, a version of the code and its documentation that is authoritative — the one against which claims can be checked and from which the next round of change can be derived. Everything else people value about releases follows from this: the stabilization, the ability to say what is installed, the possibility of interpreting a fault report at all. Even then the authority is imperfect, since variant modules for different situations may still coexist, but there is a defined thing where before there was drift.

Seeing releases this way changes what you protect. The discipline worth defending is not the ceremony around a shipping date but the correspondence, at the release instant, between code and its description — because the moment documentation is maintained by inference from behavior rather than from analysis of meaning, the authoritative version stops being authoritative and the whole system slides back into having no definite state. It also explains why fragmenting a system into many divergent site-local variants is not merely an operations inconvenience: it destroys the only object that anybody could have reasoned about, and it destroys it for every future change, not just the current one.

**Source:** [On Understanding Laws, Evolution, and Conservation in the Large-Program Life Cycle](../works/on-understanding-laws-evolution-and-conservation-in-the-large-program-life-cycle.md) — the passage opening the interpretation of the fifth law, which describes the flux of code and documentation between releases and identifies the release as the moment an authoritative version comes into existence.
