---
type: lesson
title: "Keep the example that killed each simplification, and count before generalizing"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Keep the example that killed each simplification, and count before generalizing

**Lesson:** Anything you build for others to use — a notation, a method, an interface, a framework — has a history of simplifications you tried and abandoned. That history is the most valuable documentation you will ever produce about the thing, and it is the documentation nobody writes. Its value is in the pairing: each abandoned simplification recorded together with the specific case that defeated it. "This apparently redundant part could be dropped, and here is the concrete example where dropping it fails" is a complete answer to a question that will otherwise be asked repeatedly, and answered wrongly at least once by someone who noticed the redundancy and not the reason. Without it, every user must rediscover your dead ends, and the good ones will resent the apparatus while the incautious ones will remove pieces they needed.

The record is honest about limitations too, which is a second reason to keep it. If some restriction you imposed is inconvenient in a way you already know about — a constraint that forbids expressing something perfectly reasonable — say so, and say what breaks if you lift it. A user hitting that wall then knows it is a known wall with a known reason rather than an oversight, and knows what they are taking on if they work around it. A limitation you have named and bounded is a design decision; the same limitation undocumented is indistinguishable from a bug.

The complementary discipline governs growth. When one case exposes a gap — some property your method cannot exploit, some pattern it handles clumsily — the reflex is to generalize immediately, because the fix is visible and the case is in front of you. Resist long enough to ask how often the situation actually arises. Extending an apparatus to cover one observed instance is how methods and frameworks accumulate features that each serve a single historical need, and every such feature is charged to every future user forever. Count first; generalize when the count justifies it.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the interference-method subsection of the alternatives chapter, which reviews specification variants considered and rejected, including the hope of separating a dynamic-behaviour condition from a final-state condition (which worked for some problems but failed on the equivalence-relation operation) and the acknowledged inconvenience of requiring transitive interference assumptions, with the note that lifting transitivity causes problems beyond two participants; and the even/odd refinement in the examples chapter, where a missing exclusive-write property is diagnosed with the remark that it would be worth observing how often the property arises before seeking to extend the proof rules.
