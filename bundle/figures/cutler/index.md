---
type: figure
title: David Cutler
description: b. 1942, DEC/Microsoft. Architected RSX-11M and VMS at DEC, then led Windows NT's kernel design.
status: accepted
layer: implementation-mapping
subdomains: [operating-systems-and-systems-programming]
tags: [figure, accepted]
---

# David Cutler

**Dates:** b. 1942. American software engineer.

## Why a candidate
Personally engineered VMS and then NT's kernel, embodying disciplined, mechanism-first kernel engineering carried across two major commercial OS families over five decades.

## Top 10 most influential works
Non-publishing systems builder — no confirmed academic papers found. Output is shipped code and internal design documents, not publicly accessible:
1. VAX/VMS operating system (DEC, 1977) — the artifact itself — `not applicable` (shipped commercial software)
2. Windows NT kernel (Microsoft, 1993) — same — `not applicable`
3. Computer History Museum oral history interview — `public`

Does not fit the "top 10 works" format — flagged plainly rather than inventing papers he didn't write. Worth the vetting round confronting this directly: a lot of foundational systems work never got written up as papers.

## Phase 3 access flag

Confirmed at source-discovery time: this figure has no academic papers, public design
specs, or self-archived writing of any kind. Two genuinely public, citable artifacts
were found and formalized into `work` files:

1. `works/oral-history-of-david-cutler.md` — CHM oral history, Feb 2016, ~3 hours,
   first-person walkthrough of his whole career (institutional host, CHM's own
   archive subdomain).
2. `works/decwest-sdt-agenda-prism-vs-mips.md` — a slide deck Cutler personally
   authored and presented internally at DEC, May 30 1988, on whether to keep funding
   PRISM or switch to MIPS (third-party-rehost, bitsavers.org preservation archive).
   Historically load-bearing: this is the internal argument that preceded PRISM's
   cancellation and his move to Microsoft to build NT.

Other candidates turned up and were deliberately excluded, not overlooked:

- **VAX/VMS and Windows NT themselves** — shipped commercial software, not citable
  documents. Left as `not applicable` per the stub.
- **DEC's internal Mica design documents** (bitsavers.org/pdf/dec/prism/mica/ —
  Object Architecture, Process Structure, Internal System Services, etc.) — these
  describe the OS Cutler's team built at DECwest (Mica/PRISM, NT's direct ancestor),
  but each one checked is issued by a named team member (e.g., Lou Perazzoli, Mark
  Lucovsky), not by Cutler. Team artifacts under his leadership, not his authored
  work — excluded to avoid misattribution.
- **PRISM architecture/system reference manuals** (same bitsavers directory) — same
  issue, DEC engineering-team documents, not personally authored by Cutler.
- **"880811_Cutler_resignation.pdf"** (bitsavers) — despite the filename, this is an
  internal email from a colleague (Myles Connors) announcing that Cutler's
  resignation was accepted, not anything Cutler wrote. Excluded as misattributed.
- **"890619_Cutler_1st_anniversary.pdf"** (bitsavers) — a satirical "June fools"
  email Cutler himself posted a year after PRISM's cancellation, genuinely authored
  by him and publicly archived, but pure in-joke humor with no design content worth
  a Phase 4 lesson pass. Excluded as too thin to count as a work.
- No Charles Babbage Institute interview, no USENIX/ACM keynote transcript, and no
  DEC Technical Journal paper under his name turned up in search.

Net: the "no papers" framing in the Phase 1 stub holds. What exists instead is one
institutional oral history and one archived internal strategy document he personally
wrote — genuinely thin, but genuinely public and citable, which is the bar this pass
sets.
