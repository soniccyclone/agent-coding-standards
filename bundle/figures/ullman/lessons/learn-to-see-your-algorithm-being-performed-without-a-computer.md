---
type: lesson
title: "Learn to recognize your algorithm being performed without a computer"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Learn to recognize your algorithm being performed without a computer

**Lesson:** During a nineteenth-century cholera outbreak, a physician marked each case on a street map of the city. The marks fell into groups around particular road junctions, those junctions turned out to be the sites of wells, and the people who drew water from them were the people falling ill. The author's judgment is unhedged: without the ability to group the data this way, the cause would not have been found. No computing machinery was involved, and the procedure is nonetheless exactly the grouping algorithm the book spends a chapter on — points in a space, proximity, and a summary of each group.

The lesson is about what a technique's identity actually consists of. It is not the code, not the library, not the machine — it is the operation on the data. Once that is clear, two useful things become possible. You can recognize your methods being carried out by people, on paper, in domains that never used the vocabulary, which is the cheapest available source of validation that the method is sound rather than merely fashionable: a procedure that repeatedly proved itself by hand before anyone automated it is a procedure with evidence behind it. And you get a genuine account of what automation contributes, which is scale and speed and nothing else. The physician's insight did not require a computer; a city of ten million cases would have.

That second point cuts both ways and is worth stating plainly. If the technique works by hand at small scale, then a failure of your automated version is a failure of engineering, not a limit of the method, and looking for the analogous manual procedure is a fast way to tell which you are facing. Conversely, if you cannot describe how a person would perform your analysis on a hundred rows with a pencil, that is evidence you do not yet understand what your code is doing — the description is a comprehension test, and failing it usually means the operation on the data has not been separated from the machinery implementing it.

The reflex, then, is to keep asking of any method: what is the pencil-and-paper version, who did this before it had a name, and what exactly did the computer add. The answers keep the technique's essential content distinct from its implementation, which is what lets you carry it to a new domain, judge whether it has real support, and notice when an impressive pipeline is doing something a map and a pen would have done.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 1's example of clustering, which recounts John Snow plotting cholera cases on a map of London entirely without computers, the cases clustering around road intersections that were the locations of contaminated wells, with people living nearest those wells falling ill while those nearer uncontaminated wells did not, and concludes that without the ability to cluster the data the cause of cholera would not have been discovered.
