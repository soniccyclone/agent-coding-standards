---
type: lesson
title: "A picture too tangled to draw honestly is evidence about the program, not about the picture"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A picture too tangled to draw honestly is evidence about the program, not about the picture

**Lesson:** Every abstract description of a system leaves things out — that is what makes it abstract and useful. But there is a difference between omitting detail and omitting *structure*, and the line falls in a specific place: within whatever the description claims to cover, it must show every interaction path that actually exists. If a message travels between two parts, the connection carrying it appears, full stop. You are not permitted to leave one out on the grounds that it is transient, or minor, or only used once during startup. Either the path is needed, and then it is part of the structure, or it is not needed, and then nothing should be sent along it.

The interesting case is what to do when honouring that rule produces an unreadable picture. The tempting response is to tidy the picture — drop the awkward arrows, split the diagram, redraw at a higher level until it looks manageable. That instinct treats illegibility as a presentation problem. The better reading is that the illegibility is a *measurement*: the tangle in the drawing is the tangle in the program, faithfully reported, and the correct response is to go simplify the program logic until an honest picture of it is readable. Fixing the diagram instead is not just self-deception, it is discarding the one signal that told you something was wrong.

This gives abstract descriptions a role beyond communication. A notation with the discipline that it cannot be drawn incompletely becomes an instrument: its own unwieldiness measures coupling you would otherwise have to hunt for. A programmer who takes this seriously stops asking "how do I make this diagram clearer" and starts asking "what is the diagram telling me about what I built" — and treats the urge to simplify a picture of a system, rather than the system, as a warning sign about their own honesty.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 4's section on implementing ports and interfaces, which states that a model may simplify but must represent the collaboration structure truly within its area of concern, refuses the excuse that a path lasting only microseconds can be omitted, and directs the reader to simplify the program rather than falsify the view.
