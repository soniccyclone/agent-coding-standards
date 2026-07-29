---
type: lesson
title: "A description complete enough to generate the system has become the system, and needs its own abstraction"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# A description complete enough to generate the system has become the system, and needs its own abstraction

**Lesson:** There is a recurring ambition to make high-level descriptions rich enough that the running system can be produced from them automatically — no hand-written implementation, the diagram is the deliverable. Follow that ambition to its conclusion and something quietly inverts: a description containing every detail needed to generate a program *is* a program, and the notation it is written in, graphical or not, is a programming language. Whatever you gained, you did not gain an escape from programming. You changed which language you program in.

What makes this worth noticing is that the original question then repeats itself unchanged. If the reason for having a high-level description was that the program was too intricate to hold in mind, and your new description is complete enough to generate that program, then it carries essentially the same intricacy and the same need for something simpler above it. You have not climbed a level; you have relocated. The regress ends only where a description is *deliberately* incomplete — where it suppresses detail on purpose, and where that suppression is the source of its value rather than a deficiency to be engineered away.

That reframes what a good intermediate artifact looks like. One useful form sits between design and product: something that genuinely executes, so it can expose gaps in the logic that no diagram would reveal, while lacking the efficiency and robustness a finished system needs and omitting whole categories of target-system concern. Its incompleteness is deliberate and its purpose is to fail informatively. A programmer who has absorbed this stops treating a model's inability to generate the system as a weakness, and starts asking of any modelling notation what it refuses to express — because a notation that refuses nothing is just another programming language with worse tooling.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 4's treatment of the "100% rule" from database description methodologies, which observes that such a description is a program and its language a very high level programming language, notes that the whole argument then repeats, and introduces executable specifications as the deliberately incomplete alternative.
