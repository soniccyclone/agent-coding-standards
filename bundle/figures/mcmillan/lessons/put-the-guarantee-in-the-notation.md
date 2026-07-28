---
type: lesson
title: "Put the guarantee in the notation, and make the escape hatch visibly worse"
figure: mcmillan
works: [symbolic-model-checking-an-approach-to-the-state-explosion-problem]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Put the guarantee in the notation, and make the escape hatch visibly worse

The description language built for this work offers two ways to say what a system does. The general way lets you write an arbitrary logical condition relating current and next configurations — maximally flexible, and capable of expressing outright nonsense. Assert a contradiction and you get a system with configurations that have no successors, which silently makes requirements true for vacuous reasons and describes a thing that cannot be built. The restricted way is a parallel-assignment form in which every variable's next value is given by an expression, checked at compile time against double assignment and circular dependency.

The interesting property is what those two checks buy: any program written in the restricted form is guaranteed to describe something realisable, because the checks establish that some execution order for the assignments exists. The guarantee is not a lint rule or a convention or something the author must remember — it is a consequence of staying inside the notation. And the thesis is explicit that the general mechanism, while retained for people writing translators from other languages, is not recommended, precisely because its extra power is power to be wrong.

What makes this a lesson rather than a preference is the shape of the trade. The restricted form is *less* expressive and that is the source of its guarantee; the two are the same fact viewed from either side. This inverts the usual instinct that a notation should be as general as possible with discipline layered on top. Discipline layered on top is advisory. A restriction baked into the grammar is load-bearing, and it moves the error from runtime confusion — a requirement mysteriously satisfied, a design that cannot be implemented — to a compile-time complaint about a specific line. The same thesis makes the parallel choice for its data: only finite, static types, because those are what the underlying technique can represent, and admitting more would produce descriptions the checker could not honour.

The practice this suggests is to identify, for each guarantee you care about, the smallest syntactic restriction that forces it, and then make that restriction the default path rather than the disciplined one. Keep the general mechanism if some consumer genuinely needs it, but let its documentation say plainly that it forfeits the guarantee, and expect that the sublanguage — not the full language — is where your reasoning tools will work.

**Source:** [Symbolic Model Checking: An Approach to the State Explosion Problem](../works/symbolic-model-checking-an-approach-to-the-state-explosion-problem.md) — the chapter introducing the SMV description language, its parallel-assignment discipline and compile-time checks, and the discussion of why the direct relation-and-initial-condition declarations are discouraged.
