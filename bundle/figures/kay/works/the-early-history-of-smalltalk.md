---
type: work
title: "The Early History of Smalltalk"
figure: kay
description: Kay's own retrospective, written for ACM's second History of Programming Languages conference, tracing Smalltalk's lineage from Sketchpad and Simula through his FLEX machine thesis and into the successive PARC Smalltalk versions. It is the primary source for his claim that "objects" and "messages" were meant as a cell-biology metaphor for encapsulated, communicating computation rather than a data-typing convenience, along with his often-quoted regret about how "object-oriented" came to be understood. Extensively cited as the authoritative account of Smalltalk's design motivations.
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
year: 1993
url: https://worrydream.com/EarlyHistoryOfSmalltalk/
survey_text_layer: full
access: public
host: third-party-rehost
extraction: complete
tags: [work]
---

# The Early History of Smalltalk

**Venue/year:** ACM SIGPLAN Notices / HOPL-II (Second ACM SIGPLAN History of Programming Languages Conference), April 1993, pp. 69-95.
**Source:** https://worrydream.com/EarlyHistoryOfSmalltalk/ — live HTML transcription of the full paper (including references), rehosted on Bret Victor's worrydream.com. Verified 200 OK; full text confirmed present through the closing section and references.
**Reading copy:** full text is served as HTML, not PDF (~25,133 words). Fetch the URL and read the HTML directly; `pdftotext` on it returns nothing, which is what made earlier surveys record this as having no text layer.

**Coverage note (Phase 4, 2026-07-31):** the running body — introduction through the closing Coda, i.e. the paper's pp. 1-41 — was read in full and is the basis of every lesson below. Correcting the source line above: the transcription does *not* in fact carry the references section or Appendices I-V (the table of contents links to them but the page ends after the Coda's final paragraph). Those are the KiddiKomp memo, the Smalltalk-72 interpreter sketch, an acknowledgements document, an event-driven loop listing, and Smalltalk-76 internal structures — supporting material and code listings rather than argument. `extraction: complete` below attests exhaustion of the argument text available at this URL, not of the printed appendices.

## Lessons
- [Read the previous generation as almost a new thing, take an extreme position to force the new one out, and be willing to burn what already works](../lessons/read-the-previous-generation-as-almost-a-new-thing.md)
- [Never divide a system into kinds of thing weaker than the whole; make every part carry the whole system's power](../lessons/never-divide-a-system-into-things-weaker-than-itself.md)
- [Make the hardest thing you need your one primitive, and judge a small basis by its slope rather than its size](../lessons/build-from-the-hardest-thing-and-judge-a-basis-by-its-slope.md)
- [The exceptions to a system's central claim are where the next design lives, so invert the default instead of encoding around them](../lessons/the-exceptions-to-your-central-claim-are-the-design.md)
- [Replace changing a component's state with asking it to achieve something, and measure a construct by the intent it carries](../lessons/replace-assignment-with-goals.md)
- [Progress is the history of moving decisions later, and generality costs nothing if the common case runs full speed and only the exception traps](../lessons/progress-is-moving-decisions-later.md)
- [When capable people fail at a task you think is easy, count the non-obvious ideas it contains](../lessons/count-the-nonobvious-ideas-in-the-task.md)
