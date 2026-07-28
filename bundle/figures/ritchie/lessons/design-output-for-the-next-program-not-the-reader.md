---
type: lesson
title: "A component's output is an interface, so verbosity and interrogation are design errors rather than taste"
figure: ritchie
works: [unix-time-sharing-system-a-retrospective]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A component's output is an interface, so verbosity and interrogation are design errors rather than taste

**Lesson:** Ritchie takes the famous terseness of his system's programs, which is usually discussed as a matter of aesthetics or machismo, and shows it is forced by composability. Two ordinary commands illustrate it: one that lists the users currently logged in, one that counts lines. Chain them and you get a count of users, for free, from programs that were never designed together. Add a decorative heading to the first and the count is wrong. Have the second one stop to ask which quantity you meant and it cannot participate at all. So the discipline is not that fewer words are more elegant; it is that anything a program emits beyond its actual result is noise in a channel some other program will read, and anything a program demands from a human is a blockage in that channel.

The same logic runs through the rest of the interface discussion. Missing arguments produce a one-line usage note and an exit rather than a prompt, because insisting on a conversation removes the program from every non-interactive context. Success is signalled by an unobtrusive prompt rather than an announcement, and resource consumption is reported only when asked, because the caller who cares can ask and the caller who does not should not have to filter. Ritchie is careful not to overclaim: he says plainly that some of this is taste, that beginners find it disconcerting, that not every table should omit its headings, and that the editor's single diagnostic character is genuinely confusing at first. The argument is that where taste and composability disagree, composability decides.

There is a general principle underneath, which is that a program has two audiences and one of them cannot complain. A human reader can tolerate extra prose; a downstream parser silently produces wrong answers. Designing for the audience that can complain optimizes the wrong side.

A programmer who believes this treats stdout as a typed interface rather than a place to talk. Progress chatter, banners, and confirmations go somewhere separable or behind a request; questions to the user become arguments with defaults; and the result of a program is shaped so a machine can consume it without knowing anything about the program's internals. When a tool has to be wrapped in filtering to be reused, they read that as a defect in the tool's contract.

**Source:** [UNIX Time-Sharing System: A Retrospective](../works/unix-time-sharing-system-a-retrospective.md) — the user-interface section, particularly the two-command pipeline used to argue that extraneous output and insistence on interaction would break composition, and the surrounding remarks on prompting and diagnostics.
