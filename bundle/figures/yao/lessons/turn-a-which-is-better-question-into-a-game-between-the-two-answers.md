---
type: lesson
title: "Turn a which-is-better question into a game between the two answers, and read off the equivalence"
figure: yao
works: [a-journey-through-computer-science]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Turn a which-is-better question into a game between the two answers, and read off the equivalence

**Lesson:** Two rival techniques for the same job invite a benchmarking exercise, and benchmarking is almost always the least informative thing you can do with the pair. The better move is to notice that each technique is a choice made by a player, and that the two players are choosing against each other: one picks how the procedure behaves, the other picks what the procedure is fed. Once the comparison is posed as a game with those two moves, the question stops being "which of these is stronger on the cases I happened to try" and becomes "what is the value of this game" — a single quantity that both techniques are pushing toward from opposite sides. The payoff is not a winner. It is the discovery that under the right formulation there is no winner, and that the two apparently unrelated design philosophies are two readings of one number.

An equivalence like that is worth far more than a verdict, because it converts a question you cannot attack into one you can. The hard direction is usually establishing that a self-modifying, unpredictable, adaptive procedure has a limit; nothing in its behavior stands still long enough to argue about. The easy direction is exhibiting one fixed adversarial input population and computing how badly a rigid procedure does on it, which is ordinary analysis. When the two sides are proved to meet, every bound you can prove on the tractable side is automatically a bound on the intractable side, and the intractable side never has to be analyzed at all. This is the general shape of leverage in a limits argument: find the dual view where the quantity you cannot compute is the same as one you can, then work entirely in the comfortable view.

Two working habits follow. First, when a new capability arrives and nobody can say what it cannot do, suspect that the missing ingredient is a dual formulation rather than more cleverness; the capability's limits are probably already visible in a mundane setting under a different name. Second, look outside your own field for the formalism, because the structure "two agents choosing against each other, meeting at a value" was solved elsewhere long before you needed it. Importing a mature result from an adjacent discipline is cheaper and far more reliable than deriving a bespoke argument, and it is what makes the whole reframing legitimate rather than merely suggestive.

**Source:** [A Journey Through Computer Science](../works/a-journey-through-computer-science.md) — the minmax-complexity section, where the question of whether randomized procedures beat distribution-tailored ones is recast as a contest between a procedure choosing stochastic moves and an adversary choosing the input distribution, with von Neumann's game-theoretic minmax principle supplying the coincidence of the two limits and thereby a handle on limits of randomization that had resisted direct analysis.
