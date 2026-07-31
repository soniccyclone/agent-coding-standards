---
type: lesson
title: "A design method cannot supply the invention, only the retrospective explanation — and that is still worth having"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A design method cannot supply the invention, only the retrospective explanation — and that is still worth having

**Lesson:** Any methodology presented as a sequence of derivation steps invites a false reading: that if you follow the steps you will arrive at the answer. For most routine work the reading is close enough to true, which is exactly why it goes unchallenged. But there are results that no amount of systematic refinement produces, because the essential move in them is a leap — someone noticed that a particular quantity, for no locally motivated reason, happens to characterise exactly the thing being sought. A method cannot manufacture that noticing, and pretending otherwise sets people up to conclude they are bad at the method when in fact they are up against something the method was never able to do.

The honest position is that a derivational method is an explanation technology rather than a discovery procedure, and that this is a substantial thing to be. Take a construction you already have and no longer believe, and rebuild it as a chain in which each step is small enough to check: an abstract version whose correctness is obvious, then the extra state that records what the abstract version was doing, then the representation that makes it cheap. What you get out is not the invention but the reason it works, factored into pieces each of which can be verified without holding the rest in your head. That is the difference between an artifact you use because it has not failed yet and one you can modify without fear.

Two practical consequences. First, when you meet a piece of work that resists explanation, do not conclude it is beyond understanding; conclude that nobody has done the reconstruction yet, and that the reconstruction is a distinct piece of work with its own value. Second, resist letting a clean derivation in a write-up imply that the author walked it forwards. Presenting reconstruction as discovery is a small dishonesty with a large cost — it teaches readers to expect that good structure emerges from procedure, when in fact good structure is usually imposed afterwards on something that arrived by other means.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the introduction to Section 5.4, where Reynolds applies the data-representation-structuring methodology to Tarjan's strongly-connected-components algorithm, describes the algorithm as unusually difficult and ingenious, lays out the three-stage plan from abstract recursive depth-first search through added abstract state to concrete representation, and states plainly that although the presentation will show why the algorithm works it will hardly make it obvious — that methodology cannot supply the ingenuity needed to invent an algorithm of this kind, but can provide a clear retrospective explanation.
