# 0025. Muster and Tender are built together, and what 0017 and 0018 left open is settled

- Status: Accepted
- Date: 2026-11-23
- Standard: 2026.1122.1851
- Capture: 707b329b-8b67-49d3-8140-2906b3a768a7
- Amends: 0017 (point 6: redgreen takes the name Muster now, and forgitten retires once Muster takes its first reports), 0004 (Muster takes one package from platformkit, the device door)

## Context

Decision 0017 made redgreen and forgitten one member, Muster. Decision
0018 gave the suite one device agent, Tender, so a machine's report
reaches a member without a catalog token. Neither was built, and the two
left eight questions open between them.

Since then, decision 0024 opened every member's source in one org. That
answers 0017's first question for free: redgreen's repository and
forgitten's are both public in `orchard-suite`.

The owner asked for all of it in one pass: the new name, Tender, the
door, the reader, and forgitten's retirement. These facts were read on
2026-11-23:

- redgreen is at v2.0.1, one Go program that reads forges and writes
  the standard's software blueprints (`sw_repository`, `sw_pipeline`, and
  the rest) into Orrery.
- forgitten is at v1.0.0. Its scan reads, per checkout and worktree:
  staged, modified, untracked, and conflicted files, commits no remote
  holds, branches ahead, behind, or with a deleted upstream, stashes, and
  repositories with no remote.
- One estate's device management already issues device certificates for
  client authentication, with the key kept on the device. The other
  estate has no device management and no certificate authority.

## Decision

### Muster

1. **redgreen is Muster from today.** Its repository is renamed
   `orchard-suite/muster`, and its program, image, settings, telemetry,
   and catalog source take the name. Its next release is a major one.
2. **A machine's work lands on a checkout.** Muster offers one more
   blueprint, `sw_checkout`: one record for each repository on each
   machine, linked to the repository's record when its remote is one the
   catalog holds, and always to the machine's record. A repository with
   no remote has no forge record, so its checkout hangs from the machine
   alone. This answers where work goes that has no forge record. A
   repository's record counts the machines that hold work it has not
   seen.
3. **What a report keeps.** For each checkout: the remote it names (or,
   with no remote, the folder's name), counts of staged, modified,
   untracked, and conflicted files, stashes, and worktrees, and each
   branch's name with how far it is ahead of or behind its upstream, and
   whether that upstream is gone. Never a file's name, a path above the
   folder, a commit message, or a file's contents. Branch names tell a
   person where to look; file names say more about a person's work than
   the job needs.
4. **A checkout is private to the machine's person.** The blueprint
   Muster offers lets only that person and the estate's admins read a
   checkout. An estate that wants wider readers widens it before it
   turns the reader on.
5. **Muster's door comes from platformkit.** The check a member makes on
   a device's post is the same for every member that takes one, so it is
   written once, as platformkit's `device` package. Muster takes that
   package and keeps decision 0004's rule for everything else.
6. **forgitten retires** once Muster holds its first machine reports in
   each estate: its hub, store, page, and CLI go, and its repository is
   archived. The suite then has nine members.

### Tender

7. **Tender is its own public repository, `orchard-suite/tender`,** in the
   shed. It is written in Go, like the readers it carries.
8. **It runs as the person, and its certificate names the person and the
   device.** It reads that person's files, so it runs in their session:
   a login agent, a user service, or a task at sign-in.
9. **It proves itself by signing each post.** Each post carries a short
   assertion that Tender signs with the device's key: who it is for, the
   method, the address, a hash of the body, a unique id, and a life of a
   few minutes, with the certificate chain beside it. It is not a TLS
   client certificate, so it passes every front door and proxy an estate
   runs.
10. **The key stays where the estate put it.** Tender uses the key in the
    operating system's own store, where device management put it, and
    never copies it out. Where an operating system has no such store, it
    uses a key file only its user can read.
11. **Tender does not update itself.** Whatever installed it installs its
    next release: device management, or the owner's own tool list, from
    the estate's forge, signed (rule
    `serve-distributed-artifacts-from-the-estate-s-forge-republis`).
12. **Friction gets no reader yet.** Decision 0008 left open where
    friction is sensed, and nothing has changed that.

### The door

13. **The door checks five things:** the chain reaches the estate's
    device authority, the certificate is for client authentication and
    still valid, the authority has not revoked it, the assertion is for
    this member and this request and has not been seen before, and the
    body matches its hash. It then names the device and the person.
14. **Revocation is how a member knows the estate still manages a
    device.** Device management revokes a device's certificate when it
    stops managing it, so the door reads the authority's revocation list
    and refuses a revoked certificate. It refuses every post when it
    cannot read a current list.

### An estate with no device management

15. **It runs a small certificate authority of its own,** in its
    cluster, for client authentication only (rule
    `limit-a-certificate-authority-to-its-one-purpose-and-give-ea`). A
    person enrolls a machine once by signing in, as they sign in to any
    of the estate's apps. Tender makes the key in the machine's own store
    and hands the authority a signing request; the authority signs it.
    No token is made or handed out by hand. That is as little as it can
    be: one service, one sign-in per machine, and a renewal Tender asks
    for before the certificate runs out.

## What members owe

| Who | What it owes |
| --- | --- |
| Muster | The rename. The `sw_checkout` blueprint and its count on the repository. Its reader as a small module, and a door that takes its posts. |
| platformkit | The `device` package: the door's five checks, and the device and person it names. |
| Tender, a new tool | The agent: readers off until given an address, the question before a post, a signed assertion with the estate's certificate, a saved place, sending again, and a signing request for an estate that enrolls by sign-in. |
| forgitten | Retirement once Muster holds its reports, and an archived repository. |
| Each estate | Device certificates (from device management, or a small authority of its own), Tender's address list, and Muster's deployment. |

## Consequences

- `members.md`, `pillars.md`, `README.md`, and the diagram show Muster in
  redgreen's place, and Tender in the shed as built.
- `roadmap.md` rows 27, 28, 29, and 31 close when each part ships. Row 30
  (Tally's reader) stays owed: Tally can take the same door from
  platformkit.
- Every deployment of redgreen changes its image, its command, its
  settings, and its catalog source, as the renames of 0024 did.

## Rules

Builds to, from the platform standard, version 2026.1122.1851:

- `devices-report-to-the-house-nothing-commands-them`: Tender only
  reports, and a device never writes to the catalog.
- `read-the-catalog-first-and-keep-it-complete`: forgitten's board and
  store go; the catalog holds every checkout.
- `limit-a-certificate-authority-to-its-one-purpose-and-give-ea`: the
  small authority signs for client authentication only.
- `serve-distributed-artifacts-from-the-estate-s-forge-republis`: Tender
  reaches machines as a signed release.
- `keep-one-list-of-tools-for-every-machine-and-want-the-newest`: the
  owner's machines take Tender from the tool list.

Departs from: `enroll-an-installed-agent-through-device-management-s-own-sc`.
Decision 0018 chose a certificate over a token made on the machine, for
the reasons it gives. This record keeps that choice.

New to the standard: a device's post proven by a signed assertion beside
its certificate chain, rather than by a TLS client certificate; and
revocation as the test that the estate still manages a device.
