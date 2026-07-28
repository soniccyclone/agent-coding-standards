---
type: lesson
title: "Reify the history to fit it through a narrow slot"
figure: peter
works: [uber-den-zusammenhang-der-verschiedenen-begriffe-der-rekursiven-funktion]
axes: [expressiveness, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Reify the history to fit it through a narrow slot

The apparent gap between "this step may look at everything computed so far" and "this step may look only at the previous result" is not a gap in power, because the previous result can be made to *be* everything computed so far. Péter's move is to carry, in the single slot the restrictive scheme allows, a composite value that packs the whole run of earlier values into one number via unique factorization, with a companion function that pulls any chosen earlier value back out. The restrictive scheme then advances that packed value one step at a time, and the function you actually wanted is recovered by one extraction at the end.

The general principle is that a channel's width is not a limit on the information that crosses it, only on how the information must be shaped. Whenever a mechanism offers you one place to keep state, you can trade richness of access for richness of representation: a fold whose accumulator is a log has the same reach as an interpreter with random access to its own past. What you pay is the cost of packing and unpacking, and the obligation to keep the encoding and decoding provably inverse.

For a working programmer this reframes a whole family of "the framework won't let me" complaints. A callback that receives only the last value, a reducer with one accumulator, a state machine with a single register, a protocol field that carries one token — each of these is as expressive as its unconstrained cousin the moment you decide what structured value lives in the slot. The design question stops being "is this interface powerful enough" and becomes "what is the right thing to keep in the one place I am given, and can I get it back out cleanly." That is a much more productive question, and it keeps the core mechanism small instead of growing a special access path for every case that seemed to need one.

**Source:** [Über den Zusammenhang der verschiedenen Begriffe der rekursiven Funktion](../works/uber-den-zusammenhang-der-verschiedenen-begriffe-der-rekursiven-funktion.md) — the section reducing course-of-values recursion, which introduces an auxiliary function whose values encode the entire preceding run and shows the encoded version satisfies an ordinary one-step recursion.
