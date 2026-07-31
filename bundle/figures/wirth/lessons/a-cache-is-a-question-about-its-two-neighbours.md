---
type: lesson
title: "A cache is a question about its two neighbours, not about itself"
figure: wirth
works: [project-oberon]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A cache is a question about its two neighbours, not about itself

**Lesson:** Deciding whether to keep a computed or fetched result is usually treated as a local judgement — is this expensive enough to be worth remembering? That framing is wrong twice over, because a cache is not a local object. It sits between the layer it fetches from and the machinery that reclaims memory, and both of those neighbours have a veto. Ask them first, and the question of whether the operation is expensive often stops mattering.

Downward: find out what the layer you are fetching from already keeps. A great deal of caching in application code exists to avoid re-reading something from a store that was already going to serve the second read out of its own buffers, in which case the memoization buys nothing measurable and costs a coherence obligation forever — a second copy of the truth that must be invalidated when the first changes, and that will eventually not be. If re-deriving a value means re-reading a short span that the substrate is certain to still be holding, deriving it twice is not a compromise, it is the correct design, and it is worth saying so in the record so that a later reader does not mistake the absence of a cache for an oversight. The general rule is that a cache is only justified against a *measured* cost of the layer below, never against an imagined one.

Upward: a cache is a set of live references, and live references are exactly what stops a reclaimer from reclaiming. A structure that retains an entry for every distinct thing ever asked for will, in a process whose working set drifts — a long-running service handling varied requests rather than one user doing one job — accumulate everything it has ever seen. This is not a slow leak that tuning a size limit fixes properly; it is a category error about ownership. The clean resolution is to make the cache visible to the reclaimer as a weak association rather than a strong one, so that entries survive because something is still using them rather than because the cache remembers them. And the general shape of the failure is worth carrying beyond caches: any table that grows by insertion and never by intention, kept by a component that has no idea when its entries stop mattering, is holding memory on behalf of a decision nobody is making.

**Source:** [Project Oberon](../works/project-oberon.md) — section 5.3's remark, attached to the character-location and width procedures, that retaining character widths was found to be an unnecessary optimization because of the buffering capabilities of the underlying file system, so the text is simply re-read; and section 5.4's account of the font cache, where internalized fonts are held in a private list so that repeated internalization returns the cached copy, together with its acknowledged side-effect that a font used only briefly is thereby never collected, the print-server-with-many-large-fonts case in which memory fills with fonts nobody is using, and the conclusion that the only clean remedy in this and analogous cases is to make the cache known to the garbage collector.
