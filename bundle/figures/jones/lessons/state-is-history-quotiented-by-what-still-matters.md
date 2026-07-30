---
type: lesson
title: "State is history divided by what still matters, and keeping the history instead is the lazy answer"
figure: jones
works: [systematic-software-development-using-vdm]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# State is history divided by what still matters, and keeping the history instead is the lazy answer

**Lesson:** Faced with a component whose behaviour depends on what has happened to it, there is a describe-everything option that is always available and always tempting: record the sequence of everything that was done, and define each result as a function of that sequence. It is honest, it needs no invention, and it is almost always the wrong description. Many different sequences leave the component in situations that no future interaction can distinguish, and a description built on sequences cannot say so. What you want instead is the thing those indistinguishable sequences have in common — and that is precisely what state is. State is not "the data the component happens to hold"; it is the quotient of all possible histories by the relation "these lead to identical future behaviour."

Reading it that way turns designing a state into a definite task with a checkable answer, rather than a matter of taste. Ask, for each piece of information you are inclined to keep, whether any future operation's result could differ depending on it. If not, it is history rather than state, and keeping it is the temporal form of building distinctions no observer can detect. Ask, conversely, whether any two histories your candidate state conflates could actually be told apart later. If so, the state is missing something. Both questions are answerable by inspecting the operations, and the answers do not depend on how the thing will be built.

This is also the honest reply to the position that a component is best described purely by its externally visible sequence of events and should have no inside at all. Sequences are a real and sometimes ideal description, but adopting them everywhere does not eliminate state — it replaces a small explicit state with a large implicit one, and buries the fact that most of it does not matter. The eliminating of irrelevant detail is the actual work, and having somewhere to put the result is what makes a description short. A well-chosen state earns its keep by being exactly the part of the past that the future can still feel.

**Source:** [Systematic Software Development Using VDM](../works/systematic-software-development-using-vdm.md) — the operations section of the functions-and-operations chapter: its calculator example showing several distinct operation sequences reaching the same register value, the observation that the value rather than the history determines the effect of the next operation, the footnote characterizing the state as inducing an equivalence class on histories with an extreme choice being to store every operation executed and abstraction being the process that fixes what is irrelevant, and the accompanying remark that regarding operations as functions over the history of all state changes is possible but hides the fact that different histories give rise to situations which are not detectably different.
