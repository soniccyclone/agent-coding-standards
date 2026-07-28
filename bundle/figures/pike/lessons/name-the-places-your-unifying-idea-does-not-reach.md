---
type: lesson
title: "Name the places your unifying idea does not reach"
figure: pike
works: [the-use-of-name-spaces-in-plan-9]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Name the places your unifying idea does not reach

A system built on one strong organizing idea faces a temptation at the edges:
stretch the idea over the cases it fits badly, so the story stays clean. This
work does the harder thing and states the exceptions outright — creating a
process, naming hosts across dissimilar networks, and sharing memory are all
left outside the file model, each for a stated reason. Process creation carries
too much structure to survive being flattened into a single write. Network
addressing has genuinely incompatible naming and connection-establishment rules
across protocols, so a common hierarchy would be a lie. Memory is deliberately
excluded because expressing it in a remotable namespace would advertise a
capability the system cannot actually deliver over a wire.

That last reason is the sharpest one, and it generalizes: an abstraction is a
promise about what operations mean, and putting something inside it promises
everything the abstraction promises. If your uniform interface implies remote
access, then anything you place in it must survive being remote. Forcing a local
resource in there does not extend your generality, it corrupts it — callers now
have a legitimate expectation you must either satisfy or handle as a special
case, and you have paid the cost of the abstraction while forfeiting the
guarantee that made it worth having.

The practical habit is to keep an explicit list of what your central idea
deliberately does not cover, with the reason attached, and to treat that list as
part of the design rather than as an embarrassment. Boundaries that are written
down get argued about and can be revisited when circumstances change; boundaries
that are papered over become folklore, and the special-case code that enforces
them accumulates where nobody is looking. Stated limits are also what make the
claim of uniformity checkable at all — a model that is said to cover everything
tells you nothing about any particular case.

**Source:** [The Use of Name Spaces in Plan 9](../works/the-use-of-name-spaces-in-plan-9.md) — the closing "Position" section, which enumerates the resources kept out of the file-and-namespace model and gives a specific reason for each rather than defending the model's universality.
