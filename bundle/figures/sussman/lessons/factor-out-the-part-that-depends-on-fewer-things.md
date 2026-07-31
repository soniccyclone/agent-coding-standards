---
type: lesson
title: "Look for the part that depends on fewer things than the whole, and factor along that seam"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Look for the part that depends on fewer things than the whole, and factor along that seam

**Lesson:** Handling operations across types by writing each combination explicitly means the work grows with operations multiplied by type pairs. Coercion replaces that with one conversion per ordered pair of types, and the authors name exactly what makes the reduction legal: the appropriate transformation between two types depends only on the types, not on the operation being applied. That single sentence is the whole argument. It identifies a factor of the problem that varies over fewer dimensions than the problem does, and the saving is proportional to the dimension you eliminated, not a constant.

This is a move to look for deliberately, because it is easy to miss when the cases are enumerated in front of you. Given a matrix of situations, ask which of its axes each piece of the work actually depends on. Anything that turns out to depend on only some of them can be lifted out and written once per combination of those, then composed with the rest. Serialization that depends on the type but not the transport; authorization that depends on the role but not the endpoint; retry policy that depends on the failure class but not the caller — all the same shape. When work is being duplicated across a matrix, the duplicated part is usually the one that never needed the full index.

The authors are careful about the limits, which is what keeps the technique honest rather than universal. Coercion still costs on the order of the square of the number of types, which is better than before but is not free. A footnote observes that if the conversions compose, you can supply far fewer and let the system search the graph of relations to derive the rest — a second factoring, applied to the residue of the first. And the scheme still fails when neither of two values converts to the other but both convert to some third type, which is precisely the case pairwise thinking cannot see. Factoring buys you an exponent, not a solution; you get to keep asking what structure the remaining problem has.

The general discipline that comes out of this: before writing the n-by-m cases, spend the time to ask what each case is really a function of. If the answer is genuinely all of the inputs, write them out and stop feeling bad about it — the authors say explicitly that for unrelated operations on unrelated types, the cumbersome explicit version is the best anyone can do. The technique is not "always factor." It is "find out whether there is a factoring, and know which structural fact licenses it," because that fact is also what tells you when the factoring will break.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.5.2's subsection on coercion, which introduces conversion procedures installed in a coercion table indexed by pairs of type names, modifies apply-generic to try each direction of conversion when no direct method exists, states that only one procedure per pair of types is needed rather than one per collection of types and operation because the appropriate transformation depends only on the types and not on the operation, notes in a footnote that composable conversions let the system search the graph of type relations and derive conversions it was not given, and concedes the scheme fails when two values must both be converted to a third type.
