# Quality

This page is the suite's answer to one question: how does an estate keep
what it ships good, when agents write most of the changes? Decision 0010
adopted it, and decision 0011 added the half before a change exists. It
uses the words of `garden.md`.

## What quality is

Quality is not zero bugs. No estate reaches that, and chasing it makes
changes large and slow, which makes each failure worse.

Quality is four things. A person who uses the software notices the first
three. Its owners pay the fourth.

| Part | Plain meaning | The number |
| --- | --- | --- |
| **Rare** | A defect seldom reaches the people who use the software. | Change failure rate. |
| **Cheap** | One that does is small, and gone fast. | Time to restore, and the loop. |
| **True** | The software stays what its owners meant it to be. | Laws that hold, and who changed each law. |
| **Known** | Knowing all of that costs a known amount. | What checking costs per change, and what each check caught. |

An **escape** is a defect that reached the people who use the software.

## Bound, do not inspect

There are two ways to control what ships.

- **Inspect** each change. Someone, or some model, reads it and gives an
  opinion. The cost is paid on every change.
- **Bound** every change. Set limits once. Each limit then holds for every
  change, at the price of running a check.

Agents multiply the number of changes. So the cost of inspecting grows
with every agent an estate adds, and the cost of bounding does not. The
suite bounds. It does not gate a change on anyone's opinion of the code,
a person's or a model's (rule
`judge-results-with-a-cross-provider-council-never-gate-worki`).

A change has five bounds:

1. **Size.** A small change fails less, is read faster, and is undone
   faster.
2. **Reach.** Which paths it may touch.
3. **Laws.** What must stay true after it.
4. **Agreement.** Who must say yes before it ships, if anyone.
5. **Undo.** How it comes back out. What is asked, landed, and undone is
   one unit: every commit names the request it belongs to, so what a
   request landed comes out as one.

## It starts at the request

A change can pass every law and still make the software worse. A person
asks for ten special cases. An agent builds all ten, with tests. Nothing
that was promised broke, and the system now has ten rules where one would
do. The next grower copies them. No law catches this. A plan does
(decision 0011).

- **A request is evidence, not a specification.** It says a problem
  exists. It does not say what the fix is. Each claim in it is checked
  before anything relies on it: in the code, in its history, in the
  running system.
- **Fit the change to the system.** For a feature, find how the system
  already does like things. One general way beats a case for each field,
  page, or person. Decline, defer, or narrow what does not fit, and say
  why in words the person who asked would accept.
- **Judgment is spent on the plan, never on the code.** Where an owner
  must agree, they read a brief: what was asked and the problem under it,
  what will change as people will see it, what will not and why, the calls
  only they can make, what was checked, and a recommendation. It names
  behaviour and no files. It reads in two minutes.
- **The approved plan is a contract.** A machine holds the change to it.
  A change that grows well past its plan stops and asks again.
- **Agreement is one conversation.** One ask, with numbered rounds, where
  the owner already works. Each answer is planned into the next round. The
  builder gets the final shape: the request, the plan, and everything the
  owners said.

So the two costly kinds of attention go where each works. A person judges
intent, once, on a page. A machine judges the code, every time.

## Three roles

| Role | Who | What they own |
| --- | --- | --- |
| **Owner** | Whoever answers for what a bed is meant to be. A product owner for one bed, the gardener for the estate. | The laws. |
| **Grower** | A person or an agent session. | The code, and the working tests it writes to check itself. |
| **Gate** | The pipeline, the runner that lands a change, and the judge. | Running the checks, from where a grower cannot reach. |

One rule joins them: **nobody marks their own work.** A grower never
changes a law in the change that law judges.

The gate is not a new service. An estate's pipeline is already one. So is
a runner that lands an agent's change while the agent holds no credential.
So is the suite's one judge, Trellis.

**One bar, whoever builds.** A change made through a request desk, by an
agent at a keyboard, or by a person passes the same gate. So a
repository's rules are laws the gate runs. They are not lines in one
tool's instruction file, and not something a second agent reads a finished
change for. When someone has to read a change to see whether it kept the
repository's rules, a law is missing.

## Laws

A **law** is a rule that must stay true in a bed. It has three parts:

- one plain sentence a person can read,
- a check that runs and can fail,
- a home on a path that only the bed's owners change.

A law is a fence, in the words of `garden.md`: it holds whether anyone
reads it or not. A working test is not a law. A grower writes working
tests, changes them freely, and may be wrong in them. Both are needed. An
agent needs working tests to check itself as it goes. An owner needs laws,
because a test its author can edit proves only that the author agreed with
itself.

### Kinds of law

| Kind | What it says | Example | A tool an estate brings |
| --- | --- | --- | --- |
| Structure | How the parts may depend on each other, and what the bed is built from. | "The domain never imports the web layer." "No new runtime dependency without an owner." | ArchUnit, ArchUnitNET, dependency-cruiser, import-linter, go-arch-lint, cargo-deny |
| Contract | What callers were promised. | "No change breaks a caller of this API." | oasdiff, buf, GraphQL Inspector |
| Behaviour | What holds for every input, or every move of a state machine. | "An incident only moves forward, except to reopen." | fast-check, Hypothesis, rapid, proptest, FsCheck |
| Operation | How a change reaches people. | "A new feature ships switched off." "A migration only goes forward." | The pipeline's own steps, a migration linter such as Squawk |

Structure laws are the oldest idea here. The book *Building Evolutionary
Architectures* named them fitness functions in 2017: "an objective
integrity assessment of some architectural characteristic(s)". They are how
an architecture decision keeps holding after the person who made it has
left the room.

The suite ships none of these tools and names no default. Each was read
at its repository on 2026-11-18 and found maintained and free to run.

### Two sets of laws

- **The estate's laws** are the gardener's. They say what every bed must
  be: its security, its telemetry, its interfaces, how it is built and
  delivered. They are Trellis's packs.
- **A bed's laws** are its owner's. They say what this one product must
  do. They are checks in the bed, in its own language, on a protected
  path.

One judge reads both, so an agent and a person read one verdict.

### Where laws come from

Not from imagination. A law comes from one of two places:

1. **A decision.** A decision record says why. Where the decision can be
   checked, a law checks it. A decision with no check is soil: a grower
   may ignore it. The folder of decision records is itself a protected
   path.
2. **An escape.** When a defect reaches people, its trace ends in one
   remedy from the ladder in `garden.md` (rule
   `respond-to-an-escape-by-turning-it-off-then-closing-exactly-`). A law
   is the fence rung.

So a bed's laws stay few. Ten that hold beat a hundred nobody reads.

### A law must be able to fail

A check that cannot fail guards nothing (rule
`a-null-result-counts-only-if-the-test-could-have-come-out-po`). Three
proofs, cheapest first:

- **A failing case kept beside it.** Trellis asks this of every rule in a
  pack: a failing, a passing, and a no-data fixture.
- **Red, then green.** A fix carries a test that fails without the fix and
  passes with it. Graft asks this of every small fix.
- **A break-it run.** A tool breaks the changed lines on purpose and sees
  whether a check goes red. It is called mutation testing. It costs
  machine time and no model. It runs beside the path, on changed lines
  only.

A check also counts only where it ran. A test a builder wrote and the gate
could not run is not proof. A plan that leans on such a check needs an
environment that can run it, or it waits for a person.

### The door

Sometimes a law and a task disagree. Then the grower stops and asks. It
does not bend the code to fit, and it does not touch the law. The owner
rules: the task changes, or the law changes by the owner's hand.

This door matters more than any lock. One study gave coding agents tasks
whose tests could not be passed honestly. With a way to stop and flag the
task, one model's rate of cheating fell from 54% to 9%, and another's from
49% to 12%. Read-only tests stopped agents editing the tests, and did not
stop other tricks such as writing code that special-cases the test's
inputs.

## The ladder of proof

Proof is evidence that a change works. Pick the lowest rung that gives the
proof a change needs. Each rung down costs more and says less for certain.

| Rung | What it is | It costs | Its answer |
| --- | --- | --- | --- |
| 1. Types and schemas | The compiler and the data shapes refuse the wrong thing. | Nothing extra | Certain |
| 2. Structure and contract laws | Fixed rules read from the code and its definitions. | Seconds of machine time | Certain |
| 3. Behaviour laws and working tests | Checks that run the code. | Seconds to minutes of machine time | Certain for what they try |
| 4. A break-it run on changed lines | Proof that the checks above can fail. | Minutes of machine time | Certain for what it breaks |
| 5. A run in a real environment | The change deployed as production runs it, and used. | Minutes, and a place to run | Observed |
| 6. A watched rollout | Real use, a little at first, with an undo ready. | Exposure of real people | Observed, on the real thing |
| 7. A model's opinion of the change | A second agent reads the work. | Tokens on every change | A guess that shares the first agent's blind spots |
| 8. A person's approval | A person reads a brief of the plan and decides. Never the code. | The scarcest time there is | A judgment |

Rungs 1 to 6 are machines and facts. They cost the same whether an agent
or a person wrote the change. Rungs 7 and 8 are opinions, and they are for
the changes that need one.

## Three dials

Three things set what a change needs. Each answers a different question.

| Dial | The question | What it sets |
| --- | --- | --- |
| **Lane** | Who is asking? | How far a request may go with no person in the way. |
| **Kind** | Does the change restore what the software is meant to do, or alter it? | Whether an owner's judgment is needed. A fix restores. A feature, or any change in behaviour, alters, and always needs an owner. |
| **Class** | What does a failure cost, and can it be undone? | How much proof stands in the path. |

A fix that changes what people see is a feature. A small change in a top
class still needs top-class proof. The dials do not stand in for each
other.

### Class

Every bed has a **class**: how much its worst plausible failure costs,
and how hard that failure is to undo (rule
`set-rigor-by-what-a-failure-costs-in-a-few-named-classes`). The class
sets which rungs stand in the path.

Undo is the part that speed cannot buy back. A wrong colour comes out with
the next release. A lost row, a sent payment, a leaked secret does not.

| Class | When | In the path |
| --- | --- | --- |
| Low | A failure is cheap and easy to undo. | Rungs 1 to 3, and a fast undo. |
| Middle | A failure hurts someone. | Also a watched rollout, and break-it runs with a budget. |
| Top | A failure is hard to undo: money, access, lost data. | Also a check from outside the context that built the change, a rehearsed undo, and a person's approval. |

The class lives on the bed's entry in the catalog. Each estate names its
own classes. The suite ships none.

A risky kind of change raises the rigor of one change in any class: a
change to data shape, to sign-in, to a secret, to a contract others call
(rule `risk-trip-wires-derived-from-evidence-independent-of-size`).

### In the path, or beside it

A check **in the path** must pass before a change lands. A check **beside
the path** runs after, reports, and opens a request when it finds
something.

Every check in the path makes the loop longer. The loop is also how long
a fix waits. So a check in the path slows every restore, and that is a
cost paid during an escape, when it hurts most. The bed's loop budget is
the limit: what does not fit moves beside the path. In a low class nearly
everything costly sits beside it.

The suite's own pipelines work this way (decision 0026). The full check
runs once in the path, on the machine that lands the change. In CI the
tests are a witness: they run beside the build, from a clean checkout,
and the class sets whether a deploy waits for them.

## What checking costs

One change costs its owners this much:

```
  cost of one change  =  cost of checking it
                      +  chance it escapes  x  cost of an escape
```

and for a failure that can be undone:

```
  cost of an escape   =  people it reaches  x  how long until it is restored
```

Three things follow.

**1. Speed is the cheapest check, where undo exists.** Small changes, a
short loop, a rollout that drops no request, and a fast undo all shrink
the second line. Then less checking is worth paying for. An estate that
ships a small change every few minutes and restores in minutes is not
being careless. It has moved its spending from the first line to the
second.

**2. Speed buys nothing where undo does not exist.** For a top-class
failure the second line has a floor. That is where checking before the
change ships earns its cost.

**3. A second opinion from a model costs more than it looks, and returns
less.** Its cost is paid on every change, so it grows with the number of
changes. Its return shrinks with each reviewer added, because models make
the same mistakes.

### The evidence

Read at each source on 2026-11-18. These studies ran on the models of
their day, and newer models will score higher. The shape is what lasts:
cost that grows in a straight line, and return that flattens.

| Finding | Source |
| --- | --- |
| Two models that are both wrong agree on the same wrong answer about 60% of the time. Chance would be 33%. Models from one company agree more. | Kim and others, 2025 |
| The best code review tool tested found 23% of real issues, and 17% of what it flagged was real. Pooling ten reviews raised a combined score by 44%, to 21.9 out of 100. Gains flattened past five, and cost kept growing in a straight line. | SWR-Bench, 2026 |
| A team of debating agents used about 50 times the tokens of one agent, for a gain of 0.1 points on a coding benchmark. | Chun and others, 2026 |
| Agents watching other agents caught 42% to 50% of cheating on realistic coding tasks. | ImpossibleBench, 2025 |
| Developers acted on 0.9% to 19.2% of valid review comments from a model, and on 60% of those from a person. | Sun and others, 2026 |
| One vendor's review costs $15 to $25 a pull request and takes about 20 minutes. This is the vendor's own figure. | Anthropic, 2026 |
| A break-it run limited to changed lines: developers called 82% of what it raised useful. It uses no model. | Google, 2021 |
| A formal review by someone outside the team was not linked to fewer failed changes. | DORA |
| The gains from AI depend on working in small batches. In 2024 a 25% rise in AI use went with a 7.2% fall in delivery stability, and the report's own guess was larger changes. | DORA, 2024 and 2025 |
| In one vendor's data, 84% of changes over 1,000 lines drew findings, 7.5 each on average. Under 50 lines it was 31%, and 0.5 each. | Anthropic, 2026 |

Vendors report far better numbers for their own review tools than the
independent studies do. This page counts a vendor's benchmark of its own
product as a claim.

### What the suite does with this

- **No member gates a change on a model's review of the code.** A working
  change that passes its bounds is the proof.
- **A model's opinion has two uses.** In the top class, as the check from
  outside the builder's context, from a different provider than the
  builder. And where judgment is the point: a design, a plan, a name.
- **Every estate reads its own curve.** The studies above describe other
  people's code. Each bed carries two numbers of its own (below). A check
  that costs more than it catches is pruned.

### Two numbers

Plain counts and money, beside the three numbers of `garden.md`.

| Number | What it measures | Plain name in a table or an API |
| --- | --- | --- |
| **Cost of checking** | What a bed spends to check one change. | Pipeline minutes per change; money spent on agent sessions that check, per change. |
| **Catches** | What each check found. | Per check: times it failed on a change that was then fixed, and when it last did. |

The delivery measures stay the guard here too. A bed that cuts its
checking and sees its change failure rate or its rework rate rise has cut
too far. Decision 0016 made the guard five measures: rework rate is the
share of deployments that are unplanned and happen because of an incident
in production. It catches a defect that reached people without failing a
deployment. Nothing counts it yet (the roadmap).

## At every size

The same parts fit one person or a large organization. The dials differ.

| Part | One person, one project | A team | A large organization |
| --- | --- | --- | --- |
| Size and undo | Trunk, a small push, a release that rolls back. | The same. | The same, with a watched rollout for middle and top classes. |
| The request | The owner asks, and weighs it as they go. | An owner reads a brief before a feature is built. | A desk checks each claim and writes the brief. Owners answer in rounds. |
| Reach | The owner is at the keyboard. An agent's own rules keep it off the law paths. | Law paths need an owner's yes at the forge. | Lanes: who is asking sets what a request may do with no person in the way. |
| Laws | Types, and a handful of bed laws. | Bed laws, and the estate's packs in every pipeline. | The same, with packs for the industry's own rules. |
| Class | One class: low. | Two. | Three, set per workload in the catalog. |
| Proof in an environment | The machine in front of them. | A preview per change where reviewers need one. | A sandbox per agent session and a preview per change. |
| Cost | Nothing to run but the pipeline. | The judge in the pipeline. | The whole suite. |

An estate tailors in three layers, and each has one owner: the estate's
packs and classes, a program's lanes and protected paths, and a bed's own
laws.

## Environments

Rung 5 needs a place to run. The suite builds no environment tool and
names no default (decision 0010). An estate brings one and registers an
Orrery action that stands up an environment for a change. The standard
says how to name them, find them, and remove them (rule
`ephemeral-environments-named-by-owner-discovered-through-a-r`).

Whether a bed needs one follows how it ships. A person who can run the
whole system on their own machine needs no preview. A team that reviews
changes needs one per change. An agent that works unattended needs a
sandbox per session.

Judge an environment tool as any dependency (rule
`judge-a-dependency-by-license-maintenance-and-governance-and`): its
license, whether it is maintained, and whether its shared parts run
without a paid account.

## What the suite covers

Each part, and what answers it today. The ratings are a judgment, made on
2026-11-18 from each app's repository: Graft at v6.2.0 and Trellis at
v5.5.0. Graft's rows were read again the same day for decision 0011.
The facts in the proof, undo, cost, and red-then-green rows were read
again on 2026-11-20, from Graft at v6.6.0. No rating changed.

Quality is one of the map's three outcomes (decision 0016, `pillars.md`).
This table rates the parts that produce it.

| Part | Covered by | Rating | What is missing |
| --- | --- | --- | --- |
| Weigh the request | Graft | Partial | Graft checks each claim in a request against the code and its history, and keeps each check in the brief. A request made to an agent outside the desk is weighed by nobody. |
| Judgment on the plan | Graft, Orrery's approvals | Partial | A plan is a brief for its approvers and a build plan for its builder, and code holds the brief to its shape. One approval gains rounds. Only for a change made through the desk. |
| Bound size | Graft | Partial | Graft lands a clear defect unasked only under a size limit an admin sets. Nothing bounds the size of a change made outside the desk. |
| Bound reach | Graft | Partial | Graft holds each repository's protected paths to the lane an admin marks. Outside the desk the fence is the forge's own, and on some forges it needs a paid plan. |
| The estate's laws | Trellis | Covered | Nine packs, the same in the board and in a pipeline. Each rule ships a failing, a passing, and a no-data fixture. |
| A bed's laws | Nothing | Gap | No member reads which of a repository's checks are laws, or judges whether an owner changed them. |
| The door | Graft | Partial | A build that touches a protected path its plan did not name stops, and Graft asks again. A grower outside the desk has no door but a person. |
| Class | Trellis's catalog pack | Partial | The pack checks that an app in the catalog has a tier: how much it matters when the app is down. No member reads a class to set the rigor of a change. |
| Red, then green | Graft | Partial | Asked of every small fix. Not asked of a feature. Since v6.6.0 every criterion of a plan needs a proof before a build lands: a test that shows it, or a screenshot, or an approver's waiver. |
| Break-it runs | Nothing | Bring your own | The engines are open and free. No member reads what they find. |
| Proof in an environment | Graft's sandbox | Partial | Each agent session runs in a sandbox of its own. Graft's gate runs the check a repository names in its own file, or its `make check`. A failed gate names the command. A gate that passes does not say what ran. A build lands only when its builder says it is finished and each criterion is proven. A preview of a change is the estate's own. |
| Undo | Graft, and the estate's deploy tool | Partial | Graft names the ticket under every commit, and takes its commits back out when a round sends the build back and none are left. A build that fails its gate stalls, is kept, and never reaches the forge. A landed change whose pipeline is not green stalls the request, and the ticket links the commit and each failed job. A person decides what happens next. A new feature ships switched off. The rollout is the estate's own. |
| Watch | Dispatch, Muster | Partial | Dispatch holds each incident and its postmortem. Muster counts failed changes and time to restore. A postmortem does not name the law that would have caught it. |
| Cost of checking | Tally, Muster, Graft | Partial | Tally counts every agent session's tokens and each repository's build cost. Graft keeps what each request's agents spent on its catalog record, by stage: the screen, the plan, and the build with its proof. Muster writes each pipeline's median duration. Nothing joins them per change outside the desk. |
| Catches | Nothing | Gap | Muster reads a pipeline's result, not which check failed. |

## Sources

- Zhong, Raghunathan, Carlini. ImpossibleBench. 2025. <https://arxiv.org/abs/2510.20270>
- Kim, Garg, Peng, Garg. Correlated Errors in Large Language Models. 2025. <https://arxiv.org/abs/2506.07962>
- SWR-Bench. 2026. <https://arxiv.org/abs/2509.01494>
- Chun and others. Multi-agent debate on coding tasks. 2026. <https://arxiv.org/abs/2503.12029>
- Sun and others. A study of AI review comments. 2026. <https://arxiv.org/abs/2508.18771>
- Anthropic. Code review. 2026. <https://claude.com/blog/code-review>
- Petrović, Ivanković, Fraser, Just. Practical Mutation Testing at Scale. 2021. <https://arxiv.org/abs/2102.11378>
- DORA. Streamlining change approval. <https://dora.dev/capabilities/streamlining-change-approval/>
- DORA. Accelerate State of DevOps. 2024. <https://services.google.com/fh/files/misc/2024_final_dora_report.pdf>
- DORA. State of AI-assisted Software Development. 2025. <https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf>
- Ford, Parsons, Kua. Building Evolutionary Architectures. 2017. <https://nealford.com/books/buildingevolutionaryarchitectures.html>
