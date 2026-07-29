---
type: lesson
title: "Sort your correctness claims by who can check them, because a tool's silence is not approval"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Sort your correctness claims by who can check them, because a tool's silence is not approval

**Lesson:** When one description is built out of others, the question "is the result still correct?" turns out to be three questions with three different answers, and the useful move is to separate them before you start rather than discovering the difference later. The first kind is structural: does every part of the ingredients appear in the composite, do the connection points still line up, are the permitted messages preserved, do the multiplicity constraints on each connection stay within what the ingredients allowed? All of that is mechanically checkable and a tool can simply guarantee it. The second kind is behavioural: does the composite still produce the sequences of events the ingredients promised? That is checkable in principle but not automatically — it needs an argument, and the argument has to be made by someone. The third kind is whether the composite still *means* what its ingredients meant, and this one is permanently outside any tool's reach.

The third category is the one worth dwelling on, because it is where confidence is most often misplaced. You can verify with complete rigour that a parent-child description has every structural property of a tree description, and that verification tells you exactly nothing about whether either description faithfully represents parents and children. The correspondence between a written model and the mental model it was built to capture is not a property of the artifact; it lives in the heads of the people who wrote and read it, and can only be checked by those people talking to each other. A tool that reports no errors has confirmed the first category and stayed silent on the third — and silence reads like approval to anyone who has forgotten which question was asked.

What follows practically is a habit of labelling. For each property you care about, decide up front whether it is machine-checkable, argument-checkable, or judgement-only, and then route it accordingly: automate the first, demand a written argument for the second, and schedule a human conversation for the third instead of hoping it falls out of the other two. The failure mode this prevents is the common one where a green build is treated as evidence about intent, when intent was never in the checkable set.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 3's treatment of what survives a synthesis operation, which separates static correctness (automatable, with an explicit list of what a tool must preserve), dynamic correctness (requires due diligence), and the retention of a base model's semantics, where the text states plainly that correspondence to a mental model can only be checked through mental processes.
