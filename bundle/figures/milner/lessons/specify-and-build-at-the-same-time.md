---
type: lesson
title: "Specify and build at the same time; they catch different defects"
figure: milner
works: [the-definition-of-standard-ml]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Specify and build at the same time; they catch different defects

**Lesson:** The conventional ordering is design, then specify, then implement, with each stage validating the one before. The development recorded here refuses that ordering for the hardest part of the language, and the participants' retrospective judgment is blunt: having done design, formal definition, and implementation as one interleaved activity, they could not imagine how the three could have been done properly apart. The module system began as a design proposal and was then subjected in parallel to a draft formal account, a prototype implementation of the checking, a separate implementation of the execution, an independent semantics written in a different style, and a thesis proving properties of a stripped-down version. Each of those found things the others did not.

The reason they find different things is that they fail differently. A prototype reveals what is awkward to use and what is impossible to implement efficiently, but happily accepts an under-determined design — it just picks one behavior. A formal account cannot pick; every case must be decided, so it surfaces the questions the prose left open, and the record names specific examples of both kinds: a capability the design simply lacked, and a question about whether an interface constrains a module beyond what it states, which nobody had noticed was ambiguous. A proof effort finds the cases where the intended property is false. A second, independently-styled semantics finds where the first one's choices were artifacts of its own machinery. None of these detectors subsumes another, and running them in sequence means the early ones report against a design the later ones will change.

Two further details are worth noting. Implementation experience fed back into the formalism rather than merely conforming to it — a unification technique developed to make the prototype's checking work was subsequently adopted into the official static semantics. And when the design reached a genuine fork, the decision was made at a meeting by people who had all three kinds of evidence in hand, on a question that only the formal account had been able to pose sharply. The claimed result is high confidence in both the language and its definition, which is the only outcome that justifies the expense.

The practical version for ordinary systems: write the specification and the working code in the same week, on the same design, and treat every disagreement between them as information about the design rather than as a defect in whichever one you trust less. A specification that lags the implementation documents history; one that runs ahead of it documents wishes. Only a specification being written concurrently is an instrument.

**Source:** [The Definition of Standard ML (Revised)](../works/the-definition-of-standard-ml.md) — the preface's remark on the closeness of design, definition and implementation, and the development appendix's sections on modules and on semantics, which record the successive scrutiny of the module design by prototype, draft static semantics, denotational semantics and thesis, and the resulting design changes.
