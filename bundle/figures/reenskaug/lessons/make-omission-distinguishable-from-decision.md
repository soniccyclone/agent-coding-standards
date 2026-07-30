---
type: lesson
title: "Require a redundant statement for every choice, so forgetting is distinguishable from deciding"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Require a redundant statement for every choice, so forgetting is distinguishable from deciding

**Lesson:** In a method where the programmer must decide, for each piece of state a thing holds, whether the new copy gets its own version or shares the original's, the convention adopted is that *every* piece must be mentioned — including the ones where the answer is "share it," which requires no code at all. Those get a statement assigning the field to itself: semantically nothing, syntactically a record that a human considered this field and chose. An automatic checker then flags any such method that fails to mention every field, so adding a new field to a type immediately reports the copy logic as incomplete.

The idea generalizes past copying, and the reason it works is that it repairs a specific blind spot in code review. Absence is invisible. A reviewer reads what is written and cannot see the field nobody thought about, because there is nothing on the page to notice — and the failure mode that actually happens is not choosing wrongly but never having considered the case, typically because the field was added later by someone who did not know this method existed. Requiring the null statement converts that absence into a presence: the field either appears, in which case someone decided, or it does not, in which case a tool says so. Nothing is left to memory or diligence.

Two properties make this worth the redundancy it costs. The check is mechanical and exhaustive over an enumerable set — the fields of a type — so it needs no understanding of the semantics to be useful, and it cannot be defeated by inattention the way a checklist can. And the no-op is doing real work despite compiling to nothing: it is a claim by an author, addressed to future readers and to the tool, that this case was examined. Code whose only purpose is to be counted is usually a smell, but here the thing being counted is human attention, which has no other representation.

The author notes the same discipline applies to other methods where a decision must be made per field. That is the transferable rule: wherever correctness requires a per-item judgement and the items are enumerable, demand an explicit mark for every item including the default one, and have a tool verify the marks are complete. Anywhere the default can be reached by silence, you have no way to tell a considered default from an oversight — and since the two are indistinguishable at review time, in practice you must assume the oversight.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 11 section 11.4.2's footnote on the postCopy convention: the dummy statement `palette := palette` does nothing with the reference, and the Taskon convention is that every instance variable shall be assigned a value in postCopy to show that the programmer has considered it, so that when a new instance variable is added to a class the automatic quality checker flags the postCopy method as incomplete — with the note that the same applies to other methods such as initialize and release.
