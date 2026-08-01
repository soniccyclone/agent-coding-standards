---
type: lesson
title: "Two states are equivalent only if no future can separate them"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Two states are equivalent only if no future can separate them

**Lesson:** The standard justification for compressing state is that the discarded distinctions do not affect any answer you give. Applied to a system that is still running, that test is too weak, and the gap between it and the correct test is where a whole family of subtle bugs lives. Two states can agree on every answer available today and still be genuinely different, because the process continues: feed both the same subsequent input and they evolve into states that disagree. A representation that merged them cannot un-merge them, so from the moment of divergence it is simply wrong, and nothing in the reasoning that justified the merge would have predicted it.

The correct criterion is the one automata theory settled long ago and that engineering rediscovers painfully: two states may be identified only if, for every continuation, the outputs after that continuation agree. Present agreement is necessary and not sufficient. In practice you rarely need to check every continuation exhaustively; you need to ask one honest question about each proposed merge, which is whether there is any input sequence that would drive these two apart. If yes, the merge is sound only under the assumption that no more input arrives, and that assumption should be written next to it, because it is usually false.

The bugs this catches all look alike once you have the shape. A cache key omits a field that does not influence the current response but does influence the next one. A deduplication step collapses records agreeing on the fields projected by today's report. A compaction keeps totals and drops the components, and then someone needs a total over a subrange. A protocol implementation treats two connection states as one because they currently behave identically, and they stop doing so on the next message. In every case the local argument was correct and scoped to a snapshot, while the system was not a snapshot.

The constructive use is that the criterion also tells you what to keep. Working out which continuations separate two states hands you exactly the fields that must survive compression, which is a much better place to start than deciding what looks droppable. And it gives you a clean way to make a merge legitimate rather than abandoning it: restrict the continuations. If the input is closed, or the state is retired, or the interface stops accepting anything that could separate them, the merge becomes sound — the compression was never wrong in itself, only wrong relative to the futures the system still permits.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 4's lower-bound argument for exact counting in a window, particularly the second stage, which handles the case where two windows sharing a representation happen to have equal counts by appending further bits until their contents differ only in the leftmost position and the counts must disagree.
