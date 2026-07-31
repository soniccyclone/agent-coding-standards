---
type: lesson
title: "Enumerate your rule violations and grade them by what they constrain"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability, hardware-affinity]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Enumerate your rule violations and grade them by what they constrain

**Lesson:** Every system announces disciplines it means to hold to — this part depends on nothing outside itself, this process looks only one step ahead, this layer knows nothing of that one — and every system breaks some of them. The two common responses are both wrong. Dropping the discipline because it is not perfectly held throws away the value of the parts where it does hold. Pretending it is held leaves the breaks undocumented, so that the first person to rely on the stated property discovers the exceptions by being wrong. The workable response is to write the breaks down as a finite list and grade each one.

The grading is the part that carries information, and the criterion is not how ugly the break is but what it prevents. A break that embeds a decision nobody will ever want to differ costs essentially nothing: the property was nominally lost but no future change is blocked, and it should be recorded and then forgotten. A break that embeds a fact which genuinely varies between the settings this thing is meant to serve is the expensive one, because it is precisely the thing that will have to be found and changed, and it is worth knowing exactly how many places it appears in and whether they can be collected into one. Two violations of the same stated rule can therefore differ by orders of magnitude in cost, and lumping them together as "exceptions" loses that.

Enumerability is also what makes the break tolerable in the first place. Three named places where a process consults context it claimed not to need is a fact a reader can hold; "sometimes it uses context" is not. Once you can count them you can also ask the useful question about each — was the break bought for something, and was the price fair? Frequently it was: collapsing a swarm of one-line indirections into their callers is a real gain in comprehensibility, paid for with a specific loss of independence, and stating both halves lets someone later re-open the trade instead of either honoring it blindly or ignoring the rule entirely.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.4, which states that the rule of parsing strictly on single-symbol lookahead without reference to context is violated in three places and then names each (statements beginning with an identifier, qualified identifiers, and selectors followed by a parenthesis, all resolved by the mode of the identified object); and the immediately following passage explaining that handling declarations inside the parsing routines avoids an unjustifiably large number of very short procedures but loses the parser's strict target-computer independence, distinguishing the harmless loss (variable allocation strategy and alignment, on the grounds that the strategy is hardly controversial) from the genuine target-dependence (the sizes of basic types, embodied in explicitly declared constants, mostly held in the type definitions initialized by the table module).
