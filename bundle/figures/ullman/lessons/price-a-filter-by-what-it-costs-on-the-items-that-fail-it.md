---
type: lesson
title: "Price a filter by what it costs on the items that fail it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, parallelizability]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Price a filter by what it costs on the items that fail it

**Lesson:** The cost of a screening step is dominated by the population it rejects, because in any selective workload that population is nearly everything. Yet screens are habitually evaluated by how well they behave on the items they accept — how few false positives survive, how cheap the follow-up comparison is — and the per-item cost of running the screen at all is treated as a constant that does not matter. It matters more than anything else. A screen that must read an entire object to decide charges the full price of examination to every object in the collection, including the overwhelming majority that will never be looked at again, at which point it has not saved the work it was supposed to save.

That turns the design question into one about how little of an object can be inspected while still producing a usable grouping key. Reading a fixed prefix is cheap but conflates everything that shares a boilerplate opening, which is exactly the structure real data has. Reading everything discriminates perfectly and defeats the purpose. Sampling a handful of positions, fixed once and used for every object, keeps the per-item cost at a small constant while being insensitive to shared prefixes, and pushes the full read down into the rare case where two objects actually collide. The full read still happens, but it now happens only on the accepted population, which is where it was affordable in the first place.

The general shape is a budget allocated by expected frequency rather than by importance. Work placed on the path every item takes should be constant and tiny; work proportional to object size belongs on the path only survivors take. This is the same instinct behind checking a cheap hash before a full comparison, checking a length before a string equality, testing a bloom filter before a disk seek, and comparing bounding boxes before geometry. In each case the second stage is not made faster; it is made rarer, and the first stage is kept from becoming a full pass in disguise.

The failure this guards against is specific and easy to walk into: a filter whose asymptotic cost is the same as the operation it was meant to avoid, wearing the clothes of an optimisation. The check is arithmetic and takes a minute. Multiply the per-item cost of the screen by the total item count, compare it against the cost of the work saved, and confirm that the first number is small. If the screen touches an amount of each item proportional to its size, that product is a full scan of the data, and the screen has to be justified on some other ground than saving time.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's discussion of finding identical documents, which rejects hashing on the first few characters because documents may share a common header, rejects hashing the whole document because it forces every character of every document to be examined, and settles on a hash of a few positions fixed at random in advance so that a document falling into a bucket of its own is never fully examined.
