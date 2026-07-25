---
type: lesson
title: "Nobody can state what they want before using something, so make the system exist immediately and keep it alive while it acquires function"
figure: brooks
works: [mythical-man-month, no-silver-bullet]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Nobody can state what they want before using something, so make the system exist immediately and keep it alive while it acquires function

**Lesson:** The hardest part of building a system is deciding precisely what to build, and the person who needs it cannot tell you. Not from evasiveness: they have never had to answer the questions at the level of detail a working system forces, and a system is a thing that acts over time, which is exactly what imagination models badly. So a complete and correct statement of requirements, produced in advance by a client working with a designer, is not merely difficult, it is unavailable. The requirement is discovered by using versions of the thing, which means the specification has the status of a hypothesis under continuous test rather than of a contract settled at the start.

That epistemic fact condemns any staged process that defers the first end-to-end assembly until most of the design and coding is done. Such a process assumes the mistakes will be concentrated in the low-level realization, where they can be fixed as testing proceeds, and it therefore discovers unusable interaction, unacceptable performance, and hostility to error only after full construction has been paid for. The remedy of deliberately building a throwaway pilot is a diagnosis of the right disease with too crude a cure, since it still puts a single large discard between you and the knowledge. The better response is to make information flow backwards continuously: let what is learned during implementation reach the architecture, and what is learned by users reach both.

Concretely this means starting from a complete skeleton that does nothing and does it correctly, then growing function into it so that at every moment there is a system that runs and has been tested. Regression cost rises as it grows, and that cost is the price of the property being bought. The payoff is not only earlier feedback and the option to stop when the budget runs out and still ship something. It is also that the thing you are reasoning about is always real, so claims about it are checkable rather than projected, and the effect on the morale of the people building it is out of all proportion to the amount of function the first running version contains. Organic growth beats fabrication as a working metaphor because complexity that has been alive at every stage has been under test at every stage.

**Source:** [The Mythical Man-Month](../works/mythical-man-month.md) — the retrospective chapters, which withdraw the earlier advice to plan on discarding a first system and replace it with progressive refinement of an always-running skeleton, together with the critique of the staged model that advice presupposed. [No Silver Bullet](../works/no-silver-bullet.md) argues the same conclusion from the other end, in its sections on iterative extraction of requirements and on growing rather than fabricating systems.
