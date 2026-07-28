---
type: lesson
title: "A general procedure is only communicable when a concrete instance is carried alongside it"
figure: knuth
works: [ancient-babylonian-algorithms]
axes: [cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A general procedure is only communicable when a concrete instance is carried alongside it

**Lesson:** A procedure and an example of the procedure running are different objects, and the second is not a lesser form of the first — it is the channel through which the first becomes intelligible to another mind. The scribal tradition Knuth examines had no symbolic algebra, so it stated general methods as a sequence of operations narrated over one particular set of values. The values were incidental; the shape of the operation sequence was the content. You can tell the shape was the content because the narration sometimes performs a step that does nothing at all for the particular numbers at hand, like a multiplication by unity: the instance is being bent to fit the general rule rather than the rule being specialized to the instance.

The counter-evidence is more instructive than the evidence. The handful of surviving procedures written with no numbers in them — pure operation sequences, the closest thing in the corpus to modern parameterized code — were the ones that resisted interpretation for decades. Nothing was missing from them logically; a reader who already knew the intended identity could follow them exactly. What was missing was the anchor that lets a reader who does *not* already know check their reading against something. Generality removes the thing you would have used to detect that you had misunderstood.

For a programmer this reframes the relationship between abstraction and documentation. Extracting a routine over its parameters is a real gain in reusability and a real loss in comprehensibility, and the loss is not paid by the author, who still remembers what the parameters meant. It is paid by every later reader, and it is paid at the worst moment, when they are trying to decide whether the code does what they think. The fix is not prose commentary about what the routine is for; it is a canonical traced instance — a test with real values, a documented example run — kept next to the general form and maintained as part of it. A worked instance is not an aid to the specification. In practice it is half of the specification, because it is the half a reader can independently verify.

**Source:** [Ancient Babylonian Algorithms](../works/ancient-babylonian-algorithms.md) — the discussion of why tablet procedures qualify as genuine algorithms rather than one-off answers, including the observation about steps carried out even when vacuous, set against the later remark on how badly the number-free procedures were understood.
