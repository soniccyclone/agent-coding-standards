---
type: lesson
title: "Gather requirements from the people already suffering, then keep the decision to yourself"
figure: torvalds
works: [comp-os-minix-original-announcement, linux-kernel-source-and-design]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Gather requirements from the people already suffering, then keep the decision to yourself

**Lesson:** The announcement does two things that look contradictory and are not. It asks a whole community what they like and dislike about the system they are currently running, and in the same breath declines to promise that any suggestion will be implemented. That combination — solicitation without obligation — is the governance structure that let one person's design survive contact with thousands of contributors. Input is cheap and should be collected in bulk from people whose complaints are grounded in daily use rather than speculation; the authority to decide what goes in is expensive and should not be distributed, because a design that accepts every request stops being a design.

Asking the incumbent's users specifically is the sharp part. People running an existing system in anger know precisely which limitations cost them time; they are a source of prioritized, falsifiable requirements in a way that a survey of hypothetical future users never is. Their dislikes double as a map of where the incumbent's abstractions leak, which is exactly where a new system has room to be better. This is why the request was not "what should an operating system do" but "what bothers you about the one you have."

The reason the veto matters is that a system's comprehensibility is a shared, finite budget. Every accepted feature adds interactions with every existing feature, and the growth is not linear; past some point no maintainer can predict the consequences of a change, which is the state in which systems ossify. Holding a single point of final judgment keeps the accumulated design inside one person's (or one hierarchy's) working model of it. The kernel later scaled this by nesting the same arrangement — subsystem maintainers with local authority, one integrator at the root — rather than by abandoning it for consensus.

A programmer who believes this runs open intake and closed adjudication. They make it easy to report a real problem and hard to get a feature merged on enthusiasm alone; they say no in public with a reason; and they treat "many people asked for this" as evidence of a problem worth understanding, not as a mandate for the particular solution requested.

**Source:** [Original Usenet Announcement, comp.os.minix](../works/comp-os-minix-original-announcement.md) — the request for feedback on what Minix users liked and disliked, paired immediately with the refusal to promise implementation. Also [Linux Kernel Source and Design](../works/linux-kernel-source-and-design.md), where the maintainer hierarchy scales that same open-intake/reserved-decision arrangement.
