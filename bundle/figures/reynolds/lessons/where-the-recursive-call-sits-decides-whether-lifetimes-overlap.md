---
type: lesson
title: "Whether a resource's lifetimes nest or pile up is decided by where the recursive call sits"
figure: reynolds
works: [the-craft-of-programming]
axes: [hardware-affinity, cognitive-load]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Whether a resource's lifetimes nest or pile up is decided by where the recursive call sits

**Lesson:** A recursive procedure that acquires a scratch resource — a buffer, a lock, a handle, a connection — has two arrangements available that look almost identical in the text and differ enormously in what they cost. Either the acquisition happens in a region that does not contain the recursive calls, or it happens in a region that does. In the first arrangement, every deeper activation has already released its resource before this one acquires, so the peak demand is the single largest instance. In the second, the whole chain of activations from the top of the recursion down to the deepest one holds its resource simultaneously, so the peak demand is the *sum* along a path in the call tree. Moving one declaration a few lines outward converts a bounded cost into one that grows with recursion depth.

The reason this is easy to get wrong is that the two arrangements are indistinguishable from the point of view of naming. Both give each activation a private copy; both are correct; both read as "a local." Visibility is a static question and the compiler answers it. Coexistence is a dynamic question about which activations are simultaneously live, and nothing in the declaration announces the answer. You get it by asking a different question entirely: from the point where this resource is taken until the point where it is dropped, does control ever re-enter the procedure? If yes, the resources stack up.

The habit to build is to reason about scope in terms of lifetime overlap rather than in terms of who can see the name — and, in a recursive setting, to locate every recursive call relative to every acquisition before estimating anything. The rule of thumb "declare things as locally as possible" is usually justified on grounds of readability and reduced interference; under recursion it also carries an order-of-magnitude claim about space, and that is the version worth remembering, because it is the one that fails loudly. It also pays to keep separate books on which part of the demand is an artifact of your arrangement and which part the method itself requires no matter how it is coded; only the first kind can be tuned away.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.2.2's space analysis of the merge-sorting procedure, where the temporary array is declared in a block that the recursive calls lie outside of, so all storage used by lower-level calls is released before the block using the temporary is entered and the blocks never overlap; together with the observation that moving that declaration outward to the block containing the recursive calls would make several arrays live simultaneously with combined size equal to the sum along a path in the calling tree, called a vivid instance of the importance of declaring arrays as locally as possible; and the closing remark that a substantial extra-storage requirement is inherent in the underlying method rather than removable by better coding.
