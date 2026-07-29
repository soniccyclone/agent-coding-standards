---
type: lesson
title: "The layer nobody can replace should offer the common divisor of the options you skipped"
figure: thompson
works: [unix-implementation]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# The layer nobody can replace should offer the common divisor of the options you skipped

**Lesson:** There is a specific discipline owed by any part of a system that its users are forbidden to swap out. Everything above it can be rewritten by someone who disagrees with it; it cannot. That asymmetry, not aesthetics, is what should govern how much it decides. The rule that follows is stricter than "keep it small": having refused to offer users a dozen alternative ways to do a thing, you do not then get to pick your favourite of the dozen and impose it. You are obliged to find the thing that all dozen have in common — the operation each of them could have been built out of — and provide only that.

This is a different move from minimalism and from configurability, and it is easy to mistake for either. Minimalism says offer less. Configurability says offer everything behind a switch. The divisor rule says offer exactly one mechanism, chosen so that none of the discarded alternatives is actually lost, because each remains reachable by composition in the replaceable layers above. A mechanism chosen this way is unopinionated in the only sense that matters: it does not decide anything the levels above it are still entitled to decide differently. And a mandatory layer that decides too radically fails a second way, socially rather than technically — nobody adopts it, so the elegance never gets tested against real use.

The programmer who takes this seriously starts every design at the replaceability question. Which parts of this can a dissenting user route around, and which are load-bearing for everyone? For the load-bearing part, the design task becomes factoring rather than selecting: line up the competing designs you might have shipped and look for their greatest common factor. If a candidate primitive can express only some of them, it is too opinionated for that position, however convenient it is for the common case. This also reframes what counts as a feature request: a request for a new mechanism in the immovable layer is usually a report that the existing primitive was not general enough to divide the space, and the honest fix is to generalise it, not to accumulate a second one beside it.

**Source:** [UNIX Implementation](../works/unix-implementation.md) — the introduction's argument about why the kernel, as the only code a user cannot substitute, should make as few real decisions as possible, and the qualification that this means one way to do a thing rather than many options, with that one way being the common divisor of the options not offered.
