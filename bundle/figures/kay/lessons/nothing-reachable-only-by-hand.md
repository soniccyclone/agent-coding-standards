---
type: lesson
title: "Every capability should be equally reachable by hand and by program, and every object equally open to inspection"
figure: kay
works: [personal-dynamic-media]
axes: [expressiveness, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Every capability should be equally reachable by hand and by program, and every object equally open to inspection

**Lesson:** Systems usually grow two disjoint control surfaces. There is the direct one, where a person points and drags, and the programmatic one, where code manipulates state; and the sets of things reachable through each are never quite the same. Capabilities that exist only in the interactive surface cannot be automated, composed, or scaled up, so any task requiring a thousand repetitions is simply out of reach. Capabilities that exist only in the programmatic surface are unavailable to the person who has the intent but not the fluency, at exactly the moment they are motivated. The discipline worth adopting is parity: whatever can be done by hand can be done by program and vice versa, treated as an invariant of the design rather than a feature request.

Parity has a structural cost that is also its main benefit. It forces every interactive gesture to be backed by a nameable operation on a real object, which means the interface cannot be a special-purpose contraption bolted to the side of the model — it has to be a view onto operations that stand on their own. That in turn is what makes a hand-performed sequence capturable as a description, editable as data, and replayable later; automation stops being a separate feature you build and becomes a consequence of how the controls were factored. A system where recording a user's actions requires bespoke machinery has told you that its two surfaces have already diverged.

The companion invariant is uniform openness: anything the system holds can be displayed and changed, including the things a designer would ordinarily consider infrastructure rather than user data. When the parts a user is normally forbidden to touch — the appearance rules, the tools themselves, the running process mid-flight — are ordinary editable objects, users adapt the system to purposes you never anticipated, and the boundary between using and extending stops being a cliff. The usual argument for keeping such things closed is safety, but the cost is that everyone who wants something slightly different must wait for you.

**Source:** [Personal Dynamic Media](../works/personal-dynamic-media.md) — the statement that all of the described systems are equally controllable by hand or by program, the claim that every description or object in the system can be displayed and edited, the recording and editing of interactively played musical input for later playback, and the animation tool's ability to edit any component of any frame while the animation is running.
