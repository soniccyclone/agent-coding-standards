---
type: work
title: "On the Security of UNIX"
figure: ritchie
description: A short, unusually frank memo stating that Unix "was not developed with security, in any realistic sense, in mind" and walking through the concrete consequences — set-UID program risks, the dangers of unrestricted mount, weak default file permissions — along with practical mitigations available to administrators of the time. First circulated with the 6th Edition manual and later folded into the 7th Edition documentation, it reads more like an internal admission than a marketing claim.
subdomains: [operating-systems-and-systems-programming]
year: 1979
url: https://www.tom-yam.or.jp/2238/ref/secur.pdf
extraction: complete
survey_pages: 3
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# On the Security of UNIX

**Venue/year:** Originally distributed with the UNIX Programmer's Manual, 6th Edition (1975); the commonly cited version accompanies the 7th Edition (1979).
**Source:** https://www.tom-yam.or.jp/2238/ref/secur.pdf — third-party rehost on a long-running Japanese archive of historical Unix/PDP-11 reference documents. No surviving copy was found on Bell Labs' own site (the original bell-labs.com/usr/dmr/www address for this memo is gone with no Wayback snapshot, and it is absent from the current Nokia-hosted Bell Labs mirror of Ritchie's papers); this rehost's text matches the memo's known opening and content verbatim. Verified live.

## Lessons
- [An unbounded resource is a fault mode before it is an attack, so audit for missing limits rather than for attackers](../lessons/an-unbounded-resource-is-a-fault-mode-first.md)
- [Where a mechanism lends its authority, its inputs become the security perimeter](../lessons/lent-authority-makes-inputs-the-security-perimeter.md)
- [Individually logical rules compose into a policy nobody chose, so evaluate the composition against the property you wanted](../lessons/individually-logical-rules-compose-into-unchosen-policy.md)
- [Set a defensive parameter by paying the attacker's cost yourself, not by arguing about it](../lessons/set-the-parameter-by-paying-the-attackers-cost.md)
