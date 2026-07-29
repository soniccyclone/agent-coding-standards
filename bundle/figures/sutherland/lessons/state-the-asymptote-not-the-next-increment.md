---
type: lesson
title: "State your project's asymptote, so you can tell essential limits from current ones"
figure: sutherland
works: [the-ultimate-display]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# State your project's asymptote, so you can tell essential limits from current ones

Most of Sutherland's paper is a sober inventory of what the hardware of the moment could do — dots, lines, short strokes, keyboards, styluses, knobs. Then he abandons the inventory entirely and names the terminal case: a room where the machine controls whether matter exists, where a displayed chair holds your weight, displayed handcuffs restrain you, and a displayed bullet kills you. He does not hedge it, stage it, or dress it as a roadmap. The move looks like showmanship and is actually a piece of engineering method, because a limit case is the only thing that tells you what kind of machine you are building.

The reason it works is that a field defined by its next increment cannot distinguish an essential constraint from an accidental one. If your goal is "a display draws pictures," then area filling is a feature, force feedback is an unrelated gadget, and eye tracking is a novelty; there is no principle saying which to pursue. If the goal is stated as a machine that can present any modeled world to any sense a person has, the same list reorganizes itself instantly: sight is one channel of several, the missing ones are gaps rather than extras, and the absence of a smell display is a fact about the goal rather than an oversight. The asymptote supplies the ordering that incremental framing cannot.

It also inverts how you read your own limitations. Working forward from today's parts, every constraint feels like a property of the problem. Working back from the limit, most constraints turn out to be properties of this year's components, and a small handful are real. Sutherland could tell that the shortage of meaningful computer-generated sound was a temporary embarrassment while the impossibility of ordering a two-dimensional picture by neighborhood was structural. That distinction is what let him spend effort in the right place, and it is not visible from the incremental view.

A programmer who works this way writes down the version of the system that would need no compromises at all, in plain terms, before planning any of it. Not as a promise and not as a schedule — as a measuring stick. Then each design decision gets scored on whether it moves toward that limit or merely polishes the current rung, and each apparent impossibility gets classified as component-limited or genuinely impossible. The unhedged extreme statement is doing work here precisely because it is unhedged: a goal softened into achievability has already had the useful information filtered out of it.

**Source:** [The Ultimate Display](../works/the-ultimate-display.md) — the contrast between the device-by-device survey in the body and the closing paragraph that jumps to a room in which displayed objects have physical consequence.
