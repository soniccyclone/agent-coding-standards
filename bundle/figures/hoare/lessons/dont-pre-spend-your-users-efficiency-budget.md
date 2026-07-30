---
type: lesson
title: "Don't pre-spend your users' efficiency budget, and make any optimization visible in their own terms"
figure: hoare
works: [hints-on-programming-language-design]
axes: [hardware-affinity, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Don't pre-spend your users' efficiency budget, and make any optimization visible in their own terms

**Lesson:** Every abstraction has some slack to spend, and the argument that hardware improvement makes that slack free is only honest at small multiples. A designer trading ten or twenty percent for a real gain in clarity or safety is making a defensible engineering decision; a designer taking a factor of two or ten, in both time and space, has taken something that was not theirs to take. The allocation question is the substance of the point: whoever is closest to the problem should be the one who decides to spend performance on clarity, because they alone can see which parts of their program deserve the spending. A tool builder who consumes the budget in advance leaves users doing the opposite of good work — obscuring their own structure and writing worse code in order to recover headroom that was taken from them before they arrived.

The standard escape from this obligation is to promise that a sufficiently clever optimizer will recover the loss later. Treat that promise skeptically, and not only because such optimizers are large, slow, and late. An optimizer that rewrites programs invisibly introduces three worse problems: no guarantee that the transformed program computes what the untransformed one did; a cliff effect where a small edit silently disables the optimization and the performance drops unpredictably; and, most corrosive, the removal of the practitioner's own sense of responsibility for and control over the quality of what they produce. When performance is somebody else's magic, nobody owns it.

The constructive form is a three-part discipline that composes better than heroic optimization. Design so that a plain, unclever translation already produces something comparable to what a competent, deliberately unclever hand implementation would produce — not brilliant, just not wasteful. Make the notation expressive enough that the improvements users care about can be *expressed*, so they do not have to hope the tool finds them. And where automatic improvement is genuinely wanted, prefer a transformation whose output is presented in the same language the user wrote, because then the user can read the result, verify the trade, and keep ownership of it. An optimization you can inspect in your own vocabulary is a different kind of object from one that happens invisibly.

**Source:** [Hints on Programming Language Design](../works/hints-on-programming-language-design.md) — the Efficient Object Code discussion, including its accounting of who is entitled to introduce inefficiency, its four objections to relying on optimizing compilers, and its proposal for non-pessimizing translation with source-to-source improvement.
