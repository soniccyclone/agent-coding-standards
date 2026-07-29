---
type: lesson
title: "Start from the extravagant version nobody could build, then compress it to exactly what the decisions read"
figure: schneider
works: [synchronization-in-distributed-programs]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Start from the extravagant version nobody could build, then compress it to exactly what the decisions read

There is a design route that reliably produces both a correct mechanism and an explanation of every existing mechanism in the same area, and it starts by deliberately building the wasteful thing. Take the coordination problem and restate it against a structure of absurd generosity: every participant holds the complete, totally ordered, unbounded history of everything that has ever happened, and every decision is a predicate over that history. This is obviously unbuildable — unbounded memory, complete knowledge — and that is fine, because correctness against it is trivial to see. The history contains everything, so if a decision is expressible at all, it is expressible here.

Then compress, in two independent moves. First, replace complete knowledge with local knowledge: each participant keeps its own copy of the history, and the design's real content becomes the question of which portion of that local copy is already final. Second, replace the unbounded history with the minimum state the decision predicates actually consult — a finite summary that is updated as the history is extended, retaining nothing the predicates never read. Neither compression is a heuristic; each is justified by a property established at the extravagant stage, which is why the result is trustworthy in a way that a directly-invented protocol is not.

The compression's legality rests on the decision rules being one-way — once true, never falsified by further information. Because of that, a predicate may be evaluated against any sufficiently complete portion of the history rather than requiring the whole thing, which is exactly the license needed to throw the history away and keep a summary. Notice the dependency structure: the property chosen to make distributed decisions safe is the same property that makes the memory bound possible. One well-chosen invariant paying for two apparently unrelated problems is the signature of having framed the problem correctly.

The route has a further dividend that is easy to miss. Because the extravagant version is maximally general, existing mechanisms in the same problem area turn out to be recognizable as particular compressions of it — the shared-memory variables of a conventional synchronization primitive are visible as a summary of exactly this history, and hand-tuned protocols in the literature can be read as optimizations of the derived one. You get a taxonomy for free alongside the artifact. A programmer working this way resists the urge to invent the efficient protocol first, because inventing it first forfeits both the correctness argument and the map of the design space.

**Source:** [Synchronization in Distributed Programs](../works/synchronization-in-distributed-programs.md) — the derivation in the synchronization section that recasts shared-variable coordination as a predicate over an append-only global history and then replicates that history locally, together with the implementation-considerations section replacing the unbounded queue with a finite-state encoding.
