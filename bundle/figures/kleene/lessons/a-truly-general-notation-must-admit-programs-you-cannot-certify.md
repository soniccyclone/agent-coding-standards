---
type: lesson
title: "A notation general enough to express all computation must admit texts you cannot certify are meaningful — that is a proof of adequacy, not a defect"
figure: kleene
works: [general-recursive-functions-of-natural-numbers]
axes: [verifiability, expressiveness]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# A notation general enough to express all computation must admit texts you cannot certify are meaningful — that is a proof of adequacy, not a defect

**Lesson:** A definitional scheme for computable functions has an uncomfortable property: given a candidate set of defining equations, there is no mechanical way to tell whether it actually pins down a value for every input. The instinct is to treat this as sloppiness in the design and to look for a stricter scheme where well-formedness is checkable. That instinct is exactly backwards, and the argument is short. Suppose you could mechanically filter the well-behaved definitions. Then you could list them, run the diagonal construction across that list, and produce a function that computes but is outside your class — so your class was never the full class of computable functions in the first place. Undecidable well-formedness is therefore a necessary symptom of having captured everything. Any scheme lacking that symptom is provably incomplete.

The situation is worse than mere undecidability, and the difference matters for how you think about tooling. The valid definitions cannot even be effectively listed: no generator, however clever, enumerates all and only the definitions that denote total functions. So "just be conservative and enumerate the safe ones" is not a fallback — it is impossible in principle, not merely expensive. Meanwhile the diagonal trick that seems so threatening turns out to be harmless whenever you *can* list the family you are diagonalizing over: adding one to the diagonal of an effectively enumerated family of computable functions yields another computable function, safely inside the class. Diagonalization only escapes a class when the class's own membership resists enumeration. Understanding which side of that line you are on tells you whether a self-referential construction is a threat or a triviality.

For someone building or choosing languages, this converts a vague trade-off into a forced choice with a known price. You can have a notation where every text is certified meaningful, and then you are missing computable functions. Or you can have universality, and then your notation necessarily accepts texts whose meaningfulness is not merely hard to check but beyond any checker, and beyond any generator of the safe subset. There is no third option and no amount of engineering closes the gap. What follows practically is to stop treating "the compiler should reject the ones that don't terminate" as an ambition and start treating termination discipline as something the programmer supplies as extra structure — a bound, a decreasing measure, a restricted sublanguage — because it cannot be recovered from the general text.

**Source:** [General Recursive Functions of Natural Numbers](../works/general-recursive-functions-of-natural-numbers.md) — §2, which opens by arguing that the absence of any constructive test for when a definition succeeds is required for the definition to be adequate, then proves the defining indices are neither recursive nor recursively enumerable, and separately shows the diagonal construction over an effectively enumerated family stays inside the class.
