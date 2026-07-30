---
type: lesson
title: "When participants cannot coexist, weaken each assumption until the promises can supply it"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [parallelizability, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# When participants cannot coexist, weaken each assumption until the promises can supply it

**Lesson:** A design in which components cannot be shown to tolerate one another presents a choice, and the usual choice is to add machinery — a lock, a phase, an ordering — until the intolerance disappears. There is a cheaper move to try first, and it is a search rather than a construction. Ask what the least you could assume about the outside world is, such that the component can still deliver what it promises. Then ask whether the other components' promises actually supply that much. If they do, you are finished and nothing was added. If they do not, weaken again, and keep going until either the assumptions close on each other or you have proved that they cannot, at which point you know exactly what the extra machinery has to buy.

Running this search is where the design gets discovered rather than merely checked. A first attempt to state what a component may assume is almost always far too strong — typically some form of "nothing important changes" — and each weakening exposes what the component genuinely depends on. One participant turns out not to need the world to stay still, only that nothing splits apart what it has already grouped. Another turns out not to need a strict ordering preserved, only that no two things ever swap places relative to each other, which is just enough to keep its traversals from circling forever. Neither of those conditions would have been written down by someone trying to describe the intended behaviour; they surface only under the pressure of the search, and they are precisely the conditions under which the components compose.

The termination test for the search is worth stating explicitly, because it is what tells you a design is sound rather than merely untried: each participant's assumption must be implied by what the others promise, including — for participants you intend to run several copies of — by its own promise. A component whose assumption is not a consequence of its own guarantee cannot be duplicated, and noticing that is how you learn whether a design admits one worker or many before writing any code. This search also does not require inventing new formal machinery. It is a discipline of asking "what is the least I can rely on" repeatedly, and it is available to anyone reasoning informally about concurrent components.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the multiple-cleanup-tasks subsection of the examples chapter, which starts from the observation that the earlier specification cannot be duplicated because its rely-condition is not a consequence of its own guarantee-condition, then successively weakens two conditions — from preserving the retrieved mapping to merely never splitting a group, and from strict order preservation to a weaker no-two-elements-ever-swap-relative-position condition motivated by traversals otherwise circling forever — until the coexistence obligations close.
