---
type: lesson
title: "Prove a construct is missing with a closure property, not with an appeal to symmetry"
figure: hoare
works: [communicating-sequential-processes-paper]
axes: [expressiveness, parallelizability, verifiability]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Prove a construct is missing with a closure property, not with an appeal to symmetry

**Lesson:** Noticing that a notation treats two dual operations unequally — one may appear in a position the other may not — is a useful smell but a worthless argument. Symmetry is an aesthetic preference, and languages are full of deliberate asymmetries that earn their keep. To turn the smell into a finding you need a property the language ought to satisfy that fails without the construct. The strongest available property is a closure claim about the layers of the language itself: whatever a composite form can present to the outside world should also be presentable by some form from the simpler layer. If concurrency is meant to be a structuring device rather than a new semantic universe, then the externally observable behavior of any concurrent composition ought to be reproducible by some single sequential text. That is checkable, and failing it is a real defect rather than an offended taste.

Doing the check properly requires resisting the near miss. The obvious encoding of "offer both of these interactions, in whichever order the world will take them" is to pick an order and perform them in sequence, choosing the order nondeterministically. That looks equivalent and is not, and seeing why is the whole lesson: the encoding commits to an order before learning anything, whereas the composite form commits only when a partner actually engages. The distinction is invisible when you examine the fragment alone. It becomes visible only against an environment whose own internal ordering forces the opposite sequence — two peers arranged so that one cannot interact until the other has. Then the committed version blocks forever and the composite version does not.

Two habits follow. First, when you suspect a construct is missing, look for the counterexample in the *environment* rather than in the fragment, because expressiveness gaps in interaction only show up under composition, and a designer who tests fragments in isolation will conclude everything is already expressible. Second, state the closure property you intend your language to have and keep it as a standing obligation, because it will keep finding gaps: each time a composite form can do something no simpler form can, you have either found a needed primitive or discovered that the composite layer is more than the structuring device you claimed it was.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-paper.md) — the discussion of output guards, where the symmetry observation is set aside in favor of the requirement that every parallel command's externally visible behavior be modelable by a sequential command, and the proposed sequential substitute is refuted by exhibiting two peer processes whose mutual synchronization forces the order the substitute has already committed against.
