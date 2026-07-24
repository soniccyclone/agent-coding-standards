---
type: figure
title: Amir Pnueli
description: 1941-2009, Weizmann/NYU. Introduced temporal logic as the specification language for concurrent/reactive properties. Turing Award 1996.
status: accepted
layer: implementation-mapping
subdomains: [formal-methods-and-verification]
tags: [figure, accepted]
---

# Amir Pnueli

**Dates:** 1941-2009. Israeli computer scientist, Weizmann Institute/NYU.

## Why a candidate
Introduced temporal logic as the specification language for concurrent/reactive program properties, founding the branch of verification that model checking later automated.

## Top 10 most influential works
Fewer than 10 distinct works confidently identified:
1. "The Temporal Logic of Programs" (1977, FOCS) — `unavailable` (see Phase 3 access flag)
2. "The Temporal Logic of Reactive and Concurrent Systems: Specification" (1991, with Manna) — `paywalled`, confirmed (see Phase 3 access flag)
3. "Temporal Verification of Reactive Systems: Safety" (1995, with Manna) — `paywalled`, confirmed (see Phase 3 access flag)
4. "On the Synthesis of a Reactive Module" (1989, with Rosner) — `paywalled`, confirmed (see Phase 3 access flag)

## Phase 3 access flag
Verification pass (2026-07-24) found **zero** of the four listed works publicly accessible. No `work` files were created for this figure.

- **"The Temporal Logic of Programs" (1977, FOCS)** — this is the single work the "why a candidate" case rests on (it's literally the paper that introduced temporal logic to CS). Checked: Unpaywall (`oa_status: closed`), Semantic Scholar API (`openAccessPdf.status: CLOSED`), IEEE Xplore/ACM (paywalled, no author-side OA program covers 1977 FOCS), Pnueli's own Weizmann homepage bibliography (recovered via Wayback Machine snapshot of `wisdom.weizmann.ac.il/~amir/c-and-j.html`, 2005) — listed as a plain citation with no download link, Zohar Manna's Stanford homepage and self-archived papers directory (`theory.stanford.edu/~zm/papers/amir/`) — dozens of other Manna/Pnueli papers are self-archived there but not this one, and general web search for course mirrors/scanned copies. No legitimate public copy exists anywhere. This is a real gap: the corpus's flagship Pnueli work is undiscoverable through legal open channels.
- **"...Specification" (1992, Springer)** and **"...Safety" (1995, Springer)** — both confirmed `closed` via Unpaywall against their Springer DOIs. Scan-piracy sites (epdf.pub, vdoc.pub) turned up copies but don't qualify as legitimate hosts under the sourcing rules, so excluded.
- **"On the Synthesis of a Reactive Module" (1989, POPL, with Rosner)** — ambiguous: Unpaywall flags this `oa_status: gold` pointing at `dl.acm.org/doi/pdf/10.1145/75277.75293` (likely a stale record from ACM's old free-access-to-older-content program), but every fetch attempt (WebFetch, curl with multiple browser user-agents) hit an ACM Cloudflare bot-check wall ("Just a moment...") rather than actual content — couldn't satisfy the "verify the URL actually resolves" rule. ResearchGate and Academia.edu mirrors both required login (403). Treated as unconfirmed/excluded rather than risk citing a link that doesn't actually deliver the content.

Net effect: Phase 4 lesson extraction for `pnueli` will have no seminal-work source material unless this gap is revisited (e.g. with institutional/IEEE access, or if ACM's Cloudflare block is bypassable through legitimate means).

## Next steps for a fresh pass (not yet tried)
Nathan cares about getting Pnueli's material into the corpus (functional reactive
programming lineage). Leads worth checking that this pass didn't reach:

- **Item 4's `dl.acm.org/doi/pdf/10.1145/75277.75293` specifically** — Unpaywall
  tags this `oa_status: gold`, meaning ACM's own metadata says it should be free,
  but every fetch here hit a Cloudflare "Just a moment..." bot-check rather than
  real content. Worth a retry with a different fetch approach (real browser
  session, different UA, or just checking whether the block was transient).
- **Amir Rosner's own page** (co-author on "On the Synthesis of a Reactive
  Module," 1989) — only Manna's and Pnueli's self-archives were checked, not
  Rosner's.
- **CORE.ac.uk or BASE** (academic aggregators) — these sometimes mirror the
  actual PDF behind a "gold OA" Unpaywall tag rather than just linking back to
  the paywalled publisher copy.
- **NYU's institutional repository** — Pnueli was NYU faculty later in his
  career; only his Weizmann homepage (via Wayback) was checked.
- **Direct Google Scholar search** on all four titles — sometimes surfaces a
  rehost that Unpaywall's crawler missed entirely.
