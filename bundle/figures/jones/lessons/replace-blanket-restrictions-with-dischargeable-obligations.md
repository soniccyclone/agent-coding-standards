---
type: lesson
title: "Replace a blanket restriction with an obligation you can discharge case by case"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [expressiveness, verifiability]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# Replace a blanket restriction with an obligation you can discharge case by case

**Lesson:** When a method cannot handle some class of construct, the fast fix is a rule forbidding it: no more than one reference to shared state per statement, no writes in this position, this pattern is not allowed. Such rules are cheap to state, cheap to check, and always wrong at the edges, because they are drawn to be safe under the worst assumptions rather than under the assumptions that actually hold. The better move, wherever you can afford it, is to replace the prohibition with a condition to be established. Then the cases the prohibition banned unnecessarily become available, and the cases it would have permitted unsafely get caught.

The shared-state case makes the difference concrete. A statement that reads a value and writes back a function of it is unsafe in general, so a syntactic rule outlaws it. But whether it is safe depends entirely on what the surrounding world is permitted to do: if nothing else may touch the value, the statement is fine; if others may only lower it, a weaker but still useful claim about the outcome survives; if others may move it arbitrarily, nothing survives. One obligation, evaluated against the declared tolerance for disturbance, decides all three — and it decides them correctly, where the syntactic rule was merely conservative in the first case and silent about the second.

The trade is real and should be made with open eyes. Prohibitions are mechanically checkable and require no thought at the point of use; obligations require judgement and are easy to skip. So the exchange is worth making where the banned constructs are genuinely valuable and the obligation is genuinely simple to evaluate, and not worth making where a rule costs nothing. What is never acceptable is leaving a prohibition in place while forgetting it was a stand-in for a condition — that is how a method's temporary limitation calcifies into a belief about what good code looks like.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the guarantee-conditions subsection of the interference chapter, which observes that the strict rule permitting only one global reference per assignment can be dispensed with, since an increment of a shared variable supports a claim about its outcome determined by the prevailing rely-condition, with the claim weakening as the tolerated interference grows; and its note that practical examples with two global references in one assignment occur in the examples chapter.
