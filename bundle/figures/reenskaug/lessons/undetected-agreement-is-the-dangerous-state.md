---
type: lesson
title: "Known confusion is safe; it is the undetected mismatch that destroys projects"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Known confusion is safe; it is the undetected mismatch that destroys projects

**Lesson:** Two people discussing a system can be in three states, not two. They can understand each other. They can fail to understand each other *and know it*. Or they can each interpret the same words differently while both believing agreement has been reached. The second state is harmless — it is uncomfortable, it is visible, and it resolves itself because the discussion simply continues until things are clear. The third is where the large failures come from, and it is the only one of the three that feels like progress while it is happening.

That reframes what communication work is for. The goal is not to reach agreement, since apparent agreement is exactly the failure mode; the goal is to make disagreement *detectable*. Which means the useful moves are the ones that force interpretations into the open: restating the other party's position in your own words and having it corrected, working through a concrete instance rather than a general description, showing something running. All of these are ways of manufacturing the harmless second state on purpose so it cannot quietly become the third.

There is a sharp corollary about outcomes that most people get backwards. If delivery *exceeds* what the users expected, that is not a success to celebrate — it is evidence of the same defect. It means their understanding of what was being built diverged from what was built, and this time the divergence happened to fall in a pleasant direction. The specification or the communication was inadequate either way, and there is a real cost hiding in the good news: had they understood the full value, the work could have been scoped, priced, or prioritized differently, and probably would have come out better still. The success criterion worth holding is that people get exactly what they expected, in both directions.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 7's discussion of understanding the user community, which states that no harm arises from a mutual misunderstanding both parties are aware of and that the real danger is participants interpreting data differently without realizing it, claims misunderstanding is the mother of the most gigantic information-system failures, and separately argues that results exceeding expectations indicate poor specification or communication rather than success.
