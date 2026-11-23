# 0004. redgreen becomes the forge source

- Status: Accepted, amended by 0017 (it becomes Muster, with forgitten)
- Date: 2026-11-07
- Standard: 2026.1106.144
- Amends: 0001

## Context

redgreen was a web app with its own board, its own outcomes page, and its
own store of every repository. Orrery has since learned to do the board's
work itself: windowed counts, rates and percentiles over related records,
calculated fields, a calculated status with its reason, and status that
rolls up along relations. So redgreen kept a second inventory beside the
catalog, computed what the catalog can compute, and read Dispatch's
incidents directly though Dispatch already writes them into Orrery. Its
store grew to hundreds of megabytes of cached forge answers, and the
server's blocking reads of it crashed the app.

## Decision

Orrery is the board and the math. redgreen is the forges' door into it.

redgreen is a headless Go service. It reads GitHub, GitLab, and Azure
DevOps behind one provider interface, and writes repositories, pipelines,
services, deployments, and issues into the catalog. It keeps only what it
needs to ask a forge cheaply, and computes only what needs a forge call or
a neighbouring record: a deployment's lead time, whether it failed, and how
long its restore took. The health rules and the four delivery measures are
calculated fields on the blueprints redgreen offers, so every estate gets
the same rules, and a rule change needs no resync.

A product owns the definitions it brings. Orrery marks a field a source
offered, and that source's next offer updates it until a person edits it;
then the estate's edit wins.

redgreen shares contracts with the suite, not code: it uses Orrery's
published client and OpenTelemetry, not platformkit.

## Consequences

- redgreen has no pages and no sign-in. Its board is Orrery's wall and
  grids, and Dispatch's incidents reach it through the catalog, not
  directly.
- The measured outcomes pillar is covered by Orrery's DORA fields, fed by
  redgreen.
- An estate that ran its own pipeline and issue pushers retires them and
  hands their records to redgreen.
