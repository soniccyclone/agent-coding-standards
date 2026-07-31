---
type: lesson
title: "A delimiter drawn from the alphabet buys itself a transformation at both ends"
figure: wirth
works: [project-oberon]
axes: [primitive-count, verifiability, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# A delimiter drawn from the alphabet buys itself a transformation at both ends

**Lesson:** When a stream has to be divided into units, the boundary marker has to come from somewhere, and there are only two places. Either it is carried outside the data — a separate signal, a length agreed in advance, a distinct channel — or it is a value from the same alphabet the data is drawn from. The second is almost always the cheaper-looking option, because it needs no extra apparatus, and it always incurs the same debt: the marker's pattern must now be impossible inside the data, and the data does not naturally honour that. The cost is not avoided, only relocated into a pair of mutually inverse transformations, one applied on the way out and one on the way in, whose sole job is to guarantee that the reserved pattern never arises by accident.

The design decision is therefore not "which character shall the delimiter be" but "what am I willing to pay to make it unambiguous". Paying with an escape convention is paying in expansion — the encoded form is longer than the original by an amount that depends on the data, so the transformation is not size-preserving and any downstream reasoning about length must happen on the correct side of it. Paying with an out-of-band signal is paying in coupling: the receiver now needs a facility the medium may not offer, and the format stops being self-describing when copied into some other container. The one payment you must not accept is a promise that the pattern will not occur, since a promise about data is not a property of data, and the first input that breaks it produces a framing error whose symptom appears arbitrarily far from its cause.

What makes this worth deciding deliberately is that the transformation pair is exactly the kind of thing that gets pushed down until nobody remembers it exists. Done well, it is invisible and belongs entirely to the boundary layer: the layer above hands over arbitrary values and gets them back unchanged, and the encoding is not visible in any interface. That invisibility is the goal, but it has a precondition — the transformation and its inverse must be genuinely inverse for every input, including the pathological ones consisting entirely of the reserved pattern, and this is a property somebody must actually establish rather than assume. Wherever the pair is implemented, the honest description of the layer is: it costs a bounded expansion and a matched pair of passes, and in exchange the framing is self-contained and needs nothing from the medium.

**Source:** [Project Oberon](../works/project-oberon.md) — section 9.3's account of the synchronous packet format, where the start and end of a packet are marked by a flag consisting of a fixed run of one bits, which forces that run never to occur in the data section, and the problem is resolved by the transmitter inserting an extra bit after each shorter run and the receiver removing it again, with the pre- and post-fixing of flags and the insertion and deletion performed by the interface hardware; contrasted in the same section with the point-to-point line, where framing is carried per byte instead.
