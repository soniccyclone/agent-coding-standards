---
type: lesson
title: "Distinguish a cost you incurred by transcribing the definition from a cost the problem actually has"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Distinguish a cost you incurred by transcribing the definition from a cost the problem actually has

**Lesson:** Two expensive computations look alike and are not. One is a direct transcription of a mathematical definition into code: it recomputes enormous amounts of duplicated work, and there is a well-known reformulation that carries a few state variables and runs in linear time. The other — counting the ways to make change — is also a direct transcription, also generates a wastefully redundant tree, and here the authors say plainly that it is *not obvious* how to design a better algorithm, and leave it as a challenge.

Holding those two apart is the lesson, because the response differs completely. When slowness comes from naive transcription, the cure is a reformulation you can search for, and the search has a known shape: find the quantities that would let the process carry fixed state instead of deferring work. When slowness is a property of the problem as posed, no amount of restructuring will find the trick, and effort should go instead to mechanical mitigation — caching results so each distinct subproblem is computed once — or to changing the question.

The trap is that both cases present identically. You have working code, it is too slow, and the redundancy is visible in both. Assuming the first case means an open-ended hunt for a cleverness that may not exist; assuming the second means shipping an exponential algorithm that a known reformulation would have fixed. The honest first move is to try to state what the iterative version's state variables would have to be, and treat failure to state them as evidence — not proof — that you are in the second case.

There is a defence of the naive version worth keeping. Being little more than the definition rendered as code, it is straightforward, obviously correct by inspection against the specification, and therefore a good thing to have — as a reference to check the clever version against, and as the artifact you keep when the clever version does not exist.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 1 section 1.2.2 on tree recursion, which presents the naive Fibonacci procedure as a prototypical tree recursion that is a terrible way to compute Fibonacci numbers because of redundant computation, notes it is little more than a translation of the definition while formulating the iterative version required noticing the computation could be recast with three state variables, then gives counting change as a contrasting case where the tree-recursive process is similarly redundant but no better algorithm is obvious — with the footnote on tabulation as the mechanical way of avoiding recomputation.
