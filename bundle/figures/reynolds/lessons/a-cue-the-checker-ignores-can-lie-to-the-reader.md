---
type: lesson
title: "A structural cue the checker ignores is a channel where the reader and the machine can silently disagree"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# A structural cue the checker ignores is a channel where the reader and the machine can silently disagree

**Lesson:** Layout — line breaks, indentation, alignment — is worth spending effort on, because a reader recovers structure from it far faster than from the tokens alone. But if the tool that assigns meaning discards layout entirely, then you have created two independent renderings of the same structure, one authoritative and one merely persuasive, with nothing keeping them in agreement. When they diverge, the persuasive one wins in every human review, which is exactly the wrong outcome. The failures this produces are not spread evenly; they cluster at the places where the two renderings encode the same fact differently, which in practice means separators and terminators sitting at the ends of lines, where the eye takes the line break as the separator and stops looking.

Notice that the cue's helpfulness and its danger are the same property. Layout works precisely because a reader trusts it without checking, and it is capable of masking a defect for precisely the same reason. So "format carefully" is not a fix — careful formatting makes the misleading case more convincing, not less. The real responses are structural. Either make the tool that decides meaning read the same signal the human reads, so the two cannot come apart; or make the redundancy machine-checkable, so a formatter or linter fails on any file where the two renderings disagree; or drop the redundant channel. Any of those closes the gap; exhorting people to look harder at line ends does not.

The general shape recurs well beyond program text. A diagram beside a schema, a comment naming an invariant, a directory layout implying a module boundary, a name encoding a unit — each is a second statement of something the authoritative artifact already states, addressed to a reader rather than to a checker. Each is genuinely valuable, and each will eventually contradict the artifact. The question to ask of every such channel at the time you introduce it is what mechanism keeps it honest, and if the honest answer is "someone will notice", treat the channel as a known hazard and put the effort into checking it rather than into polishing it.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Appendix B's introductory remarks on program layout, which advise using line breaks and indentation to reveal program structure as clearly as possible to human readers while warning that these visual cues do not influence the compiler and can therefore mask syntactic errors, singling out an omitted semicolon or comma at the end of a line as especially hard to perceive, and a missing blank at the end of a line running to the last usable column as harder still.
