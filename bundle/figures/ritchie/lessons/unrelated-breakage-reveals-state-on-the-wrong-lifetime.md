---
type: lesson
title: "When a new mechanism breaks something unrelated, you have found state attached to the wrong lifetime"
figure: ritchie
works: [evolution-of-the-unix-time-sharing-system]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# When a new mechanism breaks something unrelated, you have found state attached to the wrong lifetime

**Lesson:** The day process creation was added, the command for changing the current directory stopped working, and Ritchie describes the team reading code and searching their consciences over how those two things could possibly be connected. The answer was that they were connected all along and nobody could see it. Previously there was exactly one process per terminal, so a command that adjusted its own current directory adjusted the only one that existed. Once each command ran in a freshly created process that promptly died, the change went with it. Nothing about the directory logic was wrong; the state it modified had simply been living on an entity whose lifetime had just been shortened underneath it, and only the change of lifetime made the misattribution visible.

The same diagnosis arrives a second time, later and more expensively. The position at which the next read or write to an open file would occur was kept inside the process that opened the file. That is invisible until a script redirects its output and runs two commands in sequence: each command inherits a copy of the position rather than sharing it, so the second one starts writing at the beginning and destroys the first one's output. The fix was structural — a table holding those positions independently of any process — because the underlying error was a category error about ownership. A read/write position belongs to an open file, which several processes can legitimately share; it never belonged to a process at all.

Generalizing: a piece of mutable state has a natural owner, defined by the scope over which it must remain coherent. Systems accumulate state parked on whatever object happened to be convenient, and that mistake is undetectable as long as the convenient object's lifetime coincidentally matches the required one. Introducing concurrency, retries, request scoping, or any new unit of creation and destruction breaks the coincidence, and the resulting failures look bizarre and unrelated because the reasoning chain runs through an ownership assumption nobody wrote down.

A programmer who believes this treats "this new feature broke something that has nothing to do with it" as a specific, recognizable diagnosis rather than a mystery, and goes hunting for state whose home was chosen by convenience. Better, they ask the ownership question up front: for each piece of mutable state, over what scope must it stay coherent, and does the thing holding it live exactly that long. When the answer is no, they move the state rather than patching the symptom, because every future change to lifetimes will otherwise produce another one of these.

**Source:** [The Evolution of the Unix Time-sharing System](../works/evolution-of-the-unix-time-sharing-system.md) — the process-control section's two aftereffects of introducing fork: the directory-change command silently losing its effect, and the file read/write pointer having to be relocated out of the process into a shared table.
