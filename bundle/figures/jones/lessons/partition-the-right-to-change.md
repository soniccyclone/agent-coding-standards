---
type: lesson
title: "Let concurrent participants coexist by partitioning what each may change, not by scheduling when each may run"
figure: jones
works: [tentative-steps-toward-a-development-method-for-interfering-programs]
axes: [parallelizability, verifiability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Let concurrent participants coexist by partitioning what each may change, not by scheduling when each may run

**Lesson:** Two activities on the same data structure are usually made safe by taking turns, which is a statement about time. The cheaper way, when it is available, is a statement about authority: carve the structure into aspects and give each participant exclusive licence to alter one aspect and an obligation to leave the others alone. If the aspects are chosen so that neither participant's work depends on the aspect the other may move, they can run continuously and simultaneously with no mutual awareness at all. The obligation each carries is the same shape as the assumption the other needs, so the coexistence argument is a one-line match rather than a case analysis over interleavings.

Finding such a partition is design work, and the useful move is to look past the representation to the observations that matter. A structure typically supports several distinguishable questions, and an activity that changes the representation may leave some of those questions' answers untouched. Reorganizing a structure for speed can preserve every classification it encodes; changing the classification can leave the internal arrangement intact. Where two activities disagree about the representation but not about any observation the other depends on, they are not actually in conflict, and reading them as conflicting is an artifact of describing them in terms of storage instead of in terms of meaning. The generalization: express what each participant may do in terms of the abstract observations it preserves, and the disjointness becomes visible where the raw writes overlapped.

Read-only participation deserves explicit notice because it is the degenerate and most valuable case. A participant with no write authority carries the strongest possible restraint obligation for free, so it needs no argument to be admitted to any group — but it does still inherit the disturbance its neighbours are allowed to inflict, and so must be built to tolerate it. Freedom from having to promise anything is not freedom from having to assume something.

**Source:** [Tentative Steps Toward a Development Method for Interfering Programs](../works/tentative-steps-toward-a-development-method-for-interfering-programs.md) — the parallel treatment of the equivalence-relation example, where the tree-compacting task and the merging task are made to coexist by giving one authority over roots and the other over the interior links, expressed as predicates saying which abstract observations each leaves unchanged; plus the remarks that read-only access carries an implicit no-change guarantee and that a subprogram must nonetheless inherit its caller's rely-condition.
