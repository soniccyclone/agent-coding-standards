---
type: lesson
title: "A difference a free parameter can absorb is not a difference"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [foundations-of-computation, algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A difference a free parameter can absorb is not a difference

**Lesson:** Two operations can differ by a rearrangement — a reversal of order, a transposed index, a sign convention, a relabelling — and the difference can matter enormously or not at all, depending on where the operands come from. If one operand is given to you, the rearrangement changes the answer and the two operations are genuinely distinct. If that operand is instead something the system determines for itself, the rearrangement changes nothing anyone can observe, because whatever the system would have determined under one convention it will determine, pre-rearranged, under the other. The distinction survives in the mathematics and evaporates in the implementation. Recognising which situation you are in saves an argument that cannot be settled, since neither side can exhibit a case where the choice shows.

The practical rule is to check, before disputing a convention, whether anything downstream of it is free. Index order in a symmetric structure, the sign of a basis element, the direction of an edge in a graph whose weights get fitted, the byte order of an identifier nobody compares across systems: in each case, if the consumer adapts to whatever it is handed, the convention is not carrying information and the discussion is about spelling. The energy belongs on the conventions where something fixed sits on the other side and cannot adapt.

The cost of the evaporated distinction is paid in vocabulary. A name that was correct for the original operation gets kept for the rearranged one, because the two are interchangeable in the setting where the name was adopted, and it then travels to settings where they are not. Anyone who comes to the system already knowing the named operation will import its identities, its symmetries, and its literature, and some of those imports will be false of the thing actually implemented. So the same observation that makes the argument pointless makes a note in the documentation mandatory: state plainly that the implemented operation is the rearranged one and that the name is inherited by resemblance. That costs one sentence and forestalls a class of confident, wrong reasoning.

There is a converse worth holding onto. The freedom that absorbs a difference is itself a resource, and it can be spent deliberately. If two formulations differ by something a fitted or configured component can compensate for, you may choose between them purely on grounds the formulations were never about: which one is cheaper, which one indexes more conveniently, which one the available library already implements. Establishing that the choice is unobservable is what licenses picking on those grounds without further justification.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 13's short subsection on convolution and cross-correlation, which works out that what a convolutional layer computes is the convolution of the input with a flipped kernel, equivalently the cross-correlation of the input with the filter, notes that the resemblance to the convolution operation of signal processing and probability theory is the reason for the layer's name, and lets both the name and the filter-versus-kernel terminology stand.
