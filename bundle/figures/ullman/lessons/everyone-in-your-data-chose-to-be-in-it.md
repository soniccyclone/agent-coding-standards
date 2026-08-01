---
type: lesson
title: "Everyone in your data chose to be in it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Everyone in your data chose to be in it

**Lesson:** There are two ways to learn what people think of something: ask them, or watch what they do. Asking gets you a rich answer on a graded scale, and it gets it from a population defined by willingness to answer, which is a trait that travels with other traits. The people who file ratings are not a random draw from the people who have opinions, so the distribution you recover is the opinion distribution of respondents, and calling it the opinion distribution of users is a substitution nobody performed deliberately and nobody wrote down. Watching behaviour has the opposite profile: it covers everyone, it needs no cooperation, and it yields a signal with almost no resolution, since a purchase or a view records interest and nothing else. The choice between them is a trade of expressiveness against representativeness, and it should be made explicitly rather than by taking whichever channel was already instrumented.

The same self-selection reappears in miniature, deep inside estimation, where it is much easier to miss. Predicting one unknown value by averaging over the most similar parties who did supply a value means averaging over a small group defined by the fact that they showed up. If that handful happens to consist of enthusiasts, the average inherits their enthusiasm, and you will read it as a property of the thing being estimated. The fix is the same at both scales: subtract each contributor's own baseline before pooling, so that what gets averaged is each contributor's departure from their own habits rather than their absolute level. Then add the target's baseline back. The pooled quantity becomes a statement about relative response, which is far less sensitive to who happened to be in the pool.

The habit worth carrying past this setting is to ask, of every dataset and every aggregate inside a computation, what determined membership. Logs of failures contain the failures someone reported. Support tickets contain the problems of people who contact support. A benchmark suite contains the programs somebody thought were worth submitting. None of these are wrong to use, and all of them are wrong to describe as though the selection had not happened. Writing the selection rule down next to the result costs one sentence and stops the result from being quoted as something broader than it is.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 9's treatment of populating the utility matrix, which notes that users are generally unwilling to supply ratings and that information from those who do may be biased by their very willingness, alongside behaviour-derived data that has only one value; together with the neighbour-averaging discussion in the collaborative-filtering section, which normalizes each of the few similar users who rated the item in question precisely because that small set may consist of habitually high or low raters.
