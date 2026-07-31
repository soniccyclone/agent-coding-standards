---
type: work
title: "The Craft of Programming"
figure: reynolds
description: A textbook that teaches programming with specification and proof as first-class concerns from the start, rather than as debugging bolted on after the fact. It works through fundamental data structures and control constructs with a running emphasis on correctness arguments and cost analysis, reflecting Reynolds's view that a programmer should be able to justify a program's behavior, not just observe it. Went out of print with Prentice-Hall, after which Reynolds reclaimed the rights and released it himself.
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
year: 1981
url: https://www.cs.cmu.edu/afs/cs/user/jcr/ftp/craftprog.pdf
survey_pages: 449
survey_text_layer: full
survey_fetch_mb: 33
access: public
host: self-archived
tags: [work]
---

# The Craft of Programming

**Venue/year:** Prentice-Hall International Series in Computer Science, 1981.
**Source:** https://www.cs.cmu.edu/afs/cs/user/jcr/ftp/craftprog.pdf — live PDF (HTTP 200, ~34MB scanned copy), self-archived by Reynolds in his own CMU FTP directory. His page https://www.cs.cmu.edu/~jcr/craftprog.html explains: "It is now out of print, and all rights have reverted to the author, who has decided to make it publicly available."

**Coverage note (in progress).** Reading copy is `scratchpad/craft/craftL.txt` — `pdftotext -layout` over the 449-page scan (19,912 lines). The `-layout` flag matters: plain `pdftotext` on this file returns column-scrambled text that is unusable. Earlier passes covered the preface through Section 3.1.5 (call by value and result). This pass resumes at line 8101 (Section 3.1.6, Array Parameters). Sections read so far this pass: 3.1.6 through 3.3.12 (lines 8101-11642).

## Lessons
- [Comment the part of a program that holds still, because the code already shows you what moves](../lessons/document-what-holds-still-not-what-changes.md)
- [To make a loop faster, loosen the relation it preserves so more of the state is free to move](../lessons/loosen-the-invariant-to-buy-freedom-of-movement.md)
- [Test whether a contract says enough by letting an adversary rewrite the state within it](../lessons/test-a-contract-by-letting-an-adversary-rewrite-the-state.md)
- [Keep facts about your mechanism separate from facts about your subject matter, and give them exactly one joint](../lessons/confine-domain-facts-to-one-designated-joint.md)
- [Learn the formal method so you can tell when the informal argument is enough](../lessons/learn-the-formal-method-to-know-when-to-skip-it.md)
- [Find the loop's invariant by asking how much of the goal you can have for free](../lessons/split-the-goal-into-the-free-part-and-the-earned-part.md)
- [When the uniform algorithm fails at one edge, try extending the definition before adding a branch](../lessons/extend-the-definition-instead-of-branching-on-the-edge-case.md)
- [Locality is something you discover in the contract, not something you decide when declaring](../lessons/read-a-variables-scope-off-its-contract.md)
- [If renaming a component's internal names can change what it means, you have no encapsulation](../lessons/if-renaming-can-change-meaning-you-have-no-encapsulation.md)
- [Design against an idealized machine, then insist the real one turn every deviation into a hard failure](../lessons/design-for-the-idealized-machine-and-make-the-gap-fatal.md)
- [When two guards are equivalent inside the contract, choose by what they do outside it](../lessons/choose-among-equivalent-guards-by-behavior-outside-the-contract.md)
- [Reasoning that feels hard is often only unfamiliar, so build the vocabulary the domain is missing](../lessons/difficulty-that-is-only-unfamiliarity-is-fixed-by-building-vocabulary.md)
- [Refuse constructs that hide iteration, because counting loops is the only cost model you have](../lessons/keep-hidden-iteration-out-of-the-expression-language.md)
- [A set of simultaneous updates is not the same as performing them one at a time](../lessons/simultaneous-updates-are-not-a-sequence-of-updates.md)
- [What the property depends on, plus what you already know, sets the floor on how much you must examine](../lessons/what-the-predicate-depends-on-sets-the-floor-on-work.md)
- [A generalization earns its place only with several real instances below it and nontrivial laws above it](../lessons/a-generalization-earns-its-place-with-instances-below-and-laws-above.md)
- [When a step needs a messy operation, find the weakest property that discharges it rather than unfolding the definition](../lessons/prove-from-the-weakest-property-not-the-definition.md)
- [An arbitrary order, agreed on by everybody, buys speed without meaning anything](../lessons/an-arbitrary-agreed-order-buys-speed-without-meaning-anything.md)
- [When a rule breaks on updating part of a thing, lift the update to the whole value instead of patching the rule](../lessons/lift-a-partial-update-into-a-whole-value-update.md)
- [A case split in a basic law is a prediction of where the bugs will be](../lessons/a-case-split-in-a-basic-law-predicts-where-the-bugs-will-be.md)
- [Attack your own specification with a cheating program, then add the clause that stops it](../lessons/attack-your-own-specification-with-a-cheating-program.md)
- [Define an operation up to the equivalence you actually care about, not up to equality](../lessons/define-the-operation-up-to-the-equivalence-you-actually-need.md)
- [Push the caller's actual question into the computation, because a comparison is cheaper than a value](../lessons/compute-the-question-the-caller-asks-not-the-value.md)
- [Classify an interface position by what kind of phrase it admits, not by what kind of value flows through it](../lessons/classify-a-position-by-what-kind-of-phrase-it-admits.md)
- [Sort every obligation by who can enforce it, and give each class its own notation](../lessons/sort-obligations-by-who-can-enforce-them.md)
- [A mechanism's hazard and its expressive power are often the same property seen twice](../lessons/a-hazard-and-a-capability-are-often-the-same-property.md)
- [To say anything about change, name the old value with something the program cannot touch](../lessons/name-the-old-value-with-something-the-program-cannot-touch.md)
- [Keep "it finishes" and "it is right" as two separate arguments, because one can die while the other still stands](../lessons/keep-finishing-and-being-right-as-two-separate-arguments.md)
- [Structure is a property of what a reader can see, not a record of the order you built it in](../lessons/structure-is-what-the-reader-can-see-not-how-you-built-it.md)
- [Do not make everyone pay for a safety measure that only one kind of caller needs](../lessons/charge-the-caller-who-needs-the-workaround-not-everyone.md)
- [Every expression you can write in the program must be legal in an assertion about it](../lessons/keep-the-expression-language-usable-inside-assertions.md)
- [A parameter you never do anything to can accept any phrase, and that is how control structures become library code](../lessons/an-unconstrained-position-generalizes-from-a-name-to-a-phrase.md)
- [Whether a resource's lifetimes nest or pile up is decided by where the recursive call sits](../lessons/where-the-recursive-call-sits-decides-whether-lifetimes-overlap.md)
- [Derive the cost formula first; it names the one coefficient worth attacking](../lessons/let-the-closed-form-cost-tell-you-which-coefficient-to-attack.md)
- [The quantity you make shrink is a design choice, and changing it gives a different algorithm with the same shape](../lessons/the-measure-that-shrinks-is-a-design-variable.md)
- [A rule you validated on closed code can be false the moment a name can be supplied from outside](../lessons/a-rule-valid-in-a-closed-program-can-fail-once-names-come-from-outside.md)
- [You need two separate maps — names to things, things to values — before aliasing is even expressible](../lessons/two-levels-of-map-are-needed-before-aliasing-is-even-expressible.md)
- [Move the side condition inside the claim, and instantiation can no longer produce a falsehood](../lessons/move-the-side-condition-inside-the-claim.md)
- [Give the metavariables real types and the rule schema collapses into an ordinary statement](../lessons/give-your-metavariables-real-types-and-the-schema-becomes-a-statement.md)
- [Belonging to the type is not obeying the law, so name the law separately](../lessons/some-things-of-the-right-type-still-break-the-law.md)
- [Carry each claim's assumption set with it and compose by union, or the assumptions get lost](../lessons/ship-the-assumption-set-with-the-claim-and-compose-by-union.md)
- [A name can only do harm from a position that acts, so compute dependencies by position, not by presence](../lessons/a-name-can-only-do-harm-from-a-position-that-acts.md)
- [A declaration is a settlement point: it grants a fixed set of facts and pays off exactly the debts naming it](../lessons/a-declaration-is-where-the-debts-get-settled.md)
- [Recursion forces you to write the contract before you can check the body](../lessons/recursion-forces-the-contract-to-be-written-before-the-body.md)
- [Compare two implementations by implication between their contracts, and read the difference as the calls that distinguish them](../lessons/compare-implementations-by-implication-between-their-contracts.md)
- [A control abstraction demands a specification of its behaviour argument and yields the inference rule for the construct](../lessons/what-a-control-abstraction-demands-is-a-specification-and-what-it-yields-is-a-rule.md)
- [If an argument's value moves with something else, name the function it secretly is](../lessons/if-an-argument-changes-with-something-name-the-function.md)
- [A name invented solely to be mentioned once is a defect of the notation, and the fix must be eliminable](../lessons/a-name-that-exists-only-to-be-mentioned-once-is-a-notation-defect.md)
- [A rule cluttered with conditions about substitution should be restated over a function instead](../lessons/hoist-the-substitution-machinery-into-one-mechanism.md)
- [Independence analysis works at the granularity of names, so buy finer granularity with laws about selectors](../lessons/buy-back-granularity-inside-an-aggregate-with-laws-about-selectors.md)
- [A pure function's contract is an equation; a state-changing procedure's contract is a theorem you must prove](../lessons/a-pure-functions-contract-is-an-equation-not-a-theorem.md)
