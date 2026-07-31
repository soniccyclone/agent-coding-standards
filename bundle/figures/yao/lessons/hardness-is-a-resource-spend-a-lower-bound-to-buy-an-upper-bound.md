---
type: lesson
title: "Hardness is a resource: a proof that something is impossible can be spent to buy a capability elsewhere"
figure: yao
works: [theory-and-applications-of-trapdoor-functions]
axes: [verifiability, expressiveness]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Hardness is a resource: a proof that something is impossible can be spent to buy a capability elsewhere

**Lesson:** A negative result is normally filed as a boundary — here is what cannot be done, stop trying. That reading wastes it. A proof that some task defeats every solver in a class is a strong structural fact about that class, and structural facts are convertible. Spend the fact in the right place and it purchases a positive capability, sometimes in a dimension that looks unrelated to the one where the difficulty was established. The clearest instance: if a transformation is genuinely beyond the reach of small solvers, its output is unpredictable to them, and unpredictability that no member of the class can penetrate is interchangeable with real unpredictability for any purpose a member of that class could serve. Difficulty, in other words, is a manufacturing input for randomness, and randomness is a thing algorithms pay for. So the assumption that a problem resists all cheap solvers ends up tightening the best deterministic simulation of computation that uses coin flips — a lower bound in one accounting bought an upper bound in another.

Two features of the exchange are worth internalizing. First, the trade crosses between different notions of computation: the hardness is asserted against a rigid, non-uniform kind of solver, one allowed to be custom-built per input size, while the capability delivered is about ordinary uniform procedures. That crossing is what makes the result surprising and also what makes it usable, since the hard-to-satisfy side of the trade is the side where hardness is most plausible. Second, the price is negotiable and worth negotiating: the same conversion goes through under materially weaker hypotheses if you choose the source of difficulty carefully, including hypotheses about worst-case rather than typical instances, and a version paying less for the same conclusion is strictly better because the conclusion inherits the weaker premise's plausibility.

The habit this recommends is to keep an inventory of the impossibilities your domain has established and periodically ask what each one could be spent on. Physical limits, information-theoretic barriers, and hardness results are all latent assets — a bound on what an adversary, a competitor's optimizer, or a downstream consumer can compute is exactly a permission to depend on something they cannot do. Practitioners who only read negative results as prohibitions leave that entire ledger unspent.

**Source:** [Theory and Applications of Trapdoor Functions](../works/theory-and-applications-of-trapdoor-functions.md) — the abstract-complexity-theory section of Part 2, which derives from the existence of a function no small circuit can invert a sharper deterministic simulation of randomized polynomial time than was previously known, remarks explicitly on this being a case where a lower bound on non-uniform complexity yields an upper bound on uniform complexity, and then obtains the same conclusion from a weaker premise about discrete logarithms that, unlike the rest of the paper, concerns worst-case rather than average-case difficulty.
