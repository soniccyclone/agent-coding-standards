---
type: lesson
title: "A structure is defined by its selectors, not by the set of values it can hold"
figure: wirth
works: [algorithms-and-data-structures]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# A structure is defined by its selectors, not by the set of values it can hold

**Lesson:** Compare two ways of composing data by the values they admit and they can come out identical — a fixed-length aggregate of similarly typed parts and a fixed-length aggregate of individually named parts describe the same product of value sets, and the count of possible values obeys the same multiplication rule. Mathematically there is nothing to choose between them. What actually distinguishes structuring methods is the operation each provides for reaching a component: one names components by a literal that must appear in the program text, another names them by a value computed at run time, a third permits no naming at all and only advances through them in order. The selector is the content of the structure. Everything a structure is good and bad at follows from what its selector can express.

Two consequences make this more than a definition. First, when choosing between structures, comparing their capacities is the wrong comparison and comparing their selectors is the right one — ask what questions each selector can answer and at what cost, because that is where the differences are. Second, the power of a selector is exactly proportional to its hazard. A selector that must be written literally can be checked completely before the program runs, and it can never designate something that does not exist. A selector that is a computed expression makes whole families of algorithms possible, and by the same token it can produce a designation of something outside the structure, which is why that is among the most common mistakes there is. You do not get one without the other; the checkability was a consequence of the restriction that also made the structure weak.

That symmetry is the design lever. If a structure is being misused in a way that keeps producing out-of-range designations, the fix is often not more careful arithmetic but a structure whose selector cannot express the mistake — and conversely, if a structure is too weak, the thing to relax is specifically its selector, accepting the class of errors that relaxation admits and arranging to detect them. State the detection arrangement explicitly rather than assuming it, since a computed selector without a range check is a construct whose failures are silent and arbitrary rather than local.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 1.2's account of structured types and the cardinality rule, with its statement that a general-purpose language must offer several structuring methods which in a mathematical sense are equivalent and differ in the operators available to select components; and section 1.4's treatment of the array, its identification as a random-access structure selected by an index, the observation that because indices are integers they may be computed so a general expression can stand in place of a constant, the immediately following note that this generality is both a most significant programming facility and the origin of one of the most frequently encountered programming mistakes when the computed value falls outside the declared index range, and the accompanying assumption that a decent system warns on such an access.
