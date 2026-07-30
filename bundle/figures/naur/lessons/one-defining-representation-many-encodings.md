---
type: lesson
title: "Fix the defining form for human understanding, and let every machine encoding be a transliteration of it"
figure: naur
works: [revised-report-on-the-algorithmic-language-algol-60]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Fix the defining form for human understanding, and let every machine encoding be a transliteration of it

**Lesson:** A definition that must serve many incompatible machines faces a choice: write it in the intersection of what those machines accept, or write it in whatever form is clearest and require each machine to supply its own mapping. Take the second. Choose the symbols of the defining form by what makes agreement easiest among the people who must read it, explicitly not by any device's character repertoire, any existing coding convention, or any pre-existing mathematical style. Then declare that concrete encodings differ from the defining form only in the choice of symbols, and that structure and content are identical across all of them. That single sentence is what makes the whole arrangement work: it turns every implementation's local dialect into a lookup table rather than a variant of the thing itself.

The consequence is a division of labour that is easy to state and easy to police. The defining form is the reference for anyone building a translator and the arbiter of every dispute. Each concrete encoding carries the obligation to publish its own transliteration rules and is otherwise unconstrained. And a third form can exist for a purpose neither of the others serves — human communication in print and handwriting, where subscripting, raised exponents and typographic variety are worth having — provided it too maintains a one-to-one correspondence with the defining form. Notice what this buys: three audiences each get a notation suited to them, at the price of one mapping apiece, and no audience gets to degrade the definition to fit its constraints.

The failure this avoids is the common one where the most limited consumer silently becomes the specification. Once the defining document is written in the poorest available character set, every reader thereafter pays for a hardware limitation that may not even exist anymore, and the limitation becomes indistinguishable from a design decision. Keeping the definition in the clearest form and pushing degradation to the edges also makes the degradation visible and dated: a transliteration table is obviously a concession to a machine, and can be thrown away when the machine is.

**Source:** [Revised Report on the Algorithmic Language ALGOL 60](../works/revised-report-on-the-algorithmic-language-algol-60.md) — the introduction's treatment of reference, publication and hardware levels, including the stipulation that reference characters are settled by ease of mutual understanding rather than computer limitations, the requirement that each hardware representation carry its own transliteration rules, and section 1's insistence that representations differ only in choice of symbols.
