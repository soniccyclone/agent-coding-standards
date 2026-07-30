---
type: lesson
title: "Test a candidate primitive by re-deriving the constructs it should replace, then keep them anyway"
figure: hoare
works: [communicating-sequential-processes-paper]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Test a candidate primitive by re-deriving the constructs it should replace, then keep them anyway

**Lesson:** When a field has accumulated a dozen competing mechanisms for the same job and no agreed criterion for choosing among them, the proliferation itself is the evidence that nobody has found the underlying operation. The productive response is not to add a thirteenth mechanism but to guess at a much smaller basis and then discharge the debt honestly: take the standard exercises that each of the existing mechanisms was invented to handle, and rebuild every one of them from the proposed basis. If a construct that was previously a distinct language feature falls out as a short, natural arrangement of the primitives, that is real evidence about which of the two was fundamental. If it comes out contorted, that is equally real evidence pointing the other way, and it should be reported rather than skipped. The exercise is a measurement, so it is only informative if you are willing to publish the awkward results alongside the elegant ones.

The conclusion people usually draw from a successful reduction is the wrong one. Showing that a construct is definable from simpler parts is not an argument for deleting it. A construct earns its own name and notation when it is used often, when reasoning about it is simpler than reasoning about its expansion, or when it can be implemented better than the general case allows — and none of those properties are affected by its being derivable. What the derivation buys is different and more valuable: it is the guarantee that the named construct is consistent with the rest of the system, because it has been exhibited as a special case rather than bolted on as an independent mechanism with its own semantics to be reconciled later.

So the two activities separate cleanly. Finding the small basis is how you discover what the subject actually is and keeps the semantics from growing an unbounded number of interacting features. Providing the familiar named constructs is how the thing gets used, and the basis is what licenses each of them. A designer who conflates these ends up in one of two failure modes: a minimal system nobody can write in, or a rich one whose features were never shown to be mutually consistent and whose interactions are discovered by its users.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-paper.md) — the introduction's survey of the many competing structuring and synchronization proposals with no recognized criterion for choosing between them, the long sequence of worked exercises reconstructing coroutines, subroutines, data representations, monitors, semaphores and iterative arrays from the same small basis (including the explicitly clumsy recursion simulation), and the conclusion's argument that a frequently useful, more-provable or more-efficiently-implementable construction still deserves its own notation, with derivability serving as the consistency guarantee.
