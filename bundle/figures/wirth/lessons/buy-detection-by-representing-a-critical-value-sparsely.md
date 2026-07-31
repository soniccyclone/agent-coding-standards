---
type: lesson
title: "Buy detection by representing a critical value sparsely"
figure: wirth
works: [project-oberon]
axes: [verifiability, hardware-affinity, primitive-count]
subdomains: [operating-systems-and-systems-programming, foundations-of-computation]
tags: [lesson]
---
# Buy detection by representing a critical value sparsely

**Lesson:** Not all fields are equal under corruption. Damage a byte of payload and one item is wrong; damage a value that says *where* something lives and the system follows it into unrelated storage and may destroy far more than it lost. Since the consequences are so unequal, the protection should be unequal too, and the interesting observation is that detection for the dangerous fields can be nearly free. A value that is stored in its natural encoding uses every available bit pattern, so every corruption of it yields another legal value and nothing can tell. Store it instead in an encoding whose legal values are a sparse, easily-tested subset of the representable ones, and the same corruption almost certainly produces something outside the subset, which a single cheap test detects.

The construction is elementary and that is the point. Keep the value scaled by a fixed factor, and require that legal values be exact multiples of it; a change of any single bit shifts the value by a power of two, which cannot be absorbed by a factor that shares no divisor with two, so every single-bit corruption becomes visible. The cost is a multiply and a divide at the boundary and a modest reduction in range — nothing per access, nothing in the structure, no extra field. What is being bought is a property the hardware may or may not provide: the same detection implemented in software, so the system's integrity does not depend on which machine it is running on. That is a good general reason to build such a check even when the current hardware happens to have one, since a guarantee you implement yourself travels with the code.

Two placement rules make it work in practice. Put the encoding and decoding at the single pair of procedures through which every access to the resource passes, so there is one place to be right and no possibility of a caller handling a raw value; the whole scheme collapses if the sparse representation leaks into arithmetic done elsewhere. And apply it selectively — the point of the analysis is that a small number of fields carry disproportionate consequence, and spreading the same treatment over everything would trade the cheapness away for protection that ordinary error handling already provides. The general habit is to ask, of each field in a persistent structure, what happens if this one is wrong, and to spend representation slack only where that answer is bad.

**Source:** [Project Oberon](../works/project-oberon.md) — the third of the comments following the file module in section 7.3, which states that sector pointers, though of an ordinary integer type, are actually stored as the sector number multiplied by twenty-nine, so that any single-bit error produces a value that is not a multiple of twenty-nine and is therefore easily detected; the description of this as software parity checking of the crucial sector addresses, making them safe against single-bit errors even on machines without a hardware parity check; and the placement of the check in the kernel's sector reading and writing procedures.
