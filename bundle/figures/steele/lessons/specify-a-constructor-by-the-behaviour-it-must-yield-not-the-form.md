---
type: lesson
title: "A description of a thing is not the thing; specify a constructor by the behaviour it must yield, never by the form it must produce"
figure: steele
works: [the-revised-report-on-scheme]
axes: [expressiveness, hardware-affinity, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A description of a thing is not the thing; specify a constructor by the behaviour it must yield, never by the form it must produce

**Lesson:** The report insists on a distinction most dialects of the day blurred: the textual form that introduces a procedure is not a procedure. It is a partial description of one, and it becomes a procedure only by being combined with the context its free names refer to. This sounds like pedantry and is not, because the report then builds a primitive on the distinction and gets something valuable out of it. The primitive takes a description of code and a description of a context and returns a usable procedure — and the report is emphatic that neither description says anything about how the implementation actually stores code or contexts. What the primitive promises is only that, given a description of desired behaviour, it yields something invocable that behaves that way and answers affirmatively to the language's is-this-callable test. The report spells out the range this leaves open: the operation could be as cheap as allocating a pair, or it could be an entire compiler.

That is a general recipe for interface design and the payoff compounds. Because the contract is stated as *produce something satisfying this predicate from this description*, and not as *produce this data layout*, the implementation is free across an enormous range, and callers cannot accidentally couple to the representation because they were never shown it. The report pushes the idea to its natural conclusion with a thought experiment: nothing about the contract requires the description to be in this language's notation at all. One could offer sibling constructors that take a procedure written in an entirely different language and return something the host can call, with the foreign realization hidden behind the same predicate. The interoperability falls out of having specified behaviour instead of form.

The discipline also does defensive work. The report records that an earlier primitive which evaluated a form in the *current* context had to be withdrawn because it destroyed the ability to reason about what a name meant by looking at the text around it, and that the authors deliberately declined to expose contexts as first-class inspectable objects even while accepting descriptions of them. That is the same principle read in the other direction: handing out the real internal thing, rather than a description you agree to interpret, is what forecloses your own future changes and breaks your users' ability to reason locally.

A programmer working this way writes factories and builders whose arguments are statements of intent, and whose return values are guaranteed only by an interface, so that the trivial implementation and the heavily optimized one are both legal on day one. They notice when an API has started handing out its own internals — a live handle to the environment, a mutable view of the parse tree, the actual configuration object — and they treat that as the point at which the abstraction stopped existing.

**Source:** [The Revised Report on Scheme: A Dialect of LISP](../works/the-revised-report-on-scheme.md) — the description of the closure-constructing primitive in the primitives section, and the notes explaining that program text is not a procedure and why the earlier current-context evaluation primitive was removed.
