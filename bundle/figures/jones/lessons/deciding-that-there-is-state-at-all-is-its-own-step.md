---
type: lesson
title: "Deciding that a thing has state at all is a design step, and it should not be the first one"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Deciding that a thing has state at all is a design step, and it should not be the first one

**Lesson:** Most people start describing a component by naming its variables. That feels like the beginning of the work, and it is actually a decision several steps in — one taken silently, before anything has been said about what the component is for. Variables are the machinery of a particular kind of machine, one that reuses locations over time. Nothing about the job you are trying to do requires that. The job is a relation between what you are given and what you must produce, and it can be stated completely without ever mentioning a place where something is kept.

Separating the two buys you an ordering. First say what is computed: inputs, outputs, the condition relating them, the restriction on inputs under which you promise anything at all. That description is short, has no ordering in it, and can be argued about with the people who care about the answer rather than the mechanism. Only then choose the collection of named values the eventual code will work in — and when you do, you are making a real decision with real consequences, which is now visible as a decision instead of buried in how you happened to start writing. The step from the stateless statement to a stateful one with the same inputs and outputs is small and mechanical, which is precisely the point: making it explicit costs almost nothing and stops the state from being assumed.

The payoff shows up as leverage on two things that are otherwise hard. One is that everything you can say without state is easier to manipulate, because you are not also tracking when. Anything you can push into the stateless part of a description stays cheap to reason about; anything you let leak into the stateful part you pay for repeatedly. The second is that once you have written the stateless statement, the state-based version is something you check *against* it, rather than the only description in existence. Without that, the variables are simultaneously the design and the standard the design is judged by, which is no standard at all.

There is a structural fact worth taking with this. A piece of code can change what its variables hold but not which variables exist — whatever new names come into scope inside it are gone by the time it finishes, so the shape of the state before and after is identical. That is what lets you name a class of states once and hold every operation to it, and it is why the shape of the state is a stable thing you settle deliberately rather than something that drifts as you write. Structure is decided; contents are what execution touches. Keeping that line sharp is what makes it possible to say anything general about a body of code at all.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 4's "General Operations" section, where the factorial example is first respecified as a function-level operation over inputs and results with no state named, with the remark that this is the better specification and that only once it is agreed is it time to decide on a class of states for a program that solves it, and the observation that moving from a function to an operation of the same domain and range is a simple development step; together with the "Operations" section's argument that a states clause rather than a plain state-to-state type is used because a statement or a closed block can change the values held but never introduce or delete variables, leaving the structure of the state as it was.
