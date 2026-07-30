---
type: lesson
title: "Have one name-binding construct, and make everything that binds names be that construct in disguise"
figure: naur
works: [revised-report-on-the-algorithmic-language-algol-60]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [programming-languages-and-semantics]
tags: [lesson]
---
# Have one name-binding construct, and make everything that binds names be that construct in disguise

**Lesson:** Naming is where systems accumulate special cases, because many different constructs turn out to introduce names and each one invites its own rule. Refuse that. Pick a single construct whose job is to open a new level of naming, define its rule once — a name declared here exists only here, and a name not declared here means what it means one level out — and then make every other name-introducing context be that construct, either literally or by stipulation. A subroutine body counts as one whether or not it is written as one. A statement label counts as declared in the innermost enclosing level, though nobody wrote a declaration for it. The rule is applied recursively, so a name that is external to one level may still be internal to the level containing it, and no additional machinery is needed to say so.

The payoff is that awkward rules stop being stipulations and become consequences. Since labels are bound by the enclosing level like everything else, jumping in from outside is not forbidden by a separate prohibition; it is impossible, because the target name does not exist out there. Grouping constructs that merely bracket statements without binding anything remain jumpable-into, and you do not have to remember which is which — you read off the answer from whether the construct binds. Re-using a name inside a level for something else makes the outer thing unreachable there, including when the outer thing was an argument to the routine you are inside; that is not a quirk, it is the one rule applying.

Where the same rule cannot save you is when text from one naming context is physically moved into another, which any substitution-based mechanism does. There the discipline is to state, at each such place and in the same words, that collisions between the incoming names and the resident ones are resolved by systematically renaming, and to state it for every mechanism that moves text rather than trusting the reader to generalise from one. Uniform binding does not remove the capture problem; it makes the fix a single sentence that can be repeated verbatim, and it makes the places needing that sentence enumerable — you look for every construct that relocates text.

**Source:** [Revised Report on the Algorithmic Language ALGOL 60](../works/revised-report-on-the-algorithmic-language-algol-60.md) — section 4.1.3 on blocks introducing a level of nomenclature and the recursive reading of local and non-local, the treatment of labels as declared in the smallest embracing block, section 5.4.3's insistence that a procedure body acts as a block whether written as one or not and its consequence for redeclared formal parameters, the derivation of the jump restriction in 4.3.4, section 2.4.3 on disjoint scopes permitting reuse of an identifier, and the parallel renaming clauses in 4.7.3.2, 4.7.3.3 and 5.3.5.
