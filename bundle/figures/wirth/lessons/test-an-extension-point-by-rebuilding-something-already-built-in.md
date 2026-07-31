---
type: lesson
title: "Test an extension point by rebuilding something already built in"
figure: wirth
works: [project-oberon]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Test an extension point by rebuilding something already built in

**Lesson:** An extension mechanism is a claim, and like any claim it can be false while looking fine. The usual way it is false is that the mechanism admits exactly the additions its designer had in mind and quietly refuses everything else, because the information an extension would need was never exposed, or because the built-in behaviours reach state that no extension can reach. Nothing in the interface reveals this, and it is not discovered by writing more of the extensions the designer already imagined. It is discovered by picking an addition adversarially and trying to build it.

The best adversarial choice is a capability the system already provides internally. Take an operation the core performs intrinsically, and try to construct an outside variant of it using only what an extension is given. This test has a property that ordinary trial extensions lack: you already know the behaviour is achievable, so a failure is unambiguously a defect in the extension mechanism rather than a hard problem or an unreasonable request. It also probes exactly the places where privilege tends to hide, since the intrinsic operations are the ones written before the extension boundary existed and are therefore the ones most likely to depend on something never published. If the outside version comes out as a small assembly of exported parts, the boundary is real. If it requires reaching around the interface, or turns out to need a capability that only the core has, you have found the missing export while it is still cheap to add.

Two further returns make the exercise worth its cost beyond the verdict. The variants built during the test are usually worth keeping — an outside version of an intrinsic operation is generally more parameterizable than the intrinsic one, because it had to be assembled from parts rather than fused, so it can be pointed at things the built-in version cannot. And the collection of them, taken together, is the honest documentation of what the extension mechanism can do: a worked set of examples someone can imitate, rather than an interface plus an assurance. Do this early, while the core can still be changed. An extension boundary evaluated only after release is evaluated by people who cannot fix it.

**Source:** [Project Oberon](../works/project-oberon.md) — section 5.5, which frames the built-in editing operations of a text frame as an interpreter of intrinsic commands and the desire to extend that set with customized ones as the motivating problem; states that trying to add further tools seamlessly is a worthwhile test of any framework or basic toolbox, and presents the Edit module as the result of exactly that attempt; and notes that several of the resulting toolbox commands — copying a font to the selection and changing the font, colour and vertical offset attributes of it — are extrinsic variations of the intrinsic copy-look operation already provided by the frame itself.
