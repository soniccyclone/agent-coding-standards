---
type: lesson
title: "Compare two architectures by which event fires their expensive operation, not by how expensive the operation is"
figure: schneider
works: [byzantine-generals-in-action-implementing-fail-stop-processors]
axes: [hardware-affinity, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Compare two architectures by which event fires their expensive operation, not by how expensive the operation is

Two designs can use the identical expensive mechanism and still differ enormously in cost, because they attach that mechanism to different events. If one design must run the costly coordination protocol on every durable state update, and another must run the same protocol only when an external input enters the system, then the whole comparison reduces to a question about the workload: which of those two events happens more often here? Neither design is faster in the abstract. The mechanism's per-invocation cost is the least interesting number in the analysis; the invocation rate is everything.

This reframes architecture selection as an empirical question with a checkable answer, which is a large improvement over arguing about elegance. Find each candidate's expensive operation. Identify the event that triggers it. Estimate the frequency of that event under the real workload. The design whose trigger is rare wins, and it can win by a margin large enough to overwhelm every other consideration. It also explains why the same two designs swap places between deployments without either one having changed: only the trigger frequencies moved.

The comparison has a second axis that is easy to leave out because it does not show up in a latency budget: what each design demands of the programmer. One approach may let a program be written as though nothing ever fails, with all recovery handled beneath it. Another may require the programmer to split program state into the part that must survive and the part that need not, keep durable references infrequent because they are slow, and hand-write the logic that reconstructs a running computation from whatever was saved. That is a large, permanent, error-prone tax on every program written for the platform, and it belongs in the cost column next to processor counts even though it is denominated in something else.

There is also a discipline lesson in doing this comparison at all when both designs are your own. The honest move is to lay out the cases where your other approach wins — tighter timing, no state partitioning, no recovery code to write — rather than advocating for whichever one you are currently presenting. Two approaches that both survive an honest comparison and win in different regimes are a more useful result than one approach declared superior, because a reader can then tell which regime they are in.

**Source:** [Byzantine Generals in Action: Implementing Fail-Stop Processors](../works/byzantine-generals-in-action-implementing-fail-stop-processors.md) — the section comparing this construction against the state machine approach, which turns on whether durable-storage accesses or external input reads are the more frequent event, and lists the programmer-facing burdens of state partitioning and recovery.
