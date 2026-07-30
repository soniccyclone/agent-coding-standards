---
type: lesson
title: "Let the requirement for privilege, not functional cohesion, draw your module boundaries"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Let the requirement for privilege, not functional cohesion, draw your module boundaries

**Lesson:** When some part of a task needs an authority that the rest does not, that difference should dominate the decomposition — ahead of what belongs together conceptually, ahead of what is convenient to call, ahead of every other cohesion criterion. The objective being minimized is the amount of code holding each authority, so the rule is to strip out of a privileged component everything that does not require the privilege and put it in an unprivileged one. A component that formats input, talks to a user, or validates arguments does not need the authority the component's core step needs, and leaving those things inside means the authority now covers all of them and every future change to them.

The same reasoning applies to splitting a task across components that already hold different authorities. If step one requires the ability to read a description and step two requires the ability to install a result, and some existing component already legitimately holds the second authority, then step two belongs there and step one belongs in a component that never acquires it — rather than giving one component both because it is doing one job. The right question at every seam is not "is this the same job" but "does this side need to be trusted with that."

There is a second half of the discipline that operates on the authorities themselves rather than the code. Where a single grant confers several powers, split it, so that a caller needing one of them cannot exercise the others. This applies even to powers whose consequences look equivalent: if you cannot actually establish that abusing one is no worse than abusing the other, separate them, because the cost of an unnecessary separation is a small amount of plumbing while the cost of a wrongly merged pair is unbounded and discovered later. Being unable to prove two authorities interchangeable is itself the argument for keeping them apart.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's statement that keeping privileged code as small as possible is the major consideration in deciding module scope, with the worked case of a privileged component kept small by moving its user-interface material into an unprivileged one; the separation-of-privilege discussion where creating and modifying authority were kept distinct despite the consequences of abuse appearing similar; and Chapter 4's division of deferred procedure construction between a component that reads the description and the trap handler that already had the authority to install the result.
