# 0011. Quality starts at the request

- Status: Accepted, amended by 0016 (point 8: run as a product is a property, still Partial)
- Date: 2026-11-18
- Standard: 2026.1107.1839
- Amends: 0009, 0010

## Context

Decision 0010 said how the suite answers for quality. It began at the
change: a change is bounded, and laws judge it. It said little about what
comes before a change exists.

That half matters most. A change can pass every law and still make the
software worse. A person asks for ten special cases. An agent builds all
ten, with tests, and each passes. The system now has ten rules where one
general rule would do, and the next grower copies them. No law catches
that, because nothing that was promised broke.

Slipway met this in use and recorded what it learned. These facts were
read from Slipway's repository on 2026-11-18, at v6.2.0:

- A request is taken as evidence of a problem. Every claim of fact in it
  is checked before a plan relies on it: in the code, in the repository's
  history, and in the running system where a tool reaches it. Each check
  is kept in the brief, found true or false (its record 5003).
- For a feature, the planner fits the change to how the system already
  does like things, and prefers one general way over a case for each
  field, page, or person (5003).
- Every plan is two documents. A brief is for the approvers: it names
  behaviour and never files, and is read in two minutes. A build plan is
  for the builder, and is the contract the diff is held to. Code holds the
  brief to its shape (5002).
- In a lane whose plans wait, a feature or any change in behaviour always
  waits for a decision. Only a clear defect ships unasked: a fix that only
  makes the system do what it was already meant to do (2004).
- A plan is one ask that gains rounds. Approvers answer on the ticket or
  in the hub, and each answer is planned into the next round. A file an
  approver sends joins the next round (2005, 2006). The builder gets the
  approved plan, the request, its files, and every note (5004).
- Slipway names the ticket under every commit itself, so the commits of
  one request can be found and taken back out as one (5005).
- Each agent session is keyed by its request and its step.
- The gate runs the repository's own `make check`, where its root Makefile
  has one.
- When a round sends the build back and no rounds are left, Slipway takes
  the commits it landed back out. When the gate itself fails past the last
  round, the request ends as failed, and any part that had landed stays on
  main (`internal/desk/build.go` and `internal/desk/land.go`).

Decision 0009 left one question open: whether a request to Slipway changes
the rating of platform as a product. It said to judge that once it was
built. It is built.

## Decision

1. **A request is evidence, not a specification.** What a person asks for
   says that a problem exists. It does not say what the fix is. Claims in
   it are checked before anything relies on them. A feature is fitted to
   the system for everyone who uses it, and one general way beats a case
   for each person who asks. This holds for any grower: an agent at a
   desk, an agent at a keyboard, or a person.
2. **An owner's judgment is spent on the plan, never on the code.** Where
   a person must agree, they read a brief of the plan, in behaviour, in
   about two minutes. The approved plan is then a contract, and a machine
   holds the change to it. This is what rung 8 of the ladder of proof
   means.
3. **Three dials set what a change needs.** The **lane** is who is asking:
   it sets how far a request may go with no person in the way. The
   **kind** is what the change does to what the software is meant to do:
   a fix restores it, and a feature or a change in behaviour alters it.
   Altering it always needs an owner. The **class** is what a failure
   costs: it sets the proof. Decision 0010 named class only.
4. **Agreement is one conversation.** One ask, with numbered rounds, where
   the owner already works. The builder receives the final shape: the
   request, the approved plan, and everything the owners said.
5. **One bar, whoever builds.** A change made through the desk, by an
   agent at a keyboard, or by a person passes the same gate. So a
   repository's rules are laws the gate runs. A supervisor who reads a
   finished change against the repository's rules is inspecting, which
   decision 0010 turned down. The remedy is to make the rule a law.
6. **A check counts only where it ran.** A test a builder wrote and the
   gate could not run is not proof. A plan that leans on such a check
   needs an environment that can run it, or it waits for a person.
7. **What is asked, landed, and undone is one unit.** Every commit of a
   request names its ticket. What a request landed comes out as one. A
   request that ends says what it left on main.
8. **Platform as a product stays Partial, for a new reason.** This is a
   judgment, made on 2026-11-18. A request to Slipway is how a person says
   what they need: from inside an application, in a lane, with one answer
   back. So the suite now listens. Which applications people choose is
   still My Apps. The pillar's question is split across two apps, and the
   standard counts that as a pillar with no single owner.

## What members owe

| Member | What it owes |
| --- | --- |
| Slipway | Take a failed request's landed commits back out, or say on the request what it left on main. Say which checks its gate ran. |
| Tally | Nothing new for a change made through the desk: Slipway keys each session by request and step. The row in decision 0010 stands for sessions outside the desk. |

## Left open

- **Weighing a request outside the desk.** A person who asks an agent at a
  keyboard has no investigator, no brief, and no rounds. Whether that path
  gets them, or stays a habit of the person, is not settled.
- **Which checks a desk's gate can run.** A check that needs a browser or
  a running system runs today only where the repository's own pipeline
  runs it. Point 11 of decision 0010 puts environments with the estate.
  How a desk asks for one is Slipway's own design.

## Consequences

- `quality.md` gains the half before the change: the request, the plan,
  and the three dials. Its table of what the suite covers gains two rows.
- `pillars.md` reads rows 1 and 14 again.
- `strategy.md` drops the question decision 0009 left open.
- Decision 0010 is amended in two places. Class is one of three dials, not
  the only one. Tally's owed row is narrowed to sessions outside the desk.
- Decision 0009's open question on pillar 1 is closed.
- The suite still has ten members and fourteen pillars.

## Rules

Builds to:

- `an-exploration-dossier-that-separates-facts-from-hypotheses` and
  `defect-track-runtime-evidence-first-no-design-questions-unti`: a
  request's claims are checked, and each check is kept as evidence.
- `question-the-operator-in-themed-pages-evidence-first-and-let`: judgment
  calls reach the owner with the evidence and a recommendation.
- `run-implementation-unattended-from-the-specification-alone`: the
  builder works from the approved plan.
- `set-rigor-by-what-a-failure-costs-in-a-few-named-classes` and
  `risk-trip-wires-derived-from-evidence-independent-of-size`: class and
  kind are separate dials.
- `judge-results-with-a-cross-provider-council-never-gate-worki`: a
  person judges a plan, and nobody gates working code on a read of it.
- `one-approvals-inbox-as-a-catalog-record-every-system-pushes-`: one ask
  per request, however many rounds it takes.
- `a-null-result-counts-only-if-the-test-could-have-come-out-po` and
  `written-is-not-working-observed-local-gated-hands-on-then-gr`: a check
  counts only where it ran.
- `every-commit-traces-to-a-work-item-that-existed-first`: the ticket in
  every commit is what makes a request one unit.
- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`: a
  pillar split across two apps has no single owner.

Departs from: none.

New to the standard: the standard has no rule that a request is evidence
and not a specification, that an owner's judgment is spent on a brief of
the plan and never on the code, for the kind of a change as a dial beside
its class and its lane, for one bar whoever builds, or for a request as
the one unit that is asked, landed, and undone.
