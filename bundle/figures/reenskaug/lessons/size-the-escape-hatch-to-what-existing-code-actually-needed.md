---
type: lesson
title: "Size a general escape hatch to what existing code actually needed, and admit when you cannot justify it"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, primitive-count]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Size a general escape hatch to what existing code actually needed, and admit when you cannot justify it

**Lesson:** Designing the payload of a change notification, this team considered the obvious flexible answer: include one general-purpose parameter whose meaning each programmer decides. They rejected it explicitly on the grounds that it reproduces the difficulty they had set out to remove — an open-meaning field means every sender and receiver must negotiate a private convention, which is the original problem wearing a wrapper. So the flexible option was not merely unnecessary, it was a regression, and this is the usual fate of the general parameter: it does not remove a coupling, it moves the coupling out of the type system and into folklore.

Having refused the general slot they still needed *something*, and the method for sizing it is the transferable part. They went back through their existing working implementations and asked what special information those had actually required. The answer came back as exactly one thing — the affected geometric regions — so exactly one typed parameter was added. This is the empirical route to a small interface, and it is stronger than either of the alternatives people usually take. Guessing at future needs produces the general slot. Refusing all extension produces reimplementation in every caller. Surveying what current code demanded produces a specific, named, checkable field, and the survey is cheap because the evidence already exists in the codebase you are replacing. When later needs appear, they arrive as concrete cases that can be sized the same way.

The passage closes with something rarer than either design move: the authors say they cannot decide whether the region parameter reflects something fundamental about change notification or whether it is just a hack, and include it anyway. That admission is a design artifact worth imitating, not a lapse. It marks the feature as the place to look first when the design is next revisited, it tells the reader not to build theory on top of it, and it does so without stalling delivery on a question that evidence cannot currently settle. The alternatives are both worse — inventing a principled-sounding rationale, which converts an open question into a false certainty that outlives everyone who knew better, or withholding a feature the code demonstrably needs until the theory arrives.

Held together, the two halves make a usable rule. Justify an extension point by past demand rather than by imagined future demand, keep it as narrow as that evidence supports, and label the parts whose principle you cannot state.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9 section 9.6's reasoning about parameters to the changed-update messages, which rejects a general programmer-defined parameter as bringing back the original difficulties, notes that reverse engineering of the existing solutions showed only one special parameter was needed (the areas affected by an attribute change), and states outright that they cannot quite decide whether this is a profound truth about changed-update or just a hack but include it anyhow.
