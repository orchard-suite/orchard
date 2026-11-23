# 0014. Vantage holds a system's documents and analyzes no code

- Status: Accepted
- Date: 2026-11-20
- Standard: 2026.1120.412

## Context

Vantage began as diagrams written as code. It has since learned to hold
what is written about a system beside the pictures of it. An estate now
wants the same for software nobody has documented: read the code, and
write the first documents from it.

That raises a question about what Vantage is. The work of reading a whole
project could go inside the hub, or stay outside it.

The two jobs are different in kind. A hub is a web service that answers in
seconds. An analysis is a job that runs for an hour or more, reads every
line of a project, and spends money under a budget. An analysis inside the
hub would make the hub hold access to the source of every project it
documents.

These facts were read from Vantage's repository on 2026-11-20, at v2.27.2:

- A document in a hub holds one YAML file, the views it draws, and pages
  of prose. A page is a Markdown file the YAML names. It names the model's
  boxes by id and embeds the document's pictures.
- A hub keeps every version of a document, with the files attached to it.
- Decision records live in a hub too, in numbered registries, beside the
  diagrams of the systems they decide about.
- A hub keeps an attached file only when a view or a page names it. A file
  that nothing names is refused.
- Vantage reads no file in a code repository that says which document
  describes it.
- The plugin ships six skills. None of them starts a project's first
  documents.

## Decision

1. **Vantage is the home of a system's living documents and diagrams.**
   It stays a hub: a place that holds, versions, checks, and shows them.
2. **Vantage analyzes no source code.** Reading a repository to work out
   what a system is does not happen in the hub.
3. **A code analyzer is a separate runner with its own access.** It reads
   a repository, writes a specification, and publishes a set of pages and
   a diagram to the hub, the way a connector pushes facts in.
4. **After the first publish, people and coding agents keep the documents
   fresh.** The analyzer comes back on a slow schedule, such as once a
   quarter, and reports where the documents and the code disagree. It
   flags. It never overwrites.
5. **The specification is kept with the document it describes.** It is a
   file attached to the document. So it gets the document's version
   history, and a tool can compare it with the living pages without a
   model.
6. **An analyzed repository is changed by one file only.** That file is a
   pointer. It names the hub, the workspace, and the document. An analyzed
   project is often one nobody wants to change, so one file is the most it
   carries.
7. **A small or new project needs no analyzer.** A coding agent reads it
   in one session and writes the first documents.
8. **An analyzer belongs to an estate.** It is on the estate's side of the
   seam, like a pusher. It meets the hub only through the hub's own
   document format. No member joins. The suite still has ten members.

Three things were weighed and turned down:

- Making the analyzer a part of Vantage. Point 2 says why.
- Keeping each project's last specification on the analyzer's own
  storage. Point 5 keeps one copy, with history, where its readers are.
- Running the analyzer again on changed files only. A full run on a slow
  schedule is affordable, and it is simpler.

Decision 0013 stands. This repository names no estate, and a hub belongs
to one. So the suite's own documents and its diagram file stay here, and a
hub holds a copy.

## What members owe

| Member | It owes |
| --- | --- |
| Vantage | An attached file that is kept, versioned, and downloadable but never drawn, and a way for a tool to read it back from the newest version. |
| Vantage | A pointer file a code repository can carry (`vantage.yaml`: the hub, the workspace, the document), and its plugin reading it. |
| Vantage | An onboarding skill that sees a project has no documents in the hub and offers to write the first set. |

## Left open

- **Where an analyzer's findings show.** This decision says the analyzer
  reports where the documents and the code disagree. It does not say
  where a person reads that report.

## Consequences

- `members.md` says what Vantage holds and what it does not do.
- `seam.md` lists code analyzers with what an estate holds.
- `README.md` names documents in Vantage's row.
- `roadmap.md` gains rows 16 to 18, one per thing Vantage owes.
- The diagram file gains the analyzer on the estate's side, and the rows
  that are owed.
- Vantage's pillar and its tending job do not change. No rating changes.

## Rules

Builds to:

- `keep-a-system-s-documentation-in-the-diagram-hub-tied-to-the`: a
  system's documents live in the hub, in the same document as its
  diagram, and generated ones are published through the hub's API.
- `keep-the-architecture-diagram-in-a-diagram-hub-updated-in-th`: the
  diagram is a document in a hub, not a file in the code repository. The
  pointer is the one file the repository keeps.
- `check-diagrams-for-drift-by-diffing-names-from-code`: the analyzer's
  later visits are a drift check that makes findings.
- `new-capability-goes-to-a-standalone-product-not-the-house-vi`: the
  analyzer is its own runner, not a new part of the hub.
- `stage-budgets-for-agent-runs-with-a-held-back-wind-down`: an analysis
  spends under a budget.
- `let-software-describe-itself-from-a-file-in-its-repository`: a
  repository says where its documents are with one small file.
- `skills-in-the-agent-plugin-read-the-rules-from-the-hub-and-n`: the
  onboarding skill ships in Vantage's plugin.
- `admit-a-tool-to-the-platform-suite-only-by-a-written-members`: weighed,
  and no member joins.

Departs from:

- `keep-a-system-s-documentation-in-the-diagram-hub-tied-to-the`: the rule
  has generated documents published again and again, each publish merged
  line by line over the last. Here the analyzer publishes once. After
  that it only reports. Why: once people and agents keep a document, the
  document is theirs, and a report cannot overwrite an edit.

New to the standard: the standard has no rule that a diagram hub never
analyzes source code, for a code analyzer as an estate's own runner with
its own access, for keeping a generated specification attached to the
document it describes, for a pointer file as the only change to an
analyzed repository, or for skipping the analyzer on a small or new
project.
