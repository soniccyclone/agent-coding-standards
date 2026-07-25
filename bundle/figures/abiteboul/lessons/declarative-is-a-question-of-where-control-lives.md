---
type: lesson
title: "Declarative and procedural is not a dichotomy; ask instead where the control lives"
figure: abiteboul
works: [datalog-extensions-for-database-queries-and-updates]
axes: [cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# Declarative and procedural is not a dichotomy; ask instead where the control lives

**Lesson:** The usual framing sets declarative languages against procedural ones as opposites and asks which side a given language falls on. This work replaces that with a better question. It argues that meaning defined purely by which structures satisfy a set of sentences hits a ceiling: past a certain point, extending a rule language while keeping a purely satisfaction-based account of meaning produces accounts so elaborate and contrived that they stop being worth having. The way through is to admit a procedural element into the definition of meaning itself, specifying the intended answer as the outcome of iterating an operator to a stable point. The languages built this way still deserve to be called declarative, and the reason given is precise: the programmer writes no explicit control. The procedurality is real but it belongs to the semantics rather than to the program text.

That is a much more useful axis than the binary. It says the property a programmer cares about is whether sequencing, branching, and iteration are things they must write and maintain, or things the evaluator supplies uniformly. A language can have a thoroughly operational definition and still relieve its users of writing control. The work also shows the ceiling on how much you get for free: with only implicit control from fixpoint iteration, sequencing one computation after another is achievable but requires encoding, and the encodings needed to hold a phase back until a data-dependent number of stages have elapsed are involved, essentially reconstructing a clock out of the rules themselves. The prior art it positions itself against, giving meaning to negation by layering rules into strata, is read the same way: that convention is already a departure from satisfaction-based meaning, since it effectively prescribes an evaluation order.

Someone who thinks this way stops asking whether a tool is declarative and starts asking two concrete questions. How much control does the evaluator supply on its own, and what is the shape of the encoding when the control I need exceeds that? If the answer to the second is that users end up building sequencing out of marker facts, generation counters, and completion flags, the language is not saving them work; it has only moved the control into a less legible place. That diagnosis is what motivates offering explicit sequencing as a first-class construct alongside the rules, so that the program says what it does.

**Source:** [Datalog Extensions for Database Queries and Updates](../works/datalog-extensions-for-database-queries-and-updates.md) — the introduction's argument that purely satisfaction-based meaning limits expressive power and that fixpoint-based meaning overcomes it while remaining declarative for want of explicit control, together with the later discussion of simulating composition and iteration and the closing list of recurring encoding techniques, which is in effect an inventory of what hand-built control looks like inside such a language.
