---
type: lesson
title: "Judge a proposal's idea separately from its notation, and expect the first notation to be wrong"
figure: ritchie
works: [evolution-of-the-unix-time-sharing-system]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# Judge a proposal's idea separately from its notation, and expect the first notation to be wrong

**Lesson:** Ritchie records that the pipeline was proposed to them years before it existed, rejected, and then adopted only because its proposer would not let it go. The objections are worth listing because they are all about surface. The suggested form made commands infix operators between their input and output, which felt too strange to people habituated to writing the command first. It was unclear how ordinary arguments would be distinguished from the operands. And the one-in, one-out shape looked too confining. Not one of these is an objection to the actual proposition — that a chain of programs can pass a stream between them and run as coroutines. Ritchie's verdict on his own reasoning is blunt self-criticism about a failure of imagination, and the mechanism, once someone insisted, was a relatively simple job to build.

The sequel is the other half of the lesson. The first notation shipped was not the surviving one: it overloaded the redirection characters so that what followed could be either a file or a command, needed a trailing marker to say the last stage should not be treated as a file, forced quoting to give a stage an argument because the token was delimited by spaces, and admitted two spellings of the same pipeline. It lasted a couple of months and was replaced by a dedicated separator. So the notation genuinely did matter — enough to be redone quickly and publicly — while being exactly the wrong thing to have evaluated the idea on years earlier. Ritchie also notes that the replacement has its own real limits, being stubbornly linear when comparing the outputs of two programs is an obvious thing to want.

The structural insight is that ideas and their syntax have different revision costs and should therefore be reviewed on different clocks. Semantics that are wrong stay wrong; notation that is wrong is discovered by contact with users and swapped out in weeks. Reviewing them together lets the cheap-to-fix component veto the expensive-to-find one.

A programmer who believes this restates a proposal in the plainest terms available before arguing with it, and asks whether their discomfort is with what it does or with how it reads. They also stop treating the first notation as a commitment: ship it, watch what people write, and be willing to break it while the idea is still young. And they take persistence from a colleague who keeps returning to the same rejected idea as evidence worth re-examining, since the reasons for rejection may have been about the packaging all along.

**Source:** [The Evolution of the Unix Time-sharing System](../works/evolution-of-the-unix-time-sharing-system.md) — the section on pipes, covering the original infix proposal and the objections raised against it, the short-lived first notation with its ambiguities, and the replacement by a dedicated pipeline operator.
