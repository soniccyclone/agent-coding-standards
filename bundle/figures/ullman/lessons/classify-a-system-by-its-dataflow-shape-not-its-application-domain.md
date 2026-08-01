---
type: lesson
title: "Classify a system by its dataflow shape, not its application domain"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, expressiveness, parallelizability]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Classify a system by its dataflow shape, not its application domain

**Lesson:** Systems are marketed by what they are for and understood by how they are shaped, and the two categorisations disagree often enough to matter. A framework sold as machine-learning infrastructure — different vocabulary, different data type, different audience, rarely grouped with the data-processing tools — can turn out to be a workflow engine underneath: a graph of stages, each applied across partitions of a typed dataset, each publishing only on completion. Recognising that is not pedantry. Membership in the family is what tells you which properties the thing inherits: whether failed stages can be retried safely, what happens when you introduce a loop, where the materialisation costs land, and which of your existing intuitions transfer without modification. None of that is derivable from the application domain, and all of it is derivable from the shape.

The same lens explains why specialised runtimes keep dissolving. A system built around a distinctive computational model arrives with its own storage layer and its own failure handling, because it needed both to exist. What survives it is the model — the way a programmer states the computation — while the storage and failure machinery gets discarded and the model reimplemented as a layer over a general substrate that already has those parts. That is not a defeat for the specialised system; it is the normal outcome, and it is a useful thing to predict. When evaluating a new system, separate the part that is a genuinely different way of expressing computation from the part that is infrastructure the author had to write to ship it. The first part is what you are actually adopting and what will outlive the product. The second part is a commodity that will be replaced, and betting on it is how you acquire migrations.

The habit to build: on meeting a new system, ignore the domain nouns and answer four questions instead. What is the unit of data that moves between stages, when does a stage publish, is the graph allowed to have cycles, and what is assumed durable. Two systems with the same four answers behave alike under load and under failure regardless of whether one processes web logs and the other trains models, and the transfer of hard-won knowledge between them is nearly free. Two systems in the same advertised category with different answers do not transfer at all, which is the more expensive mistake and the one the marketing category invites.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 2's extensions section, which observes that TensorFlow is not generally recognised as a workflow system because of its very specific targeting of machine-learning applications yet has a workflow architecture at heart, and notes that graph-model facilities of the Pregel kind are now commonly implemented on top of a workflow system so as to use the latter's file system and failure management.
