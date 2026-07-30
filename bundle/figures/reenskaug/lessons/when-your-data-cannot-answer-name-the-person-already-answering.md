---
type: lesson
title: "When your data cannot answer the question, find the person already answering it and name the role"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# When your data cannot answer the question, find the person already answering it and name the role

**Lesson:** Building information systems for decision makers, this team kept hitting the same wall: the information the decision maker actually needs is surprisingly often not derivable from anything in the organization's computer systems. Not hard to query, not scattered — absent. The natural engineering responses all fail, because better integration, better queries, and better models are all transformations of data, and no transformation produces information the inputs do not contain. That is worth stating as a category: some requirements are not retrieval problems wearing a disguise, and continuing to treat them as such produces indefinite effort with no result.

The move that works is to look for the person already supplying the missing input. In these organizations someone was collating from many sources, weighing what was credible, interpreting it, and passing on a digested view — doing exactly the work no query could do, and doing it informally, off the record, as an unnamed part of somebody's day. The intervention was to make that a declared role in the organization with a name, and route it through the same system as everything else.

The three properties that formalization buys are the payoff, and they are worth separating. It becomes *visible*, so the organization knows this work exists and how much of it there is, which is a precondition for staffing it or noticing when it stops. It becomes *respectable*, so the effort is legitimate rather than something absorbed at the margin of a job description that does not mention it — which matters because unnamed work is the first thing cut under pressure and the last thing anyone is credited for. And it becomes *repeatable*, so it survives the departure of whoever was quietly doing it, which is otherwise a single point of failure nobody has noticed because it was never on a diagram. Nothing about the work changes; what changes is that the system now has a place for it.

The reflex generalizes past decision support. Any time a system's data provably cannot answer a question people nevertheless answer every day, the missing capability is human judgment operating off the books. The design task is to locate it, name it, and give it a supported channel — not to model harder. The corollary is a warning about automation projects: a workflow that appears to consist of retrieval steps may depend on an unnamed interpretive step, and automating the visible steps while eliminating the invisible one removes the only part that was supplying the answer.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 10 section 10.3 on Business Information Systems, which reports that information essential to decision makers surprisingly often cannot be derived from what is available in enterprise computer systems, so it must come from skilled personnel; describes introducing the Information Editor as a new organizational role — a highly competent person who collates from many sources, evaluates and interprets, and presents digested results through the common information system; and notes the work is not new but done informally in most organizations, with official introduction making it visible, respectable and repeatable.
