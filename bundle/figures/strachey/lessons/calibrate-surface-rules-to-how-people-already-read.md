---
type: lesson
title: "Calibrate surface rules against how people already read the notation, not against internal regularity"
figure: strachey
works: [the-main-features-of-cpl]
axes: [cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics]
tags: [lesson]
---
# Calibrate surface rules against how people already read the notation, not against internal regularity

**Lesson:** Where a notation overlaps one your users have been reading all their lives, the rules governing its surface have a correctness criterion that is not internal: they are right when the meaning the system assigns to a written form agrees with the meaning a competent reader takes from it. That criterion cuts against uniformity. A perfectly regular scheme — every operator at one level, one associativity throughout — is easier to state and will systematically disagree with the reader on the cases they encounter most, because the existing reading practice is itself irregular in specific, well-worn ways. The right move is to work backwards from a handful of forms whose intended reading is unmistakable and choose the rules that reproduce those readings, accepting whatever irregularity results.

The same reasoning licenses forms that are not compositional at all if the existing practice treats them as ordinary. A chained comparison means, to any mathematician, a conjunction of the adjacent comparisons; providing it directly with that meaning is a concession to established reading rather than to convenience, and refusing it on grounds of grammatical purity would be a decision to disagree with every reader in order to keep a rule short. What makes this respectable rather than lax is that the concession is specific and the reasoning recorded: this form, this reading, because this is what the notation already means outside our system.

The failure mode on the other side is worth naming, because the argument can be abused. Matching existing practice is only a defence where a genuine external practice exists and can be stated. Where there is no established reading — a construct with no analogue outside the system — there is nothing to calibrate against and regularity should win, since the rule will be learned from your description and nothing else. So the discipline is to know, construct by construct, whether you are competing with a habit or creating one.

**Source:** [The Main Features of CPL](../works/the-main-features-of-cpl.md) — the numerical expressions section, whose system of precedence and association is justified by the close correspondence it produces in most cases between the language's interpretation of an expression and a mathematician's reading of it on paper, illustrated by a quotient with an implicit product in its denominator; together with the introduction of extended arithmetic relations, where a chained comparison is defined to mean the conjunction of the adjacent ones.
