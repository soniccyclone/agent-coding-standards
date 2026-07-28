---
type: lesson
title: "Mark where the specification stops and the machine begins, and classify each divergence by what should happen to it"
figure: ritchie
works: [c-reference-manual]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# Mark where the specification stops and the machine begins, and classify each divergence by what should happen to it

Any specification written against real hardware contains three kinds of statement, and a document that fails to distinguish them is worse than useless because it invites confident wrong reasoning. There are the things the definition guarantees everywhere. There are the things this particular compiler on this particular machine happens to do, which a program may observe and must not rely on. And there are the things the definition deliberately refuses to pin down so that implementations can pick whatever their instruction set makes cheap. The C manual annotates all three inline, at the point where each one arises rather than in a disclaimer at the front: word widths and sign propagation are flagged as consequences of the target's addressing structure, arithmetic-versus-logical shifting is flagged as not surviving transport to another machine, multi-character character constants are flagged as inherently machine-dependent and to be avoided, and the order in which subexpressions are evaluated is declared open so the compiler may reorder for efficiency even in the presence of side effects.

That last category is the one people misread as sloppiness. Leaving evaluation order open is a transfer of latitude from the programmer to the implementer, made on purpose, because pinning it would tax every generated instruction sequence on every target forever to buy a guarantee that well-written code does not need. Silence in a specification is a resource, but only if it is deliberate and marked. Unmarked silence is indistinguishable from an oversight, and readers will fill it in with whatever their compiler did last Tuesday.

The sharper move is what the manual does with the divergences it cannot yet eliminate. Rather than hiding the fact that two implementations disagree, it enumerates them and tags each one with its intended disposition: this one is inherent to the two machines and will remain, this one is a defect in one implementation that should be fixed, this one is a defect that is hard to fix. That single tag converts a list of embarrassments into a work plan. An inherent difference is information for the portable programmer. A should-be-fixed difference is a ticket. A hard-to-fix difference is a warning that will outlive the current release, and readers deserve to know which they are looking at. The list is also visibly a group effort with named contributors, which is what makes it credible — nobody produces an honest catalog of their own system's inconsistencies from memory.

A programmer who thinks this way stops writing documentation that describes only the happy uniform case, and stops treating a known behavioral difference between environments as something to be quietly tolerated. Every place the abstraction leaks gets named where the leak is, and every known deviation gets a verdict attached: permanent, or a bug with an owner. The payoff is that consumers can compute what they are allowed to depend on, which is exactly the question portability turns on, and it cannot be answered by a document that presents guarantees and accidents in the same voice.

**Source:** [C Reference Manual](../works/c-reference-manual.md) — the inline implementation notes throughout the conversions and expressions chapters, the explicit refusal to fix evaluation order, and the closing appendix cataloguing implementation peculiarities with a per-entry disposition code.
