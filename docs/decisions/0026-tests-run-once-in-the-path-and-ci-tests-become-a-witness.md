# 0026. Tests run once in the path, and CI tests become a witness beside the build

- Status: Accepted
- Date: 2026-11-23
- Standard: 2026.1122.1851
- Capture: daa3bb22-2d93-4f59-83cd-be7ec61dd00b

## Context

`quality.md` sorts every check into the path or beside it, and says the
loop budget decides which (decision 0010). The members' own pipelines do
not do that yet. The owner asked how the suite keeps shipping fast and
stays good without more spend, and how it keeps its pipelines the same
across repositories.

These facts were read on 2026-11-23, from each member's workflows and its
release runs on GitHub:

- Every member releases with three jobs in a row: test, then version,
  then build. The test job runs `make check`, which `make land` already
  ran on the machine that pushed.
- Across twelve repositories, one release each, the test job was 29 of 71
  minutes: 41%. It was the largest job in Orrery (362 of 570 seconds) and
  Vantage (478 of 628). The history is one to three runs per repository,
  because decision 0024 started each with a fresh history.
- The workflows are copies, and they drift. The repositories use
  `actions/checkout` at v4, v6, and v7, `actions/setup-go` at v5, v6, and
  v7, and `docker/build-push-action` at v6 and v7. Each build file repeats
  the same steps to sign, attest, verify, and tag an image.
- Graft's image build took 524 seconds. Its Dockerfile installs Go, Node,
  .NET, Rust, uv, Playwright's libraries, and Claude Code on every
  release. Tally's took 252 seconds, installing three CLIs with npm.
- Trellis reads every workflow (its build fact: what each job runs on,
  runs, and uses). Its delivery pack has two rules about pipelines, and
  both ask only whether a private repository should have one.

Hosted minutes are free for a public repository. The cost of a slow
pipeline is the time a person waits for it.

## Decision

### Where tests run

1. **The test runs once in the path:** the full check, on the machine
   that lands the change. This is the rule already
   (`run-the-full-check-before-every-commit`).
2. **In CI the tests are a witness, beside the build.** A push to main
   versions, builds, signs, and tags at once. The tests run alongside,
   from a clean checkout. The clean checkout is what the witness is for:
   it catches a file that was never committed, which a working tree
   hides.
3. **The class sets what waits for the witness** (`quality.md`, "Class").
   A low-class bed deploys once its image is signed. A middle-class bed's
   deploy takes an image only with the witness's passing attestation. A
   top-class bed also waits for a person. A red witness on a version that
   shipped is fixed forward.
4. **A red witness becomes work, not a stopped release.** It opens a
   request on Graft. Where the bed's class is middle or top, it also
   opens an incident on Dispatch.

### One shape

5. **One pipeline kit, in the shed.** A public repository,
   `orchard-suite/pipelines`, holds versioned reusable workflows for each
   kind of bed (a Go service, a Node service, a CLI, a plugin, a prose
   product) and one action that signs, attests, verifies, and tags an
   image. Every member calls it at a major version, such as `@v1`, and
   copies nothing. It is a tool, not a member: an estate may use it, and
   the suite requires nothing of it. The suite is still not a build
   system (`strategy.md`).
6. **Trellis judges pipelines, with a pipeline pack.** Its build fact
   grows to read triggers, concurrency, the order of jobs, cache
   settings, the kit's version, and each Dockerfile's stages. The pack
   judges any estate's pipelines, whether they use the kit or not. Its
   first rules: the release calls shared workflows at a current version;
   every action is pinned; a release never cancels another; the image
   build reads and writes a cache; an image is signed and verified before
   its version tag; no test job stands before the build; dependency
   manifests are copied before source; base images are pinned and run as
   a user who is not root; a heavy toolchain lives in a base image. Only
   a high-severity rule stops a pipeline. The rest are findings on the
   board, with dated waivers.
7. **A heavy toolchain lives in a base image of its own,** rebuilt on a
   schedule. A member's release then adds one layer: its own program.

### The wait as a number

8. **Muster measures the wait.** It reads each job's time in the queue
   and its run time from the forge's job webhook, and writes each
   repository's time from landing to a published image.
9. **Orrery keeps a budget beside it,** so a slow pipeline is a finding
   and not a feeling. This is the loop number of decision 0007, made
   exact.

## What members owe

| Who | What it owes |
| --- | --- |
| A new shed tool, the pipeline kit | Reusable workflows per kind of bed, and the action that signs, attests, verifies, and tags. |
| Every member | Call the kit in place of its own workflows. Run its tests as a witness beside the build. |
| Graft and Tally | Move their toolchains and CLIs into a base image of their own. |
| Trellis | The build fact's new fields, and the pipeline pack. |
| Muster | Each job's queue and run time, and landing-to-published time per repository. |
| Orrery | Landing-to-published time as a field an estate's model may name, with a budget. |
| Graft | Take a red witness as a request. |
| Dispatch | Take a red witness on a middle- or top-class bed as an incident. |
| Each estate | Have its deploy tool check the witness's attestation for middle- and top-class beds. |

## Left open

- Where the witness's attestation is checked when an estate's deploy tool
  cannot read one.
- Whether break-it runs join the witness (decision 0010 left their source
  open).

## Consequences

- A release no longer waits for a second run of tests that already
  passed. Taking the test job out of today's runs would shorten releases
  by a fifth to three quarters. That is an estimate from very few runs.
- A commit that is red in a clean checkout can get a version and a signed
  image before anyone knows, and a low-class bed can deploy it. It is
  fixed forward.
- Every member depends on one workflow repository, so a broken release of
  the kit breaks every pipeline at once. The kit is versioned, and a
  member moves to a new major version on purpose.
- `members.md` lists the kit in the shed, as owed. `roadmap.md` gains a
  section for this decision.

## Rules

Builds to, from the platform standard, version 2026.1122.1851:

- `run-the-full-check-before-every-commit`: the one test in the path.
- `bound-every-change-instead-of-inspecting-it` and
  `count-what-checking-costs-and-catches-and-prune-the-rest`: a check in
  the path, or beside it.
- `give-a-repository-a-pipeline-only-when-something-consumes-it`: a
  public repository keeps full CI; the tests still run.
- `own-quality-with-the-one-conformance-judge-never-a-second-ju`: the
  pipeline pack lives in Trellis.
- `scope-rules-once-per-pack-and-tune-board-and-pipeline-from-o`: the
  board and the pipeline read one tuning file.
- `measure-every-ci-job-hosted-or-self-hosted-from-the-forge-s-`: the
  wait.
- `the-template-s-root-makefile-is-a-contract-that-changes-ever`: one
  kit changes every pipeline at once.
- `keep-templates-in-each-estate-and-plant-them-through-one-cat`: the kit
  is a tool beside the suite, and an estate keeps its own templates.

Departs from: `one-pipeline-per-push-release-calls-ci-first-pr-ci-cancels-p`.
That rule cuts a version only after CI's tests pass. The owner ruled on
2026-11-23 that the tests run beside the build, for the reasons above.
