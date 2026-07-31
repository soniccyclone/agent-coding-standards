---
type: lesson
title: "A value invented to satisfy the machinery is indistinguishable from a requirement once it is written down"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# A value invented to satisfy the machinery is indistinguishable from a requirement once it is written down

**Lesson:** Reasoning tools nearly always work better on total things than on partial ones — every case answered, no gaps, no side conditions. So when you adopt a tool that prefers totality, it quietly demands that you supply an answer for situations where the problem has none: what a removal from an empty collection yields, what an inspection of nothing returns. You make something up, because you must, and you choose whatever makes the algebra tidiest. This is a legitimate and often correct move. The hazard is entirely in what happens next: the invented answer is now written in the same place, in the same notation, with the same authority as the answers that came from the problem. Nothing on the page marks which is which.

Downstream that distinction is exactly what people need and cannot recover. An implementer reading the description sees a defined behaviour for the empty case and implements it, and is correct to. A second reader sees the same line and infers that somebody thought about the empty case and decided this was the right thing for it — the strongest available reading of a written commitment, and the wrong one. Meanwhile a change that would have been free, had the case been genuinely open, is now a compatibility break, because callers have had years to depend on the fiction. The convenience you took on for the benefit of the proof apparatus has been converted into a promise to the outside world, and the conversion happened silently, at the moment of writing.

The alternative is not to refuse the convenience. It is to keep the two categories separately visible: state the restriction where the problem genuinely has nothing to say, and let the notation carry that restriction rather than papering over it with a manufactured result. Then any totalization done for the reasoning machinery is a derived, marked-as-derived layer sitting on top of a description that is honest about its own domain, and a reader can always ask which they are looking at. When the tool will not tolerate that — when it insists on totality all the way down — the cost is not a formality, it is the permanent loss of the ability to tell a requirement from an accommodation.

The general instruction is to be suspicious of any place where the shape of your tooling forces a choice the problem did not force. Those choices are the ones that get mistaken for design, because they are made under pressure, recorded without comment, and defended later by people who assume there was a reason.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 16's presentation of the implicit stack definition, where removing from an empty stack is defined as yielding an empty stack and the range of the inspect operator is extended with a distinguished indicator for the empty case, together with the stated explanation that operators are normally extended in this way because of the relative ease of dealing with total algebras, and the explicit contrast drawn there with the pre-conditions used throughout the rest of the book to record the same restrictions instead.
