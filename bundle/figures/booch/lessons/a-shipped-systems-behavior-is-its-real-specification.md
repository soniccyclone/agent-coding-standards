---
type: lesson
title: "Once a system has users, its observed behavior becomes the specification, defects included"
figure: booch
works: [the-future-of-software-engineering, the-promise-the-limits-and-the-beauty-of-software]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Once a system has users, its observed behavior becomes the specification, defects included

**Lesson:** A deployed system stops being an implementation of its requirements and becomes a requirement in its own right. People build workflows on what it actually does, which includes behavior nobody intended, and once they have, correcting a genuine defect breaks real work and is therefore a regression regardless of what the original intent was. This is not a failure of discipline; it is what it means for software to be in use. The practical consequence is that the specification of a mature system is unwritten, unbounded, and only partially discoverable, so rewriting it exactly is not a matter of effort but of information that no longer exists anywhere.

Two forces make replacement harder than the sum of its parts. The first is that the accumulated behavior cannot be enumerated, so a rewrite discovers its own incompleteness only through the complaints of people whose work has stopped. The second is that the original keeps moving: it is maintained, extended, and adapted while the replacement is being built, so the target recedes at something close to the speed of pursuit. The combination is why competent teams with correct diagnoses of terrible code abandon rewrites, and why systems written in the idioms of decades past are still running the machinery of national institutions after several serious attempts to displace them. The constraint is not sentimentality about old code; it is that continuity of service is a hard requirement and the specification is captive inside the artifact.

The mental adjustment is to treat legacy not as a defect to be eliminated but as a constraint to be engineered against, and to expect it in every system including the one being started today. Any project that succeeds acquires this property, and the appearance of freedom in a new codebase is a temporary condition, not a category. A programmer who accepts this designs for incremental replacement rather than eventual replacement: they keep boundaries where continuity will have to be preserved, they treat any externally visible quirk as something to inventory before touching, and they stop proposing rewrites as a solution to structural problems that incremental transformation is the only available means of solving.

**Source:** [The Future of Software Engineering](../works/the-future-of-software-engineering.md) — the account of a mature word processor whose users depended on genuine defects, where the correction itself became the bug report and the rewrite was abandoned because the original kept advancing, alongside the tax administration whose core remains in decades-old assembly across repeated replacement attempts. Also [The Promise, the Limits, and the Beauty of Software](../works/the-promise-the-limits-and-the-beauty-of-software.md) — the argument that a continuously operating system cannot be switched off to be replaced, and the transit example where the inherited constraint predates software entirely.
