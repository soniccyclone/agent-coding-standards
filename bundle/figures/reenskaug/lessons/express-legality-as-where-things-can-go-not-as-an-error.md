---
type: lesson
title: "Express legality as where things can be placed, not as an error after they are"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Express legality as where things can be placed, not as an error after they are

**Lesson:** The authoring tool in this system carries a two-sided guarantee: its user can construct every permissible arrangement, and cannot construct anything else. What makes it interesting is the mechanism, which is not validation. The structure being edited shows explicit insertion points, and each insertion point offers only the additions that are legal at that position. Legality is therefore expressed as the presence or absence of a place to put something, and the illegal arrangement is never composed, never submitted, and never rejected — it simply has nowhere to be typed.

Compare the ordinary approach, where the user builds something and a checker reports what is wrong. That arrangement has three costs which the positional one avoids entirely. The user invests effort in a construction that turns out to be void, so the cost of the mistake scales with how long they worked before checking. The rules exist in two places — the editor that permits anything and the validator that knows what is actually allowed — which is a divergence waiting to happen. And the rules are only discoverable by violating them, so learning the system means accumulating a private list of things that got rejected, rather than reading what is available. Positional legality collapses all three: one description of the rules, consulted at the only moment it matters, presented as options rather than as prohibitions.

The two-sidedness deserves emphasis because it is easy to deliver half of it. A tool that prevents everything questionable is trivially safe and useless, and a user who cannot express something legitimate will produce it outside the tool where none of the guarantees hold — which is worse than the illegal state you prevented, because now it is also unmodelled. So completeness over the legal space is not a nicety alongside the restriction; it is what makes the restriction survivable, and the claim to check is that both halves hold rather than just the one that is easier to demonstrate.

The requirement this imposes is that the rules be declarative and machine-readable, since the interface must compute what is offerable at each position rather than having it hand-written. That cost is what buys the property, and it is the reason the approach shows up in schema-driven editors, typed structural editors, and configuration systems built over a grammar — and is absent wherever the rules live only in a validation routine. The general reflex: when you find yourself writing an error message, ask whether the state that triggers it could have been unofferable instead.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 12 section 12.4, which describes the intelligent editor for the Service Contract Document as permitting the Service Provider to create any and all permissible service variants while automatically preventing illegal combinations, with small black triangles marking insertion points that indicate where objects may be inserted and that only permit new objects appropriate at that point in the structure as specified in the OOCS Schema; and section 12.5's statement that the tools will ensure he can create any legal service specification and none other.
