---
type: lesson
title: "Relative size in source text is read as a statement of purpose, so the notation ends up rewriting your design decisions"
figure: knuth
works: [literate-programming]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Relative size in source text is read as a statement of purpose, so the notation ends up rewriting your design decisions

**Lesson:** The most surprising claim in this paper is one Knuth says surprised him too: he expected to have built a documentation tool and found that the programs themselves came out better. His explanation is a small, entirely convincing mechanism. Consider a routine whose job is to update some structure, which must first check that its input is sane. The update is two lines. Thorough recovery from bad input might be twenty. Written conventionally, the routine now looks like an error-message printer with an update tacked on the end — its proportions announce a purpose that is not its purpose. The programmer feels this, and shortens the recovery. Not as a decision, as a reflex; the writer is optimizing for how the text will read, and the text reads size as significance.

So the notation has caused a real engineering outcome. The rare path is under-built, systematically, across an entire industry's codebases, for a reason that has nothing to do with anyone's judgment about how important error recovery is. Give the recovery its own named place and reduce it to a single mention at the call site, and its whole visible purpose becomes doing recovery well, so it gets done well. The improvement did not come from more effort or better intentions. It came from removing a signal the writer was involuntarily servicing.

The general principle is that reading is inference from every available cue, proportion and adjacency included, and writers anticipate inference. Any cue a notation makes unavoidable therefore becomes a constraint on content, not merely on style. This is why "it's just formatting" is usually false. It also generalizes past code size: a function's position in a file, whether something is a top-level entity or a nested helper, whether a concern gets its own module — each is read as a claim about importance, and each will pull the thing being described toward matching that claim.

The practical move is a specific audit, and it is uncomfortable because it asks about motives you did not observe yourself having. Go through the short parts of a system and separate the ones that are short because the work is small from the ones that are short because a fuller treatment would have looked out of proportion. The second set is where the expensive, rarely-exercised failures live: partial recovery, unhandled cases, retries that give up early. Where the notation can be bent, bend it and let each part be the size it deserves. Where it cannot, the compensation is deliberate rather than automatic — move the disproportionate concern somewhere it is allowed to be large, and accept that the call site will now understate it.

**Source:** [Literate Programming](../works/literate-programming.md) — the passage in the section on programs as webs that works through a validate-then-update routine to explain why programs written in the system came out better rather than merely better documented.
