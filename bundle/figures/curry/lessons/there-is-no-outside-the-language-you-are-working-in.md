---
type: lesson
title: "There is no outside the language you are working in, so carve the layer you need out of the inside"
figure: curry
works: [a-theory-of-formal-deducibility]
axes: [expressiveness, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# There is no outside the language you are working in, so carve the layer you need out of the inside

The standard story about talking rigorously about a language is that you need a
second language to talk about the first, a third to talk about the second, and so
on upward forever. Curry rejects the story's premise. Any actual investigation is
conducted not in some arbitrary higher language but in the one the participants
actually share, and there is no getting behind it: whatever you study, you study
by means of it. So the tower has no ground floor and no top — it has a single
floor you are standing on, and the honest description of what you do is not
ascent but *carving*. You take a segment of the language you are already using,
fence it off, name it, introduce vocabulary inside your working language for
referring to the fenced-off part, and now you have a layer over it. Then you can
fence again. The layering is real; the escape is not.

He is unusually frank about what that working language is like, and the honesty is
the useful part. It is specific rather than generic — saying the discussion is "in
English" tells you nothing, since plenty of English discussions are unintelligible
to any given competent English speaker. It grows and gets refined as you go, while
somehow staying the same language. It is permanently a bit vague, and yet you can
reach any precision you need by successive approximation. It cannot be exhaustively
described, and it will produce contradictions if handled carelessly. His analogy is
to a physicist's experimental constants: not known absolutely, known to whatever
accuracy the purpose requires. That is not resignation. It is the correct model of
how precision is actually achieved — incrementally, from inside, against a
background you never fully pin down.

For anyone building tools this reframes a familiar frustration. The host language,
the shell, the config format, the ambient conventions of your codebase are not a
neutral substrate your abstraction sits on top of; they are a participant that
shapes what your abstraction can express, and they are drifting under you. The
consequence is that a DSL, a schema language, an IR, or a query layer is never
"above" its host — it is a named region carved out of the host, and everything
outside the fence remains in play. Which is why embedded DSLs leak host semantics,
why config languages grow toward the host language they were meant to avoid, and
why the meta-circular ambitions of self-describing systems bottom out in something
handwritten that nobody describes.

The working practice is twofold. First, stop looking for a neutral outside and
instead be explicit about which segment you have fenced and what vocabulary you
introduced to refer to it, because that fence is the only thing separating the
layers and it exists by convention rather than by construction. Curry does exactly
this repeatedly: he names the fragment introduced by a system's own notation, names
the technical vocabulary added for talking about variables and substitution, and
keeps saying which fragment a given statement lives in. Second, expect and budget
for imprecision at the boundary, and refine it when the purpose demands rather than
trying to make it exact up front. Demanding total precision from the substrate is
demanding an outside that does not exist; getting the accuracy the task needs, and
knowing which parts you have not yet made precise, is what is actually available.

**Source:** [A Theory of Formal Deducibility](../works/a-theory-of-formal-deducibility.md) — the semiotical sections of the opening chapter, which reject the infinite regress of metalanguages in favour of a single language being used, enumerate its characteristics, and describe layering as isolating a segment and introducing vocabulary for it from within.
