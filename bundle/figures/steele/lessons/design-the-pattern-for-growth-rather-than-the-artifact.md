---
type: lesson
title: "Small loses to real needs and large loses to the clock, so design the pattern for growth and hand the growing to your users"
figure: steele
works: [growing-a-language]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Small loses to real needs and large loses to the clock, so design the pattern for growth and hand the growing to your users

**Lesson:** This work sets up a dilemma and then refuses both horns. A small system can be finished, ported, and learned quickly, but it cannot meet what people actually need — the talk lists what its era's users were demanding, and none of it fits in a design of the size that was tractable to specify twenty-five years earlier. A large system can meet those needs but cannot be built in time; something smaller and warty arrives first, fills the niche, and cannot afterwards be displaced. Steele accepts that argument, having heard it made against always building the right thing, and then finds its gap: users tolerate the warts of whatever arrived first, but they do not tolerate them indefinitely. They complain, and the thing grows. Growth is therefore not a failure mode to be prevented by getting the design right, it is the certain future of anything that gets used. The only real choice is whether the growth was planned for.

What follows from that is a change in what the design object is. You are not designing a system; you are designing the space of systems it can become, with some decisions made now and others deliberately left open for people who will know more than you do. The talk reaches for the vocabulary of patterns to say this: a plan whose parts include empty slots, where some choices belong to the plan and others belong to whoever instantiates it, and which says something about how change over time is supposed to happen. And it takes the step of applying the idea to itself — the design of a language should be understood as a pattern for language designs, a tool whose output is more tools of the same kind.

The second half is about who does the growing, and the talk is precise about why delegation wins in a way that is easy to get wrong. The advantage of open, distributed development is not simply that more hands are available, since large centrally-planned projects also had many hands, nor even that you get help with the design, real though that is. The advantage Steele identifies is that the plan itself can move in response to the people using it, which is what makes them keep investing in it. He pairs this with an argument, borrowed from Alexander, that a fixed master plan actively estranges the people who live inside it, because it tells them their influence is confined to trivia. But he also declines pure decentralization: someone has to judge, test, and sift contributions quickly and republish them, precisely so that every user is not forced to independently evaluate every claim. Curation is a load-bearing part of the growth mechanism, not bureaucracy attached to it.

A designer who thinks this way spends their early effort differently. They ask which decisions must be fixed now because everything else depends on them, which can be deferred without poisoning the foundation, and what mechanism will let other people make the deferred ones. They treat "our users will extend this in directions we did not imagine" as a requirement rather than a risk, and they budget for the curation role from the start, since an extension mechanism with nobody sifting its output produces volume rather than a language.

**Source:** [Growing a Language](../works/growing-a-language.md) — the central argument that the designer should build neither a small nor a large language but a growable one, the survey of how Fortran, PL/I, and Pascal each fared against unplanned growth, and the discussion of patterns, going meta, and the role of a fast-moving curator.
