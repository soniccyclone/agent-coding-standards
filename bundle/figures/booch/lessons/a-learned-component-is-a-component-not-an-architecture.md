---
type: lesson
title: "A learned component is a component; what the surrounding structure remembers decides what the system can do"
figure: booch
works: [building-the-enchanted-land, the-future-of-software-engineering]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A learned component is a component; what the surrounding structure remembers decides what the system can do

**Lesson:** When a statistical component is dropped into a system, the temptation is to describe the result as an intelligent system. Dissection of the impressive examples says otherwise: what they are is conventional structures, often stunningly plain ones, with learned parts occupying specific positions. A staged arrangement that widens a question into many candidate answers, gathers evidence for each, and narrows back to a ranked few is an ordinary pipeline; the learned pieces sit inside the stages, and the pipeline is what makes them add up to something. Recognizing this defuses both the hype and the anxiety, because it means the existing discipline still applies and the learned parts are new material rather than a new profession.

The sharpest structural question is what the system is allowed to remember. A component that maps the current situation to a response, with no dependence on how the situation arose, is reactive by construction, and no amount of training will give it behavior that requires history. Whether that limitation matters is a property of the problem: for a board position it may be irrelevant; for anything where an earlier observation should change present vigilance, it is disqualifying, and the fix is not a better model but a structure that carries state the model cannot see. Deciding what history the assembly holds, and where, is therefore an architectural decision of the highest order, and one that inspecting the learned component alone will never reveal.

Two further shifts follow for anyone building this way. The data becomes the primary design surface, since the selection and preparation of what the system is taught determines its behavior more than any coding decision, and the biases and consequences baked into that selection are engineering responsibilities rather than someone else's ethics problem. And because the resulting behavior depends on the order in which teaching occurred, the artifact is no longer a fixed input-output relation that can be probed the way a program can. Diagnosis becomes an interrogation of something that cannot explain itself, which is a reason to keep symbolic, inspectable machinery in the parts of the system where accountability is required, and to reserve the opaque parts for the places where their strength genuinely lies.

**Source:** [Building the Enchanted Land](../works/building-the-enchanted-land.md) — the dissections of a question-answering system as a pipeline with learned stages and of a game-playing system as history-free by construction, the argument that such systems are systems-engineering problems with learned components rather than a separate category, and the treatment of data curation as the dominant and ethically loaded part of the lifecycle. Also [The Future of Software Engineering](../works/the-future-of-software-engineering.md), which names the order-dependence of taught systems and the diagnostic role that will be needed to investigate them.
