---
type: lesson
title: "Build a theory of your data structure separately, so arguments about algorithms stay about algorithms"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference, systematic-software-development-using-vdm]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Build a theory of your data structure separately, so arguments about algorithms stay about algorithms

**Lesson:** Explanations of algorithms over nontrivial structures tend to be muddy for a diagnosable reason: most of the reasoning is not about the algorithm at all. It is about the structure — what stays true when a link is redirected, which elements are reachable from which, when a traversal is guaranteed to stop. Mixed into the algorithm's argument, this material buries the two or three steps that are actually specific to the algorithm. Extract it. Give the structure its own named concepts and its own body of established facts, developed once and cited thereafter, and what remains of the algorithm's justification is short and about the algorithm.

The right level of investment is more than most people expect. You want the concepts chosen for how often they let you avoid restating something, the facts stated in the general form rather than the form the current algorithm needs, and the legality condition on the structure written down explicitly so that the totality of your basic operations is a consequence of it rather than a separate worry each time. The payoff compounds: a second algorithm over the same structure inherits the whole body, a variant of the first algorithm re-uses most of it, and someone reading either can check the algorithm-specific reasoning without also checking the structural reasoning.

This is also the mechanism by which a body of knowledge accumulates instead of evaporating. Individual projects that reason from first principles each time leave nothing reusable behind, so the next project starts where the last one did; projects that factor out structural theories leave assets. Treat the choice of which concepts and lemmas to name as engineering work with the same standing as choosing interfaces, because it determines whether your discipline has a literature or merely a history.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the objects-and-properties section of the data-refinement chapter, whose stated motivation for developing theories of data types is to avoid starting each proof from scratch and to build an engineering literature, and whose forest theory is explicitly credited to dissatisfaction with existing proofs of a tree-merging algorithm that were clouded by structural results having nothing to do with the algorithm; also the general-refinement section, which extends the ambition to reusable results about refinement steps themselves. Also [Systematic Software Development Using VDM](../works/systematic-software-development-using-vdm.md) — the theories-of-data-types section, which recommends investigating the properties of every new class of object as it arises, and whose closing admission that its own worked theory was extracted from a first attempt at a specification rather than designed in advance is the useful practical note: theories are harvested from work in progress, not planned ahead of it.
