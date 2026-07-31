---
type: lesson
title: "Treat your outermost level as a stand-in for a layer you did not model"
figure: strachey
works: [continuations-a-mathematical-semantics-for-handling-full-jumps]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# Treat your outermost level as a stand-in for a layer you did not model

Every account of a system has to stop somewhere, and the stopping point is almost always dressed up as a natural terminus rather than the arbitrary cut it is. Once Strachey and Wadsworth have argued that no fragment of a program can be described in isolation, they immediately turn the argument on themselves: if a command cannot be understood without knowing what follows it, neither can a whole program. The thing that follows a program is not nothing. It is whatever supplied the program with its starting conditions and will do something with its results, which for them meant the operating system, and above that a job, and above that a human being at a console. The initial "nothing more remains to be done" they use as a base case is a convenient fiction, and they say so in the same breath as they adopt it.

Two things follow from being honest about the cut, and both are practical. The first is that you learn where the construction has to grow. If the reason a program needs its successor made explicit is that control might leave in an unplanned way, then the same reason applies one level up, and the machinery you built for jumps is already the machinery you will need for processes abandoning, jobs failing, and sessions being interrupted. Recognising the base case as a placeholder tells you your abstraction generalises upward rather than being special to the level you happened to start at. The second is that the tower does not terminate inside the machine at all. At some level the thing that decides what happens next is a person intervening, which is a genuine limit rather than a gap to be filled in later, and knowing where that limit sits stops you looking for a formal account of something that has none.

The habit to build is to interrogate whatever you wrote at the edge of your model. A top-level handler, a default that "the caller deals with it", an assumption that the process simply exits, a mock standing in for the environment — each one is a claim about a layer you declined to describe, and each is fine so long as it is labelled as such. The failure is not the cut; it is a cut that has been forgotten, because the constant you chose starts being reasoned about as though it were true. A programmer who writes down what lies beyond the boundary converts a hidden assumption into a stated one, and usually finds that the interesting cases were sitting just on the far side of it.

**Source:** [Continuations: A Mathematical Semantics for Handling Full Jumps](../works/continuations-a-mathematical-semantics-for-handling-full-jumps.md) — the footnote to the discussion of a whole program's meaning, which concedes that treating a single program in isolation is no better justified than treating a single command in isolation, sketches the further hierarchy of process, job and operating-system continuations that a fuller account would need, and observes that the outermost levels are not inside the machine but are supplied by operator intervention.
