---
type: lesson
title: "Build the first version for the machine you actually own, and let generality be earned later"
figure: torvalds
works: [comp-os-minix-original-announcement, linux-kernel-source-and-design]
axes: [hardware-affinity, cognitive-load, primitive-count]
subdomains: [operating-systems-and-systems-programming]
tags: [lesson]
---
# Build the first version for the machine you actually own, and let generality be earned later

**Lesson:** A designer starting a systems project faces an immediate temptation: abstract over the hardware from day one so the thing will work everywhere. The announcement takes the opposite stance without apology. It commits to one processor family's task-switching mechanism, to the one class of disk controller the author physically possessed, and states plainly that portability is not on offer. That is not a confession of amateurism; it is a scoping decision that makes the project finishable. A portability layer is an abstraction whose shape you cannot know before you have implemented against at least one machine honestly, and building it first means guessing at the seams — usually wrongly, and always at the price of an extra indirection between your code and every mechanism it needs to drive.

The reason this holds is that hardware-facing code has almost no slack. Interrupt delivery, privilege transitions, and address-space switching are not interchangeable services with a common interface waiting to be discovered; they are idiosyncratic mechanisms whose differences are exactly the interesting part. Writing directly to one of them keeps the number of concepts in play small enough that a single person can hold the whole control path in mind, and it keeps the mapping from intent to mechanism direct enough that when something misbehaves you are debugging the machine rather than your own guess about a family of machines. The generality that later made this same kernel run on everything from wristwatch-class chips to the largest machines built was extracted from working code, one port at a time, by people who could see where the real variation was.

What a programmer who believes this does differently is refuse to pay abstraction costs on speculation. They pick the narrowest hardware target that makes the project real, write to it without a compatibility veneer, and treat every subsequent target as evidence about where the abstraction boundary belongs. They also say out loud what they are not supporting, because an honestly narrow scope attracts the right collaborators while a vaguely universal one attracts complaints. The corollary is a willingness to be wrong later: code written this way will need restructuring when the second platform arrives, and that restructuring is cheaper than the wrong abstraction defended for years.

**Source:** [Original Usenet Announcement, comp.os.minix](../works/comp-os-minix-original-announcement.md) — the closing caveats, where the author declares the system non-portable because it exploits one processor's task switching, and limits device support to the only hardware he owned. Also [Linux Kernel Source and Design](../works/linux-kernel-source-and-design.md), whose eventual multi-architecture structure grew out of that single-target start rather than preceding it.
