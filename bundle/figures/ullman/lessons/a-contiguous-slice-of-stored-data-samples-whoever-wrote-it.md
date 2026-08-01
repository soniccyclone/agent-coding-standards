---
type: lesson
title: "A contiguous slice of stored data samples whoever wrote it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# A contiguous slice of stored data samples whoever wrote it

**Lesson:** Drawing a proper random sample from a large stored collection requires reading all of it, deciding for each record independently whether to keep it. That is expensive, and there is an obvious-looking economy available: take the first however-many records, or grab a few storage blocks at random, and treat the result as a sample. The economy is real and so is its cost, which is that you have not sampled the records at all. You have sampled the process that laid them down.

Physical layout is never arbitrary. Records land in the order they arrived, which makes position a proxy for time; blocks are placed by whichever ingestion job or tenant or region produced them, which makes block identity a proxy for source. A prefix is therefore a sample of the past, and it will faithfully report a world in which whatever became popular later does not exist. A handful of blocks is a sample of a few sources, and if sources differ in their conventions — different instrumentation, different equipment, different local practice — the sample reports one convention's data as though it were everyone's. Neither failure produces an error, an anomaly, or a warning. Both produce a clean, self-consistent, thoroughly wrong picture, and the wrongness is invisible from inside the sample because the sample has no record of what it is missing.

The distributed case deserves separate attention because the layout there is doing something people forget it is doing. Chunks in a distributed store feel like an implementation detail, a mechanical division for parallelism, so choosing chunks at random feels like choosing data at random. It is not, because the chunk boundary usually coincides with a real-world boundary: one upload, one day, one customer, one site. Whatever variable the boundary encodes is the variable your sample is now stratified on, with a stratum count equal to the number of chunks you took, which is small. Parallel processing frameworks inherit the same problem in their default partitioning, so a job's per-partition statistics can differ wildly for reasons that have nothing to do with the data's actual structure.

The rule to carry away is that a sampling shortcut is only sound if you can name what the storage order encodes and argue it is unrelated to what you are measuring. Sometimes you can, and the shortcut is then correct and worth taking. When you cannot, the choice is between paying for the full scan and paying an unbounded, undetectable bias, and the second is not cheaper — it just moves the cost somewhere that never gets billed to the sampling decision. The instinct to develop is that "random position" and "random record" are different things, and the difference lives entirely in facts about the writer that the reader cannot see.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 6's boxed aside on why one should not simply take the first part of the file when sampling baskets, which contrasts a per-basket independent selection against taking a prefix of a date-ordered sales file (old data, no recently popular products) and against picking random chunks of a distributed file whose chunks each come from a different hospital.
