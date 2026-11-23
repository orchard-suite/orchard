---
name: propose
description: Send a decision about Orchard, the suite of core platform services, back to the suite as a GitHub issue. Use when a conversation settles what the suite is or is not, admits or removes a member, changes a pillar or its rating, moves the line between the suite and an estate, changes the quality framework, or decides something a suite member now owes.
---

# Propose a decision to the suite

The suite's documents learn from the work. Each proposal is one GitHub
issue on `orchard-suite/orchard`. The machine that owns that repository
folds each one into a decision record, the documents, the roadmap, and the
diagrams, and closes it with what it became.

## When

- A conversation settled what the suite is, or what it will not become.
- A tool was admitted, removed, or turned down as a member.
- A pillar, its rating, or what covers it changed.
- The line between the suite and an estate moved.
- A decision left a member owing something.

One decision per issue. A decision about how one app behaves goes in that
app's own repository, not here. A practice that holds on any platform goes
to the platform standard, not here. One conversation can produce both.

## Steps

1. Check `gh auth status` shows an account that can open issues on
   `orchard-suite/orchard`. If it does not, tell the person and stop.
2. Look first. Read the decision the proposal touches with the `consult`
   skill, and list the open proposals:
   `gh issue list -R orchard-suite/orchard --label proposal --state open`.
   Do not file what an accepted decision already says, or what an open
   proposal already asks.
3. Decide the origin. Work done for an employer is `work`; everything else
   is `personal`.
4. Write the issue:
   - **Title**: the decision, as a short statement ("The suite ships its
     documents as an agent plugin").
   - **Body**, with these headings:
     - `## Decision`: what is decided, in plain sentences.
     - `## Why`: the forces behind it, and what was turned down.
     - `## Touches`: `amends <number>`, `supersedes <number>`,
       `extends <number>`, or `new ground`, and the documents it changes
       (`pillars.md`, `members.md`, `seam.md`, and so on).
     - `## Owed`: what each member now owes, one line each. Leave it empty
       when nothing is owed.
     - `## Evidence`: a link to the commit, record, or pull request for
       personal work. Leave it empty for work.
5. Keep the suite's own rule: name no estate. Never name an employer, a
   company, a customer, a work system, a household, a person, a domain, a
   host, or a repository that belongs to one estate. Say "an estate", "a
   work estate", or "the home estate". Never use a phrase that places the
   decision at an employer, such as "at work" or "my company".
6. File it:

   ```bash
   gh issue create -R orchard-suite/orchard --label proposal --label origin:<personal|work> \
     --title "<title>" --body-file <file>
   ```

7. Tell the person the issue link.
