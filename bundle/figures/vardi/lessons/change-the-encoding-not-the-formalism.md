---
type: lesson
title: "When a problem lands just outside your formalism, change the encoding rather than the formalism"
figure: vardi
works: [on-the-expressive-power-of-datalog]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# When a problem lands just outside your formalism, change the encoding rather than the formalism

**Lesson:** A problem often looks like it needs a more powerful language when what it really needs is a different phrasing. Kolaitis and Vardi hit this squarely: the standard way of characterizing a graph property reduces it to a single-player search whose solution demands a stronger logic than the restricted rule language they are working in. Rather than concede and move up, they reformulate the same property as a *two-player* contest on the same graph and show that the question "does the responding player have a winning strategy" is expressible in the restricted language. Nothing about the problem changed. The encoding did, and the encoding was what put it out of reach.

That an adversarial framing lands in a weaker class than a search framing is counterintuitive and worth remembering as a specific move. A search asks for the existence of an object with a global property, which typically forces you to build and inspect that object. A game asks whether every challenge can be answered, which decomposes into local, recursive conditions — exactly what a positive recursive rule language is good at. The same instinct shows up in their other positive result, where a global requirement that several routes be mutually disjoint is replaced by a local one: a route exists such that from each point along it the remaining routes can still be found while avoiding that point. The equivalence is not obvious and is licensed by a min-max theorem — which is the general form of the trick, since a min-max or duality theorem is precisely a licence to certify a global property from local evidence.

Two supporting habits fall out. Look for a duality or min-max result whenever a global existence condition blocks a recursive formulation, because that class of theorem exists to convert global into local. And when the recursion still does not close, generalize the statement — they prove a stronger, parameterized version carrying an explicit set of things to avoid, because the stronger statement is the one that recurses while the original one does not. Strengthening a claim to make induction go through is the standard remedy, and it applies to a program's recursive structure just as much as to a proof's.

**Source:** [On the Expressive Power of Datalog: Tools and a Case Study](../works/on-the-expressive-power-of-datalog.md) — section six's positive results: the theorem for acyclic inputs, where the earlier single-player pebble-game reduction is noted to require fixpoint logic and is replaced by a two-player game on the input graph whose winning-strategy question is rule-expressible; and the preceding theorem, where the node-disjointness requirement is restated as a local avoiding-path condition justified by the max-flow min-cut theorem, proved by induction on a strengthened query carrying an explicit list of nodes to avoid.
