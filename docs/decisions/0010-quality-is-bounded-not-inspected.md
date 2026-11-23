# 0010. Quality is bounded, not inspected

- Status: Accepted, amended by 0011 (class is one of three dials) and by 0016 (the guard is five delivery measures); point 9 superseded by 0016 (quality is an outcome, not a pillar)
- Date: 2026-11-18
- Standard: 2026.1107.1839
- Amends: 0008

## Context

The suite had no answer to one question: how does an estate keep what it
ships good, when agents write most of the changes? None of its thirteen
pillars asks it. Measured outcomes counts failures after they ship.
Security and compliance judges an estate's standards. Neither says what a
change must prove before it ships, or what that proof may cost.

A proposal was weighed. It had three seats: a person writes a law, an
agent writes the code, and a judge the agent cannot reach checks the work.
The judge was a new hosted member. It would hold checks hidden from the
builder, break changed lines on purpose to see whether tests notice, and
replay live events against the laws. It would have been a fourteenth
pillar with a new member.

Parts of that proposal are right, and this decision keeps them: a law and
the code it judges have different owners, a check must be able to fail,
rigor follows what a failure costs, and a builder needs a way to stop and
ask. Its centre is not kept, for four reasons.

1. **The suite has a judge.** conform is one judge over an estate's
   standards, and the standard makes the number of judges a recorded
   decision (chapter 24). A second judge gives agents and people two
   verdicts to reconcile. Nothing here needs a check from outside the
   platform team, which is the standard's case for a second one.
2. **The suite has a gate a builder cannot reach.** Read from Slipway's
   repository on 2026-11-18, at v6.2.0: the builder holds no credential,
   Slipway lands the commits from its own clone, a machine judges the diff
   and not what the agent says about it, and a protected path passes only
   in a lane an admin marks. An estate's own pipeline is a second such
   gate.
3. **A service that runs a repository's tests is a build system.** The
   suite builds none (`strategy.md`).
4. **Hidden checks cost on every change and the evidence for them is
   thin.** Someone has to write them, which doubles the work of checking.
   Each failure tells the builder what the check was. The one study that
   tried hiding tests found cheating fell to near zero and the agents'
   real work got worse. The same study found a cheaper cure: a way to
   stop and flag a bad task cut cheating from 54% to 9% for one model.

The evidence on agents checking agents was read at its sources on
2026-11-18. It is in `quality.md`. In short: the cost of a model's review
is paid on every change, the return flattens as reviewers are added
because models share mistakes, and the practices that do lower failures
are small changes and a fast restore.

Three facts about the members matter here, read on 2026-11-18. conform,
at v5.5.0, ships nine packs, runs the same packs in a board and in a
pipeline, and asks of every rule a failing, a passing, and a no-data
fixture. Slipway already bounds a change by its size, by the paths it
touches, and by a test that fails without the fix. No member reads which
of a repository's checks are laws, what checking costs per change, or what
each check caught.

## Decision

1. **Quality has four parts.** Defects rarely reach people. One that does
   is small and gone fast. The software stays what its owners meant.
   Knowing all of that costs a known amount. `quality.md` gives each its
   number. Quality is not zero bugs.
2. **The suite bounds changes. It does not inspect them.** A change is
   bounded by its size, the paths it may touch, the laws it must keep, who
   must agree, and how it is undone. No member gates a change on a
   person's or a model's opinion of the code. A model's opinion is for the
   top class, from outside the builder's context and from another
   provider, and for results where judgment is the point.
3. **A law is a check its grower cannot change.** A law is one plain
   sentence, a check that runs and can fail, and a home on a path only the
   bed's owners change. A working test is the grower's and is not a law.
   A grower never changes a law in the change that law judges. When a law
   and a task disagree, the grower stops and asks, and the owner rules.
4. **Laws come from decisions and from escapes.** A decision record that
   can be checked gets a law. An escape is traced, and closes exactly one
   gap. No estate writes laws ahead of need. The folder of decision
   records is a protected path.
5. **There is one judge, and it is conform.** The estate's laws are its
   packs, as now. A bed's laws become facts conform reads and judges, with
   the same verdicts, findings, and waivers. The suite adds no second
   judge and no service that holds hidden checks.
6. **Class sets the rigor.** A bed's class is what its worst plausible
   failure costs and how hard that is to undo. It lives on the bed's
   catalog entry. Each estate names its own classes, and the suite ships
   none. `quality.md` says which proof stands in the path for each.
7. **A check is in the path or beside it.** A check in the path must fit
   the bed's loop budget, because the loop is also how long a fix waits.
   What does not fit runs beside the path, reports, and opens a request.
8. **Each bed carries two more numbers.** Cost of checking: what the bed
   spends to check one change, in pipeline minutes and in money for agent
   sessions. Catches: what each check found. A check that costs more than
   it catches is pruned. The four delivery measures stay the guard.
9. **The suite maps fourteen pillars.** The new one is **Quality**: does
   every change stay inside what its owners said must hold, and is each
   check worth what it costs? conform owns its verdict. Orrery shows its
   numbers. The standard maps twelve, and the suite now runs two ahead.
10. **No member joins.** Every part of the answer belongs to a member the
    suite has. What each owes is listed below.
11. **Environments are the estate's own.** The suite builds no environment
    tool and names no default. An estate registers an Orrery action that
    stands up an environment for a change. No crossing is added to the
    seam.

## What members owe

Each is that member's own design, recorded in its own repository.

| Member | What it owes |
| --- | --- |
| conform | Read a repository's laws and their last results as facts, and judge them. Judge whether a change to a law path was an owner's. |
| Slipway | Read a bed's class. Hold decision records and law paths as protected in every program. |
| redgreen | Write which check failed, per run, so catches can be counted. |
| Tally | Tell an agent session that checks from one that builds, so cost of checking can be counted. |
| Orrery | Offer the two numbers and the class as fields an estate's model may name, beside the three numbers. |
| Dispatch | Let a postmortem name the law that would have caught the incident. |

## Left open

- **Where the list of law paths lives.** Slipway keeps protected paths in
  a program file its admin owns. conform will need the same list. One list
  that both read is the aim, and where it lives is not settled.
- **How a pipeline knows an owner changed a law.** Inside the desk,
  Slipway's lanes answer it. Outside it the fence is the forge's own, and
  on some forges it needs a paid plan. A signed commit is another way.
- **Whether break-it runs get a source.** The engines are open and an
  estate brings them. No member reads what they find.
- **Whether the standard takes the pillar.** It is turned up or down in
  the standard, not here.

## Consequences

- `quality.md` is new. It holds the framework, the ladder of proof, the
  classes, the evidence on cost, and what the suite covers.
- `pillars.md` lists fourteen pillars and rates the new one Partial. Its
  build order puts the two numbers with the three, and a bed's laws
  fourth, after the ground view.
- `garden.md` gains four words (law, owner, class, escape) and points to
  `quality.md`.
- `strategy.md` says the suite is not a test runner or a code reviewer.
- Decision 0008 is amended in one place: the suite maps fourteen pillars,
  not thirteen. Everything else it says stands.
- `members.md`, `pillars.md`, `seam-audit.md`, and the diagram are brought
  up to Slipway v6.2.0, because this decision leans on what Slipway does
  today. Slipway has closed every seam row decision 0009 said it owed.
- The suite still has ten members.

## Rules

Builds to:

- `judge-results-with-a-cross-provider-council-never-gate-worki`: no
  member gates a change on a review of the code.
- `set-rigor-by-what-a-failure-costs-in-a-few-named-classes`: the classes,
  kept on the catalog entry.
- `a-null-result-counts-only-if-the-test-could-have-come-out-po`: a law
  must be able to fail.
- `respond-to-an-escape-by-turning-it-off-then-closing-exactly-`: an
  escape closes exactly one gap.
- `risk-trip-wires-derived-from-evidence-independent-of-size`: a risky
  kind of change raises the rigor of one change.
- `written-is-not-working-observed-local-gated-hands-on-then-gr`: proof is
  observed, and a green suite is a fallback.
- `record-architecture-decisions-as-immutable-adrs` and
  `architecture-map-yields-to-the-decision-records`: a law's reason is a
  decision record.
- `agents-deliver-their-own-verified-work-except-infrastructure`:
  protected paths wait for a person.
- `single-branch-trunk-on-main-with-one-tool` and
  `zero-downtime-rollouts-beside-the-old-pod-health-gated`: small changes
  and an undo that drops no request.
- `delivery-outcomes-as-a-sibling-of-ci-health`: the four delivery
  measures stay the guard.
- `cost-per-workload-host-agent-and-job` and
  `measure-agent-cost-per-conversation-from-the-agents-own-tran`: where
  the cost of checking is read.
- `ephemeral-environments-named-by-owner-discovered-through-a-r` and
  `judge-a-dependency-by-license-maintenance-and-governance-and`:
  environments are the estate's own, judged as any dependency.
- `admit-a-tool-to-the-platform-suite-only-by-a-written-members` and
  `new-capability-goes-to-a-standalone-product-not-the-house-vi`: weighed,
  and no member joins.
- Chapter 24's checklist: the number of judges is a recorded decision.
  This record sets it at one.

Departs from:

- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`: the
  standard maps twelve pillars. This decision maps fourteen. The rule's
  test, one app that answers a pillar's whole question, applies to the new
  pillar, and the pillar does not pass it yet.

New to the standard: the standard has no rule that defines quality by its
four parts, for bounding a change in place of inspecting it, for a law as
a check its grower cannot change, for laws that come only from decisions
and escapes, for a ladder of proof, for a check in the path held to a
loop budget, for counting what checking costs and what each check
catches, or for a pillar on quality.
