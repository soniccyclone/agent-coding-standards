---
type: lesson
title: "Every detail you refuse to expose is expressive power you have spent"
figure: abiteboul
works: [foundations-of-databases]
axes: [expressiveness, hardware-affinity]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Every detail you refuse to expose is expressive power you have spent

**Lesson:** Hiding the representation is usually discussed as pure gain, since it buys portability and freedom to re-implement. This work makes the cost side precise and quantitative. Once a language is required to treat data values as interchangeable tokens with no properties beyond the relationships the data itself records, certain trivially computable things become unstateable. Counting a set modulo two is the standard witness: on a machine that can see the encoding it takes a single pass, and in a language whose programs must respect renaming it is beyond even loop-and-assignment query languages that are hard for polynomial space. The reason is structural. Deciding parity by repeatedly removing one element requires nominating a first element, and there is nothing in the abstract data to nominate with.

The second half of the argument is the more useful one for designers. Feed the same language an ordering of the values as ordinary input and the picture inverts: the fixpoint-style language now expresses exactly the polynomial-time properties and the loop-based one exactly the polynomial-space properties. One extra piece of structure at the interface, an ordering nobody would call a feature, moves the language from having no clean complexity characterization at all to matching complexity classes on the nose. Exposure is therefore a dial with a measurable reading, and the reading is in units of what becomes expressible and how hard it becomes to compute.

The habit to build from this is to price your hiding decisions instead of assuming they are free. When you decide that callers may not see insertion order, or physical locality, or the identity of the node that holds a shard, ask what class of computations you have just moved out of reach and whether anything you need lives in it. Often the right answer is to hide the representation and then hand back one carefully chosen structural fact, since a single well-chosen exposure can restore an enormous amount of power while leaving the rest of the representation free to change. The wrong answer is to hide everything, discover something essential is now inexpressible, and win it back by smuggling representation access through a side channel that no longer has any stated contract.

**Source:** [Foundations of Databases](../works/foundations-of-databases.md) — the closing discussion of the chapter that sets up expressiveness and complexity, where the parity example is used to show that restricting programs to representation-independent behavior can make a computation harder rather than easier, and the section on ordered inputs later in the same part, which treats the presence of an ordering as a suspension of data independence and then reads off the resulting exact correspondences with complexity classes.
