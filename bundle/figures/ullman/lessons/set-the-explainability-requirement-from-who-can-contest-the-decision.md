---
type: lesson
title: "Set the explainability requirement from who bears the decision and can contest it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Set the explainability requirement from who bears the decision and can contest it

**Lesson:** Two automated decisions with identical technical shape have completely different explanation requirements, and the difference has nothing to do with accuracy. A mail system files a message as junk; the only available account of why is that it resembles other messages people marked as junk, and that is genuinely fine — the recipient's exposure is trivial, the error is visible and reversible in one click, and nobody needs to audit the reasoning. An insurer raises a premium after re-scoring a driver's risk; now the person affected has money at stake, no view of the inputs, and a legitimate demand to know what changed and why. Same machinery, incomparable obligations.

The determining variable is the affected party's position, not the model's quality. Ask who bears the cost of a decision, whether they can see that a decision was made at all, whether they can cheaply undo it, and whether they have standing to challenge it. Where those answers are "the user, yes, trivially, and no need," an opaque model is a legitimate engineering choice. Where they are "someone else, no, not at all, and yes," an explanation is part of the deliverable and not a nice-to-have.

What makes this a design-time question rather than a documentation question is that some model classes cannot answer it afterwards. A structure built from many layers of small elements, each deciding from the previous layer's outputs, may admit no coherent account of what it is doing — not because nobody has written the account up, but because the computation does not decompose into reasons a human can follow. So the choice of model class silently commits you to an explainability ceiling, and it is made early, before anyone has framed the accountability question. That is the wrong order. The requirement has to be fixed first, because it eliminates candidate approaches, and discovering afterwards that your accurate model cannot justify itself to the person it charges is not a problem you can patch.

The generalizable habit is to treat "must this be explainable?" as a question about power and recourse rather than about engineering taste, answer it before selecting a technique, and be suspicious of the reasoning that accuracy substitutes for explanation. It does for the mail filter, because the affected party does not care. It does not once someone can be harmed by a decision they cannot see, cannot reverse, and cannot argue with.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 1's discussion of machine learning, which contrasts a mail provider's spam classification (where "it looks like other messages people identified as spam" is a satisfactory explanation because the user only cares that the decision is right) against an automobile insurer scoring driver risk (where a raised premium invites a demand to know what the model changed and why), and notes that in many methods, especially deep learning where a model is layer upon layer of small elements each deciding from the previous layer's inputs, a coherent explanation may not be possible at all.
