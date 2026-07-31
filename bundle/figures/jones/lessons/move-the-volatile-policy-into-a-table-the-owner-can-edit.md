---
type: lesson
title: "Move the volatile policy into a table its owner can edit, and let the program interpret the table"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Move the volatile policy into a table its owner can edit, and let the program interpret the table

**Lesson:** Most of what gets called maintenance is not repair. It is somebody's policy changing — a rate, a threshold, a set of eligibility rules, a workflow — and the change requiring a programmer only because the policy was expressed as code. That is a self-inflicted cost, and the size of it is easy to underestimate: every such change queues behind development capacity, gets translated by someone who does not own the policy, and has to be verified by someone who cannot check it against intent.

There are three places the policy can live, and the middle one is the trap. Scattered through the records it applies to is worst: a change means touching everything. Compiled into the program is better and is where most systems settle, because it is at least in one place — but it has quietly made every future change a programming task. The third option is to identify the properties the policy actually depends on, put the combinations of those properties and their outcomes in a table held as data, and have the program interpret the table. Now the change is a data update, performed by the people whose policy it is, using an ordinary editing tool, with no development cycle in between.

The step that makes this work is the one people skip: you must first identify what the policy is a function *of*. That is analysis, not mechanism, and it is where the judgement lies — get the parameters right and the table is small and the interpreter trivial; get them wrong and you have built a configuration format that cannot express the next change either. The test is whether every change you can foresee is a change to the table's contents rather than to its shape.

The idea generalizes past business rules to control structure itself. An algorithm expressible as a set of states and transitions can be held as a table with a small interpreter over it, and the resulting program is both dramatically shorter and easier to trust, because the interpreter is checked once and everything else is data. Recognizing when a computation has that shape is a skill worth cultivating: it converts a large body of code into a small body of code plus a large body of inspectable facts, and facts are much easier to get right than control flow.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 22's "Making Programs Table-Driven" section: the observation that much of the huge burden of program maintenance could be done by non-programmers given more thought at design time; the worked comparison of three ways to hold customer discount rates — as constants in each customer record, which requires amending many records for any policy change; determined by the program, which puts changes in the hands of programmers; or, having identified the customer properties the rate depends on, built into a table of combinations and rates held in a database and updated by clerical staff using a utility program; and the related discussion of finite state machine descriptions, in which an algorithm describable by such a diagram yields a very clear and thus reliable program generated from the table, illustrated by a conversational program whose table interpreter required only eighty executable statements.
