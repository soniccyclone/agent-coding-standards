---
type: lesson
title: "Leave the bottom layer unstructured so every layer above can choose its own structure"
figure: ritchie
works: [unix-time-sharing-system]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Leave the bottom layer unstructured so every layer above can choose its own structure

**Lesson:** The usual instinct when building a foundation is to give it opinions: record formats, access methods, declared sizes, typed containers. Ritchie and Thompson went the other way. The lowest level of their system knows only about an addressable sequence of bytes with no declared length, no imposed record boundary, and no distinction between reading it in order and reading it at an offset. Any structure a file has is the private business of the programs that agree on it. The payoff is that one set of operations reaches ordinary storage, physical devices, and channels between running programs alike, and a program written for one of those has already been written for all three.

This holds because structure imposed at the bottom is structure that every client must either accept or work around, and the workarounds are what actually cost you. A layer that declares "files contain records" forces a program whose data is not records to smuggle its shape past the abstraction, and forces the layer itself to grow variants until it is no longer small. Declining to know things is what keeps the primitive count low, and a low primitive count is what makes the pieces interchangeable. It also relocates each decision to the level that has the information to make it: only the assembler knows what an object file looks like, so only the assembler should be the one saying so.

A programmer who believes this designs the substrate by subtraction. Before adding a concept to a foundational interface, they ask whether some layer above could supply it instead, and if the answer is yes the concept does not belong below. They resist the temptation to make the base layer convenient for today's dominant client, because convenience encoded low down becomes a constraint on clients that do not exist yet. They also accept a real cost knowingly: the naive caller doing byte-at-a-time work pays overhead the structured design would have avoided, and the answer is a small buffering helper on top rather than a richer interface underneath.

**Source:** [The UNIX Time-Sharing System](../works/unix-time-sharing-system.md) — the file system sections describing ordinary files, special files for devices, and the I/O calls, together with the closing discussion of why no "access method" machinery or system-maintained control blocks were needed.
