# 0021. An estate's deploy tool stands outside the suite and needs none of it

- Status: Accepted
- Date: 2026-11-21
- Standard: 2026.1120.2003
- Capture: a8ad3934-bdca-4644-8dc2-89d785d6770a

## Context

Decision 0010, point 11, says environments are the estate's own, and that
an estate registers an Orrery action that stands up an environment for a
change. Decision 0020, point 6, says Slipway changes a repository and the
actions engine carries every other change. Decision 0011 left open how a
desk asks for an environment its gate can run a check in.

On 2026-11-21 the owner decided what the tool he stands environments up
with will become. That tool is `dev`, which `members.md` lists in the
shed. It will deploy every environment an estate has, from a developer's
own to production, through a part that runs in the estate's cluster. He
ruled that it must work in an estate that runs no member of the suite.

That ruling touches the two points above. An estate with this tool has
its environments stood up, and its applications released, by something
that is not the actions engine and may run with no Orrery at all.

## Decision

1. **An estate's deploy and environment tool is not a member, and needs
   no member.** It serves an estate that runs none of the suite. This
   applies the test in `seam.md`: it is the estate's own tool.
2. **When the estate runs the catalog, the tool's part in the cluster is
   what reports to it.** It writes environments and releases as
   inventory, and it asks for an action run where a release needs a
   person's yes. A person's machine holds no setting for the catalog.
3. **Decision 0010, point 11, is amended.** An estate may register an
   Orrery action that stands up an environment. It does not have to. The
   suite still builds no environment tool and names no default.
4. **Decision 0020, point 6, is read for the suite's own apps.** Among
   them, Slipway changes a repository and the actions engine carries
   every other change. A change an estate's own tool makes is the
   estate's. Where the engine is present, that change should reach the
   engine's record of runs, by point 2.
5. **A desk may run the estate's tool inside its sandbox.** The
   environment belongs to the request and ends with it. How a desk asks
   is still Slipway's own design (decision 0011), so that question stays
   open.

## What members owe

Nothing new. Orrery already takes inventory from a source and already
offers an action a standing program can be called by. Slipway's open
question is unchanged.

## Consequences

- The suite still has ten members. No rating changes.
- `roadmap.md` gains no row. Its open question on how a desk asks for an
  environment stays, under decision 0011.
- No picture changes: the tool is outside the suite's map.

## Rules

Builds to:

- `one-application-deploy-tool-and-one-set-of-manifests-for-eve`: an
  estate deploys every environment with one tool, and that tool is the
  estate's.
- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`: Change
  is still answered by two of the suite's apps.

Departs from: none.

New to the standard: the standard has no rule that an estate's deploy
tool works without the catalog and reports to it from the cluster when
the catalog is there.
