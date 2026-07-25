---
type: lesson
title: "Choose the one invariant that must survive the boundary, and let the rest of the design be forced by it"
figure: cardelli
works: [a-language-with-distributed-scope]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Choose the one invariant that must survive the boundary, and let the rest of the design be forced by it

**Lesson:** Crossing a boundary that the original design did not contemplate, whether between address spaces, machines, processes, or trust domains, tempts you into inventing a second semantics for the far side. That road ends with two sets of rules, a translation layer between them, and behaviour that depends on where code happens to be running. The alternative is to pick a single property from the local design that must continue to hold globally and then derive everything else from the obligation to preserve it. Here the property chosen is that the meaning of a name is fixed by where it was bound and not by where it is being evaluated. It is a modest-sounding commitment with far-reaching consequences: because a computation means the same thing wherever it runs, code can be moved without changing what it does, which is what makes moving code a usable technique rather than a gamble.

The discipline is in accepting what the invariant forces. If names keep their bindings, then transmitting a computation must transmit those bindings, and therefore a reference in one address space to a location in another has to be an ordinary thing the language supports. If references cross boundaries, then reclamation and failure have to be defined across boundaries too. If the invariant is to be preserved for state, then some values must be pinned in place, so mobility of state has to be constructed rather than assumed. Each of these is a consequence rather than a separate design decision, which is exactly the mark of a well chosen invariant: the design becomes derivable and therefore explainable, and features that would otherwise conflict cannot, since they all answer to the same commitment.

The complementary discipline is to keep the invariant from becoming a claim that distribution is invisible. Meaning is location-independent while cost is not, so the design keeps distribution explicit in the program: placement, transmission, and remote execution are things you write down. A reader can tell where the network is, while a reasoner can ignore it when asking what the code means. That pairing, one invariant preserved and one reality left visible, is more useful than either full transparency or a separate remote dialect.

**Source:** [A Language with Distributed Scope](../works/a-language-with-distributed-scope.md) — the introduction's statement of the guiding principle, the distributed semantics section deriving sites, locations, network references, and value transmission from it, and the discussion contrasting location-independent meaning with explicitly programmed distribution.
