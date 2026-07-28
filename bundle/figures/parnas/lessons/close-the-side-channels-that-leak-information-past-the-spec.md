---
type: lesson
title: "Close the side channels through which knowledge reaches a client without passing through the specification"
figure: parnas
works: [a-technique-for-software-module-specification-with-examples]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Close the side channels through which knowledge reaches a client without passing through the specification

**Lesson:** Concealing an implementation is not achieved by declining to describe it. Information about how something works reaches its clients through routes nobody audits — a suggestive name, a regularity in returned values that the description never promised, the shape of the parameters, an example that shows one plausible realization. Any of these lets a client form correct beliefs that the specification does not underwrite, and once those beliefs are load-bearing the boundary has failed even though every written word of it is intact. Hiding is therefore an active discipline about all channels, not a passive one about the main channel.

Two of the countermeasures are counterintuitive enough to be worth stating plainly. First, where a description does not need to fix a value, do not merely leave it unstated — say that it is chosen arbitrarily and that no regularity in it may be relied on, and state separately the relations those values must satisfy. Clients can then use such a value (store it, pass it back) without depending on what it is, and an implementation is free to make it a link, an index, or anything else. Second, resist mnemonic naming in the formal parts. A name that telegraphs its meaning invites both reader and writer to answer questions from the connotation rather than from the text, which conceals exactly the gaps a review is supposed to find; deliberately unhelpful names, with the intended reading supplied separately in prose, force every question back onto the formalism where it can be checked. The trade is real — the description becomes harder to read on first pass — and the point is that ease of first reading was buying the wrong thing.

The same reasoning applies to examples, which are the most underestimated leak. A specification that happens to admit one obvious realization will be assumed to have that realization, and clients will quietly rely on properties only that realization has. It is worth noting explicitly when the obvious reading is not the one used, and worth accepting that limits expressed in terms convenient for one candidate implementation are a compromise: they buy usability at the cost of hinting at a structure, and may even under-report real capacity. Making that trade knowingly is different from making it by default.

A programmer who works this way reviews an interface by asking not "what does this say" but "what will a client end up believing," and treats the gap between the two as the actual defect list.

**Source:** [A Technique for Software Module Specification with Examples](../works/a-technique-for-software-module-specification-with-examples.md) — the treatment of incompletely defined functions whose values are arbitrary and whose necessary relations are stated explicitly, the footnote arguing against high-mnemonic-value function names, and the remarks on the storage example about an apparent obvious implementation that was never actually used and about parameters chosen in terms of one candidate model.
