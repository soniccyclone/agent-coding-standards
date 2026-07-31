---
type: lesson
title: "A method cannot be judged on small examples, because the property you are buying is invisible there"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A method cannot be judged on small examples, because the property you are buying is invisible there

**Lesson:** Comparing two ways of working, the natural move is to try both on something small and pick the one that came out shorter. This reliably selects the wrong one. The compactness of a method on a small problem is driven by how much it can leave implicit, and what a method can leave implicit is exactly what stops being true at scale. Certain schemes get their brevity from the fact that a component's description happens to line up with the enclosing one's — which is nearly always so on a toy and nearly never so on anything real, where every piece is used in a context it was not shaped for. The elegant version is not merely less advantageous on the large problem; the thing that made it elegant has been removed.

There is a companion trap in judging a rule by its length. The shortest possible statement of any obligation is a restatement of the goal — "make it correct" is one line and helps nobody. A longer statement that names the separate things you must establish is worse as prose and enormously better as a tool, because each named item is a place to put an answer, and a person who has filled in all of them has done the work rather than merely been reminded of it. The value of a rule lies in the divisions it draws, not in its size. Compactness is a property of the notation; constructiveness is a property of the decomposition, and only the second survives being handed to someone else. Notation history bears this out — the shorter of two competing calculus notations is not the one that survived.

The practical instruction is to change what you evaluate on. Ask which method still works when a component is reused in an unfamiliar context, when values get overwritten, when the enclosing description and the piece's description have nothing in common. Accept that the better answer will look cumbersome on the examples you can fit on a page, and that this appearance is not evidence against it. A method chosen from small trials optimizes for the situation you are not in.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 5's closing comparison of state-pair post-conditions against single-state formulations: the acknowledgement that the alternative permits a shorter statement of the properties, the observation that some of that brevity comes from relying on the predicates of units and sub-units matching and that such matches occur infrequently in large problems, the Newton-versus-Leibniz remark that it is not always the shortest notation which is best, the point that the shortest rule for proving programs correct would be to say "prove programs correct" while a longer rule indicating useful divisions of the task is far more constructive, and the concluding claim that methods which work well on small examples may be at a disadvantage against methods of greater generality when applied to large problems even though the latter appear cumbersome on small ones.
