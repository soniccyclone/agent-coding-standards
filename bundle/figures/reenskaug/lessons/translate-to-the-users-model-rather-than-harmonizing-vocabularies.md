---
type: lesson
title: "When two groups mean different things by one word, translating beats forcing them to agree"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# When two groups mean different things by one word, translating beats forcing them to agree

**Lesson:** A shared system serving several groups eventually hits the case where one term carries two entrenched meanings — one discipline's *dam* is the structure across the river, another's is the water plus every installation around it. The reflexive response is to standardize: pick one meaning, publish a glossary, retrain everyone. That response treats vocabulary as incidental, when for the people using it the vocabulary is load-bearing and decades old, which is why standardization efforts generate heat out of all proportion to their apparent stakes.

There is a second option that only becomes visible once you stop thinking of the interface as a window onto the stored structure. The thing a person interacts with can *translate* — presenting information in that group's concepts and terminology while the underlying service keeps its own — so each discipline retains its own words and the shared store stays coherent. Both options are technically available, which reframes the decision honestly: choosing between harmonization and translation is a management judgement about the organization, not a technical constraint to be discovered.

Generalized, this is what makes an interface worth building at all. The service's model is usually different from any individual user's model in scope, precision and complexity, and the interface's job is to supply enough filtering and translation that the user experiences a system organized the way *they* think. Otherwise you have merely exposed the storage layout and pushed the translation work onto every person, every time, forever — and each of them will do it slightly differently, which is where the misunderstandings come from. The design question for any interface therefore becomes: whose model does this present, and if it presents the implementation's, who is absorbing the gap?

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 7's Task/Tool/Service section, which states that a tool must provide filtering and translation so the user gets the illusion of a system supporting their own mental model, relates this to the external-schema idea from database architecture, and gives the boxed hydroelectric "dam" case with both options — harmonize the terminology or build translating tools — noting the choice is a management decision.
