---
type: lesson
title: "Work backwards from the goal, present forwards from what is known, and leave the gaps visible"
figure: jones
works: [systematic-software-development-using-vdm]
axes: [cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Work backwards from the goal, present forwards from what is known, and leave the gaps visible

**Lesson:** Arguments are found in one direction and read best in the other. You find one by looking at what you must establish, asking which step could produce it, and turning that step's requirements into new goals until every remaining goal is something already known. You read one most easily in the opposite order, starting from the known and arriving at the conclusion, because that order lets you check each step as it arrives instead of holding an unexplained target in mind. Both facts are true simultaneously and the honest response is to do both: search backwards, record forwards. What must not happen is that the mismatch goes unremarked, because someone taught only the forward form has been shown the shape of finished work and not the method that produces it, and will conclude the work requires an insight they lack.

The mechanism that makes this workable is a notation for an unfinished step: a placeholder in the position where a justification will go, standing for "this follows, but I have not yet said why." With that in place a partial argument is a legitimate artifact rather than a draft. The open placeholders are exactly the remaining work, they can be attacked in any order, and none can be forgotten because the structure will not close while one remains. This is worth more than it sounds. The characteristic failure of informal reasoning is not an invalid step, it is a step nobody noticed was needed; a form that makes pending obligations visible converts that failure mode into a bookkeeping task.

Two practical details follow from having tried it. Numbering or otherwise fixing positions while working backwards is awkward, since steps get inserted above ones already written — leave gaps, and expect to. And the goal-directed rules are heuristics rather than an algorithm: as your stock of available moves grows, several will match any given goal and some lead nowhere. The method organizes the search and records its result; it does not replace the judgement about which move to try, and pretending otherwise is how people conclude that a disciplined approach has failed them when it has merely declined to think for them.

**Source:** [Systematic Software Development Using VDM](../works/systematic-software-development-using-vdm.md) — the concept-of-proof section, which names the distinction between the discovery and presentation of an argument, observes that a proof is often found by working back from the goal while presentation runs forwards for readability, and remarks that it is unfortunate if readers-turned-writers must discover one way and document another; the worked step-by-step discoveries in the propositional-calculus and correctness-proof sections, which use a question mark in the justification position to mark steps still to be proved and note both the line-numbering difficulty when working backwards and that open justifications clearly mark the remaining work; and the caution that using the rules as goal-decomposing tactics is not an algorithm, since many rules become applicable and some lead to blind alleys.
