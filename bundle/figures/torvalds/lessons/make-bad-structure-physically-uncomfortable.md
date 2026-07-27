---
type: lesson
title: "Choose conventions that make bad structure physically uncomfortable, so the layout itself reports design failure"
figure: torvalds
works: [linux-kernel-coding-style]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Choose conventions that make bad structure physically uncomfortable, so the layout itself reports design failure

**Lesson:** The most interesting move in this style guide is that its rules are not chosen for tidiness; they are chosen to be intolerable when the code underneath them is badly decomposed. A wide indentation unit is defended not only because it makes block boundaries obvious to tired eyes but because it runs code off the right edge of the screen as soon as nesting gets deep — and that discomfort is the point. The rule does not forbid deep nesting; it makes deep nesting hurt, and then instructs you to read the pain as a message about the program rather than about the rule. The same inversion runs through the length guidance: a function's allowable size shrinks as its complexity grows, so the more convoluted a routine becomes the more aggressively the convention squeezes it.

The second half of the same idea is a set of proxy metrics for comprehensibility that are cheap to check mechanically. Count the local variables; past roughly the number of things a person can hold in mind at once, the function is doing too much and should be split. Notice whether you feel the need to comment the middle of a function body; that urge is evidence the body should have been several functions with names instead. Notice whether you are explaining how the code works rather than what it is for; if the mechanism needs prose, the mechanism is wrong. Each of these converts a vague quality — "this is hard to follow" — into an observable, arguable signal that a reviewer can point at without having to win an aesthetic debate.

Why it holds: the properties we actually care about in code (can a stranger predict its behavior, can it be changed safely) are not directly measurable, and any process that relies on individual judgment about them scales badly across thousands of contributors. Correlated surface properties that anyone can see are worth far more than accurate but unmeasurable ones. A convention that merely expresses a preference gets argued with; a convention that makes the disfavored thing awkward to write wins without argument, every time, from everybody.

What a programmer who believes this does differently: they design their conventions backwards from the failure modes they want to catch. Instead of asking "what should code look like," they ask "what would make the mistake I keep seeing physically annoying to commit," and set the rule there. They also resist the escape hatch — the reflex to loosen the rule when it starts to bind — because the binding moment is exactly when the rule is doing its work.

**Source:** [Linux Kernel Coding Style](../works/linux-kernel-coding-style.md) — the indentation rationale, which answers the complaint about code drifting rightward by saying the drift is a warning about the program; the functions chapter, which ties maximum length inversely to complexity and caps local variable count at what a person can track; and the commenting chapter's rule against explaining mechanism or annotating the interior of a function.
