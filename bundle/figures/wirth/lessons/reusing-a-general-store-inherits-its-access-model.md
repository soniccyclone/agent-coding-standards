---
type: lesson
title: "Reusing a general store inherits its access model, not only its allocator"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [operating-systems-and-systems-programming, databases-and-data-management]
tags: [lesson]
---
# Reusing a general store inherits its access model, not only its allocator

**Lesson:** Representing a new kind of thing as an instance of a facility you already have is one of the strongest simplifications available. Hold each private collection as an ordinary object of the general store and an entire subsystem disappears: no reserved region, no second allocator, no separate administration of space, no tooling that has to be written twice. The simplification is real and should usually be taken. What is easy to miss is that you have inherited the general facility's *whole* contract, and the part of that contract that never comes up while you are thinking about space is who is allowed to look.

The general store's naming and access rules were settled when its contents were ordinary and shared. Placing private material inside it does not create a boundary; it places the material on the far side of a boundary that already exists and admits everybody. This becomes concrete when the same system also offers remote access to the general store, since the two features were designed independently and neither is wrong, yet their composition is that anyone who may use the sharing service may read anyone's private collection. Nobody decides this. It is a consequence of a representation choice made on space-management grounds, in a different section, months earlier.

The discipline is therefore to enumerate a facility's properties before adopting it as a representation — allocation, naming, enumeration, durability, and access — and to check the new content against each, rather than against the one that motivated the reuse. Where a property does not fit, you have three honest options and should pick one out loud: accept the exposure because the content does not warrant protection; add a measure at the content level, such as encoding what is stored, while stating plainly how weak it is and that it defends against casual inspection rather than against effort; or decline the reuse and pay for the separate mechanism. The failure mode to avoid is the fourth option, which is to take the simplification, add something that looks protective, and leave its strength unstated — because a protection whose strength nobody wrote down will be relied upon as though it were strong.

**Source:** [Project Oberon](../works/project-oberon.md) — section 11.2's statement that representing every mailbox as an ordinary file has the tremendous advantage that no special administration is needed for a reserved partition of disk store; and the remark following the server listing that this use of files for mailboxes, combined with the file distribution service residing on the same server station, allows anyone to access and inspect any mailbox, that no claim of secure protection against snooping is made, and that a minimal protective effort was undertaken by a simple encoding of the messages held in mailbox files.
