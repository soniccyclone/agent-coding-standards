---
type: lesson
title: "Keep tools commensurate with the product, and read the tool you need as a measurement of your design"
figure: wirth
works: [from-programming-language-design-to-computer-construction]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Keep tools commensurate with the product, and read the tool you need as a measurement of your design

**Lesson:** A tool should be as simple as possible and no simpler, where the scale is set by the product and not by the state of the art. The failure to watch for is a tool that becomes a project of its own: when a substantial share of the total effort goes into mastering, tuning, or debugging the apparatus rather than the thing being built, the apparatus is now a net cost even if it is technically superior in isolation. Sophistication has an acquisition price, and that price is paid in the same currency — attention, calendar time, the ability to hold the whole undertaking in mind — as the actual work. So the right question about a general, powerful mechanism is never whether it is better in the abstract, but whether the increment of power it delivers on this problem exceeds what it costs to keep it running.

The sharper move is to notice that tooling requirements are not fixed inputs. Substantial effort can go into general table-driven bottom-up analysis machinery, and then the same designer can retreat to plain recursive descent and lose nothing — because he also controls the grammar, and a syntax chosen with the parser in mind is comfortably within reach of the simple method. The heavy machinery existed to absorb an arbitrariness that did not have to be there. Whenever a tool is straining, ask whether the difficulty lives in the problem or in a gratuitous choice made upstream, and whether that choice is still yours to make. Simplifying the input is usually cheaper than industrializing the process, and it removes the complexity rather than relocating it.

Read in reverse, this makes instrumentation a diagnostic. A hardware project taken through to working silicon on essentially an oscilloscope, with a logic analyzer needed only rarely, is telling you something specific about the processor: it was built to a systematic concept without tricks, so its behavior at any point is derivable rather than discoverable. A design that can only be understood through elaborate observation is a design whose internal structure does not explain itself. That is why escalating tool sophistication deserves suspicion before admiration — the need for a more powerful instrument is often evidence about the artifact rather than about the ambition of the work. The corollary for the builder is that investment in making the thing regular pays a second time, as tooling you never have to acquire.

**Source:** [From Programming Language Design to Computer Construction](../works/from-programming-language-design-to-computer-construction.md) — the closing passage on choice of tools: a tool being commensurate with the product and counterproductive when mastering it consumes the project, the switch from table-driven bottom-up syntax analysis back to recursive descent given a wisely chosen syntax, and the Lilith hardware being developed with only a good oscilloscope thanks to a trick-free processor concept.
