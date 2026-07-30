---
type: lesson
title: "Let people point at what they can see, and accept that some things should have no name"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Let people point at what they can see, and accept that some things should have no name

**Lesson:** Referring to a thing by recalling and typing its name asks two separate favours of a person: remember the identifier, and reproduce it exactly. Referring to it by pointing at it asks neither. That difference sounds like ergonomics and is actually about what the system can represent, because the naming approach quietly imposes a requirement — everything referenceable must have a name — and that requirement is not always satisfiable or even desirable. Some things genuinely have no good name, and for those, being visible and pointable is the *only* way a person can indicate them at all.

Taken seriously this inverts a habit. The instinct when building something referenceable is to assign it an identifier, because identifiers are what programs manipulate. The alternative is to make it visible and selectable, and to treat the absence of a name as an acceptable outcome rather than an omission to be fixed. What you gain is a whole class of mistakes that cannot occur: there is no misspelling a thing you selected, and no stale reference to a name that no longer resolves.

Pointing does not have to mean pointing at one thing, which is where this stops being merely about mice. The same principle covers describing a group by analogy or by a search that narrows the field, and then selecting from what comes back — the person's contribution is recognition rather than recall throughout, and recognition is the cheaper faculty. The generalizable test for any interface, graphical or textual: does this require the person to produce an identifier from memory, and if so, could the candidates be shown instead? Command completion, pickers and searchable listings are all the same move, and the underlying goal in every case is that the person should be able to see the thing they mean and indicate it directly — making the machinery disappear and feel like an extension of themselves rather than something to be addressed.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 7's user interface design rules, adapted from lectures by Bruce Horn and published there for the first time with his permission: the "See and Point vs. Remember and Type" rule, which notes that not everything will or should have a name, that seeing and pointing may be the only way to specify such things, and that groups can be described by analogy or search specification and then chosen from by pointing.
