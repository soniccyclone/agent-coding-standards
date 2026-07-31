---
type: lesson
title: "Price protection against a stated motive, and write the premise down"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Price protection against a stated motive, and write the premise down

**Lesson:** Protection is treated as a quality that a system either has or lacks, which is why arguments about it are unresolvable — one party can always name an attack the other has not defeated, and the escalation has no natural stopping point. The productive reformulation is that protection is not a barrier but a cost multiplier: it raises the effort required to get past it. Effort is only meaningful relative to someone's willingness to spend it, so the design input is not the set of possible attacks but a statement about who is likely to try and how motivated they are. Casual curiosity gives up almost immediately. Someone with a reason to persist does not. These call for measures that differ by orders of magnitude in cost, and neither is the right answer to the other's problem.

So the deliverable is a written premise: this is the environment we assume, this is the level of motivation we are pricing out, and here is the measure calibrated to it. That single paragraph does more work than the mechanism it describes. It makes the design reviewable, because a reader can dispute the premise instead of enumerating attacks. It stops the escalation, because measures beyond the stated level are out of scope by construction rather than by fatigue. It records the trigger for revisiting: when the environment changes — when the system becomes reachable by people the premise did not contemplate, or starts holding something worth real effort — the premise is false and the design must be reopened, which is a much easier thing to notice than a gradual mismatch between an unstated assumption and reality.

The honesty requirement runs alongside it. Deliberately choosing a modest measure is legitimate; representing that measure as more than it is, is not, because users calibrate their behaviour to what they think is protected. A stated premise makes it possible to be modest without being misleading: the mechanism is described together with what it does not stop, so nobody builds on a guarantee that was never offered. And it exposes the case that ought to be uncomfortable — a design whose premise, once written down, is one nobody is willing to sign. That discomfort is the finding. It means the protection was never calibrated to anything, and no amount of additional mechanism fixes an absent premise.

**Source:** [Project Oberon](../works/project-oberon.md) — section 11.5's statement that a protection administration is similar in purpose and function to a lock, that the race between techniques of breaking locks and of countermeasures is well known and the design makes no attempt to contribute to it, that the design is based on the premise that the server operates in a harmonious environment, and that a minimal amount of protection machinery was nevertheless included which raises the effort required for breaking protection to a level not reached when curiosity alone is the motivation.
