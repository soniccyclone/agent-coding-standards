---
type: lesson
title: "Definability is not availability — judge a mechanism by what it costs to invoke"
figure: von-thun
works: [an-informal-tutorial-on-joy]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Definability is not availability — judge a mechanism by what it costs to invoke

The standard way to dismiss a language feature is to show it can be encoded in
your own language, and von Thun blocks that move with a concession rather than a
denial. He grants outright that his recursion-shape operators could be defined in
any of the mainstream functional languages, then says they would be less useful
there — because in those languages every argument to them must be built as a
lambda abstraction over named variables, and that ceremony is heavy enough that
nobody reaches for the operator when a plain recursive definition is at hand. The
mechanism is available in principle and unavailable in practice.

This holds because the cost of a construct is paid at every use, while the cost of
its definition is paid once. A facility whose invocation is three tokens gets used
casually, in the middle of an expression, for a one-off; the same facility whose
invocation requires introducing and naming two variables competes against just
writing the thing out longhand, and usually loses. Expressive power in the
theoretical sense — what set of computations you can describe — is therefore
almost uninformative about how programs in a language will actually look. What
determines that is the ratio between the effort of using an abstraction and the
effort of not using it, and that ratio is set by notation.

The corollary cuts both ways. It means an argument of the form "you don't need
that, here's how to encode it" is not a refutation of anything, since the encoding
may be exactly the friction that keeps the idea from being used. It also means
that improving notation is real work with real consequences, not cosmetics: making
an existing capability cheap enough to reach for changes which programs get
written, even though nothing new became possible.

A programmer who believes this evaluates a library or language by writing the
call site first, not the implementation. They count the ceremony a caller must
perform and treat any abstraction that loses to copy-paste on convenience as
effectively absent from the codebase, however well built. And when reviewing a
proposal to remove a construct because an equivalent exists, they ask what the
equivalent costs at each of its uses before agreeing the two are the same.

**Source:** [An Informal Tutorial on Joy](../works/an-informal-tutorial-on-joy.md) — the remark closing the recursive-combinators section, which concedes that these combinators are definable in other functional languages and locates their reduced usefulness there in the need to supply their arguments as variable-bearing abstractions rather than as quotations.
