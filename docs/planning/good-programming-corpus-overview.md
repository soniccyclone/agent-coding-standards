---
type: project-overview
title: Good Programming Corpus — Project Overview
description: Codify "good programming" by vetting CS figures against a minimality/discovery standard, then consolidating their writing into an OKF knowledge bundle for Claude Code to reason from.
tags: [okf, epistemology, canon, claude-code]
---

> **FROZEN as of 2026-07-23.** Historical record of the project's original
> shape. Live figure status now lives in [ledger.md](ledger.md), execution
> mechanics in [technical-plan.md](technical-plan.md). Cite this file, don't
> edit it — including its "Status of figures" and "Next steps" sections below,
> both superseded.

# Good Programming Corpus

## Goal
Build a personal OKF (Open Knowledge Format) knowledge bundle that trains a coding
agent to reason from first principles about abstraction quality — not from corpus
frequency. The bundle has two layers:

1. **Reasoning primer** (foundation, read first, applies always)
2. **Vetted expert corpus** (content, read second, filtered through the primer)

## Format
Google's OKF, v0.1 (June 2026): a directory of plain markdown files with YAML
frontmatter. Only required field is `type`. Cross-links between files form the
knowledge graph. No SDK, no database, no vendor lock-in — just files, git-hostable,
readable by any tool.

## Methodology
Sit down with an AI (Claude Code) and walk the entire history of CS, figure by
figure. Explicitly approve or reject each one *before* ingesting their writing —
rejection is a first-class outcome, not a formality. The vetting criterion is not
fame or influence; it is whether the figure reasoned from irreducible primitives
or from inherited convention.

## Core standard (see `reasoning-primer.md`)
- **Minimality over frequency** — count irreducible primitives; prefer fewer.
- **Name the axis before ranking** — expressiveness, verifiability,
  parallelizability, hardware-affinity, cognitive load, primitive-count.
  Computability-class equivalence (Church-Turing) is equivalence of *extension*,
  not of *structure* — don't conflate the two.
- **Discovery, not invention** — mathematical/computational structures are
  discovered; the simplest sufficient representation is closer to their true form.
- **Default suspicion toward inherited convention** — imperative/stateful
  dominance in the corpus reflects 1950s hardware economics, not primitive-count
  minimality.
- **Vetting gate** — does the figure reason from primitives, or from convention?
  Church-style (reduction, composition) ranks above Turing-style (mechanism,
  state-table) by default, absent a stated axis to the contrary.

## Status of figures discussed so far
- **Church — accepted.** Lambda calculus: two primitives (abstraction,
  application), everything else derives. Minimal basis under the discovery
  framing.
- **Turing — rejected as a figure to emulate,** though his equivalence proof
  (TM ↔ lambda calculus, 1936–37) is retained as a fact, not a standard to
  reason from. Mechanism/state-table model treated as the more corpus-frequent,
  less minimal representation.
- All others (Dijkstra, Hoare, Knuth, Kernighan, Pike, Brooks, Lampson, Kay,
  Moore, etc.) — **not yet vetted.** To be run through the gate individually.

## Source material staged
- *The Art of Computer Programming* (Knuth) — ebook, InformIT, DRM-free
  (PDF/ePub/Mobi).

## Next steps in Claude Code
1. Load `reasoning-primer.md` as the first file the agent reads, every session.
2. Run candidate figures through the vetting gate one at a time; log
   accept/reject with the reasoning primer's criteria as the explicit rationale.
3. For accepted figures, extract writing into individual OKF concept files
   (`type: concept`, cross-linked to the primer and to each other).
4. Periodically re-derive an index/summary bundle for quick agent lookup.