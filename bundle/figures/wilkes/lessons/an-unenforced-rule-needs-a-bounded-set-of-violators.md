---
type: lesson
title: "Leaving a rule unenforced needs an argument about who could break it, not about how likely breakage is"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Leaving a rule unenforced needs an argument about who could break it, not about how likely breakage is

**Lesson:** Some rules in a system are enforced by mechanism and some are conventions that the code is simply expected to follow. Leaving one in the second category can be entirely legitimate, but only on a specific kind of argument: that the set of code capable of violating the rule is small, shared, enumerable, and inspectable. When every participant that could break the convention runs the same modest piece of shared code, the convention is effectively enforced by the fact that there is one place to get it right. What is not a legitimate argument is that violation seems unlikely, or that the current callers are careful, since neither claim is stable under growth and neither can be re-checked later.

The reason to insist on this framing is that it makes the decision auditable in the future. Recorded as "we judged this safe," the omission cannot be revisited. Recorded as "this holds because only these components can violate it, and they share their implementation," it comes with its own trigger condition: the day a new participant appears that does not share the code, the argument has lapsed and the check has to be added. The convention has a stated precondition rather than an aura of acceptability.

The mirror image of this is choosing which side of an interaction bears an obligation, and the answer is not always the side that could most precisely discharge it. It can be much cheaper to let a signal be delivered spuriously and require every receiver to tolerate being woken with nothing to do, than to make each sender establish exactly that the receiver has something to act on. Both patterns come from the same discipline: decide explicitly which party carries each obligation and on what grounds, rather than defaulting to enforcing everything at the point where it is first noticed.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 3's note that reserving a shared segment before access is a programming rule not enforced by hardware or software, held not to be a serious hazard because the processes competing for a shared segment typically run in the same simple piece of shared code; and the same chapter's interprocess messaging decision that no attempt is made to wake a recipient only when it can act on the message, so processes must be prepared to be woken with nothing to do.
