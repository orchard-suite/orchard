# AGENTS.md

This repository holds the docs and strategy for Orchard, a suite of
core platform services. It holds no application code. Each app lives in its
own repository; `README.md` lists them. The repository is also an agent
plugin, `orchard`, so an agent on any machine can read these documents and
send a decision back.

## What goes here

- The suite's strategy, its members, its pillar coverage, and its seam, as
  the documents in `docs/`.
- The plugin: `.claude-plugin/` and `skills/` (`consult`, `propose`,
  `fold`). A skill here says how to read or change the suite. It never
  repeats what a document or a record says.
- `vantage.yaml`: the pointer to what lives in the hub. It names no hub.
- Anything an app's own repository already says stays there. Link to it.

## What lives in the hub

The suite's decision records, its roadmap, and its diagrams live in a
Vantage hub (decision `ORC-0027`). `vantage.yaml` names them, and the
estate's own Vantage settings map the repository to its hub and workspace.
Never bring a records folder, a roadmap file, or a diagram file back here;
`make check` fails on each.

- **Decision records**: the registry `ORC`. A record is cited `ORC-0016`;
  a document here may say "decision 0016". Write and change records with
  the `vantage:decide` skill. A record is never rewritten once accepted; a
  new one supersedes or amends it, and the old one's status note says so.
- **The roadmap**: items of the kind `ORCR`. An item comes only from a
  record or the build order, carries `owes`, `from`, `section`, and
  `checked` labels, and links its records. Report one done only with a
  version or a commit read from the member's repository. The roadmap's
  page, `roadmap.md` in the document, lives only in the hub.
- **The diagrams**: the document `orchard`. Its views are edited in the
  hub. Its other pages are copies of `docs/*.md`: when a document here
  changes, save the same text as its page in the same pass, and never
  edit those pages in the hub.

## How a decision arrives

A decision made in any conversation, on any machine, arrives as a proposal:
an issue labelled `proposal` (the `propose` skill). The `fold` skill turns
proposals into records on a schedule. A proposal that changes an accepted
decision is labelled `needs-ruling` and waits for the owner. A decision
made in a conversation in this repository is written the same way a fold
writes one: the record and the roadmap items in the hub, the documents
here.

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
which fails on an em-dash or en-dash, a records folder, a roadmap file, or
a diagram file back in the repository, a `vantage.yaml` that is missing, lacks
a key, or names a hub, and a link to a file that is not there. The hub
numbers records and refuses a citation to one that does not exist. It then
runs `hedge audit`, which fails on any estate's name; hedge's hooks also
check every write, commit, and push.

## Delivery

Agents push to main. Land with `make land` (`make land BRANCH=<branch>`
from a worktree): it runs `make check`, then `release-damnit land`. Commit
as `<type>(orchard): <description>`:

- `feat`: the document changes a decision makes, or a change to what the
  suite is.
- `fix`: a corrected fact.
- `docs`: wording only.

A landed `feat` or `fix` releases. CI runs the document check, then
versions the plugin; never version by hand.
