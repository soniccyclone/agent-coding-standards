---
type: lesson
title: "Judge a technique by how it fails in ordinary hands, not by how it works in expert ones"
figure: boehm
works: [a-spiral-model-of-software-development-and-enhancement, software-engineering-1976]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Judge a technique by how it fails in ordinary hands, not by how it works in expert ones

**Lesson:** A method's demonstration is almost always run by its inventor or by someone equally strong, which means the demonstration measures the ceiling and says nothing about the floor. Boehm insists on evaluating the floor, and he is willing to indict his own method to do it. Judgment-driven work depends on being able to tell a dangerous unknown from a comfortable one. Someone who cannot make that distinction, or who has an incentive not to, produces an artifact with the same surface form and the opposite content: lavish depth on the well-understood parts, hand-waving over the parts that will sink the project, decorated with confident references to capabilities nobody on the team has actually exercised. Both artifacts look like progress. One of them is a project quietly heading for a wall.

The uncomfortable consequence is that flexibility and rigidity trade off in a way that has nothing to do with elegance. A rigid, uniform procedure wastes effort and buries the important questions, but it can be checked by an inexperienced reviewer, because "is every section filled in" is a question anyone can answer. A judgment-driven procedure is far more efficient in good hands and gives an inexperienced reviewer nothing to hold on to. Boehm's own diagnosis of what his framework still lacked is precisely this: guidelines, checklists, and worked catalogues of common risks, which exist for the rigid approaches only because decades of ordinary practitioners accumulated them.

He grounds the point in an unflattering look at who actually writes the software, having found the median practitioner to be modestly trained, thinly experienced, over their head, and under-supervised. His conclusion is not contempt but a design constraint: technique, like the software it produces, has to be matched to the people who will use it, and a method whose correctness depends on the presence of a rare expert is a method with a single point of failure.

A programmer who absorbs this stops asking only "does this work" and starts asking "what does this look like when someone does it badly, and can anyone tell." They prefer constructs whose misuse is visible to constructs whose misuse is silent, they write down the checklists that their own judgment would let them skip, and they treat "an expert can hold this in their head" as the beginning of a design problem rather than the end of one.

**Source:** [A Spiral Model of Software Development and Enhancement](../works/a-spiral-model-of-software-development-and-enhancement.md) — the difficulties section on reliance on risk-assessment expertise, including the inverted-detail failure mode and the illusion of progress it creates. [Software Engineering](../works/software-engineering-1976.md) — the concluding assessment of which problem region existing principles actually cover, and its footnote profile of the typical practitioner with the matching argument it draws from it.
