---
type: lesson
title: "Change what pays off instead of enumerating the shapes of the attack"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Change what pays off instead of enumerating the shapes of the attack

**Lesson:** There are two ways to stop a system from being exploited, and they have completely different long-run economics. The first is to recognise the exploit: catalogue the configurations attackers currently use and filter them out. The second is to alter the rule that decides outcomes, so that the configuration stops producing the gain in the first place. The first is a loop — every filter you add prompts a variant that evades it, and the space of variants on any structural signature is effectively unbounded, so your maintenance cost grows with the attacker's creativity while theirs stays flat. The second is a single change whose effect does not depend on knowing which variant is in front of you.

The choice is often disguised as a question about detection accuracy, which is the wrong frame. The question is whether your defence has to enumerate. A rule that says "reject inputs matching these patterns" enumerates, no matter how sophisticated the matcher; a rule that says "value derived from sources of this kind counts for less" does not, because it prices the whole category rather than recognising members of it. This is why quantifying the benefit an attacker extracts is such a useful exercise even when you have no intention of building a detector. Writing down the amplification a given structure yields as a function of your own tuning parameters tells you which parameters the exploit depends on, and that is exactly the set of levers that can defeat it categorically.

Two caveats keep this from being a slogan. First, categorical repricing has collateral damage: legitimate participants who resemble the repriced category pay too, and you should know who they are before shipping it. That cost is usually acceptable and always worth naming, whereas the same cost hidden inside a pattern matcher shows up as unexplained false positives. Second, the two approaches are not mutually exclusive, and the sane posture is to use enumeration only for the immediate, expensive-to-tolerate cases while the repricing does the structural work. What is not sane is enumeration as the whole strategy, which is how a team ends up with a rules file that only grows and a defence whose effectiveness quietly decays between releases.

The general habit: when you find yourself writing a rule that describes what the bad thing looks like, stop and ask what the bad thing is trying to obtain, and whether you can stop paying it. Descriptions of appearance age badly and require constant attention. Descriptions of value do not.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the link-spam section of the link-analysis chapter, which computes the amplification a spam farm achieves as a function of the taxation parameter, notes that structural detection invites endless variation, and turns instead to score-level modifications that lower such pages automatically without locating the structures.
