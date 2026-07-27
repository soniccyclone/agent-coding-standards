---
type: lesson
title: "Every term you introduce has a price you normally cannot feel, and anyone writing a large program is designing a language whether they admit it or not"
figure: steele
works: [growing-a-language]
axes: [cognitive-load, expressiveness, primitive-count]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Every term you introduce has a price you normally cannot feel, and anyone writing a large program is designing a language whether they admit it or not

**Lesson:** This work is delivered under a self-imposed constraint: the speaker may use only the shortest words of his own language, and any longer word must be defined on the spot before it can be used, either individually or by giving a rule that manufactures a class of new words from known ones. The constraint is not decoration. It puts the audience inside the experience of working in a language too small for the job, and it puts the speaker in a position where every abstraction he wants has a visible, immediate cost that he must pay in front of everyone. He reports what that did to him: it forced deliberation on each term, and turned every candidate abstraction into an explicit question of whether the definition was worth the trouble or whether he should make do with the clumsier phrasing he already had.

Two things fall out of the exercise that generalize well past rhetoric. The first is that concepts feeling primitive in your head are frequently not primitive in your medium, and you rediscover this by having to build them again in every new piece of work. Steele's example is the operation that picks the larger of two numbers, which is atomic to him as a thought and absent as a primitive from most languages. The general form is that the gap between your conceptual vocabulary and your medium's vocabulary is exactly the volume of definitions you will write before you can start on the actual problem, and any honest estimate of a project should include it. The second is that the constraint made hedging nearly impossible, because saying something imprecisely requires the vague words, and if you cannot reach for them you are pushed toward stating what you actually mean.

The conclusion the talk builds toward reframes ordinary programming. If getting anywhere in a language much smaller than your thoughts requires first defining a working vocabulary, then someone writing a very large program is not merely using a language, they are constructing one on top of it — hundreds of terms deep, with its own rules about how those terms combine. Steele's claim is that there is no other way to do it. The consequence is that the skills of language design are not a specialty for people who build compilers; they are what the naming, layering, and interface decisions inside a large codebase actually are, and they are being exercised well or badly regardless of whether anyone calls them that.

A programmer who accepts this treats their project's vocabulary as a designed artifact subject to review: is each term earning its definition cost, do the terms compose, is the growth rule for new terms stated anywhere, would a newcomer be able to learn the vocabulary in the order it was built. They also seek out constrained media on purpose — a deliberately small library set, a restricted subset, an explanation owed to someone without the jargon — because a constraint that makes you pay for each abstraction is the only reliable way to discover which ones you were taking for free.

**Source:** [Growing a Language](../works/growing-a-language.md) — the talk's governing rule about monosyllables and defined words, the remark about a primitive thought that is not a language primitive, the closing reflection on what the constraint did to the author's thinking, and the claim that a good programmer builds a working vocabulary and thereby does language design.
