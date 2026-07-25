---
type: lesson
title: "Give an identifier exactly one job: a key that also means something can never change"
figure: bachman
works: [the-programmer-as-navigator, oral-history-charles-bachman]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management]
tags: [lesson]
---
# Give an identifier exactly one job: a key that also means something can never change

**Lesson:** Identity and meaning have opposite change profiles. An identifier must stay fixed for the lifetime of the thing it names, because everything else refers through it; a meaningful attribute must remain free to change, because the world it describes changes. Loading both jobs onto one value therefore builds a contradiction into the design: the moment the meaning needs updating, either the identity of the record breaks everywhere it is referenced, or the meaning is frozen forever. In the Turing lecture Bachman notes this from the identity side — real systems key on account numbers and policy numbers, values manufactured purely to be unique, precisely because natural attributes like names and dates cannot be trusted to be unique or stable.

The oral history supplies the confession that makes the rule vivid. In his own transaction-dispatching design, Bachman used one code as both the primary key of a record type and the value controlling its processing priority. The consequence surfaced in production: priorities could never be retuned, because changing the value meant changing the key. The users' fix is the general recipe — add a separate field for the meaning, maintain a second ordering on it, and let the key go back to doing nothing but naming. He recounts this as the kind of error a designer makes exactly once.

The habit of mind generalizes well past database keys: whenever one value is doing two jobs whose rates of change differ, the design has coupled things that will need to move independently. A programmer who believes this mints synthetic, meaning-free identifiers by default, keeps every mutable or business-significant attribute out of anything used as a name, and reviews designs by asking of each field: if this value had to change tomorrow, what else would break?

**Source:** [The Programmer as Navigator](../works/the-programmer-as-navigator.md) — the early discussion of primary data keys as synthetic, uniqueness-only attributes. [Oral History: Charles Bachman](../works/oral-history-charles-bachman.md) — the Problem Controller design-error story in the Weyerhaeuser section, told against himself.
