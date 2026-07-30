---
type: lesson
title: "A lower bound on your method is not a lower bound on the problem; find what it solves incidentally"
figure: tarjan
works: [fibonacci-heaps-and-their-uses-in-improved-network-optimization-algorithms]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# A lower bound on your method is not a lower bound on the problem; find what it solves incidentally

**Lesson:** Having improved the classic shortest-path algorithm to a bound they can prove that *algorithm* cannot beat, Fredman and Tarjan are careful about what that proves. The floor holds because the algorithm, as a side effect of how it works, produces the distances in increasing order — which means it sorts, which means it inherits sorting's cost. But nothing in the problem statement asked for sorted output. So the bound is a fact about the method, not about the question, and the authors say plainly that it does not rule out a faster algorithm. That distinction is the entire content of the lesson, and it is routinely missed. A proof that your approach cannot do better than X is evidence about your approach. Treating it as evidence that the problem requires X is how a field stops looking.

The diagnostic that comes out of it is genuinely useful in ordinary engineering. When you have a cost you believe is irreducible, ask what your method computes that nobody asked for. Sorted output when only a set was wanted; a total order when a partial one suffices; exact values when a comparison was all that mattered; a full result when the caller only inspects part of it. Each of those is a harder problem than the one posed, and solving it drags in that harder problem's floor. The way past the floor is not to optimize your method but to construct one that stops short of the extra work — which is a search for a *weaker* intermediate result, an unnatural direction to look because more information usually feels safer.

The paper also models the right way to hold a suspicion that a known bound is not final. It notes that *verifying* a candidate answer to the spanning-tree problem is known to be cheaper than the best known method for *constructing* one, and treats that gap as suggestive rather than conclusive — a hint that construction is not yet understood, not a proof that it can be made cheaper. Gaps between checking and finding, between deciding and producing, between approximating and computing exactly are the places where the current bound is most likely an artifact of the available techniques. Cataloguing those gaps is how you keep a list of problems worth returning to, and the honesty to say a candidate improvement exists but has not been verified — which the same section does about its own unproven conjecture — is what keeps that list from filling up with wishes.

**Source:** [Fibonacci Heaps and Their Uses in Improved Network Optimization Algorithms](../works/fibonacci-heaps-and-their-uses-in-improved-network-optimization-algorithms.md) — the closing open-problems section, which derives the shortest-path algorithm's lower bound from the fact that it can be used to sort under a comparison model, immediately notes this does not preclude a faster algorithm, cites the cheaper cost of verifying a minimum spanning tree as a reason to doubt the construction bound is final, and states an unverified conjecture about a version of the structure needing neither ranks nor cascading cuts.
