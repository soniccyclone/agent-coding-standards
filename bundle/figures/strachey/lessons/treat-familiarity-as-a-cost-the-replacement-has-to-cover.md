---
type: lesson
title: "Treat familiarity as a cost the replacement has to cover"
figure: strachey
works: [the-main-features-of-cpl]
axes: [cognitive-load, primitive-count, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Treat familiarity as a cost the replacement has to cover

**Lesson:** A design that succeeds a well-known predecessor inherits an asset it did not build: everything its users already know. Every departure from the predecessor spends some of that asset, and the spending is invisible in the design document because it lands on people who are not in the room. So the burden of proof runs the wrong way from what novelty-minded designers assume. Keeping an established concept needs no argument; replacing one needs a demonstrable gain, and if two alternatives are genuinely equal on the merits, the familiar one wins by default.

CPL's authors set that policy out explicitly. They took Algol as their starting point, said plainly that someone trained in either language should be able to move to the other, and adopted the standing rule that they would only diverge where the new concept made things measurably more consistent, clearer, or more workable in practice. Notice what that rule is not: it is not conservatism, since CPL departs from Algol substantially wherever they judged the departure earned its keep. It is a filter that lets large changes through and stops small gratuitous ones — the reverse of what happens when a team redesigns by taste and ends up with a hundred cosmetic differences and no compensating gain.

The reason this holds is that unfamiliarity is a per-user cost paid repeatedly by many people, while the satisfaction of an improved detail is a one-time gain enjoyed mostly by the designer. Small differences are therefore systematically overvalued from the inside. Writing down, in advance, what a departure must buy is the only reliable way to keep that bias from accumulating.

A programmer who believes this makes their API resemble the ones their users already use unless they can name what the difference achieves, and treats "it's cleaner this way" as insufficient without a stated improvement in consistency or clarity. They also stop conflating conservatism with restraint: the same rule that blocks a renamed method for aesthetic reasons permits a wholesale rethinking of a data model when the rethink demonstrably pays.

**Source:** [The Main Features of CPL](../works/the-main-features-of-cpl.md) — the concluding section, which states the design policy of adhering to familiar Algol concepts unless replacement brings a noticeable improvement, and the introduction's framing of CPL as designed from first principles yet deliberately in Algol's spirit.
