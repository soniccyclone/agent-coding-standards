---
type: lesson
title: "The compressed form is the one people will act on, so the constraint has to live inside it"
figure: royce
works: [managing-the-development-of-large-software-systems]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# The compressed form is the one people will act on, so the constraint has to live inside it

**Lesson:** This paper is the citation given for the strictly sequential development process, and the diagram of that sequence has been reproduced for decades. The paper says that arrangement is risky and invites failure, then spends most of its length on the five things you have to add before it works. The picture propagated. The qualification attached to the picture did not. Whatever one thinks about development methodology, that transmission history is a demonstration of something general about representation, and it happens to be the most useful thing this particular source teaches.

The general claim: when a design is reduced to a memorable compressed form, a diagram, a naming convention, a public interface, a one-line summary, the compressed form becomes what people actually use, and anything you left in the surrounding prose is gone. Compression discards whatever the compressed form cannot carry, and the author does not get to choose what gets discarded. The medium chooses, and it reliably keeps the shape and drops the caveat, because the shape is what is easy to remember and repeat.

What follows from believing it is that a constraint has to be encoded in the artifact rather than stated next to the artifact. Make the invalid state unrepresentable instead of documenting that it is invalid. Put a required ordering into the interface shape so the wrong order cannot be written, rather than into a comment saying to call these in order. If a picture is going to be the thing people carry away, draw the failure mode into the picture. Every constraint that lives only in prose adjacent to a compact representation is a constraint you have decided to lose on the first retelling.

The same reasoning applies in reverse, to inherited practice. When a convention is justified by appeal to a source, go read the source, because the version circulating may be exactly the arrangement the source erected in order to argue against it. Received methodology drifts in the direction of whatever compressed better, not in the direction of what was argued.

**Source:** [Managing the Development of Large Software Systems](../works/managing-the-development-of-large-software-systems.md) — the gap between what the paper's own sequential diagram is remembered as recommending and what the surrounding text explicitly says about it, plus the five correctives the text treats as mandatory.
