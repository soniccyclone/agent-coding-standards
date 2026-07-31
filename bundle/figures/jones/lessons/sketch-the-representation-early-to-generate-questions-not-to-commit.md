---
type: lesson
title: "Sketch the representation early to generate the questions, not to commit to the answer"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Sketch the representation early to generate the questions, not to commit to the answer

**Lesson:** Writing down precisely what a loosely worded requirement means flushes out a first batch of questions — which cases count, what the boundaries are, what the output should contain. That batch is not the whole set. A second batch exists that the abstract statement cannot produce, because those questions are only meaningful once something has been decided about how the data will actually be held: whether a group can be empty when groups are marked by separators, whether an item may span a physical boundary, what happens at the last one. Nobody can ask them from the abstract level, so if you go to the user with only the first batch, you will be back.

The move that follows is easy to state and cuts against the instinct to defer. When it genuinely matters to settle everything before development starts — a firm-price contract, a user you get one meeting with, a regulated interface — sketch a candidate representation early, on purpose, and write down how it would be read as the abstract thing. You are not choosing it. You are using it as an interrogation device: every place the reading is undefined or ambiguous is a question about the requirement that had been hiding underneath the representation decision, and now you can take it to the person who can answer it. Having harvested the questions you are free to discard the sketch and choose differently later.

What makes this safe rather than a violation of staying abstract as long as possible is keeping the two purposes distinct in your own head. A representation adopted as a commitment constrains everything below it and should be delayed. A representation written to see what it exposes commits nothing and can be thrown away in an hour. The general habit: when you cannot get any more questions out of the level you are working at, drop one level speculatively and read off the questions that appear there — then decide, separately, whether you are ready to make that level real.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 21's specification section for the telegram analysis problem, immediately after the enumeration of interpretations forced by the natural-language original: the observation that if it were necessary to resolve all questions about the specification before proceeding, the representation could be brought in at that point and its relationship to the abstraction documented by a retrieve function, that this is how the problem was tackled in the earlier published treatment, and that the process exposes the questions about the specification which concern the representation — with the chapter itself then choosing to develop the data structure later, alongside the interpretations it forces.
