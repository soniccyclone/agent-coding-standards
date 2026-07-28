---
type: lesson
title: "An error return that every caller ignores is a design defect"
figure: pike
works: [hello-world]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# An error return that every caller ignores is a design defect

The decoding routines here originally did the textbook thing: given a malformed
byte sequence, report an error and let the caller decide. In practice the authors
found themselves writing the same check at every call site and then doing nothing
with it, over and over, so they changed the interface. Malformed input now decodes
to a designated substitute value and processing continues. The reasoning is not
laziness; it is that a text-processing program handed non-text has only two
sensible options, abort or carry on, and aborting is unacceptable for a tool that
must survive whatever it is pointed at. If neither option needs a decision from
the caller, then handing the caller a decision was the mistake.

The general principle: an error signal is a request for a choice, and it is only
worth its cost when callers actually have different useful answers. When the
honest answer is the same everywhere, encode that answer in the operation and
make it total — a function that always returns something meaningful is one that
cannot be misused by omission, and the check that every caller was going to skip
stops being a latent bug. Notice this cuts against the usual instinct to push
decisions outward for flexibility. Flexibility that nobody exercises is just a
uniform tax plus a fleet of unchecked returns.

Two details keep this from being an excuse for sloppiness. First, the substituted
value is a distinct, reserved thing that means "the encoding here was broken,"
carefully kept separate from the pre-existing notion of "a character we cannot
represent." Conflating a transport failure with a content limitation would have
destroyed the ability to reason about either. Second, the authors state the cost
plainly: decoding and re-encoding no longer round-trips malformed input, and they
accept that because it only happens when a text tool was given something that
isn't text. Choosing a lossy total function over a lossless partial one is a
trade, and it should be made with the loss written down.

**Source:** [Hello World or Καλημέρα κόσμε or こんにちは 世界](../works/hello-world.md) — the Libraries section's account of replacing error returns from the decoding routines with a reserved substitute value, including its distinction from the character set's own unrepresentable-character value.
