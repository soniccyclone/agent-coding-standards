---
type: lesson
title: "Before integrating two groups' data, separate their words from their concepts"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Before integrating two groups' data, separate their words from their concepts

**Lesson:** An analyst interviewed an engineering company for two weeks, then tried to draw who produced which information and who consumed it. The result was incoherent: almost nothing anyone produced was ever consumed, and almost nothing anyone consumed was ever produced. The obvious inference — the company is a shambles — was wrong, since it was demonstrably delivering complex working designs. The incoherence was in the *description*, and it came from three distinct causes worth being able to name separately.

First, synonyms: different disciplines had different words for the same thing, so one group's output and another's input looked unrelated. Second, packaging: someone produced a named bundle containing many items, and no consumer ever used the whole bundle while every item was used by somebody — so at bundle granularity the flows appeared to vanish. Both of these are merely confusing. The third is genuinely dangerous, and it stays dormant: homonyms, where different groups use the *same* word for different concepts. Homonyms cause no trouble at all while the groups work separately. They surface only when the groups are asked to share a system, which is exactly when it is most expensive to discover.

The root difficulty is that people do not naturally distinguish a term from the concept it names, so an argument about which meaning is "correct" feels like an argument about facts. In one case, a database spanning several disciplines had to reconcile a *dam* meaning the structure across the river with a *dam* meaning the body of water plus all its surrounding installations. Neither group was wrong and both were entrenched, and disputes of this kind turn into something closer to religious war than analysis. The practical discipline is to treat vocabulary reconciliation as a first-class task at the start of any integration, to hold concepts and their labels as separate things that must be explicitly mapped, and to expect the same word appearing in two groups' vocabularies to be evidence of a hidden conflict rather than evidence of shared understanding.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 7's boxed accounts of the engineering-company information-flow study, which names synonyms, information packages and homonyms as the three causes and notes homonyms cause no trouble until people try to communicate; and the hydroelectric-database anecdote about conflicting meanings of "dam", with the observation that we generally do not distinguish between term and concept.
