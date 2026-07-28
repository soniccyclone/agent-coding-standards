---
type: lesson
title: "Describe a component as an observable device, not as a sequence of steps"
figure: parnas
works: [a-technique-for-software-module-specification-with-examples]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Describe a component as an observable device, not as a sequence of steps

**Lesson:** Ask a programmer to explain a component and you get a narrative: first it does this, then it checks that, then it updates the table. The narrative is how the thing was built, so it feels like the truth about it, but it is a description of a process and it tells a client both too much and too little — too much because the client inherits internal steps he cannot use, too little because it never states what the client is actually entitled to observe. The alternative is to stop describing activity and describe an apparatus: a set of inputs that can be actuated and a set of quantities that can be read, together with what actuating each input does to what can be read. Behavior becomes a relation over observables rather than a story about time.

The reason this is more than a stylistic swap is that it forces a specific and checkable claim: everything a client can observe must be determined by the previous observable values and the input actuation. If the specification needs to appeal to some quantity the client cannot read in order to predict what he can read, the component is not describable this way — and rather than reaching for the extra machinery, treat that as evidence against the design. Hidden state that leaks into observable behavior is precisely the property that makes a component impossible to reason about from outside, and the notation refusing to express it comfortably is the notation doing its job.

The discipline also changes what the description omits. Once you are stating relations among observables, you naturally state only relations — this quantity does not exceed that one, these items are all present, this lookup inverts that one — and you never have to name a representation, because representations are not observable. A specification written this way admits implementations the author never imagined, including ones that invert the expected division of labor entirely: work the narrative version would put in a setup pass can be moved into the individual read operations, or vice versa, without any client noticing, because "when the work happens" was never something the client could observe.

Expect resistance, including your own. People with years of programming behind them find it unnatural to treat a program as a static object rather than as a thing that makes decisions in sequence, and first attempts reliably fail. The pull back toward narrative is strong and worth naming when you see it. Be honest about the limits too: this framing fits components that are actuated in small increments, and fits badly where a client hands over one large artifact and wants to know nothing about the internal progression through it — a translator, for instance. Knowing which shape you are dealing with is part of the skill.

**Source:** [A Technique for Software Module Specification with Examples](../works/a-technique-for-software-module-specification-with-examples.md) — the framing of a module as a device with input switches and readout indicators, the insistence that indicator values be determined by prior indicator values and switch positions (with the aside doubting the wisdom of devices needing unreadable indicators), and the closing hesitations about resistance and about large-unit inputs.
