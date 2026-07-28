---
type: lesson
title: "Hold the privileged code to the same discipline as the rest"
figure: saltzer
works: [protection-and-the-control-of-information-sharing-in-multics]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Hold the privileged code to the same discipline as the rest

**Lesson:** Systems habitually exempt their most critical code from the constraints
imposed on everything else, on the theory that the critical code needs freedom and can
be trusted with it. The exemption is backwards twice over. It removes the checks from
the code where a mistake does the most damage, and it strands that code outside the
ordinary toolchain, so it gets written and debugged with worse instruments than the
application code above it. Put the privileged layer under the same addressing and
checking regime as everything else and you get two compounding wins: its errors trip
the same guards that catch application errors, and it can be built with the same
compilers, debuggers, and habits, which is where most of the reduction in defects
actually comes from.

The second half of the idea is subtler and concerns where privilege is stored. A
single mutable flag that says "currently privileged" is a global variable holding a
security property, with the failure mode global variables always have: someone leaves
it in the wrong state across a transition and nothing complains, because the wrong
state is indistinguishable from the right one. Derive the current level of privilege
instead from an unforgeable structural fact — which code the executing instruction came
from — and the property becomes impossible to leave stale, because it is recomputed by
the same act that changes what is running. Every transfer of control automatically
lands in the correct regime, including the transfers nobody designed for. This is a
general pattern worth reaching for well outside protection: state that must
consistently track something else should be derived from that something, not stored
alongside it and maintained by convention.

Tightening the privileged layer's own permissions to the minimum it needs pays a
dividend that is not about security at all. When the layer that could write anywhere
is instead allowed to write only what it should, ordinary addressing bugs in it stop
being silent corruption and start being immediate faults, caught during development
rather than shipped. Constraints on trusted code are a debugging instrument as much as
a defense.

**Source:** [Protection and the Control of Information Sharing in Multics](../works/protection-and-the-control-of-information-sharing-in-multics.md)
— the primary-memory protection section, where the supervisor is treated as one more
protected subsystem running under descriptor control in the user's address space, its
privilege level determined by the origin of the current instruction rather than a
processor mode bit, and its own descriptors narrowed so that addressing errors surface
as violations.
