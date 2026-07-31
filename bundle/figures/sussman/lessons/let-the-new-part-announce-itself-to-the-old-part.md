---
type: lesson
title: "Let the new part announce itself to the old part, never the reverse"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Let the new part announce itself to the old part, never the reverse

**Lesson:** With dispatch written as explicit conditionals, every generic operation has to enumerate every representation, so adding one means editing code that was finished. The authors diagnose two symptoms — the interface procedures must know about all the representations, and no two procedures anywhere in the system may share a name — and then make the move that matters: these are one defect, not two. Both are cases of a new part requiring changes to existing parts. The fix reverses the direction of knowledge. The generic layer knows only how to consult a table; each implementation, when it is installed, writes its own entries in. Nothing that already worked is opened.

The name collision disappearing as a side effect is the tell that the diagnosis was right. It is not addressed separately. Once each implementation is packaged as a body of definitions enclosed in its own scope, its internal names are private and can be the obvious ones — every package can call its own accessor by the natural name, exactly as its author would have written it working alone. The authors point out that the internal procedures are unchanged from the versions written in isolation; all that was added is a thin registration layer at the boundary. That is the shape to aim for: code that does the work, plus a small announcement of what it can do, and no adaptation in between.

The generalization is a rule about which way dependencies point at an extension seam. A framework that names its extensions is a framework that must be edited to gain one. A framework that publishes a registration interface and knows nothing about who uses it can be extended by strangers, in code it has never seen, without its authors being consulted — which is precisely the requirement when hundreds of variants exist and no single person knows them all. The authors are explicit that at two representations none of this matters and the conditional version is fine; the argument is about what happens at scale, and about the fact that "the edit is straightforward" is not a defence, because a straightforward edit still has to be made, by someone, correctly, every time.

The residual cost is honest and worth naming. Dispatch has become a runtime lookup in a table that no compiler and no reader can see the whole of, so the question "what handles this case" is no longer answerable by reading the source, and a missing registration is a runtime failure rather than a missing branch. That is the actual trade: you exchange static visibility of the whole matrix for the ability to extend it without permission. Take it when new cases will keep arriving from outside; do not take it to make a fixed set of three cases look sophisticated.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.4.3, which lists the two weaknesses of explicit dispatch on type (each generic interface procedure must know all representations, and no two procedures in the entire system may share a name), identifies the common underlying issue as the technique not being additive, notes that the required changes are straightforward but must be made nonetheless and become serious when there are hundreds of representations and no single programmer knows them all, and then presents the install-package procedures whose internal definitions are unchanged from the isolated versions and whose interface consists only of put calls registering each operation and type into the table consulted by apply-generic.
