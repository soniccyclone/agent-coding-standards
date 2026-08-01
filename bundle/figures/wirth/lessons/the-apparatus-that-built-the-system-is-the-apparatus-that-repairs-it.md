---
type: lesson
title: "The apparatus that built the system is the apparatus that repairs it"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# The apparatus that built the system is the apparatus that repairs it

**Lesson:** During bring-up you are working with a system that does not yet function, and you write instruments to cope: something to display raw storage, something to inspect the on-disk structures directly, something to invoke a single component in isolation, something to load a replacement for one damaged part. These get treated as scaffolding, kept out of the delivered thing and allowed to rot. That is a mistake with a precise justification, not a matter of taste: the state of a system that has failed in the field is the same state as a system that is not yet finished. Both lack working higher levels, both must be examined from beneath, and both need exactly the operations you already wrote. Whatever got you through construction is, without redesign, the maintenance tool — and it did not come from foresight about failure modes, it came from having had to survive them already.

So the deliberate move is to keep the instruments, and specifically to keep them as a single component that can be reached by the same minimal means used during bring-up: a bare loading path, a keyboard and a display, nothing else. Two properties follow that are hard to get any other way. Its capability set is honest — every command in it exists because somebody needed it while the system was actually broken, rather than because somebody imagined a failure — and it works in the conditions it is for, because those are the conditions in which it was written. A diagnostic facility developed against a healthy system tends to depend on the health it is meant to investigate.

The corollary about polish is worth stating because it feels like neglect and is not. An instrument used rarely, by people who know the internals, in a situation where nothing else is available, gets no benefit from a pleasant interface, and every hour spent on one is an hour not spent on the coverage of its command set. Single-letter commands and raw numeric arguments are the correct answer, and the thing to invest in instead is the breadth of what can be inspected and changed. State that trade explicitly in the design, because the alternative — an unusable tool that is nice to use — is a failure mode that survives review.

**Source:** [Project Oberon](../works/project-oberon.md) — section 14.2's remark that extending Oberon0 into a much more versatile tool was not clever foresight but arose from the development process of the system itself, which naturally included a considerable amount of error detection and correction, so that the resulting command interpreter — memory inspection, sector inspection, directory inspection, module loading, file transfer — gives it the character of a maintenance tool; together with the accompanying judgement that user-friendliness was given no importance and that this was justified.
