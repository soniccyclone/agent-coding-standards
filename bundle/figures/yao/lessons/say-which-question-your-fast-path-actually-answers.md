---
type: lesson
title: "Say which question your fast path actually answers, because the cheap one and the useful one are rarely the same"
figure: yao
works: [should-tables-be-sorted]
axes: [expressiveness, verifiability]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Say which question your fast path actually answers, because the cheap one and the useful one are rarely the same

**Lesson:** A lookup that reports presence and a lookup that reports position are different operations, and the gap between their costs can be the whole result. It is possible to build storage where a single inspection tells you with certainty whether an item is in the collection while telling you nothing about where it lives — the inspected cell is decisive for the yes/no question because of what its contents imply about the arrangement, not because it is where the item would be. Every consumer of such a lookup who assumes the position came along for free is wrong, and will be wrong in a way that only appears once someone tries to read or update the item they just confirmed exists.

The habit this demands is to state the query your fast path answers in its weakest true form, not its most useful-sounding form. Membership, position, count, ordering, and nearest-match are a ladder, and a scheme that climbs one rung cheaply may be unable to climb the next at any price within the same budget. Whether the stronger query is even achievable under the same constraints is a separate research question, not a detail of implementation, so silently promoting the weaker answer to the stronger one is not optimism but a category error. Conversely, this is a design lever with real leverage: if the caller genuinely only needs the yes/no — a filter before an expensive path, an existence check that decides whether to do work at all — then buying only that is legitimate and can be dramatically cheaper than the full retrieval everyone assumes is the baseline.

The reason this is easy to get wrong is that the two operations are bundled in every familiar structure. Search a sorted arrangement and you land on the item; follow a chain and you arrive at it; probe a computed address and it is either there or absent. Bundling by habit becomes bundling by assumption, and the assumption becomes invisible. So the discipline is to ask, of any storage design, which questions it answers within the stated budget and which ones it merely answers eventually — and to write that down in the interface rather than leaving it in the head of whoever built it. The specification of a data structure is the set of queries it serves cheaply, and a structure that has been optimized against a weaker query set than its callers assume is a correctness problem waiting for a schedule.

**Source:** [Should Tables Be Sorted?](../works/should-tables-be-sorted.md) — the note following the single-probe construction, which points out that the scheme determines membership in one inspection but not the item's stored location, and proposes the stronger requirement as a separate open question about how large a value space could be accommodated under it.
