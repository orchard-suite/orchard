# Seam audit

Where the members cross the seam today. Rules 1 and 2 were measured on
2026-11-23, when each member moved to its public repository (decision
0024); the other rules on 2026-11-05, and Graft's on 2026-11-18. Each row
is a change a member owes before it fully meets `seam.md`. Fix a row in
the member's own repository, then delete it here.

## How it was measured

Rules 1 and 2: `hedge audit --history` in each member's repository,
against the zone of its public remote, with an estate's register, and a
look at its `deploy/` folder. hedge prints only an opaque id for each
finding, so this page names no estate. hedge's hooks keep it so on every
write, commit, and push.

The other rules: a read of each member's checkout over tracked files.

## Rule 1: product code names an estate

No member does. Clean on 2026-11-23: Orrery 2.0.0, Vantage 4.0.0, My Apps
1.0.0, Tally 1.0.0, Annals 1.0.1, Trellis 6.0.0, Dispatch 1.0.0, Graft
7.0.0, and forgitten 1.0.0. redgreen moves next, by the same check.

## Rule 2: an estate's deployment lives in the product

No member carries one. Each estate's deployment folder left the members
when they moved (decision 0024). What remains is generic: Vantage
(`deploy/helm`), forgitten (`deploy/compose.yml`), Trellis
(`deploy/kubernetes`, a base any estate overlays, and
`deploy/orrery-catalog`, its catalog model), Dispatch
(`deploy/orrery-catalog`), and Tally (`deploy/macos`, the shipper's launch
agent).

## Rule 3: one forge in the core

| Member | Forges it reads |
| --- | --- |
| redgreen | GitHub, GitLab, Azure DevOps, each behind a provider |
| forgitten | none; it reads git on each machine |
| Trellis | GitHub and its registry only |
| Orrery | GitHub Actions as the one actions backend |
| Graft | GitHub and GitLab, each behind an adapter |

## The agent runtime: one runtime in the core

Decision 0009 made the agent runtime a crossing, reached through an
adapter per runtime.

| Member | Runtimes it drives |
| --- | --- |
| Graft | one, behind an adapter |

## Rule 4 of joining: built the suite's way

| Gap | Members |
| --- | --- |
| Not on the shared kit | Orrery, Trellis, Vantage, forgitten, and redgreen by decision 0004 |
| Not shown posting to Annals in its `orrery.yaml` | Vantage, My Apps, Tally, Trellis, redgreen, forgitten |
| No `consumes` in its `orrery.yaml` | forgitten, Annals (Annals only receives, so this one is correct) |

The kit is a Go module today. Vantage is TypeScript, and
forgitten is a TypeScript hub with a .NET CLI, so the kit cannot reach
them until it has sides in those languages; the standard expects that order (rule
`the-platform-s-own-software-is-a-pillar-kit-engine-interface`). Orrery
and Trellis are Go and could move now.
