---
type: lesson
title: "Hand the extension the raw input before you finish interpreting it"
figure: wirth
works: [project-oberon]
axes: [expressiveness, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Hand the extension the raw input before you finish interpreting it

**Lesson:** A framework that interprets incoming events and then dispatches the result to a component has decided, on that component's behalf, what the vocabulary of possible requests is. Everything the component can ever be asked to do is a member of the set the framework knows how to recognise. That is exactly what you want for the common case: the recognition is written once, every component behaves consistently, and a new component gets the whole vocabulary for free. It is also a ceiling, and the ceiling is invisible until somebody wants an interaction the framework's grammar cannot express — one where the meaning of what follows depends on what the component is, and cannot be determined before it knows.

The fix is not to enlarge the grammar, which puts every future interaction back through the same bottleneck. It is to offer a second, earlier dispatch point: a notification delivered at the moment interpretation would begin, rather than after it has finished, whose contract is that the recipient may take over and consume the rest of the input itself. A component that wants the framework's vocabulary ignores this hook and receives the usual interpreted requests. A component that needs its own vocabulary answers the early notification, drives the input source directly until the interaction ends, and returns a flag saying it has handled things — at which point the framework abandons its own interpretation of the same input rather than applying it on top. That flag is the load-bearing part: without an explicit "consumed" answer the two interpretations both run and the result is a gesture that means two things at once.

The general shape applies far beyond input handling. Any pipeline that normalises then dispatches faces the same trade: normalisation is what makes the common path cheap and uniform, and it is also a lossy commitment made before the only party who knows what the data means gets to see it. Offering a pre-normalisation hook with an explicit take-over protocol keeps both properties without a mode switch or a configuration flag. The cost is honest and should be stated: a component that takes over is now responsible for terminating properly, for restoring whatever shared state the interaction disturbed, and for behaving sensibly if it is entered from an unexpected state — none of which the framework can do for it, because the whole point was that the framework stepped aside.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.9.1's note that the rectangle's `Handle` procedure is a receiver of a control message activated as soon as the middle mouse button is pressed, in contrast to other actions which are initiated only after the release of all buttons, so that this message permits actions under the control of individual handlers interpreting further mouse movements; together with section 13.8.2's `Edit`, which clears the pending key set when the object's handler reports a non-zero result.
