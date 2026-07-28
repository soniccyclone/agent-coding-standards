---
type: lesson
title: "Where the endpoints are is a property of the use, not the data"
figure: saltzer
works: [end-to-end-arguments-in-system-design]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Where the endpoints are is a property of the use, not the data

**Lesson:** A design principle that tells you to move a function to "the ends"
is only as good as your ability to say where the ends are, and that turns out not
to be a question about the data type flowing through the system. The same content,
in the same encoding, at the same bit rate, yields opposite answers depending on
what sits at the far side. When the far side is a human in a live conversation,
delay is the intolerable failure and a damaged fragment can simply be let through,
because the recipient can ask for a repeat. When the far side is a file that will
be replayed later, the recipient has lost the ability to ask, so accuracy becomes
worth waiting for and the very same lower-layer retry machinery flips from harmful
to helpful. Nothing about the medium changed. The endpoint changed.

This is why the end-to-end argument is a guideline that has to be re-derived per
application rather than a rule that can be applied by pattern match. And it is the
part most often skipped, because identifying the endpoint requires knowing what
recovery the outermost consumer of the system is actually capable of — which is
knowledge that lives outside the software entirely. The bank has auditors. The
travel agent will keep retrying until they get an answer. The caller will dial
again. In each of those cases the true end of the system is a person and a
procedure, and once you see that, expensive internal mechanisms that guarantee
something the outer procedure already catches stop looking prudent and start looking
like duplicated effort.

The habit this builds is to trace, before designing any recovery or consistency
mechanism, all the way out past the API to whoever or whatever finally decides the
operation succeeded, and to ask what they can already detect and redo. That trace
determines both where your checks belong and, more usefully, which checks you are
free not to write. Skipping the trace is how systems end up with heavy internal
guarantees that no consumer needed and no guarantee at the one place a consumer
would have looked.

**Source:** [End-to-End Arguments in System Design](../works/end-to-end-arguments-in-system-design.md)
— the "identifying the ends" section contrasting real-time packet voice with stored
voice messages, reinforced by the later examples drawn from banking audits, airline
reservation agents, and telephone exchanges.
