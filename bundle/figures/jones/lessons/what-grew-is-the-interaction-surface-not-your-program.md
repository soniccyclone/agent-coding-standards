---
type: lesson
title: "What outgrew your methods is the interaction surface, not the size of your program"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# What outgrew your methods is the interaction surface, not the size of your program

**Lesson:** When a way of building software stops working, the usual diagnosis is that the programs got bigger. That diagnosis is comforting and mostly wrong, and it sends you looking for the wrong remedy — more people, faster machines, a bigger editor window. The measure that actually moved is how much other machinery your code must be correct against. Early on, everything a program touched fit in one document you could hold; later the same program sits on an operating system, a storage layer, a database, a network stack, a dozen conventions it did not choose, and the documentation of what it must agree with fills a shelf. Line count went up some. The number of external things whose behaviour your program's correctness now depends on went up by orders of magnitude.

The distinction matters because the two quantities respond to different treatments. Sheer size is handled by decomposition: cut the thing into pieces small enough to hold, and each piece is as tractable as a small program ever was. Interaction volume is not touched by decomposition at all, because every piece still sits on the same substrate and still has to be right about it. Cutting a program in half does not halve what it must assume about the file system. So a method that only offers you "break it into modules" is answering the question that was already answered, and the one that got harder is untouched.

What interaction volume actually demands is the ability to state, precisely and briefly, what you are assuming about each thing you depend on — because you can no longer hold those assumptions in your head, and because the only alternative to writing them down is discovering them when they turn out to be false. That is a different skill from decomposition, and it is why the practical answer to growing complexity is a way of recording assumptions rather than a way of chopping things up. A useful diagnostic when a project feels out of control: ask whether the trouble is that there is too much of your own code to keep straight, or too much of somebody else's behaviour to keep straight. The second is the common case and the one that gets misdiagnosed as the first.

The failure mode to watch for is the one Jones names by analogy: someone who has built small things successfully being handed a large one and given no new method, only more time. It looks like a staffing problem and it is a method problem, and the reason it keeps recurring is that the thing that changed was invisible in the metric everyone was watching.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 1's "Background" section, on the growth of application scale outstripping available tools: the observation that increases in machine power lifted the old memory-size ceiling on program length, but that the more significant growth was in complexity of interaction with other systems, illustrated by the change in an experienced programmer's bookshelf from a single principles-of-operation document to a meter of manuals for access methods, operating systems and database systems; and the closing image of programmers entrusted with a full-scale bridge after mastering small ones, without being taught any new method.
