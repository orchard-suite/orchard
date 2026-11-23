# The garden

This page is the suite's framework. It says what a platform is, what
tending it means, and which jobs a gardener needs tools for. Decision 0007
adopted it. Decision 0008 settled where friction is counted and where
seeds live. Decision 0010 added the words for quality; `quality.md` is
that framework. Decision 0016 set the map this work sits in: the three
numbers here feed two of its outcomes, flow and quality (`pillars.md`).

## The idea

A platform is not a thing you build and hand over. It is the place where
other people's software grows. Its customers, people and agents, copy what
they find there. What they make becomes what the next one finds. So quality
compounds, up or down.

Owning a platform means tending it. This was always true. Agents make it
urgent, because an agent copies faster, and more exactly, than a person
does.

## Words

- **Bed**: one repository. It is the unit a gardener tends.
- **Grower**: whoever makes changes in a bed. One person, or one agent
  session.
- **Gardener**: whoever tends the beds. A platform team, or one person in
  the time left over.
- **Seed**: a template a new bed starts from. A good seed arrives with its
  soil, stakes, and fences already in it.
- **Nursery**: one small bed where a change to the platform is tried
  first, before every bed gets it.
- **Weed**: something that should not grow, and spreads when copied. A
  lint suppression, a skipped test, a copied block, a waiver with no end.
- **Stem**: the thing that taught a grower to make the weed. An example in
  the bed, a line in an instruction file, a slow tool, a missing check.
- **Owner**: whoever answers for what a bed is meant to be. A grower
  changes a bed. An owner says what must stay true in it.
- **Law**: a rule that must stay true in a bed, written as a check that
  runs, and kept where only the bed's owners change it. A law is a fence a
  grower cannot move.
- **Class**: what a bed's worst plausible failure costs, and how hard it
  is to undo. It sets how much proof a change needs.
- **Escape**: a defect that reached the people who use the software.

## Three materials

A gardener shapes a bed with three materials. They differ in one way: how
hard they hold.

| Material | What it is | How hard it holds | Examples |
| --- | --- | --- | --- |
| **Soil** | What a grower reads before and while it works. | It shapes. A grower may ignore it. | Instruction files, the code already in the bed, docs, error messages. |
| **Stake** | A measured number in the path of work, with a budget. | It shows. Work that breaks the budget is seen at once. | A test run under 60 seconds, a bundle under 200 KB, an error budget. |
| **Fence** | A boundary that holds whether anyone reads it or not. | It stops. | A required check, a signed image at admission, a permission, a law. |

Most of a bed is soil, and the code already there is the strongest soil of
all. A grower follows the example in front of it before the rule above it.

## Five moves

Tending is one loop.

```
  Sense -> Trace -> Fix -> Stake -> Prune -> Sense
```

1. **Sense.** See where growers struggle and where weeds appear. Agents
   send no support tickets, so the gardener has to look.
2. **Trace.** Follow one weed back to its stem. Ask what taught it.
3. **Fix.** Fix the stem, and every copy of the weed, in one pass.
4. **Stake.** Put a number with a budget where the problem was, so it
   shows if it comes back.
5. **Prune.** Delete what is no longer used: old examples, dead code,
   stale instructions, checks that guard nothing.

## The ladder of remedies

When a trace finds the stem, pick the first remedy that works, from the
top.

1. **Delete what taught it.** Remove the bad example or the stale line.
2. **Fix the tool or the loop.** Make the right thing the fast thing.
3. **Add a stake.** Measure it, with a budget.
4. **Add a fence.** Block it. A law is this rung: one escape, one law.
5. **Add an instruction.** Last, because soil grows with every line and a
   grower reads less of it each time.

## Three numbers

Each bed carries three numbers. They are plain counts and times, not
scores.

| Number | What it measures | Plain name in a table or an API |
| --- | --- | --- |
| **Loop** | How long a grower waits for an answer after a change. | Median pipeline duration; median local test time. |
| **Friction** | How often a grower gets stuck. | Retries, stops, redirects, and failed tool calls per session. |
| **Weeds** | How much there is that should not grow. | Counts by kind: lint suppressions, skipped tests, open waivers. |

The delivery measures stay: deploy frequency, lead time, change failure
rate, time to restore, and, since decision 0016, rework rate. They are the
guard: a bed whose three numbers improve while its delivery measures get
worse is being gamed.

## Running a platform is tending too

The same words cover serving customers, not only building for them.

- A customer is a grower.
- An incident is a weed. Its postmortem is a trace, and the ladder picks
  the fix. A new runbook is the last rung, not the first.
- An incident a change caused is an escape. How rare escapes are, and how
  fast each is restored, are two of the four parts of quality
  (`quality.md`).
- An error budget is already a stake.
- A support ticket is a friction signal. Agents never send one.
- Answering a live incident is response, not tending. Tending starts when
  it is over.

## What the suite covers

Each job, and what answers it today. The ratings are a judgment, made on
2026-11-12 from each app's repository, in the terms `pillars.md` uses.
The stake and seed rows were judged again the same day, after Orrery built
its ground and decision 0008 was made. The fence and prune rows were
judged again on 2026-11-18, by decision 0010. `quality.md` rates the
parts of quality the same way.

| Job | Covered by | Rating | What is missing |
| --- | --- | --- | --- |
| Sense what exists and its health | Orrery, Muster, Dispatch | Covered | |
| Sense what it costs | Tally | Covered | |
| Sense what growers did | Annals | Partial | Only Orrery, Dispatch, and Graft say they post to it. |
| Sense friction | Nothing | Gap | No member counts retries, stops, or failed tool calls. A new, small source will, and Orrery will show its numbers (decision 0008). It is not built. |
| Trace a weed to its stem | Dispatch's postmortems, Annals | Partial | A postmortem traces an incident. Nothing links a weed in code to what taught it. |
| Fix at the source, everywhere | Orrery's actions, Graft | Partial | An action can ask a backend to change many beds. Graft has an agent change one bed per request (decision 0009). No member finds every copy of a weed. |
| Stake | Trellis in a pipeline, Orrery's scorecards and field budgets | Partial | Orrery keeps a budget beside a number and shows when the number is outside it. The budget shows and stops nothing. Each estate sets its own; the suite ships none. |
| Fence | Trellis in a pipeline, with waivers; Graft's protected paths | Partial | The fences themselves (required checks, admission, permissions) are the estate's own. No member reads a bed's own laws (decision 0010). |
| Prune | Tally's right-sizing, Muster's checkouts | Partial | No member finds unused code, stale instructions, or checks that guard nothing. Decision 0010 says how a check is judged: by what it costs and what it caught. Nothing counts either yet. |
| Soil | Trellis's build pack | Partial | It checks that a bed has an instruction file. It does not judge what the file says. |
| Seed | Bring your own | Bring your own | Seeds stay with each estate (decision 0008). Orrery's ground lists the templates beds were started from, which beds have fallen behind, and the action that plants a new one. |
| Nursery | Nothing | Bring your own | An estate picks its own nursery bed. |

## The sky and the ground

Orrery is the suite's one board. It draws an estate as a sky: the sun is
everything, each area of the catalog is a sector, and each kind of thing
is a planet. The garden does not replace that view. It sits one layer
down. Orrery has built that layer. It is in preview: an admin opens it to
nobody, to the people named, or to everyone.

| Layer | What it shows | The question |
| --- | --- | --- |
| The sky | Every kind of thing, by area, coloured by its worst status. | What do we have, and is it healthy? |
| A planet | One kind, such as repositories. | How is this kind doing? |
| The ground | Every bed of that kind, each with its three numbers. | Where does a gardener go first? |
| A bed | One repository: its soil, stakes, fences, and weeds. | What does this bed need? |

A farmer's orchard reads the sky to plan the ground. The name fits.

Three rules keep the picture honest:

1. Every picture maps to one real number.
2. The plain number is one click away.
3. Tables and APIs use plain words. A column says "lint suppressions",
   never "weeds".

The garden is a view. A reader can switch it off and lose nothing: a
switch at the top of the ground shows the same things as tables under
plain names.

## The shed

Some tending tools are not services. A grower or a gardener installs them
on a machine: a CLI, a desktop app, a skill. They are not members, because
the membership test in `seam.md` is for services an estate runs. They are
listed in `members.md` under "The shed", each with the job it does.
