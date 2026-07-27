---
type: lesson
title: "Ship a small set of composable primitives, and let every convenience be visibly a composition of them"
figure: torvalds
works: [git-version-control-system]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Ship a small set of composable primitives, and let every convenience be visibly a composition of them

**Lesson:** Git was built as two tiers on purpose. The lower tier is a set of narrow, unfriendly, single-purpose operations, each of which does exactly one thing to one of three places — the object store, the working-state cache, or the files on disk — and communicates in object names on standard input and output. The upper tier, the commands people actually type, were originally short scripts that strung the lower ones together. The everyday history-viewing command was a list-the-reachable-commits program piped into a compare-two-trees program. The everyday commit command was write out a tree, wrap it in a commit, move a reference. Making the whole state of a repository nothing but files under a directory, and the operations on it nothing but programs that read and write those files, is what allowed the composition tier to be shell scripts at all.

The architectural payoff is that the primitive tier can be small and complete instead of large and accommodating. Once the lower operations compose, a request for new behavior usually does not require new mechanism — it requires a new arrangement of existing mechanism, which anyone can write and nobody has to maintain forever. That is the difference between a system whose surface grows linearly with the features asked of it and one whose surface stays roughly fixed while its capability grows combinatorially. The three-way merge is the sharpest illustration: rather than a monolithic merge engine, the cache is given the ability to hold several candidate versions of a path at once, the trivially-resolvable paths collapse mechanically, and only the genuinely contested ones survive to be handed off to a separate program that resolves single files. Merging is not a feature of the store; it is a composition over a store that happens to be able to hold ambiguity.

The second payoff is pedagogical, and it is the reason the split is documented rather than hidden. Because the conveniences are compositions, a person debugging one can descend into the layer beneath it and watch each step separately. The abstraction is transparent in the specific sense that matters: it hides work, not mechanism. You can always ask what a high-level command is actually doing and get an answer in terms of operations you can run yourself, which is not true of a system whose friendly surface is its only surface.

A programmer who believes this resists the pull to implement each new user-facing capability as a new self-contained subsystem. They ask instead which primitive is missing such that the requested capability becomes a composition, add that one primitive, and build the capability on top where everyone can see it. They also accept that the primitive layer will look hostile to newcomers, and treat that as correct rather than as a flaw to be fixed by absorbing convenience downward into the core.

**Source:** [Git Version Control System](../works/git-version-control-system.md) — the core-level tutorial in the project's own documentation, which frames the system explicitly as a low-level operational layer with a friendlier layer built over it, reconstructs the commit and history-listing commands from their constituent operations, and works through merging as a sequence of separate low-level steps over a cache able to hold multiple candidate versions of a path.
