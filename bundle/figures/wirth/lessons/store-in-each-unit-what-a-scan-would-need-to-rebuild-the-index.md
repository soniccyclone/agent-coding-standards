---
type: lesson
title: "Store in each unit what a scan would need to rebuild the index"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, databases-and-data-management]
tags: [lesson]
---
# Store in each unit what a scan would need to rebuild the index

**Lesson:** An index over a store concentrates risk in proportion to how much it concentrates access. Lose a leaf of it and you lose what that leaf referenced; lose its root and you lose everything, because there is no other route to any of it. The data are all still present and are all unreachable, which is the worst possible arrangement of facts. The defence is not a better index — it is to arrange, in advance, that the index can be reconstructed by brute-force examination of the store, and that arrangement is made in the layout of the individual units, long before anyone needs it.

Two things must be added to each unit, and both are dead weight in normal operation, which is why they get argued away. It needs a fixed constant at a fixed offset so that a scan can decide, without any external information, whether a unit is one of the ones worth collecting. And it needs its own identifying attributes — the name it is known by, the time it was created — even though the working system reads those from the index and never from here. The name is what makes a recovered unit meaningful rather than a numbered blob; the timestamp is what lets the recovery choose between several units claiming the same name, which will happen, because the store retains superseded versions that the index had already stopped pointing at. Redundancy that no normal path reads is the whole point: it is the only kind that survives the loss of the normal paths.

Two honest limits travel with the technique. Recognition by a constant is probabilistic — ordinary content can coincidentally carry the same value at the same offset, so the scan is a heuristic and must be built expecting to be occasionally wrong. And a store whose units are self-identifying does not really forget: if deletion is implemented as a change to the index alone, a scan will resurrect what was deleted, so the recovery restores more than existed. Both are acceptable when weighed against total loss, and neither should be discovered afterwards. State them as the terms of the trade at the moment the redundant fields are added, because they are properties of the design and not defects in the tool.

**Source:** [Project Oberon](../works/project-oberon.md) — section 14.3's account of the Scavenger, which scans the whole disk because a fault in a directory page makes its files and those of descendant pages inaccessible and a fault in the root loses all files; every file header carries a mark field with a fixed constant value, though data sectors may coincidentally match it; the file name is recorded in the header solely for this purpose and otherwise unused by the system; the creation date is needed because several files with the same name may be found; and the noted drawback that deleted files are rediscovered because deletion affects only the directory.
