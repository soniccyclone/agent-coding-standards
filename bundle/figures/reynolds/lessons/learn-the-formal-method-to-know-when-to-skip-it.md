---
type: lesson
title: "Learn the formal method so you can tell when the informal argument is enough"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Learn the formal method so you can tell when the informal argument is enough

**Lesson:** The usual defense of rigorous methods — that you should carry them out on your work — sets up an argument nobody wins, because carrying them out fully on everything is plainly too expensive and everyone knows it. The better position is that the purpose of mastering a formal apparatus is calibration. Correctness is sometimes obvious and sometimes only appears obvious, and the difference is invisible to anyone who has never worked the mechanism through. Knowing exactly what a complete derivation would consist of is what lets you look at a piece of code and be right when you say no derivation is needed here. Without that knowledge you are not saving effort, you are guessing, and your guesses will be wrong precisely in the subtle cases, since those are the ones where intuition has nothing to grip.

This suggests a definition of a good informal argument that is worth adopting verbatim. An adequate argument is one that gives a competent reader exactly enough to reconstruct the full derivation with no trial and error. The standard is not persuasiveness and not thoroughness. It is the absence of search: every gap left in the argument must be one the reader can close by direct application of things already known, never one that requires inventing something. Under that standard, whether a step may be left out is not a matter of taste. A step whose reconstruction is mechanical can be omitted no matter how intricate it looks; a step requiring a choice must be spelled out no matter how small it looks, because a choice is exactly what a reader cannot reproduce by grinding.

There is a corollary about how to teach and how to learn, and it is unsentimental. Formal methods do not sell themselves by polemic or by elegance. They sell themselves to someone who has just confidently written a short program they were sure was right — a binary search will do — and been shown it is wrong. Deny yourself the machine as a crutch and the failure arrives fast and cheap, and the appetite for a discipline that would have prevented it arrives with it. The same trick works on your own habits: try to be convinced by reasoning before you run anything, and the places where the reasoning will not close are the places worth the formal treatment.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 1.4.2's distinction between a logician's formal proof and a mathematician's proof regarded as an adequate collection of hints, with the conclusion that one studies formal methods in order to know when correctness is obvious; and the preface's account of teaching experienced programmers by having them attempt binary search without a computer.
