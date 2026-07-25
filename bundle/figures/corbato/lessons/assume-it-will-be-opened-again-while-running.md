---
type: lesson
title: "Assume It Will Be Opened Again While Running"
figure: corbato
works: [multics-the-first-seven-years, on-building-systems-that-will-fail]
axes: [cognitive-load, expressiveness]
subdomains: [operating-systems-and-systems-programming, programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Assume It Will Be Opened Again While Running

**Lesson:** If a system's whole promise is that it never stops, then improving it by stopping it is not available, and the ability to change it in place becomes a functional requirement rather than an operational nicety. Multics was run against that requirement hard: the entire source lived online inside the system it built, five to ten modified modules were installed on a typical day, and roughly three quarters of those went in without interrupting service, with the supervisor changes batched a couple of times a week. The Turing lecture states the general rule two decades later — assume from the outset that the system will have to be repaired or modified, because that assumption is what forces the degree of modularity and structure that makes repair possible at all.

The second half of the idea is that the system should be its own workshop. The retrospective is direct about CTSS being the pivotal reason Multics took no longer than CTSS did despite roughly ten times the code and a staff spread across three organizations and two states. Once Multics could host its own development, small groups did surprisingly large things: a full compiler by four people in two years, a debugger bootlegged into existence by one person working nights. They describe the effect as amplification, and note it was largest on the strongest people, which is the part worth remembering — tooling does not level a team, it widens it.

Someone who believes this designs the replacement path at the same time as the thing being replaced, and treats "how does a running instance get from this version to the next one" as part of the specification. They also spend early effort making the artifact usable for its own construction, on the grounds that every shortening of the loop between noticing a problem and having fixed it pays compound interest for the life of the project.

**Source:** [Multics: The First Seven Years](../works/multics-the-first-seven-years.md) — the current-status section's account of online library installation and the maintenance strategy of using the system on itself, plus the implementation-experience discussion of the amplifier effect. The Turing lecture lists designing for repair and modification among its closing recommendations.
