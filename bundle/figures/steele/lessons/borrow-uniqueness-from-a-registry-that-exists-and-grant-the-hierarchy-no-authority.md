---
type: lesson
title: "Borrow global uniqueness from a registry that already exists, and then grant the borrowed hierarchy no authority whatsoever"
figure: steele
works: [the-java-language-specification]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Borrow global uniqueness from a registry that already exists, and then grant the borrowed hierarchy no authority whatsoever

**Lesson:** A language that lets independently developed code be combined has to solve global name uniqueness, and the tempting answers are all bad: run a central registry (someone must operate it forever), hash the contents (names stop being readable and stop surviving edits), or hope collisions are rare (they are not, and they surface far from where either colliding name was written — a point this specification makes explicitly, noting that the resulting situation may be beyond the ability of either party to fix). The answer taken here is to piggyback on a uniqueness authority that already exists and that organizations already maintain for other reasons, reversing its components so the most general part sorts first. The specification is unusually candid that this is what it is doing: it says the scheme exists to avoid standing up a separate registry, and it then handles the mismatch cases — characters legal in the borrowed registry but not in identifiers, components that collide with keywords, components that begin with a digit — with mechanical rewrites rather than pretending the two name spaces are the same shape.

The second half of the decision is the part usually skipped, and it is where the design earns its keep. Having imported a hierarchical, meaningful-looking name space, the specification immediately strips the hierarchy of every power it might have seemed to carry. Nesting confers no privileged access: code in a nested name space has exactly the access to its parent that any unrelated code has. The name does not indicate where anything is stored or retrievable from, and the document says so with a worked non-example. The hierarchy's only load-bearing rule is a single prohibition that prevents one name from denoting two different kinds of thing. Everything else about it is organizational convenience for humans.

The reason to be that severe is that any authority attached to nesting immediately becomes the reason people nest. If a child name space gets extra access, the hierarchy stops describing what things are and starts describing who wanted to reach whom; the naming structure and the visibility structure become entangled, and neither can be changed independently afterward. Keeping them orthogonal costs a little expressiveness — you cannot say "these packages are family" in the name — and buys the freedom to reorganize names without changing any access relationship, and to change access without renaming anything.

A programmer who has absorbed this reaches for an existing uniqueness authority instead of inventing an identifier scheme: reversed domains, existing organizational identifiers, whatever the surrounding world already keeps unique for its own reasons — while spelling out the translation rules where the borrowed alphabet does not fit. And when designing any hierarchical name space, module paths, URL structure, config keys, topic names, they explicitly decide and then document that the hierarchy grants nothing, because the alternative is a system where the only way to obtain a permission is to be renamed into the right place.

**Source:** [The Java Language Specification](../works/the-java-language-specification.md) — the package-naming convention in the names chapter, together with the packages chapter's statement that the hierarchical structure has no significance beyond one prohibition and its worked example showing that a nested package receives no better access to its parent than any other package does.
