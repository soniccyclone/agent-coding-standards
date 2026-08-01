---
type: lesson
title: "A shape that turns up everywhere is weak evidence for your mechanism"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A shape that turns up everywhere is weak evidence for your mechanism

**Lesson:** Finding that your data obeys a familiar distributional form feels like a discovery about your domain and usually is not. The same form shows up in inbound links to web pages, in sales by rank, in the sizes of sites, in the frequency of words, and — with the same exponent as the word frequencies — in the populations of American states, which share no mechanism with vocabulary whatsoever. When a shape is that promiscuous, matching it constrains your explanation barely at all. The inference "my data has this shape, and mechanism M produces this shape, therefore M" is invalid in proportion to how many other mechanisms produce it, and here that count is large.

This matters because the temptation runs the other way. A self-reinforcing story is available and satisfying: getting more of a property makes the property easier to get, links attract links, visible sellers get advertised and sell more. It is a real mechanism, it does produce heavy tails, and it is genuinely at work in some of these systems. But the states are not getting populous because they are populous in any way resembling how a page accumulates links, and they land on the same curve regardless. So the curve is not what licenses the story. If you want the mechanism claim, you need evidence the shape does not give you — the dynamics over time, an intervention, a comparison against a population where the loop is absent by construction.

What the shape does license is engineering, and that is the payoff worth taking. Tail behavior determines the operational facts you plan against, and those transfer across domains precisely because the shape does: a small head accounts for most of the mass, so caching or precomputing the top items captures most of the traffic; the tail is long enough that its total is not negligible even though each member is, so discarding it wholesale is a different decision than it looks; any estimate built from a sample will systematically miss the tail and understate its diversity; and a threshold placed anywhere in the middle behaves badly because there is no natural break to place it at. None of these conclusions require knowing why the distribution is shaped that way. That is the useful division: use the shape for sizing, capacity, sampling design, and storage strategy, and refuse to use it for causal claims.

The general discipline is to ask, of any pattern you have matched, how selective the match is. A pattern that a hundred processes could have produced tells you something about the operational world and nothing about which process you have. A pattern that only a few could have produced is real evidence, and the way to earn that is to find a prediction the candidate mechanisms disagree on and go look at it. Otherwise you have fitted a curve and written a story next to it, and the story is doing no work that the curve did not already do.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 1's power-law section, which lists web in-degree, product sales by rank, web-site sizes and Zipf's word-frequency law as instances of the same functional form, notes that the populations of US states ordered by size follow the same law as word frequencies, and separately offers the Matthew effect — high values of a property causing that property to increase, via links attracting links and best-sellers being advertised — as the usual explanation for the steeper exponents.
