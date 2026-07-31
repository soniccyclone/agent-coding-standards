---
type: lesson
title: "What a thing could do is part of what it is: fix the vocabulary of possible interactions before describing behaviour"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# What a thing could do is part of what it is: fix the vocabulary of possible interactions before describing behaviour

**Lesson:** Before saying anything about how a component behaves, settle the set of interactions it is capable of at all, and treat that set as a fixed property of the component rather than as a summary of what it happens to do. The consequences run in one direction only. Nothing outside the set can ever occur — that is what makes the set worth declaring — but plenty inside it may never occur either, because the component is unfinished, or broken, or simply never asked. Confusing "does not" with "cannot" is the error the distinction exists to prevent, and it is the error behind a great deal of interface archaeology, where someone infers the contract from a log.

The sharpest consequence is that two components which currently do nothing at all are still different components if their vocabularies differ, and anyone interacting with them is entitled to rely on the difference. A broken machine that could have dispensed one kind of thing is not interchangeable with a broken machine that could only ever have dispensed another, even though today they are indistinguishable by observation. This is the precise reason a declared interface is worth more than a behavioural description: behaviour tells you what happened on the occasions you looked, and the declaration tells you the boundary of what could ever happen, which is the only thing that supports reasoning about cases you have not seen.

Choosing the vocabulary is therefore the first design act and the most consequential one, because it is a decision about what will be ignored. Physical attributes, maintenance operations, anything that concerns a different audience — all of it is excluded on purpose, and the exclusion is what makes the resulting description small enough to reason about. Two disciplines keep this honest. Name the audience the vocabulary serves, since "what the customer must care about" and "what the servicer must care about" are different sets and merging them produces a description useful to neither. And keep it a permanent commitment: a vocabulary that quietly grows whenever a new behaviour is added has stopped being a boundary and become a changelog.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the introduction to the chapter on processes, which defines an object's alphabet as the set of event names relevant to a description, holds it to be a permanent predefined property such that engaging in an outside event is logically impossible while an event in the alphabet may nonetheless never occur, distinguishes two never-acting objects by their differing alphabets and notes a customer knows the difference, and presents the choice of alphabet as a deliberate simplification that ignores attributes and maintenance actions on the grounds that they are of no concern to the machine's customers.
