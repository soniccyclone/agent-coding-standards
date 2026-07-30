---
type: lesson
title: "The case you dismissed as pathological is usually already load-bearing somewhere ordinary"
figure: scott
works: [outline-of-a-mathematical-theory-of-computation]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# The case you dismissed as pathological is usually already load-bearing somewhere ordinary

**Lesson:** Every theory has a case it is allowed to duck, and the standard justification is that the case is exotic. A procedure applied to itself is the classic example: it looks like a logician's amusement, the kind of thing no working system needs, so a model that cannot accommodate it is held to have lost nothing practical. The move that changes the situation is to go looking for the same difficulty in a feature nobody considers exotic at all. If the state of a machine's store is understood as a mapping from locations to contents, and a command is understood as a transformation of that state, then storing a command in a location and later running it — which every system does routinely — asks you to apply the contents of a location to the very state that contains it. That is the self-application case wearing working clothes. The exotic feature and the mundane one stand or fall together.

The consequence is that the scope of a foundational gap is almost never what its first statement suggests. A gap presented as "we cannot model this fringe construct" is worth deferring; the same gap re-presented as "we cannot say what happens when a program stores a procedure" is a hole under the floor. So when you are about to set a hard case aside, spend the effort to find out where else it lives before you decide it is affordable. The search has a specific shape: take the structural feature that makes the case hard — here, an object having to be an element of a space and a function on that same space — and ask which ordinary mechanisms have that shape once you describe them mathematically rather than procedurally. The answer is often several, and they are usually the mechanisms the system already depends on.

The failure mode this guards against is not ignorance but a mismatch between vocabulary and structure. Operationally, storing a command and applying a procedure to itself feel nothing alike — one is bookkeeping, the other is a puzzle — and that difference in feel is entirely an artifact of the operational description, which keeps them apart by talking about code words and text rather than about the objects those stand for. Describing both in terms of what they denote collapses the distinction and makes the shared difficulty visible. This is a general argument for pushing a system's description down to what things *are* before triaging which problems matter: triage conducted on surface vocabulary will systematically misjudge which difficulties are isolated and which are pervasive.

**Source:** [Outline of a Mathematical Theory of Computation](../works/outline-of-a-mathematical-theory-of-computation.md) — the section on the problem of self-application, which sets aside unrestricted procedures as the case some readers find impractical, then derives the same self-application difficulty from the everyday questions of side effects and storage of commands by treating the store as a function from locations to values and a command as a function from states to states.
