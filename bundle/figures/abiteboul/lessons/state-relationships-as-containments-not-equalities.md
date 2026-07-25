---
type: lesson
title: "Between parties you do not control, state relationships as containments and define truth as what follows"
figure: abiteboul
works: [web-data-management]
axes: [expressiveness, verifiability]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# Between parties you do not control, state relationships as containments and define truth as what follows

**Lesson:** When several independently owned systems have to answer questions together, the instinct is to write down equations: this shared concept equals the union of those two sources, that one equals a join of two others. This work argues for stating the relationships as one-directional inclusions instead, and the argument is about who has to be in the room. An equation is a closed statement, so admitting a new contributor later means rewriting it and renegotiating with everyone it mentions. An inclusion says only that a particular source's contribution belongs somewhere in the shared picture, which leaves the picture open for other contributions nobody has thought of yet. Choosing the weaker statement is what makes the arrangement extensible without a coordinating authority.

The direction of the mapping is a second, equally consequential choice, and it decides where autonomy sits. Describe each shared concept as a function of the sources and the shared vocabulary is easy to query but every source change requires touching the central description. Describe each source as a function of the shared vocabulary and each owner can write their own description in isolation, since their statement mentions only the shared terms and their own data. The second arrangement costs more at query time and buys independence, which is the right trade whenever the participants are genuinely autonomous. The accompanying shift, and the harder one, is in what counts as an answer. Since the shared state is never materialized, you do not know it; you know constraints it satisfies. An answer is therefore something that holds in every possible shared state consistent with what you have, which makes query answering a reasoning problem rather than a lookup. The work is candid that this problem is undecidable in general and that the useful systems are the ones that pick restricted forms of mapping where it is not.

The transferable habits are three. Prefer the weaker statement of a relationship, because weaker statements survive parties joining and leaving. Point your mappings in the direction that puts the writing burden on whoever owns the thing being described. Distinguish, in your own head and in your interfaces, between what you have computed from data you hold and what is entailed by constraints over data you do not hold, and expect the second to be expensive and sometimes impossible. Any federated design that quietly treats a partial local picture as the whole truth has skipped that distinction rather than resolved it.

**Source:** [Web Data Management](../works/web-data-management.md) — the introduction to the data integration chapter, which builds up from equalities between shared and local relations to inclusions, motivates the inclusion form by the freedom it leaves for further contributors, contrasts the two mapping directions in terms of the autonomy each grants source owners, and then characterizes an answer as a fact true in every instance consistent with the mappings before narrowing to the decidable cases.
