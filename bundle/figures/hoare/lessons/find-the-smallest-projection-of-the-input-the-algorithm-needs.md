---
type: lesson
title: "Find the smallest projection of the input your algorithm actually needs, compute it once, and work only from that"
figure: hoare
works: [notes-on-data-structuring]
axes: [cognitive-load, hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Find the smallest projection of the input your algorithm actually needs, compute it once, and work only from that

**Lesson:** Before designing the processing, read the conditions the answer must satisfy and ask what function of the input they actually mention. The answer is very often much less than the input itself — a few counts, a relation between pairs, a set of totals — and everything else in the raw data is irrelevant to the computation even though it is essential to the domain. Derive those quantities in a single pass, then design the algorithm as though they were the input. The raw data does not appear again.

This is worth doing even when the raw data is small enough to carry around. The projection makes the algorithm's dependencies explicit: what it needs is now a short list of named things rather than "the file," and anything not in that list provably cannot affect the result. It bounds the work, because the pass that builds the projection is linear and everything expensive afterwards runs over something much smaller. It gives you a natural seam — the projection is a stable interface between the part that knows the domain's messy details and the part that does the combinatorics — and it makes the algorithm reusable against any source that can produce the same summary. It also flushes out mistakes early: if a required condition turns out to mention something the projection does not carry, you have discovered a missing input before writing any of the hard code.

The way to find the projection is mechanical rather than inspired: write down what makes an answer correct, in whatever precision you can manage, then take the union of the quantities those statements refer to. The important discipline is that the projection is derived from the correctness conditions and not from a guess about what will be convenient. A projection chosen for convenience tends to keep whatever was easy to compute and drop something a condition needed, which is the failure that shows up much later as a special case nobody can explain.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the examination-timetable example, which first formalizes the six conditions any valid timetable must satisfy, then observes that constructing one requires no knowledge of each student's full course load, only the number of students taking each examination and the set of examinations conflicting with each one, and builds both from a single scan of the load data before the scheduling algorithm begins.
