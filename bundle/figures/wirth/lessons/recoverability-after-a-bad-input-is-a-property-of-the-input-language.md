---
type: lesson
title: "Recoverability after a bad input is a property of the input language"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Recoverability after a bad input is a property of the input language

**Lesson:** A consumer of structured input that must keep going after a malformed region is usually treated as an engineering problem in the consumer: better guesses, longer backtracking, cleverer state repair. Most of the leverage is not there. Once the consumer has lost its place, the only way back is to find a point in the remaining input whose meaning is unambiguous from the text alone, and whether such points exist at all is decided by whoever defined the input's shape. A construct that begins with a marker occurring nowhere else can be located from a standing start, so a consumer that has abandoned its current position can skip forward to the next marker and resume with confidence. A construct with no distinguishing marker at either end — an expression, an operand, a compound built purely from other constructs — cannot be located that way, and no amount of effort in the consumer conjures a synchronization point that the input does not contain.

This reframes redundant markers from clutter into infrastructure. The usual argument against them is that they are inferable and therefore wasted; the answer is that they are inferable only from a correct input, and their whole value is on incorrect ones. So the design decision belongs at the input-format level, and it is a decision about which regions of a malformed input can be recovered from and which will be swallowed whole. Knowing that answer in advance is also what lets the recovery logic stay small: aim only at the markers, accept that the marker-free constructs are unrecoverable, and stop.

The second half of recovery is knowing that your own reports are unreliable after the first one. The moment the consumer resumes on a guess, its state is a hypothesis, and every complaint it raises immediately afterwards is more likely an artifact of the guess than an independent defect. A blunt damping rule — suppress any further report within a short distance of the last — costs almost nothing and removes most of the noise, and it is better than trying to decide which of the follow-on reports are genuine, because that decision cannot be made reliably from inside the confused state. Deciding in advance that the recovery machinery will be heuristic, bounded, and occasionally wrong is what keeps it from growing into a second program larger than the first.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.4's discussion of the parser's error handling, which observes that continuing after an error requires a guess about the intended structure and is therefore based on heuristics, that incorrect guesses produce secondary diagnostics that cannot be avoided, that the reporting procedure suppresses a report lying less than ten characters ahead of the previous one, that the language is designed so most large constructs begin with a unique symbol which facilitates recovery, that open constructs such as types, factors and expressions beginning and ending with no key symbol are more problematic, and that skipping to the first symbol which may begin a following construct yields acceptable results while keeping the amount of program devoted to erroneous texts within justifiable bounds.
