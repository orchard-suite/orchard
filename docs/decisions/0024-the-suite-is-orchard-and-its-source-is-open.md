# 0024. The suite is Orchard, its source is open, and hedge holds the seam

- Status: Accepted
- Date: 2026-11-23
- Standard: 2026.1122.1851
- Supersedes: the suite's name in 0001 to 0023, and the estate word check of 0002

## Context

The suite's members lived in private repositories. A private repository
pays for every CI minute on a hosted runner, so the members ran their
pipelines on one estate's own runners, and tested only on the machine that
landed a change. The source was private because it was the owner's work,
not because it held secrets.

Before opening it, every repository and its whole history was read for
anything an estate would not publish. The scan found no live secret. It
found plenty of estate content: a copy of one estate's deployment files
inside five members (rule 2 of `seam.md` says they belong to the estate),
employer product and customer names in test fixtures, data copied from
real systems, home host names and addresses, a person's name in comments,
and commits signed with an employer address. Much of it sat only in
history, where changelogs still linked to it.

The seam's rules were written down (decision 0002) and enforced only in
this repository, by a word list kept as a forge variable. Nothing stopped
an agent from writing a real name into a member, because nothing was in
the path of the write.

## Decision

1. **The suite is Orchard.** An orchard is planted, grafted, trained on a
   trellis, hedged, recorded, and pruned: the suite's tending work. Orrery
   keeps its name and stays the centerpiece. Three members take names from
   the same ground: **Ledger is Annals**, **conform is Trellis**, and
   **Slipway is Graft**. My Apps, Vantage, Tally, Dispatch, redgreen,
   forgitten, and the planned Muster keep theirs. This repository is
   `orchard`, and its plugin is `orchard`.
2. **Every member, and the shed tools the suite builds for itself, is open
   source** under the MIT license, in one org,
   [github.com/orchard-suite](https://github.com/orchard-suite). The org
   holds the members, platformkit, hedge, this repository, and Tender when
   it is built. An owner's other tools stay where they are, listed in the
   shed.
3. **Each repository starts a fresh history.** A new repository starts from
   its old repository's files, cleaned and renamed, at its old version. The
   old private repository stays as it was, as the archive. A history cannot
   be proven clean for names nobody thought to look for, and a public
   commit cannot be taken back. A module that other repositories pin by
   version (platformkit) carries one clean commit per pinned version, so
   every pin keeps resolving.
4. **A public repository runs its full CI on hosted runners**, tests
   included, and on no estate's runners. A stranger's first pull request
   waits for approval before it runs.
5. **hedge holds the seam.** [hedge](https://github.com/orchard-suite/hedge)
   checks every write an agent makes, every commit, every push, and every
   forge post against a register of each estate's names, in the zone of
   the repository it goes to. An estate keeps its register private and its
   zones in its own toolkit; a repository holds only opaque ids. A
   repository no zone names is estate-neutral, so every member is guarded
   from its first commit. A repository goes public only through
   `hedge publish`, which checks its whole history and its issues, pull
   requests, and releases first. hedge replaces this repository's estate
   word check.
6. **A repository's pointer to its docs names no hub.** `vantage.yaml`
   keeps what is true in any estate (the document, the folders it
   describes, the record prefixes); the estate maps each repository to its
   hub and workspace in its own Vantage settings.

## Consequences

- Every member and the shed tools run their tests in public CI for free,
  and no estate runs a runner for them.
- Every deployment of a renamed member changes its image, its command, its
  environment variable prefix, its telemetry names, and the catalog keys it
  writes. Each estate makes those changes in its own repository; the
  members' release notes list them.
- Commit history before the move is in each archive, not in the public
  repository. Changelog links into the old history do not resolve.
- An estate that adopts Orchard brings its own register. A name the
  register lacks is not caught, so an estate adds a name the day it learns
  it must stay home, and a harvest from its own catalog and cloud accounts
  adds the rest.
- Trellis can judge hedge's findings in every repository through its
  command source (`hedge audit --facts`), which an estate wires in its own
  deployment.

## Builds to

From the platform standard, version 2026.1122.1851:

- `keep-every-estate-on-its-own-side-of-a-seam-with-a-closed-li`: the
  estate's deployment files leave the members, and the hub pointer leaves
  the repository.
- `put-invariants-in-deterministic-hook-handlers-and-context-de`: the seam
  is an invariant, held by hooks, not by instructions.
- `join-existing-scanners-into-one-posture-verdict`: hedge's findings join
  Trellis's board as facts; Trellis builds no scanner of its own.
- `keep-mechanism-in-the-engine-and-opinion-behind-a-config-fie`: hedge
  holds the mechanism; each estate holds its terms and zones.
- `run-the-full-check-before-every-commit`: unchanged; public CI adds the
  same check on every push.

New ground no rule covered: a private register of estate names, compiled
for hooks, that decides what each repository may name by its remote.
