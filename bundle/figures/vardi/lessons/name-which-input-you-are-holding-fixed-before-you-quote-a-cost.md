---
type: lesson
title: "Name which input you are holding fixed before you quote a cost"
figure: vardi
works: [the-complexity-of-relational-query-languages]
axes: [expressiveness, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Name which input you are holding fixed before you quote a cost

**Lesson:** Any evaluator takes at least two inputs — the program and the data it runs on — and a single cost figure quoted without saying which of them was held constant is not one measurement but a blur of several. Fix the program and grow the data, and you learn how hard the individual questions are. Fix the data and grow the program, and you learn something entirely different: how much a short text in this notation can demand, which is a property of the notation's compression rather than of any one question. Grow both and you mostly recover the second figure, because the notation's ceiling dominates. The three numbers can sit whole complexity classes apart for the same system, so the argument "this is cheap" and the argument "this is expensive" are frequently both correct about the same language and simply answering different questions.

The reason to keep the two apart is that they serve different people. Someone who writes a handful of fixed queries and runs them against ever-larger data cares only about the first figure; someone who generates or composes queries programmatically, so the query text itself is the thing that grows, is governed by the second. Report the wrong one and you will either scare a user off a language that is perfectly cheap for their pattern of use, or promise cheapness to a user whose actual workload sits on the expensive axis. This is why the parameterization is a design decision rather than a bookkeeping detail: choosing what to call the input size chooses what property you are measuring.

The generalizable habit is to treat every cost claim as incomplete until it names its variable, and to expect the separate figures to move independently. A change in notation that leaves one untouched may shift the other by an exponential; a language extension may raise both but by different amounts. When someone reports a single number for a system with two growing inputs, the useful question is not whether the number is right but which of several distinct numbers they computed.

**Source:** [The Complexity of Relational Query Languages](../works/the-complexity-of-relational-query-languages.md) — the introduction's separation of data, expression, and combined complexity, and the following discussion of what each of the first two actually measures and which kind of user each concerns.
