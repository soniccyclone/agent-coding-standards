---
type: lesson
title: "Building the formal model is how you find the design questions you never realized you had left open"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# Building the formal model is how you find the design questions you never realized you had left open

**Lesson:** The usual argument for giving a design a precise mathematical meaning is about what happens afterwards: implementations can be checked against it, two implementations can be shown to be of the same thing, and users get a stable account of behaviour they can reason from rather than a manual they must trust. All true, and worth the effort on those grounds alone. But there is an earlier payoff that gets overlooked, and it arrives before anything has been proved. Writing the model forces you to answer questions the informal design never made you notice were questions.

They are recognizable when you see them and invisible before. May a compositional construct be nested inside another instance of itself? May something defined by self-reference invoke itself in the concurrent form rather than the sequential one? May the thing you are allowed to wait for include an outgoing action, or only incoming ones? A design given as syntax plus prose neither permits nor forbids these; it simply has nothing to say, and the gap survives review indefinitely because nobody asks a question that the notation does not raise. A model has no such option. Every construct must be given a meaning as an element of some space, and the moment you write the clause you discover whether the clause makes sense in the general case or only in the cases you had pictured.

Two further observations make this worth planning for rather than merely appreciating. First, the answers a good model gives tend to be more permissive than the ones the designers would have guessed, because uniformity is what makes the definition compact — you are looking for the meaning of the construct rather than of the situations you had in mind for it, and the general definition typically covers arrangements you would have prohibited out of caution. A whole class of restrictions turn out to have been protecting nothing but the designers' unwillingness to think about a case. Second, this reverses the common ordering in which formalization is scheduled after the design is settled, as a documentation task. If the model is where the open questions surface, then postponing it postpones the design, and every month it is deferred is a month of implementation and user code built on top of decisions that have not actually been made. The model is not a transcript of a finished design; it is the instrument that finishes it.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the opening of the discussion chapter's section on mathematical models, which sets out semantics as the precise interface between users and implementors and as the only reliable ground for claiming two implementations are of the same language, then records that the early CSP design had no mathematical semantics and consequently left open several important design questions — whether one parallel command may be nested inside another, whether a recursive procedure may call itself in parallel, and whether output commands may appear in guards — all of which the book's model answers affirmatively.
