---
type: lesson
title: "Give the unchangeable reader the dumbest possible format"
figure: wirth
works: [project-oberon]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Give the unchangeable reader the dumbest possible format

**Lesson:** Every interface has two sides and they rarely cost the same to revise. When one side is fixed — burned into read-only parts, shipped in hardware, distributed to machines you will never touch again — the asymmetry should decide the whole design of what crosses between them. The fixed side must be given the smallest, least interpretive job you can construct: not a format it must understand, but a format it must merely obey. Sized chunks with destinations attached, a sentinel that ends the sequence and doubles as the handover, and nothing else. No versions, no options, no structure whose meaning could ever need to change, because a change on the fixed side is not a release, it is a recall.

Notice that this is the opposite of the usual instinct, which is to make the earliest, most privileged component the most capable one, since it is the one with nothing beneath it to lean on. That instinct produces exactly the wrong distribution of knowledge: complexity placed where it can never be corrected and where its failure has no diagnostic above it. Push everything decidable to the changeable side. If the loaded content is what says where it goes and where control resumes, then any future rearrangement of the system is a change to a file, and the immovable part never learns of it. The measure of success is not that the fixed component is small but that it has never had to be replaced, and small is what makes that likely.

The general habit is to identify, for each interface in a design, which side is more expensive to change, and to move interpretation away from it. This is worth doing even when neither side is literally immutable, because the asymmetry is usually large: a client library distributed to thousands of installations versus a server you deploy hourly, a device's firmware versus its host driver, a stored format versus the program that reads it. Whichever side you cannot fix in an afternoon is the side that should contain the least policy — and generality is what buys that, since a format that says nothing about what the bytes mean cannot be made obsolete by a change in what they mean.

**Source:** [Project Oberon](../works/project-oberon.md) — section 14.1's account of the boot loader, kept as simple as possible because it is burnt into ROM on every workstation and cannot be changed without considerable effort, with a boot file format of size/address/bytes blocks terminated by a zero-size block whose address is taken as the entry point of the next stage, a structure that never had to be changed during the entire development of the system.
