---
type: lesson
title: "Size a new variant by the obligations it inherits, not by the concept it adds"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Size a new variant by the obligations it inherits, not by the concept it adds

**Lesson:** When an interface admits new kinds, the effort of adding one is routinely estimated from how complicated the new kind is as an idea. That estimate is almost always wrong and always wrong in the same direction, because the work is not the idea; it is the set of duties the interface assigns to every implementer. A trivially simple kind whose implementation must also handle boundary conditions, partial visibility, and degenerate cases is not a simple implementation. The concept contributes a line or two; the inherited duties contribute the rest, and they contribute the same amount no matter how simple the concept is. So the honest measure of what it costs to extend a system is the fixed obligation per implementation, and that number is set once, by whoever wrote the interface, for everybody who will ever implement it.

This reframes an interface decision that usually gets made on locality grounds. Giving each implementation responsibility for a chore looks right whenever the chore depends on the implementation's own data — only the implementation knows which of its parts fall outside a limit, so let it decide. The counterweight is that the chore has now been multiplied by the number of kinds that will ever exist, and every one of them has an independent chance to get it wrong, in a way that will be found by whoever first drags one to an edge. Before delegating a duty, ask whether some weaker, uniform version could be discharged once by the caller — a conservative test at the boundary, a coarse restriction applied to everything — leaving the implementations to handle only the part that genuinely needs their private knowledge. Where that split exists it converts a recurring per-variant tax into one implementation plus a much smaller residue.

Where the split does not exist, the duty stays delegated and the right response is to say so out loud. Write down, next to the interface, that implementing this kind costs the concept plus these specific obligations, and expect the second one to be the larger. An extension mechanism advertised as cheap and experienced as expensive is a mechanism people stop extending, and they will not usually tell you why; they will just write something adjacent instead.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.9.1's observation that despite the simplicity of the notion of a rectangle its drawing method is more complex than might be expected, because drawing methods are responsible for clipping at frame boundaries, so some component lines must be shortened and others disappear entirely.
