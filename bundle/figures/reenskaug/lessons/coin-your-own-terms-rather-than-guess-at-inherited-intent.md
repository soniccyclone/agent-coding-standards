---
type: lesson
title: "When the vocabulary you inherited is ambiguous, coin your own rather than guess at the original intent"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# When the vocabulary you inherited is ambiguous, coin your own rather than guess at the original intent

**Lesson:** Before building on someone else's class library, a team read its source specifically to inventory the words it used for one concept — the region a display element occupies. They found five names that all appeared to mean the same thing, and worse, one name that meant two different things depending on which method you were reading: sometimes the space a component wants, sometimes the space it was given. That second finding is the serious one. Synonyms in a foundation you are building on cost you confusion. A homonym in a foundation costs you a class of bugs that type checking cannot catch, because both meanings are the same type and the substitution is silent.

Two moves follow, and the second is the one people resist. The first is to treat a vocabulary audit as a distinct step of adopting any base, done by reading the implementation rather than the documentation, and done before design rather than during debugging — the words are the interface you will think in, and confusion in them propagates into everything layered above. The second is to accept that you may not be able to recover what the original authors meant, say so plainly, and define your own terms anyway with precise statements of what each denotes. That feels like arrogance and reads like a failure to do the homework; it is neither. Fidelity to an ambiguous predecessor is unachievable by definition, since there is no single meaning to be faithful to, and attempting it yields a system whose terms are ambiguous for reasons nobody can explain. Consistency within your own layer is achievable and checkable, so it is the property to optimize.

The reason this is not merely license to rename things is the condition attached: the coining is justified by a demonstrated defect in the inherited vocabulary — a specific homonym exhibited in specific code — and it comes with explicit definitions and stated rules for use, not just new spellings. Renaming without that is churn. Renaming with it converts an unknowable question (what did they intend?) into a decidable one (does our layer use our words consistently?), and only the second kind of question can be enforced in review.

The general habit is to notice when you are about to spend effort reverse-engineering intent that may never have existed in a single form, and to redirect that effort into definitions you control. Being explicit that you did not fully understand the predecessor is part of the deliverable, because the next reader needs to know which terms are yours and which are inherited.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9 section 9.6, which reports studying the release 4.0 code to determine its vocabulary for window rectangles, finding five apparent synonyms plus methods that merge bounds, compositionBounds and preferredBounds so that bounds becomes a homonym, and then defining virtualBounds, actualBounds and dataBounds while stating outright that the team quite likely did not fully understand the ideas behind the existing visual component hierarchy but needed words it could use consistently.
