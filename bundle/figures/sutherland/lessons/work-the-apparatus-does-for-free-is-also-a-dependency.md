---
type: lesson
title: "Computation the apparatus performs for free is also a dependency on that apparatus"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-afips-1963]
axes: [hardware-affinity, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Computation the apparatus performs for free is also a dependency on that apparatus

Some of the hardest work a system does can be done by physics instead of by code. Sutherland's pointing mechanism never searches the drawing to find out what the operator means; the detector simply cannot respond to anything outside a small solid angle, so the act of aiming performs the first cut of the search in the optics, and only a handful of survivors ever reach a program. He names this for what it is — an analog computation supplied by the equipment — and it is the reason the identification of a pointed-at element costs almost nothing while a software equivalent would cost a scan over everything drawn. Looking for where the substrate is already computing something you were about to compute is one of the highest-leverage moves available.

The same passage contains the discipline that has to accompany the trick. Sutherland immediately notes that a display technology which holds its own image, rather than being repainted by the machine, destroys this free computation and may make the whole interaction style impractical. The leverage came from a property of the apparatus, so it is also a coupling to that apparatus, and the coupling is invisible in the code — nothing in the program says "requires a display that is redrawn under our control." Free work and hidden requirements are the same fact seen from two sides, and a designer who only notices the first side ships a system that mysteriously stops working when a component is upgraded.

So exploit the substrate, and write down what you exploited. When you lean on a device's timing, on a cache's geometry, on a coherence guarantee, on the fact that one hop is ordered, you have bought performance with a portability debt; record the assumption at the point of use so the next person can tell an accident from a requirement. The habit worth copying is not the specific reliance on optics — it is the pairing: identify the physical property that makes the cheap approach possible, then state the class of hardware that possesses it and the consequence if it is absent.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (AFIPS 1963)](../works/sketchpad-a-man-machine-graphical-communication-system-afips-1963.md) — the opening of the light-pen section, which frames the detector's limited field as an analog computation that saves program time, then remarks on the display technologies for which the same design would not work.
