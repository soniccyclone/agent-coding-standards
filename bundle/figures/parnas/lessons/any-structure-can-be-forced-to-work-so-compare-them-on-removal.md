---
type: lesson
title: "Any structure can be forced to work, so compare structures by what comes out cleanly"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Any structure can be forced to work, so compare structures by what comes out cleanly

Arguments about which decomposition is better usually proceed as though one of them might fail to deliver the required behavior. None of them will. Parnas states the deflating fact plainly: any design can be bent until it works. Given enough effort every candidate structure ends up computing the right function, which means functional adequacy carries no information when choosing between them and cannot be the thing the argument is about. His conclusion is harder than it first sounds — if you genuinely do not care which reduced systems can be assembled from your parts, then it does not matter which hierarchy you pick. The choice only acquires content once you have a set of subsets you want to be able to deliver, because ease of taking the system apart is the only respect in which the candidates actually differ.

The comparison becomes concrete when you ask what removal costs under each shape. Take a component out of a chain of data transformations and you are left with a hole: the stage before it emits something the stage after it cannot accept, so you must write a new program whose entire purpose is to bridge the gap you created — and you may find the cheapest repair is to leave the redundant stage in and let it process input it has nothing to do. Take an unused extension out of a layered structure and nothing happens, because the levels above it either used it or did not. Same functionality, radically different cost of subtraction, and the difference is visible only if subtraction is one of the things you are measuring.

This is also why the pipeline shape is so persistent and so misleading. Thinking in processing steps is how everyone learns to program and it matches how goals are stated, so it feels like the natural decomposition, and it produces a structure whose parts are individually sensible and collectively welded together. The discipline is to run the removal test before committing: for each part, name what would have to be written if a customer did not want it. If the answer is a conversion program, you have found the seam that will make every future configuration expensive, and you found it while it was still cheap to move.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — the closing remark that any design can be bent until it works and that hierarchies differ only in ease of decomposition, the summation's contrast between omitting an unneeded virtual machine facility and removing a box from a flow chart, and the earlier analysis of a chain of data transforming components with its sorting example.
