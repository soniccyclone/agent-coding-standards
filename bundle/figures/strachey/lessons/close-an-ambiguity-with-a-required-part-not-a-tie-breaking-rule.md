---
type: lesson
title: "Close an ambiguity with a required part, not a tie-breaking rule"
figure: strachey
works: [the-main-features-of-cpl]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Close an ambiguity with a required part, not a tie-breaking rule

**Lesson:** When a notation admits two readings of the same text, there are two ways out. You can legislate: declare which reading wins, and carry that decree forever as a rule people must know in order to read code correctly. Or you can change the shape of the construct so that the ambiguous text can no longer be written down at all — most simply, by making obligatory the part whose absence created the doubt. The second fix costs a few extra characters at every use site and buys the permanent removal of a rule.

CPL took that second route with its two-armed conditional. The familiar trouble is a branching form whose second arm is optional: nest one inside another and the text no longer says which branch the trailing arm belongs to, so a language ends up with a precedence rule to settle it. CPL's designers instead gave the two-armed form a mandatory second arm, with the consequence that any conditional command can be dropped into either position without a reader having to reconstruct which reading the rules pick. Both arms accept arbitrary commands precisely because there is nothing left to disambiguate.

The general point is about where a design puts its complexity. A tie-breaking rule appears to make the problem go away, but it only moves the burden onto every future reader and every future tool, and it is exactly the kind of ad hoc rule that accumulates until a language stops feeling coherent. A structural constraint puts the burden on the author, once, at the moment of writing — and an author who is being forced to say which branch they mean is being forced to say something they knew anyway.

A programmer who believes this treats every "the rule is that X binds tighter" clause in their own designs as a debt rather than a solution. Faced with an ambiguous configuration format, API, or command grammar, they look for the omitted piece that permitted the ambiguity and make it required, accepting slightly more verbose input in exchange for text that has exactly one meaning without appeal to a rulebook.

**Source:** [The Main Features of CPL](../works/the-main-features-of-cpl.md) — the section on conditional commands, where the two-armed form's second arm is made compulsory specifically so that a conditional nested in either arm cannot be read two ways, seen against the stated goal in the introduction of a language with as few ad hoc rules as possible.
