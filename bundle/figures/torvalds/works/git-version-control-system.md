---
type: work
title: "Git Version Control System"
figure: torvalds
description: The distributed version control system Torvalds wrote in 2005, in about ten days, after the Linux kernel project lost free access to the proprietary BitKeeper. Git's core design bet — content-addressed snapshots via SHA hashing rather than delta-based file history, cheap local branching, and no privileged central repository — reshaped how essentially all software is versioned today. Torvalds handed off day-to-day maintainership shortly after but the object-model design is his.
subdomains: [software-engineering-and-architecture]
year: 2005
url: https://git-scm.com/
access: public
host: self-archived
tags: [work]
---

# Git Version Control System

**Venue/year:** Created April 2005; git-scm.com is the project's official site today.
**Source:** https://git-scm.com/ — live, official Git project site, self-archived/institutional (Torvalds' own project's successor infrastructure, now maintained by the Git development community).

## Lessons
- [Name a thing by its content, and identity, integrity, and sharing stop being three separate problems](../lessons/name-things-by-what-they-are.md)
- [Make meaning independent of layout, and layout becomes a free variable you can spend entirely on the machine](../lessons/make-meaning-independent-of-layout.md)
- [A cache earns its place by being destroyable, and it is only sound if it knows the window where its key is a lie](../lessons/a-cache-must-be-disposable-and-distrust-its-own-key.md)
- [Ship a small set of composable primitives, and let every convenience be visibly a composition of them](../lessons/ship-primitives-and-let-conveniences-be-compositions.md)
- [Keep every participant's state complete and local, then refuse to encode who is in charge](../lessons/keep-the-whole-state-local-and-refuse-to-encode-policy.md)
