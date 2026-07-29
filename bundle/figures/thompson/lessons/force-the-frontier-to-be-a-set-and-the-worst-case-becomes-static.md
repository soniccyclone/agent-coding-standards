---
type: lesson
title: "Force the frontier to be a set and its worst case collapses to a static count"
figure: thompson
works: [regular-expression-search-algorithm]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Force the frontier to be a set and its worst case collapses to a static count

Advancing a whole frontier of live possibilities instead of backtracking removes one blowup but permits another: nothing in the naive construction stops the same position from being entered many times over, and a pattern with several overlapping repetitions will pile up duplicate entries until the frontier is enormous. Thompson identifies this and fixes it in one move — before adding a position to the frontier, check whether it is already there. The frontier was always conceptually a set; enforcing that it actually is one is the whole repair.

What makes this worth extracting as a way of thinking is the consequence rather than the technique. Once duplicates are impossible, the frontier is a subset of the fixed collection of positions that exist in the compiled artifact, so its maximum size is not a function of the input or of how badly the pattern is written — it is simply the number of positions the compiler emitted, a quantity you can count by looking at the output. An unbounded dynamic worst case has been converted into a bound you can read off a static structure. That is a far stronger guarantee than a tighter average case, because it holds for adversarial input, it can be checked without running anything, and it lets you size the storage in advance.

The general pattern: when a dynamic process accumulates state, ask what static structure that state is drawn from, then ask what invariant would force the state to be a subset of it rather than a multiset over it. Idempotence of insertion is usually that invariant, and it is usually cheap. Thompson notes the paired judgment too — with this bound in place, the further cleverness other authors applied to pruning redundant search would cost more time than it saves. Establish the bound, then stop; additional optimization aimed at a case the bound already contains is spending real cycles against a hypothetical.

A programmer who believes this stops treating "it can blow up on pathological input" as an inherent property of a search and starts looking for the missing uniqueness invariant. And when reporting on a system's resource behavior, they look for a bound derivable from the size of the program rather than from measurements of typical runs.

**Source:** [Regular Expression Search Algorithm](../works/regular-expression-search-algorithm.md) — the notes section, where an expression with stacked repetitions is shown to explode the runtime lists, and checking for an existing entry before insertion is shown to cap each list at the number of corresponding instructions compiled.
