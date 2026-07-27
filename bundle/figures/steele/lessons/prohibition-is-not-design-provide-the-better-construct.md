---
type: lesson
title: "Removing a construct to enforce discipline does not work; supplying a better-fitting one does"
figure: steele
works: [lambda-the-ultimate-imperative, the-java-language-specification]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Removing a construct to enforce discipline does not work; supplying a better-fitting one does

**Lesson:** A recurring instinct in language and framework design is to forbid the construct associated with bad code, on the theory that removing the tool removes the practice. This work argues the instinct is confused on two counts. Mechanically, prohibition fails: given procedures that can be passed around, conditionals, transfers that do not accumulate bookkeeping, and lexical scoping, the banned constructs are all simulable in a straightforward way, and with a macro facility the simulations are pleasant to use. You cannot subtract expressive power by deleting syntax when the remaining syntax reconstructs it. The history the work recounts bears this out — languages designed without a jump construct grew replacement escape constructs almost immediately, because the need had not gone anywhere.

The deeper objection is about where disorder actually comes from. Badly organized programs come from badly organized conceptions of the problem. Syntax cannot repair a muddled model, so restricting syntax cannot produce clarity; it can only make a muddled program more laborious to write. What genuinely helps a programmer organize a problem is the presence of constructs that fit the problem's own structure, so that the program's shape can track the problem's shape instead of translating through an ill-suited intermediary. That reframes the design task from pruning dangerous features to discovering and inventing apt ones — and it makes the interesting question about any omitted feature not "was it bad?" but "is what remains convenient enough that nobody misses it?"

For a programmer this converts a common style argument into an empirical one. When a construct is being banned by convention or lint rule, ask what job people were using it for and whether the codebase offers a construct that does that job better. If it does, the ban is redundant. If it does not, the ban will be routed around in uglier ways, and the productive move is to build the missing construct. The same test applies to one's own APIs: an interface that forbids without providing an alternative is exporting its designer's discomfort as the caller's problem.

**Source:** [Lambda: The Ultimate Imperative](../works/lambda-the-ultimate-imperative.md) — the closing paragraphs of the conclusions, plus the long note surveying languages that omitted the jump construct and then had to reintroduce equivalents.
