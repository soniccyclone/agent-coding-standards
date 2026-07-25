---
type: lesson
title: "Ask first whether the problem has precedent, then either copy shamelessly or attack its irreducible core on day one"
figure: booch
works: [architecting-the-unknown]
axes: [primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Ask first whether the problem has precedent, then either copy shamelessly or attack its irreducible core on day one

**Lesson:** The first question about any system is not how to build it but whether anyone has. Problems with precedent and problems without call for opposite strategies, and applying either strategy to the wrong class is the most expensive mistake available. Where the shape of the solution is already established, imitation is the correct engineering choice, and the modern habit of assembling systems out of found solutions is not decadence but a rational response to the existence of settled answers. It has a boundary condition worth stating plainly: the assembled result is fit for things whose failure is cheap, and unfit for things whose failure is not, because the borrowed pieces carry no argument for why they are right.

Where there is no precedent, imitation has nothing to draw on and the ordering of work inverts. The temptation is to build the visible, tractable parts first, which produces demonstrable progress and postpones the question of whether the thing is possible. The discipline is to go straight at whatever is genuinely unsolved, on the grounds that every unprecedented problem has a core difficulty that will not decompose, and that the gravest errors are committed at the outset when the least is known. Reaching that core early means the eventual failure, which is likely, happens while it is still cheap, and the eventual success arrives as a foothold that constrains everything built afterwards. Finding it is itself a search for minimality: the small set of hard things from which the rest of the difficulty follows.

Two attitudes make this workable. First, an engineer's tolerance for results that work without being understood, since on unprecedented ground a mechanism that demonstrably functions is worth more than a theory that predicts it should. Second, abandoning perfection as the target: the achievable outcome is a system that is sufficient, and holding out for one that is not sufficient but ideal guarantees neither. A programmer who works this way spends the first week on the part everyone else is avoiding, deliberately courts early cheap failure there, and treats the resulting foothold rather than a specification as the thing subsequent design must respect.

**Source:** [Architecting the Unknown](../works/architecting-the-unknown.md) — the taxonomy separating systems already known how to build, systems whose construction process is known, and systems at the edge of imagination, together with the closing guidance to engineer unprecedented systems by taking the hardest problem first, failing early and cheaply, and settling for sufficiency.
