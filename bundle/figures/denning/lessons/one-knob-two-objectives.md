---
type: lesson
title: "A single parameter pulled by two objectives with distant optima cannot be tuned, only split"
figure: denning
works: [virtual-memory]
axes: [hardware-affinity, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A single parameter pulled by two objectives with distant optima cannot be tuned, only split

**Lesson:** Denning does the arithmetic on block size twice, from two directions, and the interesting result is that the two answers do not merely differ — they differ by about a hundredfold. Approached from storage waste, the cost is a sum of two opposing terms: bigger blocks strand more unused space at the tail of the last one, smaller blocks multiply the bookkeeping needed to describe them. That sum has a clean minimum you can differentiate for, and with the segment sizes measured at the time it lands at a few dozen words. Approached from transfer efficiency, the useful fraction of a transfer is transmission divided by transmission plus positioning delay, and since the positioning delay of the devices in use was fixed and enormous, efficiency demanded blocks of many hundreds of words. Small blocks bring a third benefit besides low waste — code that a given run never executes tends to land on blocks of its own and never get fetched at all — which pushes the same direction and widens the gap further.

The point is not the numbers; it is what a gap of two orders of magnitude between the optima means. It means no setting of the parameter is good. Every value is a defeat for one objective, and the usual response — argue about it, split the difference, tune it against a benchmark — is wasted motion, because there is no value that was ever going to work. Once you have both curves written down, the gap is visible and so is the fact that the search is over.

That reframing is what makes the two real repairs findable, and both of them change the structure rather than the value. One is to attack the term that created the gap: the positioning delay is a property of the device, so put a device without moving parts between the fast level and the slow one and the transfer-efficiency curve stops fighting. Denning is blunt that on the numbers, mechanical arm-positioned storage should not be carrying this traffic at all. The other repair is to stop pretending one parameter exists: use a coarse unit sized for transfer and a fine unit sized for waste, with the coarse one an exact multiple of the fine, so the stranded space is confined to a single fine unit at the end. That buys the right answer on both axes at the cost of one more concept in the design — and Denning names the condition under which the trade is bad, namely when the objects being stored are too small to be mostly coarse units anyway, which the measurements suggested was often the case.

A programmer who has this habit does something specific when a configuration value is contentious: write the cost curve for each objective separately in whatever crude closed form is available, locate each optimum, and compare their distance to the tolerance either objective can absorb. If the optima are close, tune and move on. If they are far apart, stop tuning — the design is asking one number to be two numbers, and the only honest fixes are to remove the constraint that created the distance or to admit the second parameter.

**Source:** [Virtual Memory](../works/virtual-memory.md) — the optimal-page-size derivation in the storage-utilization discussion, the transport-time and transport-efficiency expressions for the four device classes that follow it, Denning's remark on how startling the discrepancy between the two is, and the partitioned two-tier block scheme offered as a compromise.
