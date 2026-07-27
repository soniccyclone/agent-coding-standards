---
type: lesson
title: "A deployed program becomes part of the situation it models, so it keeps invalidating its own requirements"
figure: lehman
works: [programs-life-cycles-and-laws-of-software-evolution, on-understanding-laws-evolution-and-conservation-in-the-large-program-life-cycle, metrics-and-laws-of-software-evolution-the-nineties-view]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A deployed program becomes part of the situation it models, so it keeps invalidating its own requirements

**Lesson:** When a program mechanizes some human or organizational activity, installing it does not leave the activity where it was. The people in that activity adjust what they do to whatever the program makes cheap or expensive; the surrounding technology and demand move; and the model the program embodies now has to account for the effects of its own presence. The loop closes: the system is inside the thing it describes. That makes the requirements a moving target not by accident of poor analysis but by construction, and it makes analysis of such a system unavoidably an act of prediction — you are guessing what the world will look like after your own program has acted on it.

This reframes never-ending change from a symptom of incompetence to a structural property of a whole class of software. Two separate sources of pressure are usually confused. One is imperfection: the initial model was thin, the analysis missed cases, and given time and care that debt can be paid down. The other cannot be paid down at all, because the world moves and the program's own influence on it moves too. Only the first responds to being more careful up front. Mistaking the second for the first produces the recurring fantasy that with a good enough requirements phase the changes would stop.

There is also no escape by relabelling. When a discrepancy shows up between what the program says and what the world does, you cannot rule that a new and separate problem has arrived; the problem was always whatever it is now understood to be, and what changed was the perception held by users, analysts, and implementers. So the honest accounting is that the same system must be continually re-fitted, or it steadily loses value until replacement is cheaper than repair.

A programmer who believes this designs for a lifetime of alteration rather than for an end state. They treat the cost of a single future change as a primary design variable — pushing it down at the start, and defending it against growth as the system ages — and they judge a system's economics over its whole life rather than by what it cost to first ship. Alterability becomes a property to be actively maintained, not a happy side effect of good taste.

**Source:** [Programs, Life Cycles, and Laws of Software Evolution](../works/programs-life-cycles-and-laws-of-software-evolution.md) — the treatment of programs that mechanize human activity, where the intrinsic feedback loop is drawn out, together with the opening discussion of why "maintenance" for software is nothing like restoring a worn physical part. Also [On Understanding Laws, Evolution, and Conservation in the Large-Program Life Cycle](../works/on-understanding-laws-evolution-and-conservation-in-the-large-program-life-cycle.md) — its commentary on the first law, which draws the conclusion that changeability itself has to be treated as a standing requirement of the system rather than a virtue. Also [Metrics and Laws of Software Evolution - The Nineties View](../works/metrics-and-laws-of-software-evolution-the-nineties-view.md) — its restated law set, where installation and operation are said to invalidate assumptions the software embeds, functional content must keep increasing for satisfaction to hold, and quality is said to *appear* to decline as the operational environment moves, so standing still reads as getting worse.
