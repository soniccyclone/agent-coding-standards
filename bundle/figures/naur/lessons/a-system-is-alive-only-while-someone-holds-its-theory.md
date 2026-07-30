---
type: lesson
title: "A system is alive only while someone still holds its theory, and that state is not recoverable from documents"
figure: naur
works: [programming-as-theory-building]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A system is alive only while someone still holds its theory, and that state is not recoverable from documents

**Lesson:** Track the health of a system by asking who can still answer unanticipated questions about it, not by looking at the code or the test suite. A system whose builders have dispersed can keep running and producing correct output indefinitely; the loss shows up only at the moment somebody asks for a change and no one can say intelligently how it should be accommodated. Since the useful state is held in people, it degrades on the schedule of staffing, not the schedule of code. Reorganizations, contract endings and attrition are therefore technical events, and treating them as purely administrative is how a working system silently becomes an unmaintainable one.

Reconstructing that state from the surviving artifacts is not a matter of effort. Someone building an account that has to fit a text they did not write is caught between fidelity to whatever is actually there — including its confusions and dead ends — and the coherent account they are forming, which will differ. The reconstruction that results is a different theory wearing the old program's clothes, and the mismatches surface later as changes that look correct and behave badly. That yields the uncomfortable but honest recommendation: when a system's builders are truly gone and it must evolve substantially, solving the problem again from the requirement is often no more expensive than excavating the old one, and is more likely to leave you with something someone actually understands. Rewriting is not always waste; sometimes it is the cheaper of two reconstructions.

The preventive move follows from how such understanding transfers at all: by working the material under supervision, the way a craft or an instrument is learned, not by reading a description of it. New people acquire it by handling real changes alongside people who already have it, with the conversation reaching past the code to the relevant parts of the world and to the limits of what the system was ever meant to cover. This makes overlap between departing and arriving people a load-bearing part of the schedule rather than a courtesy, and it makes the assumption that programmers are interchangeable units — hire one, lose one, no net change — a straightforward accounting error.

**Source:** [Programming as Theory Building](../works/programming-as-theory-building.md) — the sections on program life, death and revival, including the argument that revival from documentation is impossible and that a fresh solution may cost no more, the account of how new programmers come to hold an existing theory, and the closing discussion of programmers as replaceable production components.
