---
type: lesson
title: "Objects are the right decomposition only when the state actually clusters"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, parallelizability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Objects are the right decomposition only when the state actually clusters

**Lesson:** A thing has state when its behaviour depends on its history, and its state variables are whatever carries enough of that history to determine what it does next — a balance rather than the transaction log, because for answering the only question anyone asks, the balance is the log's sufficient summary. That framing already contains a design decision most people skip: naming state is choosing what history you are entitled to forget, and the entitlement is relative to the questions the object must answer. Change the questions and the same variables stop being state.

The condition the authors attach is the part worth carrying, because it is a claim nobody usually makes explicitly. Objects in a system are rarely independent; they influence each other, and every interaction couples one object's state variables to another's. The view of a system as separate objects, they say, is *most useful* when the state variables group into tightly coupled clusters that are only loosely coupled to each other. That is a statement about the domain, not about programming style. Whether the object decomposition is right is settled by how the state of the thing being modelled is actually connected, and you can look.

So there is a real test available before you commit. Write down the state variables the system needs, ignoring where they might live, and then look at which ones move together. If they fall into groups whose members interact constantly and whose groups interact rarely, the boundaries are handed to you and the objects will be genuinely independent — which is what makes the model modular, and also what makes it parallelizable and testable in pieces. If the variables are uniformly entangled, no assignment of them to objects will produce independent objects; you will get objects whose every method reaches into another's, which is the familiar shape of a design that adopted objects as a default rather than a finding.

The corollary is that this is a diagnosis you can be wrong about and later correct. A domain whose state does not cluster is not thereby unmodellable — it is telling you to organize the program around something other than objects, which is exactly what the authors do next by offering streams as the alternative world view for the same systems. Two organizing strategies, chosen against the structure of what is being modelled. The failure is not picking the wrong one; it is not noticing that the choice was there.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - the opening of chapter 3 section 3.1, which defines an object as having state when its behaviour is influenced by its history, characterizes state by state variables maintaining enough information about history to determine current behaviour with the bank balance given as the summary standing in for the transaction history, observes that objects in a system are rarely completely independent and that interactions couple the state variables of one to those of another, and states that the view of a system as composed of separate objects is most useful when the state variables can be grouped into closely coupled subsystems that are only loosely coupled to other subsystems; together with the chapter introduction's presentation of object-based and stream-based organization as two world views of the structure of systems.
