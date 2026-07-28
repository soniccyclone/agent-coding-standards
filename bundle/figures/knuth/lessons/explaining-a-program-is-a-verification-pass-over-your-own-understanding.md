---
type: lesson
title: "Explaining a program is a coverage check on your own understanding, and understanding is where the bugs are"
figure: knuth
works: [literate-programming]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Explaining a program is a coverage check on your own understanding, and understanding is where the bugs are

**Lesson:** Knuth makes an accounting claim that is easy to skip past and is the paper's most testable assertion: writing substantially more explanation did not increase the total time from starting a program to having it work, because the additional writing was repaid out of reduced debugging. He offers a personal control experiment as the reason he believes the mechanism. Programs he prepared for publication or for presentation to a class had come out comparatively free of defects for years. Programs written with no audience accumulated shortcuts that turned into serious mistakes later. The variable is not care or time; it is whether someone was going to have to follow it.

The mechanism is that a compiler will happily accept a program its author only half understands, and a test suite only exercises the cases the author thought of, whereas an explanation has to visit every part and say what it is for. Where you cannot say what a piece is for, you were guessing, and guesses are exactly where defects concentrate. That gives exposition a property no other cheap check has: total coverage of the artifact, weighted toward the places your model is fuzziest, since those are the places the sentence refuses to come out. Its guarantee is far weaker than a proof, but it applies to the whole program rather than to the fragment you had the appetite to formalize, and it costs a small fraction as much. Being in an explaining posture also makes self-deception harder in a way that reviewing your own code does not, because you have to produce a claim rather than merely inspect.

The paper is careful that the formal and informal halves are doing different jobs and neither substitutes for the other — a point Knuth credits to Naur and builds into the shape of every section, commentary first and operational text after. The formal half says what happens. The informal half says why this and not something else: which alternative was considered and dropped, what fact about the domain licenses this step, what would break if the order changed. That second category is the first thing lost to time and by far the most expensive to reconstruct, because reconstructing it means rediscovering the reasoning of someone who is no longer available. Code retains its behavior indefinitely and loses its rationale immediately.

A programmer who takes this seriously reclassifies two things. Writing time stops being overhead competing with implementation and becomes a line item in the debugging budget. And an inability to explain a component cleanly stops being a writing problem and becomes a defect report against the component — the sentence that will not resolve is evidence about the design, and the right response is usually to change the code until the sentence is easy rather than to work harder on the sentence.

**Source:** [Literate Programming](../works/literate-programming.md) — the discussion of costs, where the claim about debugging time absorbing the extra documentation effort is made and grounded in the contrast between programs written for an audience and programs written privately, together with the paper's structural insistence on commentary preceding formal text.
