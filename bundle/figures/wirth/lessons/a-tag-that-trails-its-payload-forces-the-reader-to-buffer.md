---
type: lesson
title: "A tag that trails its payload forces the reader to buffer"
figure: wirth
works: [project-oberon]
axes: [hardware-affinity, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, distributed-systems-and-networking]
tags: [lesson]
---
# A tag that trails its payload forces the reader to buffer

**Lesson:** When a sequence of elements is to be interpreted according to a discriminator, where that discriminator sits relative to the elements decides whether a reader can work in constant space. Put it first and the reader knows, before the first element arrives, which interpretation applies; it can convert each element as it comes and keep only the accumulating result. Put it last and the reader cannot interpret anything until the end, so it must retain every raw element until the discriminator arrives. The reader's storage requirement has gone from a fixed accumulator to a buffer sized by the longest sequence anyone may write, and a buffer sized by a bound implies a limit, a check, and a decision about what to do when the limit is exceeded. All of that follows mechanically from where one marker was placed.

The placement is usually chosen for the writer's convenience or for how it reads, and those are legitimate concerns — the trailing form is often more natural, since the discriminator is an afterthought qualifying something already written. The point is not that trailing is wrong but that it is not free, and the cost is paid by every reader ever written, in a currency (bounded memory, streaming capability) that the writer never sees. Where the reader is a shared piece of infrastructure and the writers are many, this is a bad exchange rate.

The same shape appears well outside notation: a length or type field at the end of a message rather than in its header, a checksum whose scope is the whole preceding body, a summary record at the end of a file. In each case the leading form permits a reader that decides once and then streams, and the trailing form obliges it to hold everything. When designing the layout, ask what the reader must be able to do before the discriminator arrives; if the answer is "nothing," you have decided to require a buffer, and you should size it deliberately rather than discovering the bound later.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.5's explanation of number scanning, which notes that the digits and letters of a number are first scanned into a buffer because hexadecimal numbers are denoted by a postfix letter rather than a prefix character, and that a further postfix letter specifies that the digits denote a character; together with the scanner's declared maximum digit-buffer size.
