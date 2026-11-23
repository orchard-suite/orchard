# AGENTS.md

This repository holds the docs and strategy for Orchard, a suite of
core platform services. It holds no application code. Each app lives in its
own repository; `README.md` lists them. The repository is also an agent
plugin, `orchard`, so an agent on any machine can read these documents and
send a decision back.

## What goes here

- The suite's strategy, its members, its pillar coverage, and its seam.
- Decisions, one file each in `docs/decisions/`, numbered in order. A
  decision is never rewritten once accepted; a new one supersedes it and
  says so.
- `docs/roadmap.md`: what the suite still owes. A row comes only from a
  decision record or the build order. Mark a row done only with a version
  or a commit read from the member's repository.
- The plugin: `.claude-plugin/` and `skills/` (`consult`, `propose`,
  `fold`). A skill here says how to read or change these documents. It
  never repeats what a document says.
- Anything an app's own repository already says stays there. Link to it.

## How a decision arrives

A decision made in any conversation, on any machine, arrives as a proposal:
an issue labelled `proposal` (the `propose` skill). The `fold` skill turns
proposals into records on a schedule. A proposal that changes an accepted
decision is labelled `needs-ruling` and waits for the owner. A decision
made in a conversation in this repository is written here directly, the
same way a fold writes one.

## The seam

Orchard is estate-neutral. Every rule in `docs/seam.md` applies to this
repository too:

- Never name an employer, a company, a customer, or a work system.
- Never name a household, a person, a domain, a host, or a repository that
  belongs to one estate. Say "an estate", "the home estate", or "a work
  estate", and use fictional names in examples (`example.com`, `acme`).
- A fact about one estate's deployment belongs in that estate's own
  repository, not here.

## Membership

A tool joins the suite only by a decision record that applies the test in
`docs/seam.md`. A tool that serves one person or one family is a private
app, never a member.

## Writing

- Plain words, short sentences, active voice. Explain a term the first
  time it appears.
- No em-dashes or en-dashes.
- Every fact about an app is checked against its repository at the time of
  writing. A rating or a judgment is labeled as one.
- Decisions cite the rules of the platform standard they build to, by id,
  with the standard's version.

## Check

`make check` must pass before a commit. It runs `python3 scripts/check.py`,
which fails on an em-dash or en-dash, a decision number used twice or
skipped, a roadmap row that names no decision or build order step, and a
link to a file that is not there. It then runs `hedge audit`, which fails on
any estate's name; hedge's hooks also check every write, commit, and push.

## Delivery

Agents push to main. Land with `make land` (`make land BRANCH=<branch>`
from a worktree): it runs `make check`, then `release-damnit land`. Commit
as `<type>(orchard): <description>`:

- `feat`: a decision record, or a change to what the suite is.
- `fix`: a corrected fact, a roadmap row that moved.
- `docs`: wording only.

A landed `feat` or `fix` releases. CI runs the document check, then
versions the plugin; never version by hand.
