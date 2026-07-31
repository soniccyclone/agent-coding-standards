---
type: lesson
title: "Put the assumption you cannot justify in one named place, introduced only where it is needed"
figure: kolmogorov
works: [grundbegriffe-der-wahrscheinlichkeitsrechnung]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Put the assumption you cannot justify in one named place, introduced only where it is needed

**Lesson:** Every formal system that touches reality contains at least one assumption its author cannot defend. Kolmogorov's is continuity, and what is instructive is how he handles it rather than that he needs it. His other axioms each get an empirical derivation. This one gets an admission: for finite systems it is a consequence of the others and therefore adds nothing where observation actually lives; for infinite systems it is genuinely independent and its empirical meaning is next to impossible to explain, because describing any observable random process only ever yields a finite field. Infinite fields are idealized models, not observations, and he says plainly that restricting attention to models satisfying the axiom is an arbitrary limitation adopted because it has proved expedient across very different lines of research.

Three structural moves there are worth copying exactly. Deferral: the axiom does not appear until the chapter that needs it, so the elementary theory stands complete without it and nothing confined to the finite case pays for it. Naming: it is a numbered axiom in its own section, not a convenience slipped into a definition or leaned on inside a proof, so every result that uses it can be traced. And separate vocabulary for the two regimes — systems obeying the extra axiom get one name, systems obeying only the rest get another — so a reader always knows which world a statement inhabits. Together these make the unjustifiable assumption *auditable*, which is the only property you can actually get for it, since by construction you cannot get evidence.

The transferable rule is that assumptions of this kind are not defects and should not be argued about; they should be concentrated. Real systems are full of them: clocks advance monotonically, a message eventually arrives, the working set fits in memory, no identifier will exceed the range a double can represent exactly. None can be established from inside the system, and all of them are load-bearing. What makes them dangerous is diffusion — the same undefendable premise asserted implicitly in forty places, with no way to enumerate what depends on it and no way to predict what breaks when it fails. Give it one home: a named predicate, a documented precondition, a single invariant asserted at the layer that first requires it, and state the honest reason, which is usually that it is expedient and the alternative is unusable. Then "what if this is false?" becomes a question you can answer by looking at one call graph instead of an open-ended search.

**Source:** [Grundbegriffe der Wahrscheinlichkeitsrechnung](../works/grundbegriffe-der-wahrscheinlichkeitsrechnung.md) — Chapter II, §1, where the axiom of continuity is introduced only at the point infinite fields are taken up, shown to follow from the earlier axioms in the finite case, admitted to be independent and empirically inelucidable in the infinite case, and adopted as an arbitrary restriction to idealized models on grounds of expedience, with fields lacking it renamed generalized fields of probability.
