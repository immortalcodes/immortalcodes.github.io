+++
title = "Juju Does Everything. Here Is What That Is Like."
date = 2026-08-08T13:40:00+08:00

tags = ["juju", "canonical", "kubernetes", "conference"]
author = "Madhur"
draft = false
description = "Why Juju's relation protocol beats Terraform, Ansible, and Helm at wiring services, and what running it in production at Canonical looks like."
summary = "Notes from my UbuCon Asia 2026 talk in Taipei, covering Juju's relation protocol, a live demo, and a debugging cheat sheet."
+++

Two weeks ago I flew to Taipei to give a talk at UbuCon Asia 2026, held alongside COSCUP at National Taiwan University of Science and Technology (NTUST). The session was called "Juju Does Everything. Here Is What That Is Like." and it was my attempt to answer a question I get asked a lot at work: why does Canonical still use Juju when everyone else has settled on Terraform, Ansible, and Helm?

Short answer: because none of those three tools talk to each other, and Juju's whole reason for existing is the gap where they meet.

**The talk, at a glance**

- Where: UbuCon Asia 2026 @ COSCUP, NTUST, Taipei
- When: August 8, 2026, Cloud and Infrastructure track
- Slides: [slides_Juju Does Everything.pdf](https://events.canonical.com/event/146/contributions/940/attachments/508/846/slides_Juju%20Does%20Everything.pdf)
- Full session listing: [events.canonical.com](https://events.canonical.com/event/146/contributions/940/)

![The Cloud and Infrastructure track room at NTUST, set up before the talk](/images/talks/juju-does-everything/venue.png)
*The room at NTUST, shortly before doors opened.*

![On stage at NTUST, opening the talk with why Juju exists](/images/talks/juju-does-everything/on-stage-wide.png)
*Opening with the question everyone actually came to hear answered: why Juju, when Terraform, Ansible, and Helm already exist.*

## The takeaway

Juju is operator knowledge, written down as code instead of trapped in someone's head. The relation protocol solves a problem the rest of the stack does not even attempt, but that power comes with a debugging model that stays opaque until you know exactly where to look. My goal for the talk was to hand the room that map: the mental model to trust Juju in production, and the commands to verify it instead of hoping.

![Mid-talk at NTUST, walking through the relation protocol live demo](/images/talks/juju-does-everything/on-stage-portrait.png)
*Mid-talk, walking through the relation protocol with a live demo.*

## Resources

- [Slides: Juju Does Everything (PDF)](https://events.canonical.com/event/146/contributions/940/attachments/508/846/slides_Juju%20Does%20Everything.pdf)
- [Full session listing on events.canonical.com](https://events.canonical.com/event/146/contributions/940/)
- [UbuCon Asia 2026 @ COSCUP](https://events.canonical.com/event/146/)
- [Juju documentation](https://documentation.ubuntu.com/juju/)

![The audience during the Q&A session at NTUST](/images/talks/juju-does-everything/audience.png)
*The room during Q&A — genuinely good questions.*

Taipei itself deserves its own separate post: the night markets, the boba tea logistics, and easily the best conference wifi I have used all year. For now, if you were in the room at NTUST, thank you for the good questions. If you were not, the slides above cover everything, minus the jokes.
