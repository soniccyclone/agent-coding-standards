---
type: work
title: "The Use of Name Spaces in Plan 9"
figure: pike
description: Introduces Plan 9's per-process name space as the system's core structuring idea, replacing the single shared Unix file tree with a private, mutable hierarchy each process can rearrange by mounting or binding resources into it. Every resource, local or remote, is represented as a file reachable through the 9P protocol, so union directories and per-process mounts do the isolation and composition work that later systems handled with bind mounts, chroot, and eventually container namespaces. It's the direct conceptual ancestor of Linux's namespace/mount-isolation model.
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
year: 1993
url: https://9p.io/sys/doc/names.html
access: public
host: institutional
tags: [work]
---

# The Use of Name Spaces in Plan 9

**Author(s):** Rob Pike, Dave Presotto, Ken Thompson, Howard Trickey, Phil Winterbottom
**Venue/year:** Proceedings of the 5th ACM SIGOPS European Workshop (Mont Saint-Michel, 1992); reprinted in ACM Operating Systems Review 27(2), April 1993, pp. 72-76.
**Source:** https://9p.io/sys/doc/names.html — live page, hosted on 9p.io, the official Plan 9 project documentation archive (originally plan9.bell-labs.com). PDF also available at https://9p.io/sys/doc/names.pdf.

## Lessons
_(empty — lesson extraction is Phase 4)_
