---
type: lesson
title: "The simple picture is a deliverable someone owns, and that someone is not in the picture"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# The simple picture is a deliverable someone owns, and that someone is not in the picture

**Lesson:** The clean diagram of a supply structure is a stack: each layer consumes what the layer below produced. Reality is an acyclic graph — each participant draws on several suppliers, who are shared, and the author says outright that his own tidy figure was made into a tree by cheating. The instinct at that point is to redraw honestly and accept the mess. He does the opposite, and the reasoning is the useful part: the linear chain is retained deliberately, because the point of the structure is that people should work in one coherent environment fitted to them, and that requires *someone whose job is to produce the linear appearance* by integrating products from several vendors into what presents as a single layer.

So the simplifying abstraction stops being a description and becomes a deliverable with an owner. That reframing has consequences a diagram cannot. It says the illusion of coherence is legitimate work rather than self-deception, it says the work is skilled — choosing technologies per layer, specifying processes, installing and integrating facilities — and it says that where nobody holds that responsibility, every consumer performs the integration themselves, badly and repeatedly, which is the normal condition of a team assembling its own toolchain from parts.

The role was discovered rather than designed, and how it surfaced is worth keeping. The team had assumed each layer would supply the facilities for the layer above, which is the natural reading. Then a project member asked what *their* role was: they were not part of the chain, yet they were designing and implementing it. The model had no place for the people building the model. That question is a general diagnostic — when a structure you have drawn has no slot for the people who drew it, the missing slot is a real role, and leaving it unnamed means the work still happens but is unaccounted, unstaffed, and unfunded.

Two further consequences follow. Where consumers dislike dealing with many suppliers while producers must specialize to be any good, the resolution is not for producers to broaden but for a distinct party to specialize in integration — a market position, not a compromise. And this role remains available even where you control almost nothing: no single organization owns every layer, but you can still identify your own segment, name who supplies you and whom you supply, and organize the part you hold.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 10 section 10.1, which shows the value chain as a linear list, then a tree, then admits real chains are acyclic directed graphs and that the tree figure was made by cheating; recounts the project member's question ("But what is our role in this? We are not part of the chain, yet we design and implement it") as the origin of production engineering; states that production engineers should create the illusion of a linear chain even while integrating several vendors' products; and notes the opposing forces of producer specialization against customers' preference for a single vendor.
