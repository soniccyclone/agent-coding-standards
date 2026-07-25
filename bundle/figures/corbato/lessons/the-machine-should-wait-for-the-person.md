---
type: lesson
title: "The Machine Should Wait for the Person"
figure: corbato
works: [an-experimental-time-sharing-system, introduction-and-overview-of-the-multics-system, on-building-systems-that-will-fail]
axes: [cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# The Machine Should Wait for the Person

**Lesson:** Two very different goals travelled under the same name in 1962: keeping every hardware component busy, and letting several people each work at their own pace on one machine. Corbató separates them on the first page and picks the second, then makes the decisive move — machine utilization is demoted from an objective to a term inside a larger utility, one that includes the people. Once you accept that framing, the quantity worth minimizing is the delay between a person forming a question and seeing the answer, and everything else is negotiable against it.

The reason this holds is that debugging and design are searches, and the rate of a search is bounded by the latency of its feedback. A programmer who waits hours between attempts runs a handful of experiments a day; one who waits a second runs thousands. Corbató's observation was that as machines grew faster, this loop had gotten *worse*, which means the field had been optimizing the cheap resource and starving the expensive one. He also noticed something less comfortable: human tolerance is not a fixed constant. People who had endured multi-hour batch turnaround became visibly impatient at delays over a second once they had felt the faster loop. The standard you build to becomes the standard you are judged against.

A programmer who believes this instruments the round trip rather than the throughput, treats a fraction-of-a-second regression in interactive response as a defect on par with a wrong answer, and is willing to pay real machine efficiency for it. Corbató paid explicitly: his scheduler is structured so that computational efficiency is guaranteed never to fall below half, and he treats that as a fair price rather than a flaw. The corollary for anyone measuring a system: a utilization number that does not contain the humans in the loop is measuring the wrong system.

**Source:** [An Experimental Time-Sharing System](../works/an-experimental-time-sharing-system.md) — the framing distinction in the introduction between hardware-oriented multiprogramming and person-oriented time-sharing, plus the operating observations near the end of the prototype section about how quickly user expectations of response time shifted; the Turing lecture's CTSS retrospective supplies the sharper version of that shift, with users who had tolerated batch turnaround growing restless at delays of more than a second. The Multics kickoff paper restates the same priority when it argues that the greatest benefit of Project MAC was not simultaneous access itself but having editing, compiling, debugging and running available in one unbroken session.
