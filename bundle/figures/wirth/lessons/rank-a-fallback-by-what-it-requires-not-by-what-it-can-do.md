---
type: lesson
title: "Rank a fallback by what it requires, not by what it can do"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Rank a fallback by what it requires, not by what it can do

**Lesson:** When a system needs a secondary route for the case where its primary route is unavailable, candidates get compared on capability — which one is faster, which reaches more, which is more convenient to operate. That comparison is the wrong one, and taking it seriously produces fallbacks that fail exactly when they are called upon. A fallback is invoked precisely when the ordinary assumptions have stopped holding, so the only property that matters is how much of the world it needs to be working. Count the required parts for each candidate: for one it may be a peer that must be running, a service that must answer, a driver that must be resident, a configuration that must be intact; for another it may be a local medium and a person. The candidate with the shorter list wins even if it is slower, clumsier, and reaches less, because a fallback that is unavailable has no capability at all.

Two consequences follow that are easy to skip. The first is that the mechanism which *selects* the fallback is itself on the dependency list, and it is the one people forget. Selecting automatically — probing to see whether the primary route works and switching if not — sounds like an improvement and quietly adds the probe, its assumptions, and the code implementing it to the set of things that must be functioning during the failure. A selector that lives outside the system entirely, operated by a person, cannot fail in a way that is correlated with what it is rescuing you from. That is worth more than the convenience of automation for a route taken rarely.

The second is that anything the fallback needs which lives in an unchangeable part of the system is a permanent commitment, and should be sized accordingly. A capability admitted into an immutable component cannot be corrected later, so the criterion for admission is not usefulness but necessity to the minimal path. This is what makes a rich fallback doubly expensive: it does not merely add dependencies at the moment of failure, it freezes them.

The counterweight, which keeps this from becoming an argument for making everything primitive: all of the above is justified by the fallback being rare. Establish that first. If the secondary route is actually taken often, its ergonomics matter and the calculation changes — but then it is not a fallback, it is a second primary route, and it should be designed and maintained as one. The mistake worth avoiding is applying fallback economics to something exercised daily, or daily economics to something exercised once a year.

**Source:** [Project Oberon](../works/project-oberon.md) — section 14.2's discussion of the alternative boot source needed to bring up a bare machine, where a removable local medium is used and its selection is made by a physical switch setting followed by reset; together with the explicit rejection of the network as the alternative source on three stated grounds — to keep network access routines outside the ROM, to keep the startup of a computer independent of the presence of a server, and in consideration of machines that operate stand-alone — and the closing observation that the need for the alternative source arises very rarely.
