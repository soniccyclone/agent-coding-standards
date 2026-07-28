---
type: lesson
title: "Know in advance which measurements could change your decision, and say so when none of them could"
figure: ritchie
works: [unix-time-sharing-system-a-retrospective]
axes: [hardware-affinity, verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Know in advance which measurements could change your decision, and say so when none of them could

**Lesson:** The most instructive passages of this paper are the ones about numbers, because Ritchie keeps stating what each number is and is not good for. He times a file copy against two other systems, reports it, and then dismantles his own result: seek time dominates, placement was not optimized, no statistical significance should be read into it. The number is offered as weak evidence against a specific worry — that a flexible file representation costs a lot — and for nothing else. He then reasons about doubling the disk block size, concludes throughput would nearly double, and declines anyway because of space utilization on a device that is already ninety-five percent full and a probable drop in cache hit rate that he says outright has not been reliably estimated. A live tradeoff is described with one of its terms explicitly unknown rather than quietly assumed away.

The sharpest move is about the cost of writing a system in a high-level language rather than assembly. He gives an honest estimate of the penalty in size and speed, notes that no thorough study was done, and then says a thorough study would be beside the point, because no plausible result would send them back to assembly language. That is not anti-empiricism; it is recognizing that the decision was dominated by terms the benchmark does not measure — programs that would never have been written at all, a system nobody could previously modify becoming modifiable by strangers, and portability across machines that arrived as an unplanned gift. Measurement retains a role, just a different one: a profiler directs attention to the small fraction of code where careful hand-work pays, which is precisely the question a measurement can settle.

A programmer who believes this asks, before running a benchmark, which way each possible outcome would move them. If every outcome leads to the same action, the benchmark is ceremony and the honest thing is to state the dominating reason instead. When they do report numbers, they report the conditions that make them fragile in the same breath, and they name the terms of a tradeoff they could not estimate rather than pretending the estimate was zero. And they reserve measurement for the questions where it is decisive: where the time actually goes, and whether a specific fear is founded.

**Source:** [UNIX Time-Sharing System: A Retrospective](../works/unix-time-sharing-system-a-retrospective.md) — the file-copy timing experiment and its self-imposed caveats, the block-size tradeoff with its unestimated term, and the section on using a high-level language where a comprehensive cost study is judged interesting but irrelevant.
