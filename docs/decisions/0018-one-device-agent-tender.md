# 0018. One device agent, Tender

- Status: Accepted
- Date: 2026-11-20
- Standard: 2026.1120.2003
- Capture: 65efbf5d-f202-4db7-bd9d-63b7322e134f

## Context

Two members need to read things that exist only on a person's machine.
Tally reads what each agent conversation used. Muster will read work that
has not left the machine (decision 0017). More may follow: decision 0008
left open where friction is counted, and it too is read from a machine.

Read from Tally's repository on 2026-11-20, at v0.0.45:

- Tally builds one program. `tally ship` is that same server program, run
  on each machine in another mode.
- It posts every minute, and each post replaces a whole minute, so a post
  sent twice is stored once.
- Each machine makes a token of Tally's own and keeps it in a file. The
  server keeps the token's hash. A fleet enrolls through a script its
  device management runs, which is the standard's rule
  (`enroll-an-installed-agent-through-device-management-s-own-sc`).

Read from forgitten's repository the same day, at v0.1.9: each device
signs in with a code a person types, and keeps a refresh token.

The owner set three requirements.

- A server program is not installed on a person's machine to run in
  another mode. It carries a store, a board, and cloud readers that have
  no place there.
- No token is made, handed out, or looked after by hand. An estate with a
  managed fleet should deploy the agent and be done.
- The agent must work in an estate that runs only part of the suite.

Four ways for a machine to prove itself were weighed.

| Way | Why it was or was not taken |
| --- | --- |
| A token made on the machine, its hash collected by device management | It is the standard's rule, and it works. The key sits in a plain file that can be copied, and the code that enrolls a machine is the suite's to keep. Not taken. |
| The signed-in person's own sign-in, borrowed from the operating system | The agent holds no secret. It ties the agent to one vendor's sign-in, each operating system does it differently, and it fails when nobody is signed in. Not taken. |
| Federation | It needs an issuer that vouches for the machine. A person's machine has none of its own. It does not fit. |
| A certificate the estate's device management issues | The key is made on the machine and never leaves it. Device management gives it and takes it away. It names no vendor. Taken. |

## Decision

1. **An on-machine agent is its own small program.** No member's server
   is installed on a person's machine, in any mode.
2. **The suite has one device agent, Tender.** It holds one reader for
   each member that reads from a machine. An estate deploys one tool, with
   one identity and one way to update it.
3. **A reader is off until the estate gives it an address.** A reader
   with no address reads nothing and sends nothing. An estate that runs
   Tally and not Muster lists one address. Nothing in Tender assumes a
   member is there.
4. **Tender asks before it sends.** It asks the address whether it takes
   that reader, and at which version. A no means the reader stays quiet
   and asks again later.
5. **Each member owns its reader.** The reader and what it sends are the
   member's, kept in the member's own repository as a small module.
   Tender owns what every reader shares: the identity, the schedule, the
   saved place, sending again after a failure, and its own updates.
6. **Only names and counts leave a machine.** Never a prompt, a reply, a
   file's contents, or a secret. Tender holds every reader to this.
7. **A machine proves itself with a certificate the estate issues.** The
   estate's device management issues it, renews it, and takes it away.
   The suite names no certificate authority and builds none. A member's
   door checks the certificate, and checks that the estate still manages
   the device.
8. **Tender only reports.** Nothing in the suite sends it a command or a
   query. It never writes to the catalog. Each member writes what it was
   sent.
9. **There is no lookup service.** Tender does not find the members
   through the catalog. An estate may run one member without Orrery, and
   a machine holds no catalog token (decision 0017).
10. **Tender is in the shed.** It is installed on a machine, so it is not
    a member and takes no membership test (decision 0007).
11. **The name.** A tender is the small boat that carries things between
    a ship and the shore. It is also one who tends.

The seam gains no crossing. Tender's list of addresses is configuration.
The certificate is sign-in: the estate says which machine is calling, as
its front door says which person is. This reading is a judgment.

## What members owe

Each is that member's own design, recorded in its own repository.

| Who | What it owes |
| --- | --- |
| Tender, a new tool | The agent: readers that stay off until given an address, a question before it sends, a certificate as its identity, a saved place, and sending again. |
| Tally | Its reader as a small module. A door that takes a reader's posts from a machine with a certificate. An end to `tally ship`, so its server is no longer installed on machines. |
| Muster | Its reader as a small module, and the same door (decision 0017). |
| Each estate | Device certificates from its own device management, and the list of addresses for the members it runs. |

## Left open

- **Whose certificate it is.** Tender reads a person's files, so it most
  likely runs as that person, with a certificate that names the person
  and the device. A certificate for the machine alone needs the agent to
  run as the system.
- **Where the member's door lives.** Every member that takes a reader
  needs the same check. The kit is the likely place.
- **How Tender updates.** The standard has an estate's forge serve a
  signed agent at a fixed address. Whether Tender updates itself from
  there, or device management does, is not settled.
- **Whether friction is counted by a reader in Tender.** Decision 0008
  left open where friction sensing lives.
- **An estate with no device management.** A small estate may issue
  certificates from a certificate authority of its own. How little that
  can be is not settled.

## Consequences

- `members.md` lists Tender in the shed, as decided and not built.
- `seam.md` lists device certificates and the address list with what an
  estate holds, and says the sign-in crossing names a machine as well as
  a person.
- `roadmap.md` gains rows 29 to 32.
- The diagram gains Tender, drawn as not built.
- The suite's member count does not change. No rating changes.

## Rules

Builds to:

- `devices-report-to-the-house-nothing-commands-them`: Tender reports,
  nothing commands it, and a device never writes to the catalog.
- `serve-distributed-artifacts-from-the-estate-s-forge-republis`: Tender
  is installed on machines, so an estate serves it from its own forge.
- `keep-every-estate-on-its-own-side-of-a-seam-with-a-closed-li`: the
  certificate authority, the device management, and the address list are
  the estate's. No crossing is added.
- `the-platform-s-own-software-is-a-pillar-kit-engine-interface`: what
  every member's door shares is written once.
- `new-capability-goes-to-a-standalone-product-not-the-house-vi`: the
  agent is its own tool, not a mode of a member.
- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: weighed,
  and no member joins.

Departs from:

- `enroll-an-installed-agent-through-device-management-s-own-sc`: the
  rule has a script make a token on the machine and print its hash, which
  the service reads back through device management. Here device
  management issues a certificate, and there is no token and no list of
  hashes. Why: the key cannot be copied off the machine, and enrolling
  becomes the estate's own tooling in place of the suite's code. The rest
  of the rule is kept: nobody signs in, nobody keeps a list, and a
  machine that leaves management can no longer post.

New to the standard: the standard has no rule that a server program is
never installed on a person's machine in another mode, for one device
agent that holds a reader for each member, for a reader that stays off
until an estate gives it an address, for asking a member before sending
to it, or for a device certificate as an installed agent's identity.
