---
type: lesson
title: "Derive the reasoning in the general setting and let only the implementation depend on your special case"
figure: karp
works: [an-n-5-2-algorithm-for-maximum-matchings-in-bipartite-graphs]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Derive the reasoning in the general setting and let only the implementation depend on your special case

**Lesson:** Hopcroft and Karp are solving a restricted problem, and they announce up front that they nonetheless intend to prove everything they can without using the restriction, precisely because they hope to carry the reasoning to the unrestricted case later. The structure of the paper follows: the facts about improvement structure, the bound on how many phases are needed, the characterization of when you are done, all of it is established for arbitrary graphs. Only when it comes time to actually find a batch of improvements efficiently does the special structure get used, because that is the only place it is genuinely needed. The restriction buys an implementation, not a theory.

This is dependency direction applied to your own reasoning rather than to your module graph, and it pays in two currencies. The obvious one is reuse: when the restriction is later relaxed, the entire conceptual half of the work still stands and only the search routine must be rebuilt. The less obvious and more valuable one is that the discipline tells you exactly where the restriction is load-bearing. If your argument silently helps itself to a special assumption in twelve places, you have no idea what you actually depend on, and any change to the setting means re-deriving everything. If it uses the assumption in one clearly labeled place, that place is the interface, and you can see at a glance what a different setting would cost you.

For a programmer this is the argument for pushing knowledge of your particular backend, format, or data shape down to a single boundary rather than letting it seep through the reasoning. The test is not whether your code compiles without the specialization but whether your explanation of why the code is correct needs it. Write the general argument first, even when you only have one case to serve, then note deliberately which step consumes the special structure. The result costs almost nothing extra to produce and repays you the first time the setting changes, which it will.

**Source:** [An n^5/2 Algorithm for Maximum Matchings in Bipartite Graphs](../works/an-n-5-2-algorithm-for-maximum-matchings-in-bipartite-graphs.md) — the stated decision to derive the second section's results for general graphs with an eye toward the unrestricted problem, confining the use of the bipartite structure to the third section's construction of the layered search.
