---
type: lesson
title: "Say which outcomes count as answers, and let the machinery for finding them be derived rather than written"
figure: floyd
works: [nondeterministic-algorithms]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Say which outcomes count as answers, and let the machinery for finding them be derived rather than written

**Lesson:** Ordinary programs are written forward: each step is caused by the steps before it, and the programmer's job is to arrange the causes so the desired effect falls out at the end. There is a second way to specify a computation, in which you supply only two things — the points where a choice among alternatives is made, and a labelling of each ending as acceptable or unacceptable — and declare that the computation *is* whichever sequence of choices ends acceptably. Nothing says how the choices get made. The specification is written in terms of the outcome it is for, not the mechanism that reaches it, and the mechanism is recovered afterwards by a uniform transformation.

The consequence that matters is what you may then infer about the program without simulating it. Because only acceptable endings count as computations, you can reason about the choices as if they were made by something that knows the answer already. In the eight-queens formulation you can conclude that a particular first choice will never occur in any computation, not by tracing the search, but because no acceptable ending exists downstream of it. That is an argument about the solution space, made in the language of the problem, and it is available before any decision about how the search will actually be conducted. Forward-written code cannot support arguments of this shape, because in it every value is whatever the preceding steps happened to produce.

This is worth separating carefully from randomness, which is the other thing the word "nondeterministic" gets used for. Nothing here is probabilistic; the underspecification is not noise but deliberate silence about a decision the specification declines to make. Such a program is unspecified in the way a person with a goal is unspecified: constrained by what it is trying to achieve rather than by what it has just done. The freedom is the author's, not the machine's, and it is freedom to postpone.

A programmer who works this way writes the acceptance condition first and treats it as the real program, on the grounds that it is the part carrying the intent and the part that any implementation must be checked against. Choice points and failure labels become the vocabulary for stating combinatorial problems directly, close to how one would describe them out loud, and the search strategy is demoted to an implementation decision — one that can be changed, or generated, without touching the statement of what is being looked for.

**Source:** [Nondeterministic Algorithms](../works/nondeterministic-algorithms.md) — the definition of an algorithm as only those execution sequences whose terminations are labelled successes, together with the closing discussion contrasting causes that precede their effects against goals for whose sake effects are carried out, and the argument that a corner queen is never chosen because no solution contains one.
