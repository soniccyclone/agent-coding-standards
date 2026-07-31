---
type: lesson
title: "An encoding's regularity decides whether its producer can be a pipeline"
figure: wirth
works: [project-oberon]
axes: [hardware-affinity, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# An encoding's regularity decides whether its producer can be a pipeline

**Lesson:** An encoding is usually judged by what it can express and how densely, and occasionally by how fast it decodes. Both of those questions are asked from the consumer's side. There is a third question, asked from the producer's side, that predicts far more about the total cost of the encoding across everyone who will ever generate it, and it has two independent parts.

The first is whether the choice dimensions are independent. If every option along one axis combines with every option along another — every way of naming an operand usable with every operation — then a producer's case analysis is the *sum* of the axes: handle operations, handle operand forms, done. If instead certain combinations are illegal or special-cased, the analysis becomes the *product*, plus a table of which combinations are permitted, plus the fallback path for the ones that are not. The difference compounds: under independence, adding one option along either axis adds one case, and under interaction it adds a row or a column. This is why regularity in an encoding is not an aesthetic preference — it is the difference between a producer that grows linearly with the encoding and one that grows quadratically.

The second is whether the layout keeps each logical part contiguous. If the parts appear in the order a producer naturally computes them, the producer can emit as it goes, holding nothing. If the layout interleaves fields belonging to different logical parts — some of each part in a shared prefix, the rest distributed later in an order unrelated to how they were derived — then nothing can be emitted until every part has been computed in full. That forces an explicit type for "a part, encoded, not yet written," a routine that produces one from the abstract description, and a second phase that writes them in the layout's order. None of that machinery is doing any useful work; it exists solely because of where fields were placed. The uncomfortable part is that the placement was probably chosen to help the consumer, and the cost fell on a side nobody was measuring. When you define a format, generate one before you fix it, and see whether the generator came out as a pipeline or as a two-phase assembler.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.8's summary of the NS-32000 instruction formats, which notes the architecture's commendable regularity in that all addressing modes are equally applicable independent of the particular instruction; and the section's closing remark on code generation for two-address instructions, which explains that because the address specifiers of both operands are contained in the basic instruction bytes and both index bytes precede all displacements, it is impossible to emit an operation code and then follow it with the two operands, so all parts of both operands' specifications must be available before any emission takes place — hence the use of two local variables of an encoded-operand type computed before the basic instruction bytes are emitted — and the accompanying observation that the prescribed instruction format is not exactly the optimal choice.
