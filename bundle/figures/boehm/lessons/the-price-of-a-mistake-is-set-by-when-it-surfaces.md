---
type: lesson
title: "A mistake's cost is set by when it surfaces, so buy discovery early"
figure: boehm
works: [software-engineering-1976, a-view-of-20th-and-21st-century-software-engineering]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A mistake's cost is set by when it surfaces, so buy discovery early

**Lesson:** The intuitive model of a defect is that it has a fixed size: a wrong assumption is a wrong assumption, and fixing it costs what it costs. The measured reality is that the same wrong assumption becomes dramatically more expensive the further downstream it is caught, and the growth is not linear. A misunderstanding corrected while it is still a sentence in a discussion costs minutes. The same misunderstanding corrected after structure, code, tests, documentation, and downstream dependents have been built on top of it costs orders of magnitude more, because the fix is no longer the change itself but the change plus everything that has to be re-derived around it. Boehm did not argue this from first principles; he collected the curve from several large organizations and found the same shape in all of them, with the steepness increasing with project size.

Once you accept the curve, a lot of apparently reasonable behavior turns out to be economically backwards. Effort spent making a target explicit early is not overhead delaying the real work; it is buying error discovery at the cheapest point on the curve. Time saved by skipping that clarification is borrowed at a punishing interest rate. The reason the curve is so steep is worth naming: a late fix requires reasoning about the mistake in the presence of everything built since, so the amount of context a person must hold to change it safely grows with the accumulated structure. The defect stays the same size; the surface it is embedded in does not.

The same data also warns against the naive reading of it. Boehm points out that projects hearing "test is expensive" often draw the opposite lesson and rush into implementation, reasoning that since debugging will dominate anyway, one may as well start generating things to debug. And the honest extension is to stop treating early discovery as sufficient: the higher-value move is preventing whole classes of mistake by asking why the last one was possible, rather than merely catching each instance sooner.

A programmer who has internalized the curve spends real effort on cheap, early, low-status activities: getting a contested definition pinned down, writing the awkward question down before writing code, standing up the thin end-to-end skeleton that would expose an integration mismatch now instead of in three months. They are also unmoved by the argument that a clarification can wait, because they know the wait multiplies the bill.

**Source:** [Software Engineering](../works/software-engineering-1976.md) — the argument for the criticality of requirements work, built on the cross-organization cost-to-fix-by-phase comparison and the accompanying data on which phases most defects originate in. [A View of 20th and 21st Century Software Engineering](../works/a-view-of-20th-and-21st-century-software-engineering.md) — the 1970s section revisiting the same curve across several organizations with project size as a parameter, and the per-decade principle list where eliminating errors early is paired with root-cause prevention.
