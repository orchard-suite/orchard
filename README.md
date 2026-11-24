# Orchard

Orchard is a suite of core platform services. Together they do one job:
they help a small team tend a platform.

A platform is not a thing you build and hand over. It is the place where
other people's software grows. Its customers, people and agents, copy what
they find there, and what they make becomes what the next one finds. So
quality compounds, up or down. Tending is the work of keeping it compounding
up: seeing what grows, finding what taught a problem, fixing it at the
source, and cutting back what is no longer used.
[docs/garden.md](docs/garden.md) is the framework.

An orchard is a garden kept for years. You plant it, graft onto good
stock, train it on a trellis, hedge it in, keep its annals, and prune what
no longer bears. Orrery, the sky over it, watches everything an estate
runs; the rest of the suite shows where each repository needs a gardener.

Every member is open source, under the MIT license, at
[github.com/orchard-suite](https://github.com/orchard-suite)
(decision 0024).

## Who it is for

Any estate. An estate is one organization's whole platform: its machines,
clusters, clouds, repositories, people, and agents. A household lab is an
estate. A company is an estate. Orchard runs in either one with
configuration, and its code and docs name neither.

## What it does not do

Orchard is not a forge, a build system, an identity provider, or a secrets
store. You bring those: GitHub, GitLab, Azure DevOps, Bitbucket, your
pipelines, your sign-in, your vault, your observability stack, and, once
two members are joined, your message broker (decision 0032). Orchard
reads them and fills the gaps the market leaves between them.

Orchard is not a portal for a business, and not an ERP. An app an estate
builds for its business has its own pages and its own rules, and uses
Orrery as an API, an inventory, an action runner, and an approval system
(decision 0029).

## The members

Each member but two belongs to one of six pillars
([docs/pillars.md](docs/pillars.md), decision 0016). Six own a pillar.
Three are parts of Catalog. redgreen is Muster now, and forgitten retired
into it on 2026-11-23, once Muster held each estate's machine reports
(decisions 0017 and 0025); its repository is archived. Rootstock and
Toolshed belong to no pillar. They stand on the floor: Rootstock deploys
software to environments (decision 0028), and Toolshed delivers tools to
machines (decision 0042). A floor member puts the platform in place,
works first, and nothing needs it (decision 0043). The suite has eleven
members.

| App | Pillar | What it answers | Its tending job |
| --- | --- | --- | --- |
| [Orrery](https://github.com/orchard-suite/orrery) | Catalog (owner), and the estate's control plane and console (decision 0029) | What exists, how it connects, and whether it is healthy. It holds the model, the actions, and the approvals, and it is where the people who run the platform see and act. | The one board. Sense, and act on many repositories at once. |
| [Vantage](https://github.com/orchard-suite/vantage) | Catalog | What a system looks like and what is written about it: diagrams as code, kept true by the catalog, with the system's living documents beside them. | Sense: the shape of the system. |
| [My Apps](https://github.com/orchard-suite/myapps) | Catalog | Which applications a person can open, and the landscape of everything the estate offers. | Sense: what people open. |
| [Tally](https://github.com/orchard-suite/tally) | Cost (owner) | What each workload, host, agent, and job costs, in money and in capacity. | Sense cost. Prune: right-sizing. |
| [Annals](https://github.com/orchard-suite/annals) | Record (owner) | What every person and agent did, across every product. | Sense and trace: who did what. |
| [Trellis](https://github.com/orchard-suite/trellis) | Rules (owner) | Whether the estate meets its standards, rule by rule, with waivers. | Stake and fence: rules in the path of work. The suite's one judge, of its laws and of the map's six properties. |
| [Muster](https://github.com/orchard-suite/muster) | Catalog | Where the code is and what state it is in: every forge's repositories, pipelines, and deployments in the catalog, which judges their health and the delivery measures, and each machine's work that has not left it. | Sense: each repository's loop and delivery, and stranded work. |
| [Dispatch](https://github.com/orchard-suite/dispatch) | Health (owner) | Which incidents are open, who owns them, and how long restores take. Also sends every product's notices, to channels and to people. | Trace: the postmortem. |
| [Graft](https://github.com/orchard-suite/graft) | Change (owner) | How a request to change a repository becomes a tested change, landed, with an agent doing the work. | Fix: the hands that change a bed. |
| Rootstock, owed at `orchard-suite/rootstock` | The floor | Which version every landing zone and environment runs, what is ready to release, and how drift went. It deploys infrastructure with `infra` and applications and their environments with `dev` (decision 0028). | Sense: the whole fleet. It also plants: it deploys the platform itself. |
| Toolshed, owed at `orchard-suite/toolshed` | The floor | What may run on an estate's machines, where it came from, and whether it is on every machine that should have it. It verifies each tool, serves it from the estate's registry, and renders signed packs into the estate's own installers (decision 0042). | Fence and plant: every tool on a machine comes through the shed. |

Two tools in the shed are the suite's own:
[platformkit](https://github.com/orchard-suite/platformkit), the Go module
every member builds on, and [hedge](https://github.com/orchard-suite/hedge),
which keeps an estate's names out of every repository that may not hold
them. `docs/members.md` lists the whole shed.

## Read next

- [docs/garden.md](docs/garden.md): the framework. What tending means, the words, the five moves, the three numbers, and what the suite covers.
- [docs/strategy.md](docs/strategy.md): why the suite exists and what it will and will not become.
- [docs/members.md](docs/members.md): each app, what it reads and writes, its tending job, and the shed of installed tools beside the suite.
- [docs/quality.md](docs/quality.md): how an estate keeps what it ships good when agents write most changes. Laws, the ladder of proof, and what checking costs.
- [docs/pillars.md](docs/pillars.md): the map. Six pillars, six properties, and three outcomes, with a rating for each and what is missing.
- [docs/seam.md](docs/seam.md): the line between Orchard and an estate, and the test for joining the suite.
- [docs/seam-audit.md](docs/seam-audit.md): where the apps cross that line today.

## Records, roadmap, and pictures

The suite's decision records, its roadmap, and its diagrams live in a
Vantage hub, not in this repository (decision 0027). `vantage.yaml` names
them: the registry `ORC`, where decision 0016 is `ORC-0016`; the roadmap
kind `ORCR`; and the document `orchard`, whose pages are the documents in
`docs/`. It names no hub: the estate that keeps them maps this repository
to its hub in its own settings, and nothing is copied to another hub. This
repository's history still holds the records and the roadmap as they stood
before the move.

## For agents

This repository installs as an agent plugin named `orchard`. Its `consult`
skill finds the document or the record that answers a question. Its
`propose` skill sends a suite decision back here as an issue, from any
machine. Its `fold` skill turns those issues into decision records and
roadmap items in the hub, and document changes here, on the machine that
owns this repository (decisions 0013 and 0027).
