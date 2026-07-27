---
type: lesson
title: "When goodness of fit cannot decide between two models, let mechanism, parsimony, and how fast each becomes predictive decide"
figure: lehman
works: [metrics-and-laws-of-software-evolution-the-nineties-view]
axes: [primitive-count, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# When goodness of fit cannot decide between two models, let mechanism, parsimony, and how fast each becomes predictive decide

**Lesson:** Two candidate descriptions of the same growth history can be statistically indistinguishable on the data you have. That is a common situation and not a dead end, because fit is only one of several criteria and not the most informative one. Three others do real discriminating work. First, whether the model's form corresponds to a mechanism you have independent reason to believe: a growth rule whose increment shrinks as the system gets larger encodes the claim that accumulated complexity acts as a brake, which is exactly what independent observation says happens. Second, how many free parameters it needs, and whether those parameters mean anything: a description with one parameter that can be read as the roughly constant work the organization actually sustains is a stronger claim than a description with more parameters that mean nothing in particular. Third, plain plausibility of the model's asymptotic behavior — a rule that says growth continues linearly forever is refuted by nothing in the dataset and by everything in experience.

The fourth criterion is the sharpest and the least used. Instead of asking how well a model fits the data it was fitted to, ask how much of the beginning of the history you need before the model's parameters stop moving and its predictions stabilize. Fit parameters from the first two points, then the first three, and watch the error settle. A model that stabilizes after a handful of releases and stays there is telling you something a fit statistic cannot: that the phenomenon has a strong, early-established character. That is simultaneously a claim about the model and a claim about the world. In the case studied here, the growth character of a real system was essentially fixed within its first several releases, which says the system's own dynamics assert themselves early and thereafter dominate the intentions of anyone steering it — the system comes to manage its managers rather than the reverse, at the level of long-run trend if not of any individual decision.

There is a discipline of restraint that goes with this. Both candidate models here describe only the smooth trend and say nothing about the oscillation around it, and the honest move is to say so rather than to quietly claim the oscillation as explained. Whether that residual is noise from thousands of local decisions or the visible signature of the feedback control that produces the trend is a separate question requiring separate work — and admitting which parts of your data your model does not address is what makes the parts it does address believable. In the same spirit, points that do not fit get pointed at and left uninterpreted rather than explained away.

A modeller who works this way stops shopping for the curve with the best correlation coefficient, and starts asking what each term in a candidate model would have to mean, how few knobs it needs, and how early it becomes predictive. Those questions are answerable from small datasets, which is fortunate, because in this domain small datasets are all there ever is.

**Source:** [Metrics and Laws of Software Evolution - The Nineties View](../works/metrics-and-laws-of-software-evolution-the-nineties-view.md) — the sections comparing a linear least-squares fit against the inverse-square growth model on the same release history, including the list of conceptual reasons for preferring the latter and the error-of-fit-versus-number-of-points analysis used to gauge how quickly the system's dynamics become established.
