---
type: lesson
title: "A fit expires where its prediction falls below the quantum of the thing measured"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# A fit expires where its prediction falls below the quantum of the thing measured

**Lesson:** A continuous law fitted to a discrete quantity carries a boundary that no goodness-of-fit statistic will report: the point at which its prediction drops below one unit of whatever is being counted. Predicting a hundredth of a book sold, a third of a page, or two-tenths of an inbound link is not a small error to be tolerated. It is the model producing a value the domain cannot express, which means you have left the region where the model means anything and the true curve must be doing something else there — flattening, truncating, or dropping to zero. Read that crossing point off the arithmetic and you have the model's domain of validity for free, without any data from the region in question.

This is worth building as a reflex because the standard diagnostics point the other way. A relationship fitted in log-log space is dominated by the head, where the observations are dense and large, and a fit can look excellent while being badly wrong across the entire tail, which is usually where you wanted to use it. Residuals will not flag it, because there are few observations out there and each one contributes little. So the check has to come from the units rather than from the statistics: extrapolate to the far end of the range you intend to apply the model over, and ask whether the number that comes out is a thing that could exist. When it is not, you have learned that the real curve departs from your law somewhere earlier, and any decision that relied on the tail — inventory depth, cache sizing, how far down a ranked list is worth serving — was resting on an artifact.

The exponent deserves the same treatment as the extrapolation. A slope chosen because it makes a picture legible, or because it fell out of two convenient points, is a slope nobody has checked against the domain, and slopes on log scales are ferociously consequential: a modest change in the exponent moves tail predictions by orders of magnitude. The habit worth copying from careful writing here is the explicit label. When an author presents a fitted parameter and says in the same breath that it is steeper than reality and used only because it makes the illustration clean, the example cannot later be quoted as a finding. Unlabeled, the same number gets cited, propagated, and eventually planned against by someone who never saw the figure it came from.

Both checks are instances of the same move: hold a model up against facts about the measured quantity that were never part of the fitting procedure. Indivisibility, nonnegativity, a known total, a physical maximum, a conservation constraint — none of these appear in a least-squares objective, all of them bound where the answer can live, and each one converts into a statement about where your model stops applying. The alternative is discovering the boundary in production, when someone asks the model a question about the tail and it answers with perfect confidence.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 1's power-law section, whose worked example of Amazon book sales by rank notes that the plotted law implies sales of a fraction of a book beyond about rank one thousand, judges that implication too extreme and predicts the real line flattens out there, and separately states that the illustrated slope is probably much too steep to describe book sales even though a shallower line would be close to reality.
