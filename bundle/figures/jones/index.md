---
type: figure
title: Cliff B. Jones
description: b. 1944, Newcastle. Developed VDM specification/refinement formalism, then rely/guarantee reasoning for concurrency.
status: accepted
layer: implementation-mapping
subdomains: [formal-methods-and-verification]
tags: [figure, accepted]
---

# Cliff B. Jones

**Dates:** b. 1944. British computer scientist, Newcastle University; DPhil under Hoare at Oxford.

## Why a candidate
Developed VDM (Vienna Development Method) as a specification/refinement formalism, then extended Hoare-style reasoning to concurrency with the rely/guarantee method for interfering programs.

## Top 10 most influential works
1. "Software Development: A Rigorous Approach" (1980) — `public` (self-archived on author's site; see `works/`)
2. "Systematic Software Development Using VDM" (1986/1990) — `public` for the 1990 2nd edition (self-archived on author's site; see `works/`); no open copy found for the 1986 1st edition beyond the DRM'd archive.org controlled-lending copy
3. "Tentative Steps Toward a Development Method for Interfering Programs" (1983, TOPLAS, founding rely/guarantee paper) — `public` (third-party rehost; see `works/`)
4. "Specification and Design of (Parallel) Programs" (1983, IFIP) — unavailable, see Phase 3 access flag below

## Phase 3 access flag
"Specification and Design of (Parallel) Programs" (IFIP '83, pp. 321-332, North-Holland)
has no public copy anywhere checked: ACM/dl.acm.org and the IFIP proceedings are
paywalled with no Wayback snapshot of full text; ResearchGate hosts a PDF but blocks
automated fetch (403) and has no Wayback snapshot either; Jones's own Newcastle
publications page lists only a bare BibTeX entry with no self-archived copy; no
course-mirror or institutional copy turned up. Judged non-blocking for Jones's
"why a candidate" case: this paper covers the same rely/guarantee ground as two
works that *are* public and verified — his 1981 Oxford DPhil thesis "Development
Methods for Computer Programs including a Notion of Interference" (PRG-25, the
original source of the interference idea) and the 1983 TOPLAS paper "Tentative
Steps Toward a Development Method for Interfering Programs" (the founding
journal publication of rely/guarantee) — so the case doesn't depend on this
specific conference paper being available.

## Lessons
Jones's characteristic move is to convert a check that would land at the end into an obligation discharged at the moment of the decision, while that decision is still the only thing in view. He got there by failing to prove an existing program correct and finding redevelopment cheaper: an argument is not a certificate attached afterwards but a by-product of having built the thing a particular way, and nobody downstream can reconstruct why the designer believed a step held. So his test for any method, formal or not, is whether a completed step can be retroactively invalidated; if you can hand someone a subspecification and nothing else and still reject their correct work later, the modularity is an illusion that surfaces at integration. Rely/guarantee is that principle applied to shared state: write down the disturbance you tolerate and the disturbance you promise not to exceed, and independent development survives concurrency. He reaches first for naming assumptions, since an omitted assumption is a commitment rather than a silence and a stated one is a licence granted, not a check to perform. He refuses blanket prohibitions where an obligation would decide the case correctly; refuses state added to a program for the sake of reasoning about it, reading that as a diagnosis of the description rather than a technique; and refuses executable specifications, because the machine's needs win and the thinking model is lost. Rigour, for him, is spent locally: fix the skeleton absolutely, leave the leaves in prose, buy detail where doubt appears. And the whole discipline runs on modesty about its own reach, spend the confidence it buys on making the same systems safer, never on attempting harder ones.
