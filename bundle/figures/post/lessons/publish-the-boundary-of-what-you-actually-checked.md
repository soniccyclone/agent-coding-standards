---
type: lesson
title: "Publish the boundary of what you actually checked"
figure: post
works: [recursive-unsolvability-of-a-problem-of-thue]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Publish the boundary of what you actually checked

Before criticizing anything, Post states exactly how far his own scrutiny extends. He worked through one portion of Turing's development in full detail; for the theorems in the following section, only outlines were given and he did not reconstruct the formal details; therefore his own downstream remarks are also left at the intuitive level rather than presented as established. He goes further and lists the concrete defects the detailed pass turned up, including one substantive omission in the universal machine's instruction table without which a step of the construction does not work, alongside a run of smaller misprints. The result is a document where a reader can tell, claim by claim, which statements rest on line-by-line verification and which rest on judgment.

The discipline matters because unmarked confidence propagates and cannot be recovered. A result stated without qualification gets cited, built upon, and relied on; if part of it was actually a plausible sketch, nothing downstream records that, and the gap becomes invisible at exactly the moment when many things depend on it. Marking the boundary is cheap for the author and irreplaceable for everyone after. Post's other observation reinforces it: the defect he found was not in the hand-waved part but in the part presented as fully worked out, which is precisely where a reader has no reason to look. Detailed presentation is not evidence of a detailed check, and only the author knows the difference.

For engineering the translation is direct and mostly unpracticed. The claim "this is tested" is nearly useless; which behaviors are covered by tests, which by types, which by a careful read, and which by nobody is the information that matters. A migration verified against production-shaped data is a different artifact from one verified against fixtures, and the difference belongs in the pull request, not in someone's memory. A refactor where you traced every caller is different from one where you trusted the compiler, and that distinction determines what a reviewer should spend attention on. When you write "should be fine" without saying what you checked, you have transferred confidence without transferring its basis.

The habit that follows is to treat the scope of your verification as part of the deliverable rather than as private context. Say what you read closely and what you skimmed. Say which invariant you proved and which you assumed. Say where you stopped. Post's appendix is a working example of the form: attack a widely accepted result hard, and be equally explicit about the limits of the attack.

**Source:** [Recursive Unsolvability of a Problem of Thue](../works/recursive-unsolvability-of-a-problem-of-thue.md) — the opening of the appendix, which delimits which pages Post checked in full and declares his own consequent claims informal, together with the accompanying footnote of corrections to the universal machine's tables.
