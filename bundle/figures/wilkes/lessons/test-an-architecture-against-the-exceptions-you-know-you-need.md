---
type: lesson
title: "Test a candidate architecture against the controlled exceptions experience says you will need"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Test a candidate architecture against the controlled exceptions experience says you will need

**Lesson:** Any scheme strict enough to be worth enforcing will turn out to need a small number of places where the rule is deliberately relaxed — one component that must see what everything else is forbidden to see, because it is doing the housekeeping that the rule itself makes necessary. Experience of building a real system, rather than reasoning about the scheme, is what reveals these, and their existence is not a defect in the discipline: the important property is that the relaxation be governed and enumerable rather than general. So a working system's most valuable output for the next design is its list of necessary exceptions, and any candidate replacement must be evaluated by whether it can express them.

This gives a sharp test that the usual comparisons miss. A proposed architecture is normally judged on the properties it guarantees and the operations it makes cheap. Judge it instead against your known exception list: if a scheme cannot accommodate the specific relaxations you have already learned you require, it does not matter how attractive its guarantees are, because the first thing you will do with it is defeat it in an ungoverned way. A design whose purity has no provision for the exceptions you know about will not stay pure; it will acquire them anyway, without the control.

It follows that the exception mechanism deserves to be designed with the same care as the rule. The relaxations should be individually authorized rather than blanket, each one held by a named component with a stated reason, and the list should be short enough to review. That posture is what lets you say the discipline holds while admitting that it does not hold everywhere — a much stronger and more honest position than either universal enforcement, which will be quietly violated, or vague enforcement, which cannot be audited.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's statement that experience designing the operating system showed very clearly the importance of being able to relax the protection rules in a controlled manner, referring back to Chapter 1's example of the post-interrupt housekeeping procedure given data-type access to a segment that everything else reaches only through capability-type access, and the resulting judgment that the tagged architecture as described would not provide the necessary flexibility.
