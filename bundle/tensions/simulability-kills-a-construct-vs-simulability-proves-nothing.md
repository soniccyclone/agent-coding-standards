---
type: tension
title: "When a construct is provably redundant, is that a reason to reject it or a reason to ship it?"
figures: [stonebraker, abiteboul]
lessons: [stonebraker/a-new-construct-must-pay-for-its-complexity-in-leverage, abiteboul/equal-expressive-power-is-not-a-licence-to-substitute]
status: resolved-by-llm
tags: [tension]
---
# When a construct is provably redundant, is that a reason to reject it or a reason to ship it?

## The decision
Someone proposes a new construct for a language or system, and you can prove the
primitives you already ship reproduce its effect at comparable cost. The proof
exists and nobody disputes it. Do you add the construct anyway, and in
particular, does "the encoded version is unreadable" count as a reason to spend
complexity?

## Stonebraker: redundancy at parity is a kill test
Stonebraker read three decades of data-model proposals and found that the ones
that died were not badly designed, they were redundant. Set-valued attributes,
tuple-typed columns, inheritance graphs: each could be built on tables and keys
and ran about as fast when you did. His conclusion in
[A new construct must pay for its complexity in leverage, not in elegance](../figures/stonebraker/lessons/a-new-construct-must-pay-for-its-complexity-in-leverage.md)
is that such a construct is pure addition to what every user must learn and
every implementer must support, funded from nobody's budget. The additions that
survived were the ones that changed what was achievable rather than what was
sayable, mostly the ability to push user code and user access paths into the
engine. So the only admissible answers are that something becomes newly possible
or newly fast, and he names the answer to refuse by name: that it becomes more
natural to express. His reason for refusing it is not contempt for readability
but a claim about where readability should be bought, namely at a layer above
the core where a mistake can still be withdrawn.

## Abiteboul: the proof measures the ceiling, not where you should stand
Abiteboul proves the simulation results himself, twice, in two different
settings, and then refuses the inference both times. In
[Equal expressive power is never a licence to substitute one notation for another](../figures/abiteboul/lessons/equal-expressive-power-is-not-a-licence-to-substitute.md)
the observation is that a simulation argument is obliged to preserve behavior
and nothing else. What it is free to destroy is the correspondence between a
piece of text and a piece of intent, and that correspondence is the thing
maintenance actually runs on. A phase boundary encoded as marker facts and
offset copies of relations computes the right answer and communicates nothing,
so every later change begins with an archaeology exercise. His operational rule
is the mirror image of Stonebraker's: catching yourself argue that a construct
is redundant means you have priced capability and not cost, and catching
yourself hand-build the encoding is evidence the construct is missing. Note
where he wants it, though. He asks for a small implicit core because that is
what keeps the semantics tractable, with the explicit constructs exposed on top.

## Resolution
**LLM DECISION — Nathan may overturn.**

The seam is whether the construct adds a semantic rule or eliminates itself by
translation, and on the first side Stonebraker is right and on the second
Abiteboul is. Ask whether a mechanical, local rewrite can remove the construct
from a program before the evaluator sees it, leaving no trace in the core's
definition. If yes, the construct costs a translation pass and some documented
surface, the implementer's model of the system does not grow, and legibility on
its own is sufficient justification, because the complexity Stonebraker is
budgeting has not been spent. If no, if the evaluator has to learn a new case,
if the optimizer has to reason about it, if the invariants of the core change to
accommodate it, then it is a core primitive and Stonebraker's test governs
without the legibility discount.

That seam is not a compromise invented to make the two agree. It is what each of
them already said. Stonebraker's escape clause is that naturalness is almost
always obtainable at the layer above without touching the core, and Abiteboul's
recommendation is exactly a small implicit core with the explicit constructs
sitting above it. Both want the same shipped artifact. What they disagree about
is which construct actually can be lifted out of the core, and Abiteboul's own
case answers that against his framing: he proved the simulation, and a proof
that a fixpoint core reproduces explicit sequencing is a desugaring waiting to
be implemented. The reason his users were suffering was not that the construct
belonged in the core, it was that nobody had written the layer, so every user
open-coded the encoding by hand. Hand-encoding by every user is not the layer
above. It is the absence of one.

What survives of the disagreement is a genuine difference in cost models.
Stonebraker's budget counts machine costs and implementer burden and declines to
count reader effort, which is visible in the fact that he will admit latency and
durability as reasons to prefer one arrangement over an equivalent one while
still refusing readability. Abiteboul supplies the missing line item. Take his
side on the accounting and Stonebraker's on where the charge lands: reader
effort is a real cost, it is charged against the surface, and it never buys a
new rule in the core. The review question to carry is Abiteboul's, aimed at any
layer claiming minimality: what do its users have to encode by hand, and does
the encoding still say what it means? A minimal core with no sugar above it has
not eliminated the complexity, it has billed it to everyone downstream.

This is the same failure the Scott and Reynolds tension turns on, one floor
down. An argument of the form "X embeds into Y, therefore nothing is lost" is
only ever true about the property the embedding was built to preserve. Behavior
survives a simulation; intent does not. Values survive an embedding; opacity
does not. In both cases the person holding the proof is entitled to a narrower
conclusion than the one they draw.

**Strongest counter-argument:** the desugaring seam may not hold up under
operation, which would make Stonebraker's blanket refusal the better rule in
practice rather than merely the cruder one. Sugar leaks downward the moment
anything goes wrong. Error messages, stack traces, query plans, profiler output
and debugger state all speak the core's vocabulary, so a user who writes the
legible construct still has to understand the encoding to diagnose it, and now
has to understand both. If that is the usual outcome rather than the occasional
one, then the legibility gain is largely illusory and Stonebraker's insistence
on newly possible or newly fast is a defensible proxy for it. The way to check
is empirical and specific: for a proposed sugar, look at whether the tooling can
be made to report in the sugar's own terms, and if it cannot, treat the
construct as a core addition even though it desugars, because that is what the
user will experience it as.
