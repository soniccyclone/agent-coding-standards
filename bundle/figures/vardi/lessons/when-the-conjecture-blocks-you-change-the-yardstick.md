---
type: lesson
title: "When an unproven conjecture blocks the distinction you need, change the yardstick to one you can actually settle"
figure: vardi
works: [on-the-expressive-power-of-datalog]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# When an unproven conjecture blocks the distinction you need, change the yardstick to one you can actually settle

**Lesson:** A well-known classification split a family of graph problems into an easy class and a hard one, with a second split between general and restricted inputs. Both splits are only real if a famous open conjecture holds; absent that, the "hard" cases might be easy after all and the classification might be describing nothing. Kolaitis and Vardi establish that both splits are genuine without assuming the conjecture — by measuring on a different axis. Instead of asking which cases are expensive to compute, they ask which cases can be *stated* in a particular restricted language, and that question they can settle outright.

The move is to notice that the distinction you care about is usually not tied to the specific measure you first reached for. If separating two things by cost requires a theorem nobody has, look for another ordering on the same objects — expressibility in a restricted formalism, provability in a weak system, definability without some construct, sensitivity to a structural invariant — where a separation is within reach. A separation on a different axis is a weaker claim than the one you wanted, and it must not be quietly reported as the one you wanted, but it is a real, unconditional fact where the original was a conditional guess.

The honesty requirement is the interesting part, and this paper meets it explicitly. It states plainly that expressibility in the logic and computational cost are in general unrelated: the logic can state things that are not even computable, and cannot state things that are trivially cheap. So the new yardstick is genuinely a different yardstick, not a proxy, and the results obtained on it neither imply nor are implied by the cost results. Precisely because the two axes are independent, an unconditional separation on the second one is informative rather than derivative. The habit: when blocked, enumerate the other orderings your objects sit under, pick one where proof is possible, and be explicit about exactly what the substitution does and does not license.

**Source:** [On the Expressive Power of Datalog: Tools and a Case Study](../works/on-the-expressive-power-of-datalog.md) — the abstract and introduction, which note that the earlier complexity dichotomies for fixed subgraph homeomorphism are proper only under a complexity-theoretic assumption and announce that both are proper unconditionally in terms of expressibility; the remark following the containment theorem that there is in general no connection between expressibility in the logic and computational complexity, with examples in both directions; and the concluding section's suggestion that using expressibility in rule-language variants to prove separation results deserves further study.
