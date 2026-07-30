---
type: lesson
title: "A replacement must not be worse than the incumbent in any way its users care about, and must not stop at imitating it"
figure: kay
works: [personal-dynamic-media]
axes: [cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# A replacement must not be worse than the incumbent in any way its users care about, and must not stop at imitating it

**Lesson:** New technology aimed at displacing an established practice tends to be judged by its builders on the axes where it obviously wins, while its users judge it on the axes where it regressed. Something that adds motion and search but loses legibility and comfort has, from the user's chair, gotten worse at the thing they were actually doing. So the entry condition for a replacement is a floor, not a ceiling: on every dimension the incumbent's users care about, you must be at least as good, and the list of those dimensions is longer and more physical than a feature comparison suggests — the qualities people never articulate because the old thing never failed to provide them. Meeting that floor is unglamorous engineering that buys the right to be considered at all.

The complementary error is stopping there. Once the substitute is faithful, the pull is to keep the incumbent's constraints as if they were part of the requirement — to preserve sequential access because pages were bound in order, to reproduce a fixed layout because ink does not move. Those constraints came from the old material, not the task, and carrying them forward means paying the substitute's costs while forgoing its advantages. The productive question at that point is what the old medium's users could never do because their material forbade it: many orderings through one body of material, structure derived on demand rather than fixed at authoring time, representation that the reader can reshape.

Held together, these give a two-stage test for any migration or rewrite: first, enumerate the incumbent's strengths honestly, including the ones nobody lists because they were never at risk, and refuse to ship until none of them has degraded. Then go back through the incumbent's *limitations* and ask, for each, whether it was essential to the problem or an artifact of the old implementation — because every one of the latter is unclaimed value sitting in your design. Systems that fail the first test get rejected; systems that pass it and skip the second become expensive imitations of what they replaced.

**Source:** [Personal Dynamic Media](../works/personal-dynamic-media.md) — the stated design goal of not being worse than paper in any important way, the accompanying account of how earlier displays won on dynamic writing while losing on contrast, resolution and ease of viewing, and the argument that a book read on such a system need not be treated as simulated paper because the non-sequential nature of the new medium admits many paths through one narrative.
