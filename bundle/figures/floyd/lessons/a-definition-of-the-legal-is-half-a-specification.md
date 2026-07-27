---
type: lesson
title: "A definition that only says what is legal is half a specification, because most of what arrives will be illegal"
figure: floyd
works: [the-syntax-of-programming-languages-a-survey]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A definition that only says what is legal is half a specification, because most of what arrives will be illegal

**Lesson:** A formal definition partitions the world into things that conform and things that do not, and it is silent about the second group beyond excluding them. Tools derived mechanically from such a definition inherit the silence: handed a conforming input they recover its structure, handed a non-conforming one they have nothing to say and typically collapse. This is not a defect of any particular derivation technique but a consequence of what the definition contains. Anything a tool is to do with a malformed input — locate the damage, describe it, recover enough to keep going and find the next problem — has to come from somewhere else, because it was never in the definition.

The reason this matters more than it sounds is a fact about usage rather than about formalisms. Over the life of a system that reads a defined notation, the overwhelming majority of inputs presented to it will be defective, because that is what working on something looks like: you write it wrong, you find out, you fix it. So the behavior the definition specifies is exercised at the end of each cycle, and the behavior it leaves unspecified is exercised throughout. Judged by where the time goes, error response is the primary interface and conformance is the special case. Deriving a tool that is excellent on conforming input and undefined otherwise is optimizing the rare path.

There is a demand hiding in this that is worth stating plainly, because it is more ambitious than error messages. If a definition is to support useful behavior on defective input, then it has to somehow account for the structure of near-misses — how a slightly damaged artifact relates to the legal ones it is close to — and at minimum it must permit the effects of a local mistake to be confined locally, so that one error does not cascade into a hundred spurious ones. That is a genuine requirement on the design of the definition, not a downstream implementation concern, and it may well be the harder half of the design problem. It is also, historically, the half that gets deferred and then never done, which is why recovery policies end up hand-written per tool with no principle behind them.

A programmer who takes this seriously treats the question "what does this do with input that violates the schema?" as part of designing the schema, not as a later question about the parser, the validator, or the deserializer. The concrete discipline is to specify the failure surface alongside the success surface — what gets reported, with what locality, and what the system is permitted to assume afterwards — and to be suspicious of any generated or derived component whose behavior on bad input nobody chose.

**Source:** [The Syntax of Programming Languages — A Survey](../works/the-syntax-of-programming-languages-a-survey.md) — the closing remarks of the syntax-controlled analysis section, which observe that neither family of analyzers can cope with non-sentences on its own, that the more flexible family still needs recovery policy supplied explicitly, and that a grammar accounting for the interpretation of ungrammatical input is doubly necessary for programming languages if only to confine the effects of mistakes; also the Unsolved Problems section, which lists synthesizing a grammar that best accounts for slightly erroneous input as an open question.
