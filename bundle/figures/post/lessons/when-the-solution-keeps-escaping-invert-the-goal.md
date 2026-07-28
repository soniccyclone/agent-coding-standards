---
type: lesson
title: "When the easiest instance resists you, stop solving and start proving impossible"
figure: post
works: [formal-reductions-of-the-general-combinatorial-decision-problem]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# When the easiest instance resists you, stop solving and start proving impossible

Post spent a long stretch trying to decide, for a trivially describable rewriting process, whether iterating it from a given starting string ever halts. He settled the whole family of the very smallest parameter choices, and then hit a single specific instance — a two-symbol rule set you could write on a matchbook — that would not yield to anything he tried, while every starting string he actually ran either stopped or fell into a cycle. The reported conclusion is not "I need a better idea." It is that this specific pattern of experience, easy cases fully solved and the next case up refusing absolutely, is itself evidence about the problem rather than evidence about the investigator.

That reading is the interesting move. Repeated failure on a problem is normally treated as private information, embarrassing and uninformative. Post treats it as data, and the data has a structure worth reading: solvable-by-hand at the bottom, an abrupt wall just above, and no gradient in between. A problem whose difficulty rises smoothly with size is probably one you can attack with more effort. A problem that is trivial at one parameter and a stone wall at the next is telling you the difficulty is not quantitative, and that you should switch from looking for a procedure to looking for a proof that no procedure exists. His account of the larger project says the direction of his thought reversed outright — the goal stopped being "solve the decision problem for arbitrary systems" and became "show it cannot be solved" — and the reversal is what produced the results.

The practical version for a working programmer: track how your failures are distributed, not just that they happened. If a scheduler heuristic works perfectly on every case you can enumerate and then falls apart on the first case you cannot, you may be looking at a hardness result rather than a tuning problem, and further tuning is the expensive way to find that out. The cheap move is to spend a day trying to prove your own goal unreachable. Either you fail and return with a much sharper understanding of why the problem is hard, or you succeed and stop burning months on a search with no target.

There is a discipline attached, though: the inversion has to be a real attempt at a proof, not a shrug. "This is probably impossible" as an excuse for abandoning work is worthless. Post's version is a decade of effort building the machinery that could actually establish impossibility, and the reason it produced a foundational result rather than a resignation letter is that he treated the negative claim as something requiring exactly as much rigour as the positive one.

**Source:** [Formal Reductions of the General Combinatorial Decision Problem](../works/formal-reductions-of-the-general-combinatorial-decision-problem.md) — the introduction's discussion of the two forms of the iterated-rewriting halting question, where Post reports the small cases solved and one small instance intractable, plus the closing historical footnote describing the reversal from solving to proving unsolvable.
