# 0009. Slipway joins the suite

- Status: Accepted, amended by 0011 (its open question on pillar 1 is closed)
- Date: 2026-11-12
- Standard: 2026.1107.1839
- Supersedes: 0003
- Amends: 0001, 0008

## Context

Decision 0003 took Slipway out of the suite. It gave three reasons.
Slipway was not a paved road a team uses to ship its own work. It reached
one forge and one registry. Its agent ran on a runtime that is not a
member. Decision 0008 added a fourth: no seed tool joins the suite.

Two things have changed since.

**What Slipway is for.** Slipway had two kinds of job. One built a new
application from one typed idea, on a template of its own. The other took
a brief to change a repository that already exists, had an agent make the
change, and landed it. The first was fun and is reckless as a way to run a
platform. Slipway drops it and keeps the second. It becomes a tool that
maintains and evolves software, and never one that starts it.

**The question asked of it.** Decision 0003 asked whether Slipway answered
a pillar well. The first check in `seam.md` asks something plainer: does
the tool serve tending? Decision 0007 made tending the suite's one job
after 0003 was written, so Slipway was never judged by it.

These facts were read from Slipway's repository on 2026-11-12, at v4.9.4:

- A change job works only in a repository on a list an operator sets. An
  agent makes the change in a clone. The runner checks the work, lands it
  on the main branch, and watches the repository's own pipeline. A red
  pipeline goes back to the agent.
- The agent never holds a forge credential. Only the runner pushes. Every
  command that reads the agent's clone runs in a container that holds no
  credential.
- A change that touches a protected path lands only after a person
  approves it.
- It builds on the shared kit at v1.3.2: the door, telemetry, the Ledger
  client, and the Orrery client. It posts every job step and every
  approval or decline to Ledger. It declares its actions on Orrery's
  self-service page and reports each job's steps into the run. Its
  `orrery.yaml` describes it.
- It reaches one forge, GitHub, through that forge's CLI and one app
  registration. Its default registry is GitHub's.
- It drives one agent runtime's CLI directly.
- Its defaults name the home estate: a domain, an owner account, a
  registry, and a committer address. `registry/apps/` lists the home
  estate's deployed applications.
- The template and the build-from-an-idea job are still there.

## Decision

1. **Slipway is a member.** The suite has ten members.
2. **Check 1 has a plain form.** Ask one question: does the app help run
   the platform, or does it only run on the platform? A member helps run
   it. An app the platform exists to run is the estate's own. `seam.md`
   keeps the words "it serves tending" and gains this question as the
   quick way to ask it.
3. **Slipway passes check 1.** Nobody builds a platform in order to run
   Slipway. It changes the platform's own software and the software that
   grows on the platform. Shipping a change with an agent doing the work
   is part of running a platform. Its tending job is **fix**: it is the
   hands that change a bed.
4. **Slipway passes check 2.** This is a judgment, made on 2026-11-12. The
   market sells agents that write code. Each comes tied to one vendor's
   forge, model, or cloud, and none joins a catalog, a ledger, and one
   approvals inbox the way a member does.
5. **Its pillar is golden paths.** This is a judgment too. The pillar
   asks whether a team can ship without a ticket. A paved road has two
   halves: starting a repository, and changing one. Decision 0008 left
   starting with each estate, and that stands. Slipway is the road for
   changing: a request goes in, and a tested change comes out, shipped.
6. **Slipway plants no seed.** The template and the build-from-an-idea job
   leave Slipway. That keeps point 3 of decision 0008: the suite ships no
   seed and admits no seed tool. An estate still starts a repository with
   its own Orrery action, and then points Slipway at it.
7. **The agent runtime crosses the seam.** Slipway starts agent sessions
   on a runtime the estate brings. The suite builds no runtime. The
   runtime joins the list of crossings in `seam.md`, reached through an
   adapter per runtime, the same way a forge is.
8. **Slipway joins owing changes.** It passes check 4 today. It does not
   pass check 3. Its rows are in `seam-audit.md`: the estate names in its
   defaults, the estate's list of applications in its repository, one
   forge and one registry in its core, one runtime in its core, and the
   template that has to go.

## Left open

- **How Slipway takes a request.** Who may ask for what, which stops a
  request makes, and which tools the agent may use are Slipway's own
  design. They are recorded in Slipway's repository, not here.
- **Pillar 1.** `pillars.md` says no member gives people a way to say
  what they need. A request to Slipway is one such way. Whether that
  changes the rating of platform as a product is judged when it is built.

## Consequences

- Decision 0003 is superseded. Its reasons about one forge, one registry,
  and one runtime are now rows Slipway owes, not reasons to stay out.
- Decision 0008 is amended in one place. Its line "Decision 0003 stands"
  no longer holds, and golden paths is no longer only "bring your own".
  Everything it says about seeds stands.
- Decision 0001 listed Slipway as a member. That is true again, for a
  different reason.
- Two lines of `strategy.md` are read again. "Not an agent runtime" still
  holds: Slipway starts sessions and the suite builds no runtime. "Not a
  controller" still holds: Slipway changes a repository only when a person
  or an agent asks, and every step is recorded.
- Orrery reading Slipway's jobs is a link inside the suite, no longer an
  estate's choice.
- `README.md`, `members.md`, `pillars.md`, `garden.md`, `seam.md`,
  `seam-audit.md`, `strategy.md`, and the diagrams say all of this.

## Rules

Builds to:

- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: Slipway
  joins by this record, which lists what it still owes.
- `keep-every-estate-on-its-own-side-of-a-seam-with-a-closed-li`: the
  estate names in Slipway's defaults are owed rows, and the forge goes
  behind an adapter.
- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`: golden
  paths gets one member, and no second app is stacked on a pillar that has
  one.
- `extend-the-existing-actions-engine-every-run-goes-to-the-led`: Slipway
  declares its actions on Orrery's engine and reports each run there.
- `one-ledger-of-what-every-agent-did-shape-defined-first`: every job step
  and decision is an event in Ledger.
- `agents-deliver-their-own-verified-work-except-infrastructure`: what
  Slipway ships is software. An infrastructure change still waits for a
  person.

Departs from:

- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: the rule
  says "serves operations". This record applies "serves tending", as
  decision 0007 set it.
- `keep-every-estate-on-its-own-side-of-a-seam-with-a-closed-li`: the rule
  closes the list of crossings at eight. This record adds a ninth, the
  agent runtime.

New to the standard: the standard has no rule for the one question that
tells a member from an estate's own app, for a member that changes
repositories, or for an agent runtime reached through an adapter.
