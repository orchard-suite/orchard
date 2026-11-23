# 0013. Decisions reach the suite on their own

- Status: Accepted
- Date: 2026-11-19
- Standard: 2026.1107.1839

## Context

An owner decides what the suite is in conversations with agents. Those
conversations happen on more than one machine and in more than one estate.
Until now a decision reached this repository only when the owner told an
agent to write it here. Three things followed.

- A decision made in one estate never reached this repository unless the
  owner carried it over by hand.
- An agent outside the machine that holds this repository could not read
  the strategy, the pillars, or a decision. So it could not build to them.
- Decisions listed what members owe, and no page said whether any of it was
  done. Decisions 0010 and 0011 alone list eight such things.

The platform standard already solved the same problem for practices. It
ships as an agent plugin with two skills: one looks the rules up, and one
sends a decision back as an issue. The issue is the mailbox. It needs no
machine of the owner's to be on, and it works from any estate.

This repository holds documents and no code. A skill is a document an
agent reads. So the same shape fits here without changing what this
repository is.

## Decision

1. **The suite's documents ship as an agent plugin.** This repository is
   the plugin, named `almanac`. Its `consult` skill tells an agent which
   document answers which question. An agent on any machine reads the
   version it installed and cites it.
2. **A suite decision made anywhere arrives as a proposal.** A proposal is
   one issue on this repository, labelled `proposal` and with its origin.
   The `propose` skill writes it. It names no estate, by the rules of
   `seam.md`.
3. **The owning machine folds proposals.** The `fold` skill turns a
   proposal into a decision record, the document changes, the roadmap rows,
   and the diagram changes, in one landing, and closes the issue with the
   record's number. It runs on a schedule and asks nobody.
4. **A proposal that changes an accepted decision waits for the owner.**
   It is labelled `needs-ruling` and nothing is written. Everything else
   lands without asking. A record is still never rewritten: the new one
   amends or supersedes it and says so.
5. **The roadmap is what decisions say is owed.** `roadmap.md` holds one
   row per thing a decision or the build order says a member owes. No row
   exists without one. A row is done only with a version or a commit read
   from the member's repository.
6. **The diagrams draw the roadmap.** The diagram file gains a view of how
   a decision travels and what is owed next. The file in this repository is
   the source. An estate's diagram hub may hold a copy, saved by the fold.
7. **A decision is a `feat`.** A commit that adds a decision record or
   changes what the suite is has the type `feat`. A corrected fact is a
   `fix`. A wording change is `docs`. A `feat` or a `fix` cuts a release,
   so every machine can tell which decisions it has.
8. **No member joins.** The suite still has ten members.

## What members owe

Nothing. This decision changes how this repository is kept, not what a
member does.

## Left open

- **Who may propose.** Today only the owner's own agents can open an issue
  here. Whether another person in an estate may propose is not settled.
- **A proposal's privacy check.** The `propose` skill tells an agent to
  name no estate, and the check in this repository scans what lands. A
  proposal that names one in the issue itself is caught only by the fold.

## Consequences

- The repository gains `.claude-plugin/`, `skills/`, a check script, and a
  release pipeline. It still holds no application code.
- `roadmap.md` is new. `strategy.md`, `README.md`, and `AGENTS.md` point to
  it and say how a decision now arrives.
- `AGENTS.md` gains a Delivery section and the commit types of point 7.
- The diagram file gains a view of the path a decision takes.
- A machine that lacks the plugin still works as before: its agents cannot
  read these documents, and its decisions do not arrive.

## Rules

Builds to:

- `follow-the-generated-platform-standard-and-report-deviations`: the same
  two skills, a lookup and a way back, around a repository agents may read
  and may not edit in place.
- `record-architecture-decisions-as-immutable-adrs`: a fold writes a new
  record and never rewrites one.
- `architecture-map-yields-to-the-decision-records`: where a document and a
  record disagree, the record wins.
- `keep-one-copy-of-a-standard-and-withdraw-rules-out-loud`: one copy of
  each document, shipped, not copied into toolkits.
- `capture-mid-task-discoveries-as-tracked-items-then-go-straig`: a
  decision becomes a tracked item at once, and the work goes on.
- `decision-posts-to-the-ledger-run-on-their-own-and-never-gate`: sending
  a proposal never blocks the change that decided it.
- `diagrams-as-one-code-file-each-view-answering-one-question`: the roadmap
  is one more view of the same file.
- `single-branch-trunk-on-main-with-one-tool`: one landing per fold.
- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: weighed,
  and no member joins.

Departs from:

- `keep-the-architecture-diagram-in-a-diagram-hub-updated-in-th`: the rule
  keeps a diagram in a hub and not as a file in a repository. This
  repository names no estate, and a hub belongs to one. So the file here is
  the source, and a hub holds a copy.

New to the standard: the standard has no rule for shipping a suite's
strategy and decisions as an agent plugin, for a roadmap derived only from
what decision records say is owed, for folding proposals on a schedule with
only a change to an accepted decision waiting for the owner, or for the
commit type of a decision.
