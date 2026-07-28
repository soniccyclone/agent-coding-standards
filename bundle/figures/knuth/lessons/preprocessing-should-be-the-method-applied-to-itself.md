---
type: lesson
title: "When a method needs a table about its own input, try computing it by running the method against itself"
figure: knuth
works: [fast-pattern-matching-in-strings]
axes: [primitive-count, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# When a method needs a table about its own input, try computing it by running the method against itself

**Lesson:** The matcher is useless without a table saying where to resume after each possible point of failure, and the obvious way to build that table is to write a second, unrelated procedure that analyzes the pattern for repeated structure. The paper does something better. The table records, for each position, how far the pattern can slide against itself before its prefix could line up again — which is a pattern-matching question, with the pattern playing both roles. So the table is computed by running the matching procedure with the pattern as the thing being searched for and also as the thing being searched. Knuth flags this in his own summary as the second of the two ideas the algorithm rests on, coequal with the first: precompute the shifts, and precompute them by sliding the pattern along itself.

The payoff is not a shorter program, though it is that too. It is that a system built from one mechanism used twice has one mechanism to understand, one correctness argument to make, and one cost analysis to do. The paper's proof that the preprocessing runs in time proportional to the pattern length reuses the argument for the matcher almost verbatim, because the situation is the same situation. And the incremental construction has a pleasing property that only shows up once you notice the self-reference: the table entries needed to compute later entries are exactly the earlier ones, already available, so the construction folds into a single left-to-right pass with no separate storage for the intermediate weaker table.

The general habit worth taking is to be suspicious of preprocessing steps that look like a different kind of computation from the main algorithm. When a method requires auxiliary information about its own input, ask whether that information is an instance of the question the method already answers. Often it is, because the auxiliary information is usually about self-similarity, overlap, or internal structure — and self-similarity questions are the original question with both arguments bound to the same thing. Two mechanisms where one would do is a cost paid forever, in reading, in testing, and in the risk that the two drift out of agreement about what they mean.

Recognizing the self-application also tends to be the moment the algorithm stops feeling arbitrary. The failure table looks like a magic array of numbers until you see that it is the record of one thing sliding along a copy of itself, at which point every entry has a reason you can reconstruct without consulting the definition.

**Source:** [Fast Pattern Matching in Strings](../works/fast-pattern-matching-in-strings.md) — the programming section, which derives the shift table by treating the pattern as its own text and then folds the construction into a single pass, and the summary that names self-application as one of the two ideas the method rests on.
