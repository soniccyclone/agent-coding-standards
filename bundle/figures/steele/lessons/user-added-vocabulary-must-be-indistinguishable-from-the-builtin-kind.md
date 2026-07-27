---
type: lesson
title: "If what users add is distinguishable from what was built in, they will stop adding; the seam is what kills extensibility"
figure: steele
works: [growing-a-language]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# If what users add is distinguishable from what was built in, they will stop adding; the seam is what kills extensibility

**Lesson:** The most testable claim in this work is a comparison of two languages that both had a single brilliant designer and both had an extension facility, and that diverged completely in whether users actually grew them. In one, built-in operations were written with special symbols while anything a user defined got an ordinary name, so a user-supplied abstraction was visibly second class. Steele traces the consequences with care. Users could not make new things that felt like part of the language without heroic effort, so they mostly did not try; growth stayed with the handful of people holding the source; and when a user contribution was judged good enough to promote into the language proper, its call sites had to be rewritten, because the notation for a built-in facility differed from the notation for user code. In the other language, user definitions looked like primitives and — this is the half people forget — the primitives looked like user definitions. Anything a tasteful user built became, without ceremony, more language. The maintainer could grow it almost for free by selecting well from what users had already written.

The general principle is that an extension mechanism is only as good as the indistinguishability of its output. Every visible seam between the native and the added does damage at three separate points. It taxes the author, who must accept a lesser status for their work. It taxes every reader, who now has to track which side of the boundary each name came from in order to know what it can do. And it taxes the maintainer, because promotion across the boundary is a breaking change rather than a relabelling, which means the cheap path from good user code to core language is closed off exactly when you most want it.

Steele then applies the criterion to his own current work, and the application is what shows the test has teeth. The recommendations he makes for Java are not features so much as removals of seams: generic types, so a user-built container is as usable as a native one, and user-definable operators, so a user-built numeric type can be written with the notation numbers get. He points at a class in the standard library whose arithmetic must be spelled out through method calls and observes, without much sympathy needed, that the people forced to use it complain. The complaint is not aesthetic. It is the seam being felt.

A programmer who holds this criterion evaluates any platform's extension points by asking what the extension cannot do that the built-in equivalent can: whether it gets the same syntax, the same tooling, the same error messages, the same performance story, the same place in the documentation. They design their own libraries and frameworks so that a caller's own types can occupy every position the library's types occupy, and they treat any privilege the framework reserves for itself as a future ceiling on how far users will carry the thing.

**Source:** [Growing a Language](../works/growing-a-language.md) — the paired analysis of why one single-designer language stalled while another grew through its users, and the later section proposing generic types and user-defined operators for Java on exactly those grounds.
