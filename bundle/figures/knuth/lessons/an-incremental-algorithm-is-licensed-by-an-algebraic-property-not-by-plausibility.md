---
type: lesson
title: "An incremental algorithm is licensed by an algebraic property of its domain, not by the plausibility of its steps"
figure: knuth
works: [fast-pattern-matching-in-strings]
axes: [verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# An incremental algorithm is licensed by an algebraic property of its domain, not by the plausibility of its steps

**Lesson:** One section of the paper knocks down a belief that a certain family of strings — those formed by concatenating even-length palindromes — could not be recognized quickly. The obvious approach is to consume the input left to right: find a palindrome at the front, chop it off, repeat. Nothing about that procedure is obviously sound, because the piece you chose to remove might have been the wrong piece, and a different decomposition might have succeeded where yours got stuck. Plausibility is not the issue; the procedure either commits you or it doesn't, and you cannot tell by looking at it.

What makes it sound is proved separately, and the proof is algebra rather than algorithmics. The authors show that an indecomposable member of this family cannot begin with another indecomposable member, from which decomposition into indecomposable factors turns out to be unique, and from *that* a cancellation property follows: strip a valid prefix off a valid whole and the remainder is still valid. That cancellation property is the entire license for consuming input greedily and never reconsidering. Once you have it, the recognition algorithm follows almost mechanically, and the authors then state the result at the level it belongs — as a theorem about any language whose starred closure cancels on the left and whose members can be detected at the front of a string cheaply. The string-matching machinery earlier in the paper supplies the cheap front-detection; the algebra supplies the permission to be greedy.

The discipline in the argument becomes visible in what comes immediately after. They exhibit a sibling family, defined by loosening the palindrome condition slightly, and point out that it contains two decompositions of overlapping strings that destroy uniqueness outright — so the entire approach evaporates, and whether that family can be recognized quickly is left as an open question. Same intuition, same greedy procedure, no theorem, no result. That juxtaposition is the lesson: the greedy step looked equally reasonable in both cases, and reasonableness carried no information at all about whether it worked.

For a programmer this generalizes to every algorithm that makes an irrevocable local decision — streaming parsers, incremental consumers of a protocol, log compaction, any single-pass transformation. The question to ask is not whether the local rule looks safe but what property of the domain guarantees that a locally correct choice cannot be globally wrong. Usually it is uniqueness of decomposition, or a cancellation law, or unambiguity of the grammar, and it is a property of the data's structure rather than of your code. If you cannot name it, you do not have a single-pass algorithm; you have a single-pass algorithm that happens to work on the inputs you tried, and the sibling case where the property fails is usually one small relaxation of the spec away.

**Source:** [Fast Pattern Matching in Strings](../works/fast-pattern-matching-in-strings.md) — the palindromes section, which establishes that indecomposable members cannot prefix one another, derives unique factorization and left cancellation from it, generalizes to any starred language with those properties, and then exhibits the closely related family where uniqueness fails and the technique does not apply.
