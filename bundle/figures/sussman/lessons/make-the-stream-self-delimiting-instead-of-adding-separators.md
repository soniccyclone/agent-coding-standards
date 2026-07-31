---
type: lesson
title: "Design the encoding so boundaries are unambiguous, rather than marking them"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [primitive-count, verifiability]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Design the encoding so boundaries are unambiguous, rather than marking them

**Lesson:** Once symbols get codes of different lengths, a reader of the bit stream has a new problem it did not have before: knowing where one symbol ends. There are two families of answer. Morse code takes the obvious one — add a pause, an out-of-band marker whose only job is to say "boundary here." The alternative is to constrain the code itself so that no symbol's encoding is a prefix of another's, at which point the reader can never be mid-symbol at a point where a complete symbol has already been spelled, and the boundaries fall out of the content with nothing added.

The generalization is a design choice you meet constantly and usually make by reflex: when a stream of things must be parsed apart, do you spend a symbol on separation, or do you spend a constraint on the encoding? The separator is easier to invent and it is why so many formats have delimiters, escape characters, escaped escape characters, and a length field bolted on when escaping got out of hand. Its real cost is not the bits. It is that separators introduce a second alphabet whose members can collide with content, which is where the entire family of injection and framing bugs comes from — the parser cannot distinguish a delimiter that means "boundary" from the identical bits that meant "data."

Self-delimiting encodings pay their cost up front and in a different currency: a restriction on which codes you may assign. That restriction is a real loss of freedom, and it is checkable — prefix-freeness is a property of the code table you can verify once, before any data exists, rather than a property of every message you have to defend at parse time. Trading a runtime obligation for a static one is almost always the better side of that deal, and it is the same move as a type system, a balanced-parenthesis syntax, or a wire format whose every field is length-prefixed.

The deeper point is that ambiguity is not something a parser resolves; it is something the encoding either has or does not have. If the format admits two readings, no amount of care in the reader fixes it, only convention and heuristics that eventually disagree. So the question to ask of any representation is not "can I write a parser for this" but "is there exactly one parse, and what property of the encoding guarantees it." A prefix code answers that question with a structural invariant, which is why it can be decoded by a machine with no lookahead, no backtracking and no state beyond a position in a tree.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.3.4's introduction to variable-length codes, which raises the difficulty of knowing when a symbol has ended, contrasts Morse code's use of a separator pause after each letter with the alternative of designing the code so no complete symbol code is a prefix of another, names the latter a prefix code, and then shows decoding proceeding by walking a Huffman tree from the root and restarting at each leaf.
