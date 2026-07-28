---
type: lesson
title: "Find the state that makes already-consumed input unnecessary, and a scan becomes a stream"
figure: knuth
works: [fast-pattern-matching-in-strings]
axes: [cognitive-load, hardware-affinity]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Find the state that makes already-consumed input unnecessary, and a scan becomes a stream

**Lesson:** The pivot of this algorithm is one observation made early and almost in passing: at the moment a comparison fails, the position reached inside the pattern already tells you what the recent input characters were, so there is no need to have kept them. Everything about the history that could matter to any future decision is recoverable from a single small integer. That is the whole trick, and it is not primarily an efficiency trick — it is a change in what the algorithm needs to have access to. The naive method reaches backwards into text it has already read; this one never does, because there is nothing back there it does not already know.

The consequences are the kind that matter when a program meets a real machine rather than a model of one. Never revisiting consumed input means the text can arrive from an external source and be discarded as it goes; working memory scales with the pattern, not the text; and the authors were careful to make the constants independent of how large the alphabet is, so the same reasoning survives changes in encoding. Knuth is explicit in the historical section that this was the origin of the whole effort: Morris was writing a text editor and wanted to avoid backing up over the file because the buffering that would have required was painful. The linear time bound came later and was almost a bonus. The real requirement was structural — be a stream processor — and the state-summary insight is what made that possible.

There is a second, subtler guarantee in the same family, and the paper treats it as a separate question deliberately. Bounded total work does not imply bounded work per input character; an algorithm can be linear overall while occasionally stalling for a long time before consuming the next character, which is intolerable if input is arriving in real time. So a later section proves a bound on how many pattern-shifts can happen between two consecutive character reads — logarithmic in the pattern length, with the base being the golden ratio — and shows the bound is achieved, by patterns built on the Fibonacci recurrence. What makes this instructive is the design consequence: a weaker version of the shift table would still give a correct linear-time algorithm, and the latency bound would be false. The stronger table exists specifically to buy the per-step guarantee, and the paper exhibits a pattern where using the weaker one produces a long run of useless work before the input advances.

A programmer who has absorbed this asks a particular question when facing any algorithm that re-reads its input: what is the smallest thing I could carry forward that would make the re-read unnecessary? Often it exists and is tiny, and finding it converts an algorithm that needs the whole input resident into one that runs on a pipe. And having got there, they know to check the second question separately — whether the work between consecutive input events is bounded, not merely bounded on average — because those two properties are bought with different mechanisms and an algorithm can have either without the other.

**Source:** [Fast Pattern Matching in Strings](../works/fast-pattern-matching-in-strings.md) — the informal development, where the remark that the pattern position recreates the recent input motivates never backing up, together with the theoretical section proving the golden-ratio-logarithmic bound on shifts between consecutive character reads and showing the weaker table fails to provide it.
