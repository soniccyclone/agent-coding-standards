---
type: lesson
title: "Apply a mechanism only where its reason holds, and let the system be asymmetric"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Apply a mechanism only where its reason holds, and let the system be asymmetric

**Lesson:** Once a system has adopted a mechanism for a good reason — a queue that decouples two components in time, a layer of indirection that buys independence, a staging step that makes failure recoverable — there is strong pressure to route everything through it. Uniformity feels like a virtue in itself, and an exception looks like an inconsistency somebody forgot to clean up. But the mechanism was justified by a specific condition, and where that condition is absent it is pure cost: an extra hop, an extra copy, an extra participant that must be running, and an extra place for the request to be sitting when someone asks why nothing happened.

So the correct habit is to re-ask the justifying question at each use site rather than to inherit the answer. If the reason for the indirection was that production and consumption have different timing and reliability requirements, then the paths where the work is immediate, small, and answerable on the spot do not have that property and should be served directly. This produces a system that looks uneven — some requests go through the staging structure and some are handled inline — and the unevenness is the point. It records where the condition holds. A design in which every path is treated identically has thrown away that information, and typically pays for the heaviest path's machinery on the lightest path's traffic.

Two obligations come with the asymmetry. It must be visible and explained, because an undocumented exception is indistinguishable from an omission and will eventually be "fixed" into uniformity by someone who cannot see the reasoning — one sentence at the branch, saying which condition is absent here, is enough. And the direct path must not quietly acquire a second copy of what the mechanism was providing; if it starts needing its own retry, its own durability, its own recovery, the condition has come back and the exception has expired. Checking that periodically is the difference between an asymmetry that reflects the problem and one that is merely old.

**Source:** [Project Oberon](../works/project-oberon.md) — section 11.2's remark that, while messages received for delivery are stored on a file and inserted into the queue as a task to be handled by the mail server later, the server's counterparts of the remaining mail commands access mailboxes directly, because the simplicity of the required actions, itself a result of the chosen mailbox representation, together with considerations of efficiency, do not warrant a detour via the task queue and the mail server; set against section 11.1's justification for the queue in the first place, namely that reliability and timing made direct handling of printing and mail dispatch unattractive and that weaker coupling in time between transmission and consumption was desirable.
