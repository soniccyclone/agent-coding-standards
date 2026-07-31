---
type: lesson
title: "Attack an intractable problem with a model too small to be fair to it, then add back only what proves necessary"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Attack an intractable problem with a model too small to be fair to it, then add back only what proves necessary

**Lesson:** The standard objection to any disciplined method is that the real problem is far bigger and messier than anything the method's examples address. The objection is usually true and almost never decisive, because it assumes the method has to be applied to the whole problem at once. The alternative is to pick one aspect, build a model of it so simplified that it is plainly unfair to the real situation, and work that model through properly. Do not defend the simplification; it is not supposed to be defensible yet. Its job is to be small enough that the method can actually be carried out on it, which is the only way to find out what the method tells you.

Three things tend to come back from such a model, and only the first is the one people expect. It yields insight about the real problem out of proportion to its size, because the simplification removed the noise rather than the substance. It frequently becomes the frame the real complexity is then hung on, so the detail arrives as elaboration of a structure that is already understood instead of as an undifferentiated pile. And — the outcome worth waiting for — some of the complexity you were sure you would have to add back turns out to be unnecessary, having been an artifact of how the problem was originally framed rather than a property of the problem. That last result is unavailable to anyone who insists on modelling the full situation from the start, because there is nothing to compare the full situation against.

The discipline is in the direction of travel. Start below the real difficulty and add, checking at each addition whether it changes any conclusion; do not start at full fidelity and try to simplify, which never terminates because every detail has an advocate. And treat the small examples in any method's exposition the same way — they are small on purpose, so the idea is not hidden by the example, and the fact that a later example handles something genuinely confusing without looking difficult is evidence about the method rather than about the example being easy.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the preface, which anticipates the reader's problems of far greater scope and complexity than the book's deliberately small examples, and advises starting from a grossly over-simplified version of a selected aspect and gradually adding what appears necessary, noting how often the over-simplified model conveys additional insight, can serve as a structure on which complex detail is later superimposed, and ends by showing some of the additional complexity to have been unnecessary after all.
