---
type: lesson
title: "A stable interface is a license to rebuild everything beneath it"
figure: stonebraker
works: [c-store-a-column-oriented-dbms]
axes: [expressiveness, hardware-affinity, primitive-count]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A stable interface is a license to rebuild everything beneath it

Independence between a logical model and its realization is usually pitched defensively: it protects existing programs from tuning changes. C-Store uses it the other way round, as an offensive weapon. Because callers only ever committed to tables, columns, keys, and a query language, the builders were free to decide that none of those things needed to exist in storage at all — no stored base tables, no secondary indexes, nothing that resembles the logical picture. What is written down instead is a set of sorted, compressed, overlapping fragments chosen to serve an expected workload, with auxiliary mappings that let full rows be reassembled on demand. The logical model was not weakened; it was made purely a contract, and everything below it became a free variable.

That reframing changes what a design review asks. If the interface really is the only commitment, then the question is not "how do we make our existing structures faster?" but "given this workload, what would we store if nothing were already stored?" — and the honest answer is frequently unrecognizable relative to the incumbent layout. The same reframing lets a resource that was bought for one reason be shaped to pay twice: copies kept for surviving node loss need not be identical copies, so ordering each one differently turns a pure insurance cost into a menu of access paths the planner can choose from. That trick is only available to someone who has already stopped believing the physical design must mirror the logical one.

The obligation this creates is that the freedom must be paid for with automation. Once physical design is an unconstrained search — which fragments, in which orders, partitioned how, replicated where — no human can be expected to solve it per installation, which is why the design assumes a tool that consumes a workload sample and emits the layout. A programmer who believes this keeps the public contract deliberately narrow and abstract, and treats every leak of physical detail through it as spending future latitude they will want back.

**Source:** [C-Store: A Column-oriented DBMS](../works/c-store-a-column-oriented-dbms.md) — the data-model section, which keeps standard relational logic and standard query semantics while storing only derived sorted fragments, plus the accompanying argument for automatic physical design and for non-identical replicas.
