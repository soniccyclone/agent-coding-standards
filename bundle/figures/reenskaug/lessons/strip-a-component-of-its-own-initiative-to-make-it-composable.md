---
type: lesson
title: "Strip a component of its own initiative to make it composable"
figure: reenskaug
works: [thing-model-view-editor]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Strip a component of its own initiative to make it composable

A component that talks to the user directly can only ever be used alone. The moment it owns the decision "the pointer went down here, therefore I will select this item," it has silently claimed the whole screen and the whole task, because nothing else can participate in that decision. Two such components on one display do not cooperate; they compete. The fix is not to add coordination machinery on top but to remove capability from below: take every place the component acted on its own judgment and convert it into a question it can answer or a request it can receive. Ask it *what is at this position*, tell it *select that item*. It no longer decides anything; it only knows things and does things when asked.

This inverts the usual instinct that a more capable component is a better one. Capability, in the sense of self-initiated action, is precisely what makes a component uncomposable, because initiative is not sharable — two parties cannot both decide the same thing. Knowledge and mechanism are sharable. So the reusable version of a display element is strictly weaker than the standalone version, and it is weaker in a specific direction: it has been demoted from agent to instrument. Something else, arriving later and knowing about the task rather than the presentation, supplies the initiative and gets to spend it across several instruments at once.

What follows is a real design discipline rather than a slogan. When you find yourself writing an event handler inside a widget, treat that as evidence you are building a leaf and not a part. Ask whether the handler encodes a policy that belongs to the task instead of to the widget, and if it does, hoist the policy and leave behind a method that merely reports or merely obeys. The payoff is that arbitrary combinations become possible without any component knowing about the others, and that the same instrument serves coordinators that were never anticipated when it was written — which is the only kind of reuse that survives contact with a new problem.

**Source:** [Thing-Model-View-Editor: An Example from a Planning System](../works/thing-model-view-editor.md) — the argument appears where the note contrasts its passive list and text views against the then-existing self-scheduling window and paragraph-editor classes, and again in the definition of the editor as the party that establishes, positions, and coordinates a set of views and owns the user's command vocabulary.
