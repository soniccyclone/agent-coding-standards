---
type: lesson
title: "When two camps both have evidence, look for the variable that makes each one right"
figure: boehm
works: [a-spiral-model-of-software-development-and-enhancement, a-view-of-20th-and-21st-century-software-engineering]
axes: [primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# When two camps both have evidence, look for the variable that makes each one right

**Lesson:** A long-running methodological fight in which both sides can produce successes and both can produce disasters is evidence that the question has been posed wrongly. The competing positions are not rival answers to one question; they are answers to different questions that nobody has separated yet. The productive move is to stop ranking the candidates and instead hunt for the hidden variable whose value decides which candidate is correct. Once that variable is named, the rivals collapse into settings of a single framework, and the argument turns into a diagnosis: not "which method is best" but "which regime is this project in."

Boehm performs exactly this reduction twice, decades apart. First against the process-model wars: a document-heavy sequential order, an incremental evolutionary order, and a specify-then-transform order each turn out to be the right ordering under a specific profile of what is uncertain and what is stable, so one risk-parameterized framework can generate all of them and, more importantly, can tell you which one you are in. Later he does it again for the plan-driven versus lightweight-and-adaptive dispute, mapping each style's home ground in terms of project size, personnel, volatility, and the cost of being wrong, with the middle of that space belonging to hybrids that borrow from both. In both cases the payoff is not diplomatic compromise. It is a genuine reduction in the number of independent things you have to know: one framework plus a selection rule replaces a growing catalogue of mutually hostile methodologies, each with its own vocabulary and its own claim to universality.

This is worth recognizing as a general intellectual maneuver, because it applies well beyond process. Two idioms, two data layouts, two consistency models that each have partisans and each have graveyards are asking to be re-described as points in one space with an axis nobody has drawn. Finding that axis is more valuable than winning the argument, and it is the only outcome that leaves the next person with less to memorize rather than more.

A programmer who thinks this way is slow to enlist in methodology camps and quick to ask what would have to be true for the other side to be right. When they see a strong claim of universality, their reflex is to look for the conditions the claim silently assumes, because those conditions are the missing axis.

**Source:** [A Spiral Model of Software Development and Enhancement](../works/a-spiral-model-of-software-development-and-enhancement.md) — the evaluation section listing the risk profiles under which the framework becomes equivalent to each of the earlier process models it was meant to replace. [A View of 20th and 21st Century Software Engineering](../works/a-view-of-20th-and-21st-century-software-engineering.md) — the treatment of agile and plan-driven home grounds and the argument for value- and risk-based tailoring between them.
