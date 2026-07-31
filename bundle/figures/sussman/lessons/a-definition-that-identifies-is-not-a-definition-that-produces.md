---
type: lesson
title: "A definition that lets you recognize the answer is not one that produces it"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, verifiability]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# A definition that lets you recognize the answer is not one that produces it

**Lesson:** The square root of a number can be defined as the non-negative value whose square is that number. This is a completely legitimate definition. It settles every question of identity — given a candidate you can check it, and you can derive general facts from it — and it tells you essentially nothing about how to obtain one. Rewriting it in program syntax changes nothing; it still merely restates the question.

The distinction being drawn is between describing what a thing is and describing how to get it, and the reason to hold it consciously is that the two are easy to confuse precisely because both look like definitions. A property-style description is a *recognizer*: it partitions candidates into acceptable and not. A procedure is a *producer*: it constructs a candidate from inputs. Confusing them is the standard failure of specification work, where a document that carefully pins down what a correct output would look like is mistaken for a document from which an implementation follows.

Two consequences are worth carrying. First, when someone hands you a specification, ask which kind it is, because a recognizer leaves the entire construction problem untouched and its apparent precision can disguise that. Second, the gap between the two is exactly where the interesting engineering lives — the recognizer for square roots is one line and the producer is an iterative approximation with a convergence argument and a termination test, none of which the recognizer hints at.

The relationship runs both ways and neither side is dispensable. Saying a program is correct is making a property-style claim about a procedure, so you need the recognizer to state what the producer owes you. The ambition of deriving producers automatically from recognizers is real and permanently partial: it works in bounded domains and cannot work in general, which means the translation from what-is to how-to remains the thing a person is paid to do.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 1 section 1.1.7's contrast between the mathematical definition of square root — a legitimate function that describes properties without describing a procedure and does not help even when rephrased in Lisp — and the distinction it draws between declarative and imperative knowledge, with the footnote on very high-level languages that attempt to generate how-to knowledge from what-is knowledge and can do so only in restricted areas.
