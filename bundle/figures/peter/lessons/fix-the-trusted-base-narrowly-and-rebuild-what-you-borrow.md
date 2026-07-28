---
type: lesson
title: "Fix the trusted base narrowly, then rebuild everything you borrow"
figure: peter
works: [uber-den-zusammenhang-der-verschiedenen-begriffe-der-rekursiven-funktion]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Fix the trusted base narrowly, then rebuild everything you borrow

Before proving anything, Péter states what she is standing on and refuses
everything else. Two starting functions, zero and successor. Only schemes that
mention numeric variables and that hand back an actually executable procedure
for computing a value from given arguments. Higher-order function types, which
another author's program required, are ruled out at the start rather than
avoided in passing. No prior results from mathematical logic are assumed. And
where she needs an auxiliary function that others had already shown to be
definable, she does not cite it — she redefines it, one by one, integer
division, remainder, primality, the nth prime, exponents in a factorization,
each rebuilt inside her own vocabulary before it is used.

That looks like scholarly punctilio and is actually a structural decision. The
value of a reduction theorem is exactly the size of what it reduces *to*, so
every borrowed convenience silently enlarges the claim and weakens it. By
rebuilding each helper from the two starting functions, she keeps the answer to
"what does this ultimately depend on?" small enough to state in a sentence, and
the reduction becomes a real statement about a small base rather than a relative
statement about an unaudited one. The admission criterion does similar work: a
scheme qualifies only if it comes with a procedure, which means nothing enters
the system on the strength of looking well-formed.

The transferable habit is to make the trusted base an explicit, deliberately
small, written-down artifact — and then to notice that convenience imports are
not free, because they move the boundary of what you are actually claiming. A
result that holds "given this library" is a different and weaker result than one
that holds given a handful of primitives, and the difference only becomes
visible when someone writes the base down. The same asymmetry shows up in a
verification effort where each assumed lemma widens what must be believed, in a
security argument where each dependency joins the attack surface, and in a
portability claim where each ambient assumption is a platform you have not
tested. Pair it with her admission rule: require every accepted construct to
arrive with the means of carrying it out, so nothing gets in on plausibility
alone.

**Source:** [Über den Zusammenhang der verschiedenen Begriffe der rekursiven Funktion](../works/uber-den-zusammenhang-der-verschiedenen-begriffe-der-rekursiven-funktion.md) — the introductory delimitation of which recursion schemes are admitted and the following section, where each auxiliary number-theoretic function used later is given its own definition instead of being cited.
