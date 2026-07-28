---
type: lesson
title: "Which design looks natural is partly an artifact of the language you judged it in"
figure: post
works: [introduction-to-a-general-theory-of-elementary-propositions]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Which design looks natural is partly an artifact of the language you judged it in

Post builds a family of systems with an arbitrary number of truth values, shows the ordinary two-valued case is one member of it, and then does something most authors would skip. Having noticed that the two-valued system still *feels* like the privileged one, he does not accept the feeling as evidence. He points out that the entire development was carried out in two-valued language, and that for exactly that reason every other member of the family is bound to look distorted. The honest test he proposes is to redo the development in the vocabulary of some other member and see whether that one then looks like the harmonious choice. He does not run the experiment; identifying that it is the experiment is the contribution.

The engineering version of this bias is everywhere and rarely named. Whichever paradigm you are fluent in supplies the metrics by which you rate the alternatives: a codebase's structure looks obviously right in the language it was written in, an API looks clean from the client library you use most, a data model looks natural in the query language you learned first, and every competing option shows up carrying extra ceremony that is really just the cost of translation into your idiom. Arguments about which is "simpler" then become unwinnable, because both sides are measuring simplicity with a ruler manufactured by their own tooling. The tell is when a design's advocates and detractors agree on all the facts and still disagree about elegance.

Two things follow for practice. First, translation cost is not the same as complexity, and you have to separate them deliberately — the honest comparison is between each option expressed idiomatically in its own terms, not between your option and a transliteration of theirs. Second, when a claim of naturalness matters enough to act on, the only real check is Post's: rebuild a nontrivial piece of the system in the rival vocabulary and see what shrinks. This is expensive, which is precisely why unexamined naturalness claims survive so long. A programmer who has internalized this stops treating familiarity-shaped judgements as architecture, downgrades them to hypotheses, and reserves the word "simpler" for cases where he has actually paid to look from the other side.

Note also what the generalization itself bought Post. He had no application in mind for many-valued logic and says so, but constructing the family is what exposed the two-valued case as a *choice* — the parameter you introduce for no immediate reason is what reveals which of your previous decisions were decisions at all.

**Source:** [Introduction to a General Theory of Elementary Propositions](../works/introduction-to-a-general-theory-of-elementary-propositions.md) — the closing section on interpreting many-valued systems, where the apparent primacy of the two-valued system is diagnosed as an effect of the language the paper was written in.
