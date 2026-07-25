---
type: lesson
title: "Design skill lives in remembered structures, so it can be extracted and handed over"
figure: gang-of-four
works: [design-patterns-abstraction-and-reuse-of-object-oriented-design]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Design skill lives in remembered structures, so it can be extracted and handed over

**Lesson:** The methodology industry of the late 1980s assumed the scarce thing in design was procedure: a notation for drawing the system plus rules for when to draw what. This paper's opening move is to reject that premise on empirical grounds. Studies of how competent programmers actually work found their knowledge organized around remembered chunks — algorithms, data layouts, recurring plans for reaching a goal — not around the syntax of any diagramming convention. Whatever an expert has that a novice lacks, it is not fluency in a notation. It is a stocked inventory of structures they have seen work before. Which means the notation-and-rules apparatus was optimizing the wrong variable entirely.

The consequence is the interesting part. If expertise is an inventory rather than a talent, it is in principle extractable. Watch enough real systems, notice which arrangements of collaborating parts keep reappearing, describe each one at a level abstract enough to survive the move between problem domains, and give it a name. What you then hold is not a summary of those systems but a piece of transferable capital: the next designer gets the arrangement without paying for the decade of mistakes that discovered it. Naming is doing real work here, not decoration. A named structure becomes a unit of thought and a unit of speech at once — it can be proposed, compared against alternatives, argued down, and pointed at during a review, all in a phrase. That is what raises the level at which a team programs, and it is measured directly in working memory: reasoning about a design in terms of six familiar named collaborations is a different cognitive task from reasoning about the forty classes those collaborations expand into.

The same effect explains something otherwise puzzling about learning unfamiliar code. Every substantial library has a house style — a handful of structural habits its authors reached for over and over without necessarily naming them. A newcomer who identifies those habits first, before touching individual classes, is decoding the library through a small key rather than memorizing a large surface. And because the habits recur across libraries, the key is partially reusable at the next library. The authors observed exactly this while teaching their own framework, and it is why they treat pattern-literacy as prior to API-literacy.

A programmer who believes this stops treating hard-won design judgment as tacit and personal. They write the structure down when they find it, they name it deliberately enough that the name carries its intent, they teach a codebase by its recurring shapes rather than by its file tree, and they are skeptical of any process that promises good design from notation and rules while saying nothing about accumulated experience.

**Source:** [Design Patterns: Abstraction and Reuse of Object-Oriented Design](../works/design-patterns-abstraction-and-reuse-of-object-oriented-design.md) — the introduction's critique of design methods against studies of expert programmers, together with the observations section reporting what happened when patterns were taught alongside a framework.
