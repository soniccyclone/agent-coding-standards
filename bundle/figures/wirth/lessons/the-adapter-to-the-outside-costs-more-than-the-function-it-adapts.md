---
type: lesson
title: "The adapter to the outside world costs more than the function it adapts"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# The adapter to the outside world costs more than the function it adapts

**Lesson:** A mechanism designed among cooperating parts of one system can be small, because both ends were designed together and every representation was chosen for convenience. The moment the same function must also reach something outside — a party that fixed its conventions before you existed and will not change them — the work is not "the same thing plus a translation". It is a second, larger project whose size is set by the outside format's history rather than by the function's difficulty, and the honest expectation is that it will take several times as long as the core it wraps. This is not a failure of estimation technique; it follows from what such formats are. They accumulate cases, ambiguities, and dialects, none of which correspond to anything in your problem, and all of which you must handle because you are the one adapting.

The structural response is to admit the two into the design as different things from the start. The internal mechanism should be defined in terms of its own representation and should not be bent toward the external format's shape in anticipation — that anticipation buys nothing, since the external format will still not fit, and it costs the internal design its simplicity permanently. The translation then lives in its own region, with the outside party appearing to the rest of the system as just another ordinary participant. This is worth doing carefully, because the whole benefit is that the size and messiness of the translation is contained: it can be wrong, replaced, or extended without the core being implicated, and a second external format later is another module rather than another set of cases inside yours.

The estimation consequence deserves stating separately, because it is where projects are lost. When the requirement reads "and also exchange with the standard format", nobody prices it, since it sounds like the tail of the sentence. Price it as the larger half. Then decide deliberately whether it is worth building at all, whether it can be bought or borrowed, and whether it must cover the whole of the external specification or only the part you actually meet — a partial adapter with a written statement of what it does not handle is frequently the right answer, and is only available to someone who separated the two pieces in the first place.

**Source:** [Project Oberon](../works/project-oberon.md) — section 11.2's account of the mail server in service at ETH, which connects to an external mail server treated as a source and sink for messages almost like other customers, with messages sent to it requiring encoding into a standardized format and those received requiring corresponding decoding; and the accompanying disclosure that, although the encoding and decoding parts are not described in the book, their design and implementation took a multiple of the time spent on the fast local message exchange to which the presentation is confined.
