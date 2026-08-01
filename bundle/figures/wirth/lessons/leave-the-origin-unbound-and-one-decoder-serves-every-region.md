---
type: lesson
title: "Leave the origin unbound and one decoder serves every region that shares the layout"
figure: wirth
works: [project-oberon]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Leave the origin unbound and one decoder serves every region that shares the layout

**Lesson:** A description of where things sit inside a region can be written two ways: with the addresses resolved, or as offsets from an origin the description declines to name. The second costs one extra parameter at every point of use and buys something that is easy to miss until it arrives — the description, and every tool that reads it, becomes applicable to any region laid out the same way. An inspector written to walk one activation record on a stack, given the frame pointer as an argument rather than reaching for it, walks every activation record; and if the compiler happened to describe a module's static data in the same offset-plus-type form, the very same inspector lists global variables when handed the module's static base instead. Nothing was designed for the second use. It falls out of having refused to bind the origin.

The habit worth taking from this is to notice when a capability arrives without being paid for, because that is diagnostic. A tool that suddenly covers a second case with no new code is telling you that an earlier decision — usually a representation decision, made for other reasons — imposed a uniformity you can now trade on, and there are generally more such cases nearby than the one you stumbled into. The converse is the more common situation and the more expensive one: when a second inspector has to be written from scratch for what is obviously the same kind of data, the duplication is not the problem but the symptom, and the cause is upstream, where two regions that could have shared a layout were described differently.

There is a limit to state alongside the technique, because unbound origins are exactly what make a description dangerous as well as portable. The description says nothing about which region it belongs to, so nothing in it can detect being applied to the wrong one; correctness rests entirely on the caller supplying an origin the description was meant for. That is an acceptable trade when the supplier is the mechanism that also chose the layout — a trap handler that got the frame pointer from the hardware, a loader that knows a module's base — and a bad one when the origin arrives from further away. Decide which case you are in before generalizing, and if the origin can come from anywhere, the description needs an identity too.

**Source:** [Project Oberon](../works/project-oberon.md) — the symbolic debugger of section 12.9, whose procedure `Locals` takes the base address of an activation record as a parameter and decodes each variable's name, offset and form from the object file's reference part, so that walking the dynamic chain requires only re-invocation with the next frame's base; and the remark that the same procedure, handed a module's static base instead, produces the listing of that module's global variables, which is what the `State` command does.
