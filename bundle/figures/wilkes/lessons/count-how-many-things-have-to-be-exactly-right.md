---
type: lesson
title: "Compare two mechanisms by counting how many of their properties have to be exactly right"
figure: wilkes
works: [best-way-to-design-an-automatic-calculating-machine]
axes: [hardware-affinity, verifiability, parallelizability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Compare two mechanisms by counting how many of their properties have to be exactly right

**Lesson:** Two mechanisms can achieve the same effect while differing enormously in how many of their attributes must be precisely controlled for the effect to occur. One arrangement requires an event to begin at a critical moment relative to a shared reference, end at another critical moment, and have sharp transitions at both ends. Another arrangement requires only that an event happen at all, with its moment, its duration and its shape all free. Both work. Only the second is robust, because robustness is not a separate quality added to a design — it is the count of things that were allowed to be approximate.

This gives a comparison criterion that survives the loss of the specific technology. Enumerate, for each candidate design, the properties on which its correctness depends and mark which of them have to fall inside a tight tolerance. Prefer the design with the shorter list, and prefer it even when it looks bulkier, because every entry on that list is a future failure mode, a manufacturing constraint, a thing that must be re-verified when any neighbouring component changes, and a thing someone must remember. The cost of a tight tolerance is not paid once at design time; it is paid again on every change and every fault.

The most common source of unnecessary entries on the list is a shared reference that forces separate parts to agree about *when*. Removing the requirement to agree on timing, and replacing it with a requirement only to agree that something happened, usually shortens the list dramatically and simultaneously loosens the coupling between the parts. The same restructuring therefore improves robustness and independence at once, which is a strong hint that dependence on precise timing and dependence between components are two views of a single defect.

**Source:** [The Best Way to Design an Automatic Calculating Machine](../works/best-way-to-design-an-automatic-calculating-machine.md) — the comparison of the waveforms needed to move a value between registers in a serial synchronous machine versus a parallel asynchronous one, where the second requires only a single pulse whose timing, length and shape are all uncritical.
