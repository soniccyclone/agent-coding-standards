---
type: lesson
title: "Decide where in a data set's life you pay the cost"
figure: stonebraker
works: [mapreduce-and-parallel-dbmss-friends-or-foes]
axes: [hardware-affinity, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Decide where in a data set's life you pay the cost

Interpreting a record costs something, and the only real question is how many times you pay it. Do the work once at admission — parse, validate, fix a layout, arrange values so later access is direct — and every subsequent pass runs against a form built for it. Skip admission entirely, take the bytes as they arrived, and each pass rediscovers the structure from scratch. Neither is right in the abstract. The two designs are priced identically at one read, and diverge linearly after that, which means the deciding parameter is not a property of the system at all but an estimate of how often the data will be looked at again.

This reframes a whole family of arguments that get conducted as if they were about correctness or discipline. Enforcing structure at the boundary is not virtue and refusing to is not sloppiness; they are opposite bets on read count. Data that arrives, gets cooked into a summary, and is never revisited should never have been admitted through a validating front door, because the front door's cost is amortized over one use. Data that a hundred queries will cross should never be stored in the form it arrived in, because you are re-paying the decode a hundred times to save it once. The mistake worth naming is not choosing the wrong side but failing to notice a choice was being made — inheriting a default storage format and then blaming the execution engine for the parsing it does every pass.

The same accounting applies to the humans, which is why it generalizes beyond storage layout. Time to first result and steady-state throughput are separate budgets, and a tool that is slow to stand up but fast once running is straightforwardly correct for a workload that will run for years, and straightforwardly wrong for a question someone needs answered this afternoon about data they will throw away. A programmer who thinks this way stops asking which tool is faster and starts asking how many times this will be read, then reads the answer off the ratio.

**Source:** [MapReduce and Parallel DBMSs: Friends or Foes?](../works/mapreduce-and-parallel-dbmss-friends-or-foes.md) — the treatment of load-time versus query-time record interpretation in the architectural comparison, together with the earlier discussion of read-once and one-off-analysis use cases where paying for admission never pays back.
