---
type: lesson
title: "Hold back along the axis your data is dependent on"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Hold back along the axis your data is dependent on

**Lesson:** Setting aside part of your evidence to check an artefact against is standard practice, and the standard implementation — pick a random subset — carries a precondition that is stated far less often than the practice itself: the observations must be independent of one another. When they are not, a random split puts observations on both sides of the line that are informative about each other, and the held-back portion stops being a stand-in for the unseen. It becomes a set of cases the artefact has effectively already been told the answers to, through their neighbours, and the check it provides is worthless in a way that flatters you.

The clearest instance is anything with an order in which earlier entries carry information about later ones. Take a random sample out of the middle and you have handed the fitting process observations from after each held-back point, which in deployment it will never have. The measurement then reports how well the artefact does when it can see the future, which is not the question. The correction follows directly from the dependence: hold back a contiguous piece from the end, so that the split reproduces the situation of actual use — everything before is known, everything after is not.

The general rule is that the split has to cut along whatever axis creates the dependence, and to identify that axis you have to ask what the artefact will be missing when it is used for real. If it will meet users it has never seen, split by user rather than by observation, or you will be evaluating on new observations of familiar users. If it will meet new locations, new tenants, new devices, split by those. Random splitting is not a neutral default; it is the correct choice for exactly one dependence structure, the one where there is none.

The reason this deserves attention out of proportion to its difficulty is that getting it wrong produces no error and no warning. It produces a number that is too good, in a direction that everyone involved was hoping for, and the mistake is only discovered in deployment, where the true performance is available for the first time and is much worse than the figure everyone had been planning against.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the regularization chapter's discussion of splitting available data into training and test portions, which states that points may be chosen at random for the test portion on the assumption that data points are independent of one another, and immediately warns that in sequence-learning problems such as time series the state at any point encodes information about the past, so the final piece of the sequence makes a better test set.
