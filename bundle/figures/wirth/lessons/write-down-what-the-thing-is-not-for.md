---
type: lesson
title: "Write down what the thing is not for; the fixed limits then stop being defects"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Write down what the thing is not for; the fixed limits then stop being defects

**Lesson:** A representation with hard limits — a fixed number of entries, a bounded total size, a capacity chosen once — is normally treated as an embarrassment to be engineered away, and the engineering is expensive: growth policies, indirection, reorganisation, and a set of failure modes that only appear near the boundary. The limits are only embarrassing, though, relative to an assumed purpose. Change the purpose and they become correct. If the thing is a place where items arrive, are dealt with, and go away, then a small fixed capacity is not a restriction on legitimate use, it is a description of legitimate use. The trouble is that nobody ever wrote the purpose down, so every limit reads as an oversight and every user who bumps into one has a plausible bug report.

Stating the non-goal explicitly does three separate jobs. It converts each limit from an accident into a consequence, so the numbers can be checked against the intended workload instead of defended in the abstract. It gives you permission to choose the simple representation — a directory that fits in one small fixed region, occupancy tracked in a single word, positions computable rather than searched — and to keep the resulting speed, which is not a minor benefit since the whole structure now fits in a form that answers the common question without touching anything else. And it tells a user what they should be doing instead when they find the boundary, which is the difference between a system that is small and one that is broken.

The discipline this demands is that you must actually decline the excluded use rather than half-supporting it. A structure that is documented as unsuitable for indefinite accumulation but grows a little to accommodate it anyway has taken on the costs of both designs and the guarantees of neither. If the excluded use turns out to be genuinely wanted, the honest response is a second mechanism built for it, with its own representation and its own costs, sitting alongside — and the fact that you can tell it is a different mechanism, rather than an extension of this one, is the payoff from having written the boundary down in the first place.

**Source:** [Project Oberon](../works/project-oberon.md) — section 11.2's statement that the mail system is primarily intended as an exchange for short messages typically sent, received, read, and discarded, that mailboxes are not intended to serve as long-term archives for a large and growing number of long texts, and that this restrictiveness of purpose is what permits a reasonably simple implementation and yields practically instantaneous access; together with the representation that follows from it — a mailbox held as a single file split into a fixed-length occupancy part, a fixed-length directory of a small number of entries, and a message area of blocks, with the resulting bound on the number of messages a mailbox may hold stated as a plain consequence.
