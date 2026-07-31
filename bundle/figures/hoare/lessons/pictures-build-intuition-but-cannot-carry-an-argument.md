---
type: lesson
title: "Pictures build intuition but cannot carry an argument, and they fail exactly where the system gets interesting"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Pictures build intuition but cannot carry an argument, and they fail exactly where the system gets interesting

**Lesson:** A diagram of states and transitions is a fine way to see what a small mechanism does, and it is worth drawing for that reason alone. It is a poor medium for two things that matter more as a design grows. First, it cannot support an argument: two drawings can depict the same behaviour while looking completely different, and there is no reliable way to demonstrate that they do by manipulating the drawings. Establishing sameness needs a notation you can rewrite according to rules, where the demonstration is a sequence of justified steps someone else can check. Second, the drawing is bounded by the page. A mechanism with a large or unbounded number of situations cannot be drawn at all, and the trick of an unlabelled arrow looping back to an earlier point is an admission of this rather than a solution to it.

Notice where the failure falls. Diagrams are most comfortable for the small, finite, already-understood parts of a system, and they give out precisely at the scale and the kind of question where you actually need help. That is the opposite of what a good tool does. It also explains a familiar organizational pattern: architecture diagrams accumulate around the parts everyone already agrees about, while the contentious or unbounded parts — the ones with a parameter in them, the ones where the argument is about whether two designs are equivalent — never make it onto the wall.

The conclusion is not to stop drawing. It is to know which job each representation is for, and never to let a picture stand in for a claim. Draw to get the shape into your head and to talk to someone quickly. Write in a manipulable notation when you need to say two things are the same, when the number of situations exceeds what you can enumerate, or when the description has a parameter in it. If a design cannot be stated in a form that supports rewriting, the difficulty is worth noticing rather than papering over, because it means nothing about that design can be established — only illustrated.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the pictures section of the chapter on processes, which introduces the tree-of-states drawing with its looping unlabelled arrow for unbounded behaviour, observes that two such pictures illustrate the very same process while proofs of that equality are difficult to conduct pictorially, and notes that processes with very large or infinite numbers of states cannot be drawn at all, a counter of sixty-odd thousand states being offered as the example.
