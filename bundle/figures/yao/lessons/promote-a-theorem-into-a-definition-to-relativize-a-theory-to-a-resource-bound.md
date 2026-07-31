---
type: lesson
title: "To rebuild a theory under a resource bound, promote one of its theorems into the new definition"
figure: yao
works: [theory-and-applications-of-trapdoor-functions]
axes: [expressiveness, verifiability]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# To rebuild a theory under a resource bound, promote one of its theorems into the new definition

**Lesson:** A settled theory usually has a central quantity defined one way and characterized another way by a theorem: the quantity is defined structurally, and then a result proves it equals the cost of the best achievable encoding. When you need the same theory under a constraint the original ignored — that everything be computable within a budget — the productive move is to swap those roles. Take the characterization and make it the definition, now with the budget written into it: the quantity becomes the shortest description that an efficient producer can compute and an efficient consumer can decode. Nothing about the original is discarded; it is re-anchored on the operational side, which is the side the constraint can actually bite on. This is why the new theory does not read as an ad-hoc patch. Its definition is a theorem of the old one, so every place the budget turns out not to matter, the two agree by construction.

The reason this is necessary rather than merely elegant is that a structurally defined quantity can be arbitrarily far from anything reachable. A body of data may in principle be describable very compactly while nobody knows how to find that description in feasible time, so a claim of the form "in principle this needs only so many bits" gives no guidance whatsoever to a system that has to produce the bits. Once the budget is inside the definition, the quantity measures accessible content rather than latent content, and the gap between the two stops being an embarrassment and becomes the object of study: exhibiting a case where the accessible measure is enormously larger than the latent one is precisely what demonstrates the new theory has content of its own.

Two consequences generalize well beyond information theory. First, whenever you find yourself saying "in principle X suffices" while designing something, notice that in-principle statements are theorems of a model whose feasibility assumptions you have not checked, and re-derive the quantity with feasibility as a defining constraint. Second, the definition must be stated over a growing family rather than a single instance, because a bound on a fixed-size case can always be met by a large enough lookup, and only the asymptotic version distinguishes real difficulty from a table.

**Source:** [Theory and Applications of Trapdoor Functions](../works/theory-and-applications-of-trapdoor-functions.md) — the introduction and effective-entropy section of Part 1, which motivates the reformulation by exhibiting a source whose in-principle description length is unreachable by any known feasible encoder, adopts the minimum feasibly computable description length as the measure, states that Shannon's first theorem is being treated as a definition, and defines everything over sequences of sources so that per-instance table lookup cannot satisfy the bound.
