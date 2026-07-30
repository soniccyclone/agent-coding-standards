---
type: lesson
title: "Treat response time as a first-class requirement, because latency decides what kind of thing you have built"
figure: kay
works: [personal-dynamic-media]
axes: [cognitive-load, hardware-affinity]
subdomains: [programming-environments-and-object-systems, operating-systems-and-systems-programming]
tags: [lesson]
---
# Treat response time as a first-class requirement, because latency decides what kind of thing you have built

**Lesson:** Latency is normally filed as a quality attribute to be improved later, which gets the causality backwards. The right model is an instrument in the hands of a player: cause and effect must be close enough together that the user's correction loop stays closed, so that intent, action and result live in one continuous act rather than three separated ones. A musical instrument with a one-second lag between the breath and the note is not a slow instrument, it is not an instrument; the delay has changed the category of the object, not merely its rating. The same discontinuity exists in any interactive system, and it sits at a threshold rather than on a slope, which is why averaging response times hides the thing that matters.

Because it is categorical, this requirement propagates upward into architecture instead of downward into optimization. If a person must be able to explore, be wrong, and adjust at the speed they think, the machine has to be dedicated to them at the moment they are thinking. That single constraint is enough to decide between growing one enormous shared resource and giving each person a smaller machine of their own — and it decides for the second even when the shared resource is technically the more impressive engineering. The lesson generalizes: a hard interaction budget is a premise you design from, and it will invalidate otherwise attractive architectures early, which is exactly when you want to know.

The second half of this is fidelity, which behaves the same way. A channel that is impoverished — coarse output, poor resolution, few simultaneous voices — does not merely make the system less pleasant, it restricts what can be expressed through it and therefore what users will attempt. Someone accustomed to rich materials will find a crude channel not worth talking through, and the ambition of the work people do in your system will silently shrink to what the channel comfortably carries. Both latency and fidelity are properties of the medium, and the medium determines the ceiling on the thought that can happen inside it.

**Source:** [Personal Dynamic Media](../works/personal-dynamic-media.md) — the design-goals passage arguing for no discernible pause between cause and effect via the analogy to playing a flute, the inference from that requirement to per-person machines rather than a several-hundred-fold larger shared one, and the observation that a low-bandwidth timeshared channel carries a correspondingly impoverished message.
