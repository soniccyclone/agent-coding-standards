---
type: lesson
title: "When a step needs a messy operation, find the weakest property that discharges it rather than unfolding the definition"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# When a step needs a messy operation, find the weakest property that discharges it rather than unfolding the definition

**Lesson:** Some primitives have definitions you would rather not read. Integer division is the classic: which way it rounds, what it does with negative operands, whether the answer is exact — all of it varies, all of it is documented in fine print, and expanding it inside an argument produces a case analysis that swamps the point you were making. The reflex to resist is unfolding the definition. Instead, isolate the single fact your step actually requires and ask whether some weak, obviously-true property of the operation implies it. For placing a probe strictly inside a nonempty range, the requirement is only that halving preserve order: if one number is no greater than another, its half is no greater than the other's half. That property holds under any sane rounding convention, and it discharges the obligation in three lines, with no reference to signs, exactness or rounding direction.

The economy here is not merely shorter proofs. An argument that rests on a weak, widely-shared property is portable in a way that an argument resting on a definition is not. The definition belongs to one implementation; the property belongs to a whole family of them, so the same reasoning survives a change of language, a change of hardware, or a change of the library's rounding rule, none of which you have to re-audit. That is worth deliberately hunting for whenever a step touches something platform-dependent — division, shifting, string comparison, timestamp granularity, floating-point rounding — because the alternative is an argument that quietly becomes false when someone moves the code.

The technique also hands you free validation of variants. Once your step is justified by order-preservation of halving alone, a completely different formula for the same probe — one that offsets from the low end rather than averaging the two ends, specifically to avoid overflowing on the sum — is justified by exactly the same argument, since it too is built from order-preserving pieces. You did not have to redo the analysis, and the improved version arrives already proved. That is the recurring payoff: identify the weakest sufficient property and you have not proved one program correct, you have characterized the set of programs that are correct, and you may then choose within that set on grounds like overflow behaviour or cost.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 2.2.10's justification of the binary-search midpoint, which explicitly declines to look at the exact definition of integer division on the grounds that the analysis would be complicated and negative operands would have to be considered, and instead derives the needed strict-betweenness from monotonicity of division by two alone; together with the following exercise in which the same monotonicity argument establishes the alternative midpoint formula that avoids unnecessary overflow.
