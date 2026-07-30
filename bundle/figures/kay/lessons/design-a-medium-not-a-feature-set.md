---
type: lesson
title: "When the users' needs are genuinely unbounded, ship a medium plus exemplars instead of enumerating features"
figure: kay
works: [personal-dynamic-media]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# When the users' needs are genuinely unbounded, ship a medium plus exemplars instead of enumerating features

**Lesson:** There is a class of system whose intended audience is so varied that no requirements process can converge, and the honest response is to stop trying. Enumerating and anticipating the needs of everyone produces a bloated pile of half-fitting facilities that serves nobody well, because each added feature is a guess about one user paid for by every other user in weight and confusion. The alternative is to classify your artifact correctly first. Some things — an appliance, a vehicle — commit to a fixed set of anticipated uses and force anyone with a different intent into heroic effort. Other things — paper, clay — offer dimensions of possibility rather than functions, and get used in ways their makers never imagined, at the cost of requiring the user to make or find tools. The design error is building the first kind while promising the second kind's reach.

The move that resolves this is to divide the problem rather than solve it: transfer the specification of the tool to the person who actually knows what the tool is for, and make your own job the construction of a substrate expressive enough that they can state their intent casually. That relocation is only legitimate under two conditions, and both are load-bearing. The substrate has to be uniform enough that describing a new tool is an ordinary act rather than a systems-programming project, and the library of already-built tools has to be rich enough that nobody starts from scratch for anything common. Ship the substrate without the exemplars and you have merely renamed your unfinished work as the user's freedom.

This reframes what generality means. Generality is not a large surface that covers many cases; a large surface is precisely the hodgepodge. Generality is a small, composable vocabulary in which the cases can be *written*, plus enough worked examples that writing them is imitation rather than invention. The diagnostic to apply to your own design: if a user with an unanticipated need would have to petition you for a feature, you built the inflexible kind of thing, whatever your documentation claims.

**Source:** [Personal Dynamic Media](../works/personal-dynamic-media.md) — the closing argument on whether a machine meant for everyone must collapse under the weight of being too many tools for too many people, the contrast between mass items that anticipate uses inflexibly and materials like paper and clay that offer open dimensions, and the stated design strategy of transferring specification to the user while supplying a general communication medium and a stock of pre-written tools.
