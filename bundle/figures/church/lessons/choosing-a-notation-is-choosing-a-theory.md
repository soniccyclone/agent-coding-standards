---
type: lesson
title: "Choosing a notation is choosing a theory of the domain, and surface similarity is no evidence of shared structure"
figure: church
works: [introduction-to-mathematical-logic]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture, foundations-of-computation]
tags: [lesson]
---
# Choosing a notation is choosing a theory of the domain, and surface similarity is no evidence of shared structure

Church is emphatic that the essential thing about adopting a formalized language is not the visible part. Replacing words with letters and special signs is the conspicuous feature and the theoretically unimportant one; what actually happens when you adopt such a language is that you commit to a particular analysis of the subject matter. The vocabulary and the formation rules encode claims about what the basic kinds of thing are, how they compose, and which distinctions are worth marking. You cannot pick a notation and stay neutral about the theory, because the notation *is* the theory in operational form.

His reason for building one at all is a diagnosis of why the alternative fails. Natural language evolved under pressure toward ease of communication, and that pressure is not compatible with precision of analysis, so the two goals pull apart and the language that won the popularity contest is the wrong instrument for the job. A formalized language deliberately reverses the trade: it follows logical structure and pays for that in brevity and convenience. Stating the trade in the open is what makes it a design decision rather than an accident.

The demonstration he uses is worth keeping. He sets two arguments side by side, phrased in nearly identical English, one valid and one not, the difference lying in structure the grammar does not expose. Linguistic parallelism, he notes, is not a safe guide to sameness of logical form — and in the easy cases the deception dissolves as soon as you think about meaning, while in the subtle cases it produces real and lasting confusion. Two expressions that read alike may be doing entirely different things, and a notation that cannot tell them apart will let the confusion through indefinitely.

For a programmer the transfer is direct and has two halves. Choosing a schema, a type vocabulary, an API's nouns, or a configuration format settles a theory of the domain, and that theory then constrains what anyone downstream can easily say — so the decision deserves the effort of an architectural one, not the ten minutes usually spent on it. And a shared shape is not a shared meaning: two endpoints, two records, or two call sites that look parallel are routinely doing incompatible things, which is why the useful notation is the one that forces the difference to appear on the surface even when doing so makes the common case more verbose.

**Source:** [Introduction to Mathematical Logic](../works/introduction-to-mathematical-logic.md) — the opening section on logic, which argues from paired same-sounding valid and invalid arguments to the need for a language that reproduces logical form, and states that adopting a formalized language means adopting a system of logical analysis.
