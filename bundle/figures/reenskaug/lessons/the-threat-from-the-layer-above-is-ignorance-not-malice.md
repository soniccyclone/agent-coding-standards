---
type: lesson
title: "Assume your consumers are hostile, but expect ignorance rather than malice — and pair every restriction with completeness"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Assume your consumers are hostile, but expect ignorance rather than malice — and pair every restriction with completeness

**Lesson:** The stated assumption for anyone supplying a platform to another team is that the consumers are hostile — followed immediately by the correction that matters: sometimes by intent, but usually through ignorance of details that are of no interest to them. That second clause turns a security posture into a design principle. Someone indifferent to your internals will damage them at a far higher rate than someone attacking them, because indifference is the normal state and is not deterred by anything. And their indifference is legitimate: those details are precisely what your layer exists to relieve them of, so a consumer who has learned your internals in order to avoid breaking them represents a failure of the boundary, not a success.

What follows is that the boundary must be enforced rather than documented. A rule stating that consumers should not reach past the interface is satisfied by everyone who read it, which is not everyone. It should be hard or impossible for anyone above you to threaten the integrity of what is below, and the enforcement belongs in the tooling wherever it can be put there, because tools apply uniformly to the careless and the conscientious while procedures only reach the people already inclined to follow them.

The corollary is the part usually left out, and it is what keeps the principle from being merely restrictive: the facilities you provide must be *complete*, meaning they enable a consumer to do everything they are legitimately entitled to do. Restriction and completeness are not competing values to be balanced — completeness is what makes restriction survivable. A consumer who cannot accomplish a legitimate task through the sanctioned interface will accomplish it another way, and the workaround will be worse than whatever you were preventing: undocumented, unversioned, reaching into internals you intended to change freely. Every gap in coverage therefore converts directly into a violation of the boundary you were protecting. This is why an audit of a platform's interface should look for missing capabilities with the same seriousness it looks for leaks, and why "they shouldn't need to do that" is a claim to verify against actual usage rather than assert.

The complement is that within the space you have sanctioned, consumers get maximum latitude to exercise ingenuity. Secure the boundary mechanically, cover the whole legitimate need, then stop specifying how people work inside it.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 10 section 10.1's discussion of "firewalls" between value chain layers: actors are assumed hostile, sometimes by intent but usually by ignorance of details of no interest to them; production facilities must be secure so it is hard or impossible for an actor to threaten the integrity of the layers below; the corollary that facilities must be complete enough to let actors do everything they are authorized to do; procedures used at the actors' discretion with maximum freedom for ingenuity; and security automatically enforced in the tool portion where possible.
