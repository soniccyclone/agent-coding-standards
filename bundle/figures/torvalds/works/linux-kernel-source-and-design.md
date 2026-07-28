---
type: work
title: "Linux Kernel Source and Design"
figure: torvalds
description: The Linux kernel itself — an open-source, Unix-like monolithic kernel Torvalds started in 1991 and still maintains as final integrator, now developed by thousands of contributors. Its design choices (monolithic-with-loadable-modules architecture, the maintainer-hierarchy development model, a famously conservative "never break userspace" stability rule) are as influential as any of its code. kernel.org is the project's own release and source infrastructure.
subdomains: [operating-systems-and-systems-programming]
year: 1991-present
url: https://www.kernel.org/
extraction: complete
access: public
host: self-archived
tags: [work]
---

# Linux Kernel Source and Design

**Venue/year:** Ongoing since 1991; kernel.org has served as the canonical release point since the mid-1990s.
**Source:** https://www.kernel.org/ — live, the Linux Kernel Organization's official site, self-archived/institutional (Torvalds' own project infrastructure). Links out to source tarballs and git trees. Note: the git web frontend at git.kernel.org is currently gated behind an Anubis bot-defense challenge that blocks automated fetches (confirmed via curl and Wayback snapshot, both returning the challenge page rather than repo content); kernel.org's own homepage was used instead as it resolves cleanly and is part of the same official infrastructure.

## Lessons
- [Spend all your stability at one boundary: freeze what outsiders observe, churn everything behind it, and make the breaker do the fixing](../lessons/spend-all-your-stability-at-one-boundary.md)
- [Define your portable contract as the weakest behavior any target could exhibit, and quarantine every place you exploit more](../lessons/write-against-the-weakest-machine-in-the-set.md)
- [Treat your compiler as an adversary wherever memory is shared, and mark the sharing at each access rather than fencing broadly](../lessons/mark-the-sharing-at-every-access.md)
- [Ordering is a protocol between participants, never a property of one of them, and the set of observers who agree is part of the specification](../lessons/ordering-is-a-two-party-protocol.md)
- [Build the first version for the machine you actually own, and let generality be earned later](../lessons/build-for-the-machine-you-actually-own.md)
- [Gather requirements from the people already suffering, then keep the decision to yourself](../lessons/gather-requirements-widely-decide-narrowly.md)
- [Keep every participant's state complete and local, then refuse to encode who is in charge](../lessons/keep-the-whole-state-local-and-refuse-to-encode-policy.md)
