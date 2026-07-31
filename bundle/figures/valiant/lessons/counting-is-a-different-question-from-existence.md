---
type: lesson
title: "How many is a different question from whether any, and the two costs can diverge without limit"
figure: valiant
works: [the-complexity-of-computing-the-permanent]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# How many is a different question from whether any, and the two costs can diverge without limit

**Lesson:** It is natural to treat a tally as a by-product of a search: if you can find one solution efficiently you feel entitled to count them all by finding them repeatedly. The entitlement does not exist. Existence and quantity are separate questions with separate difficulties, and the gap between them can be total — there are problems where deciding whether any solution exists is genuinely easy, cheap enough to be a textbook algorithm, while determining how many there are is complete for a class believed far beyond reach. The counterexamples are not contrived. Producing an assignment that falsifies a formula is trivial; counting the falsifying assignments is maximally hard. Finding a perfect pairing in a bipartite structure has a clean polynomial algorithm; counting the pairings is the hardest counting problem there is.

The reason the intuition fails is that enumeration is the hidden assumption. Counting by search is only efficient when the solutions can be listed in time proportional to how many there are — and that property is a strong, separate condition that most problems lack. Once you notice it as a condition rather than a certainty, the design consequence is clear: any aggregate over a solution space (a count, a sum, a probability, a total weight) must be budgeted as its own capability, not inferred from the presence of a decision procedure. Systems get designed on the opposite assumption all the time, with a fast existence check in hand and a "how many match" query bolted on later as if it were the same feature.

The productive habit is to sort the questions you might ask about a space by mode rather than by subject matter: does one exist, exhibit one, count them, list them, sample one uniformly, sum a weight over them. Each is a different problem about the same object, they do not share a complexity, and their ordering is not intuitive. When you notice the counting version of a problem that you already solve cheaply, treat that as a warning that something new is being asked, and go find out where the counting version actually sits before promising it.

**Source:** [The Complexity of Computing the Permanent](../works/the-complexity-of-computing-the-permanent.md) — the introduction's observation that the permanent's natural combinatorial reading is a count of perfect matchings whose corresponding detection problem is polynomial-time solvable, the section 2 examples of easy detection with hard counting (falsifying assignments, monotone formulae, two-literal monotone clauses), and the definition there of enumerability in time proportional to the number of solutions as the extra property that would make counting-by-listing work.
