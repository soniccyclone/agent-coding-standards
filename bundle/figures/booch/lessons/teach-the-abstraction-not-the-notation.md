---
type: lesson
title: "The transferable skill is abstraction, not notation, and most code is now written by people who were taught neither"
figure: booch
works: [the-future-of-software-engineering, architecting-the-unknown]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# The transferable skill is abstraction, not notation, and most code is now written by people who were taught neither

**Lesson:** The history of the field reads as a single continuous movement: each generation raises the level at which people describe what they want, and the previous level becomes something nobody has to mention. That movement runs through machine organization, languages, operating environments, and up into the way systems are described to each other, and its direction is the only stable thing about it. What follows is that fluency in any particular notation is a perishable asset, while the capacity to invent the right abstraction for a problem transfers across every level the movement passes through. Instruction that teaches syntax produces people who can operate today's tools; instruction that teaches abstraction produces people who can build the next ones.

The same reasoning deflates the appetite for new languages. Introducing one is rarely blocked by expressive power; it is blocked by everything that has to exist around it before anyone can use it, which is training, accumulated practice, and libraries. That is why a handful of languages carry most production work, and why the marginal value now sits in libraries rather than in syntax, exactly as it earlier migrated from operating environments up to platform interfaces. The exceptions are real but narrow: a genuinely new class of machine, where nobody yet knows what the right notation is, and a genuinely new class of author.

That second exception is the live one, because the demographic reality has already changed. Most of the people producing consequential software were trained in some other discipline and picked up programming as an instrument, and they are not going to become software engineers. Two responses follow, and both are engineering work rather than pedagogy. Design notations and tools that let non-specialists express what they need without the failure modes that a decade of accidentally-production prototypes taught the field to fear. And when teaching, aim at the habits of decomposition and abstraction rather than the vocabulary of a language, since the vocabulary will be obsolete and the habits will not. A programmer who believes this evaluates a proposed tool by whether it reduces friction for the people who will actually use it, and evaluates their own growth by the abstractions they can now see, not the syntaxes they have collected.

**Source:** [The Future of Software Engineering](../works/the-future-of-software-engineering.md) — the framing of the discipline's history as continuously rising abstraction, the deliberately provocative question of whether new languages are still needed and the answer that libraries and practice dominate the difficulty, the case for notations aimed at scientists and other non-specialists, and the preference for teaching computational thinking over coding. Also [Architecting the Unknown](../works/architecting-the-unknown.md), which repeats the preference and identifies thinking in abstractions rather than algorithms as the thing worth passing on.
