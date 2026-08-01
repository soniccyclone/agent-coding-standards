---
type: lesson
title: "An operation oddly harder than its sibling marks a semantic commitment"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# An operation oddly harder than its sibling marks a semantic commitment

**Lesson:** A system that manipulates content without interpreting it gets a strong property for free: every operation is a transformation of structure, so operations that ought to be similar in difficulty are similar in difficulty. That regularity is worth treating as an instrument. When one operation turns out far more complicated than its close relative — when moving something is hard while copying it is easy, though both take the same selection and the same displacement — the asymmetry is not an implementation accident. It marks a place where the system was quietly given an opinion about what the content *means*, and the opinion has to be maintained by exactly those operations that disturb the relationships it is about.

The trade is a real one and is often worth making, so the point is not to refuse it. Deciding that certain arrangements of elements mean something — that two abutting perpendicular members are joined, that adjacent cells form a region, that a particular ordering is significant — buys behaviour users genuinely want, because it lets an edit preserve an intention rather than only a geometry. What it costs is that every structural operation now has to identify the affected relationships and repair them, and that cost is invisible in the feature request. So the discipline is to name the commitment when you make it, record it as a departure from the system's stated neutrality, and expect the bill to arrive in the mutating operations rather than in the feature itself.

The instrument also runs in the other direction, which is the more useful use of it. When reviewing existing code, look for the operation whose implementation is disproportionate to its description and ask what it is preserving. The answer is usually an interpretation that nobody wrote down, adopted for a use case that dominated the system's early life and possibly no longer dominates it. Having found it, you have a decision available that was not available before: keep it and document it, or drop it and reclaim the simplicity of every operation that was paying for it. What you cannot do is leave it undiagnosed, because then the complexity looks intrinsic and nobody ever proposes removing it.

**Source:** [Project Oberon](../works/project-oberon.md) — the closing remark of section 13.8.3, that the `Move` operation appears surprisingly complicated in comparison with the related copy operation, and that the reason is a deviation from the principle that a graphics editor must refrain from interpreting drawings: because the editor was first used for circuit diagrams, adjoining perpendicular lines were taken to be connected, so displacing a line must preserve connections and `Move` must find all connected lines and extend or shorten them.
