---
type: lesson
title: "An abstraction boundary is a claim that a whole class of implementations is interchangeable"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# An abstraction boundary is a claim that a whole class of implementations is interchangeable

**Lesson:** Once a procedure is used as a black box, the claim being made is stronger and more precise than "the caller does not need the details." The claim is that *any* implementation returning the right values is equally acceptable — so a squaring routine written as a multiplication and one written as an exponential of a doubled logarithm are the same object as far as every caller is concerned. The abstraction names an equivalence class, and membership is decided solely by the values produced.

Saying it that way rather than as a slogan about information hiding buys two things. It tells you what the boundary actually promises, which is substitutability across the entire class rather than merely privacy of the current member. And it tells you what will violate the boundary: anything a caller can observe that is not a returned value. Timing, allocation, ordering, and error behaviour are all outside the stated equivalence, so the moment a caller depends on one of them the class has silently collapsed to one member and the freedom you thought you had is gone.

The example carries a second point the authors make almost in passing and which deserves emphasis: it is not even clear which of the two squaring implementations is faster, because that depends on the machine — a processor with good logarithm tables could favour the one that looks absurd. So the equivalence class is not ordered by an intrinsic quality metric. Which member you should pick is a question about a deployment, not about the code, and it therefore cannot be settled at the point where the abstraction is defined.

Held as a habit, this changes how you write a boundary. Rather than asking what to hide, enumerate what a caller may rely on, and recognize that everything else is a degree of freedom you are claiming for the implementation. If that list is uncomfortably long you have not built an abstraction, you have built a description of one implementation.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 1 section 1.1.8 on procedural abstraction, which observes that one could not tell from a caller whether a helper was built into the interpreter or defined as a compound procedure, and gives two implementations of squaring — a multiplication and an exponential-of-doubled-logarithm — arguing that at this level of abstraction any procedure computing the square is equally good, with the footnote that which one is more efficient depends on the hardware available.
