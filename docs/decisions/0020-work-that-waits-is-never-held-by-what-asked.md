# 0020. Work that waits is never held by what asked for it

- Status: Accepted
- Date: 2026-11-21
- Standard: 2026.1120.2003
- Capture: 3f8f0654-4d35-446f-b597-bed11c117261

## Context

Some work must wait for a person, or must run for a long time. A change to
infrastructure waits for an approval. A large export runs for hours.

Read from Orrery's repository on 2026-11-21, at v1.156.4:

- The actions engine has eight kinds of backend. Three hand the work to
  something that stays up: a webhook, a forge workflow, and a runner. One,
  `caller`, hands the work to nobody. Whoever asked must come back and do
  it.
- An approved `caller` run that nobody starts within the hub's limit is
  cancelled. The limit is one setting for the whole hub, sixty minutes by
  default. A run that is still running after that limit is given up.
- A runner is a standing program. It runs a command and holds it until it
  ends, for ten minutes by default and never longer than the hub's limit.

A tool whose work exists only on the machine that asked uses `caller`.
An infrastructure tool does, because the plan it will apply is a file on
that machine. So the thing that asks is also the thing that must do the
work. In use that thing is a process an agent started, and an agent's
process does not live for hours. An estate saw approved runs cancelled
because nothing was awake to start them, and saw others start only
because a person happened to open the conversation in time.

Three ways to close this were weighed.

| Way | Why it was or was not taken |
| --- | --- |
| A helper on each machine that outlives the agent and does the work when the hub calls | It still stops when the machine sleeps. It puts a program on a person's machine that the suite commands, which decision 0018 and the standard both turn down. Not taken. |
| The agent delivery member, Slipway, becomes the place jobs run | Slipway already makes one sandbox for each agent session. But decision 0009 made it the hands that change a repository, and nothing else. A second place that approves and tracks runs would stand beside the engine. An estate that runs Orrery without Slipway would get no long jobs. Not taken. |
| The actions engine starts one job for each run | The engine already approves, starts, and records every run. Taken. |

## Decision

1. **Work that waits for a person is never held by the thing that asked.**
   A tool or an agent asks, and may then stop. The wait, the start, and
   the work all happen where nothing of the asker's has to be awake.
2. **The actions engine starts one job for each run.** A job is one
   container, started the moment the run is approved, or asked when it
   needs no approval. The run names the image.
3. **A starter holds one right.** A starter is a program the estate runs.
   It connects out to the hub, as a runner does. It may start a job and
   read how the job is going, and nothing more. The job holds its own
   identity. No standing program holds the power of the jobs it starts,
   and the hub holds no credential of the estate's.
4. **A run lives by heartbeat.** A run that keeps reporting stays alive.
   A run is given up when it has gone quiet, not when a clock has run
   out. An action may still name a ceiling.
5. **A job reports on its own run only.** It is given a credential good
   for that one run.
6. **Change keeps two apps, and the line between them is fixed.** Slipway
   changes a repository. The actions engine carries every other change,
   and that now includes the long ones and the ones that wait. Slipway
   asks for its own runs through the engine already, so there is one
   record of runs. This closes the question decision 0016 left open.
   Change stays Partial. That rating is a judgment.
7. **Nothing is put on a person's machine to do the work.** Decision 0018
   stands: a device reports, and nothing commands it.
8. **Environments stay the estate's.** Point 11 of decision 0010 stands.
   Slipway is not an environment tool and not a place jobs run. A desk
   may use the tool an estate stands its environments up with. How it
   asks is still Slipway's own design (decision 0011).

## What members owe

| Who | What it owes |
| --- | --- |
| Orrery | A backend that starts one job for each run, a starter for a cluster and one for a cloud's job service, runs that live by heartbeat, and a credential good for one run. |
| Each estate | A starter, a place for jobs to run, and one identity for each family of job. |
| A tool that asks through `caller` because its work is on the asker's machine | Put what the job needs where the job can read it when it asks, and ask for a job. This is that tool's own design. |

## Left open

- **How a run that ends wakes the agent that asked.** A person is told
  through Dispatch. An agent's conversation is not. Until it is, the next
  step waits for a person to wake the conversation.
- **Where a conversation lives when no machine is awake.** A request to
  Slipway runs in the estate. A conversation a person holds with an agent
  about operations runs on that person's machine.

## Consequences

- `roadmap.md` gains rows 39 and 40, loses the open question on Change,
  and gains the two above.
- `pillars.md` says the engine now carries the work that waits.
- `members.md` says what Orrery owes.
- `strategy.md` records that the question on Change is closed.
- The suite still has ten members. No rating changes.

## Rules

Builds to:

- `extend-the-existing-actions-engine-every-run-goes-to-the-led`: one
  engine gains one backend, and no product brings a runner of its own.
- `ship-the-job-runner-as-a-bare-image-and-give-each-family-of-`: each
  family of job brings its own image.
- `self-service-cloud-operations-run-as-a-narrow-machine-identi` and
  `workload-identity-instead-of-cloud-keys`: a job runs as a machine
  identity, never as the person who asked.
- `devices-report-to-the-house-nothing-commands-them`: nothing is added
  to a person's machine.
- `give-a-sandboxed-agent-a-handle-on-one-request-never-a-hub-c`: a job
  holds a credential for its own run.
- `map-the-platform-as-pillars-each-one-a-question-it-must-answ`: Change
  is still one pillar answered by two apps, and is rated for it.

Departs from:

- `size-the-runner-fleet-by-keys-program-tier-and-power`: the rule has
  one runner hold one key, because a runner runs a command with
  everything it holds. Here a starter holds no key of the estate's
  beyond the right to start a job, and each job holds its own. Why: a
  job that must hold a project's power for days should be the only thing
  that holds it. The owner ruled on this on 2026-11-21. The rest of the
  rule is kept: keys, not teams, still size the fleet.

New to the standard: the standard has no rule that work which waits for
a person is never held by the thing that asked, for a run that lives by
heartbeat, or for one job for each run as a backend of the actions
engine.
