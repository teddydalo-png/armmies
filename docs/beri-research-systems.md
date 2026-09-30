# BERI / SBE research systems — what to build, and whether to keep PastiKerja

Assessed: 30 Sep 2026. For: research centre head, BERI, UTS Sibu.

> **Assumption flagged.** Public sources show UTS has a *School of Built Environment (SBE)* and a
> separate *School of Business and Management (SBM)*, so "SBE" here is read as Built Environment.
> "BERI" is not publicly indexed and `uts.edu.my` is blocked from this environment, so its remit is
> inferred as energy / built-environment (consistent with UTS's SCORE mandate). §4 is the only
> section that changes materially if BERI is actually business/economics-facing.

## 1. Should you drop PastiKerja?

**Deprioritise it — but not because of JobSarawak.** The competitor finding is the weaker reason.
The real reason is that PastiKerja does not compound with anything you already own.

An academic's assets are a publication record, a grant track record, a supervision pipeline, and
industry relationships in a specific domain. PastiKerja builds none of those for a built-environment
or energy researcher. It would consume two years of evenings to produce a small-margin SME SaaS in a
field you do not publish in, cannot supervise students in, and cannot fund from SRDC. That is the
disqualifier. A free state portal is merely the second problem.

Note also that as an academic you were never in the fight JobSarawak wins. A state portal beats you
on price and distribution; it does not beat you on *measurement*. Nobody — not JobSarawak, not
JobStreet, not MOHR — publishes data on how Sarawak employers actually behave after an application
is submitted. That is a genuine empirical gap.

So there are exactly two honest options:

- **Shrink it to an instrument.** Drop the marketplace entirely. Run it as a measurement study:
  recruit 100–200 Sibu/Kuching employers, submit controlled applications or track consenting real
  applicants, and measure response rate, time-to-response, and salary-disclosure behaviour by sector
  and firm size. That is a publishable paper (labour economics / correspondence-study design), it
  needs no backend, no payments, no Act 246 exposure, and it costs one semester and an ethics
  approval instead of two years. If the data is striking, *then* the platform has a reason to exist,
  and JobSarawak becomes a collaborator rather than a competitor.
- **Shelve it.** Keep the HTML. It is a good portfolio piece and a good FYP brief for a student.

Recommended: shelve the product, and only run the study if labour-market research is genuinely in
BERI's scope. If it is not, shelve it entirely and put the same energy into §4.

## 2. What research-centre staff actually struggle with

Ranked by what a centre head can fix without institutional IT approval, and what staff will
visibly thank you for.

| # | System | Effort | Needs approval? | Value |
| --- | --- | --- | --- | --- |
| 1 | Research output dashboard | 1–2 weeks | No | Very high |
| 2 | Grant radar + deadline engine | 1–2 weeks | No | Very high, time-critical |
| 3 | Proposal factory | 2–3 weeks | No | High |
| 4 | Postgrad supervision tracker | 1 week | Light | Medium-high |
| 5 | Research data vault + DMP generator | 3–4 weeks | Yes (PDPA) | High, rising |
| 6 | Sibu living lab (field instrumentation) | 1–2 semesters | Yes | Strategic |

Build **1 and 2 first.** Both run on free public APIs, need nobody's permission, and produce
something staff can see inside a fortnight. That earns you the credibility to ask for 5 and 6.

## 3. The two to build now

### 3.1 Research output dashboard

The annual scramble to collate everyone's publications into a spreadsheet is the most reliably hated
task in any Malaysian research centre. It is also completely automatable.

Pull from free, no-auth, no-cost APIs:

- **OpenAlex** — full bibliographic graph, citations, concepts, institutional affiliation. Free, no
  key, generous rate limits. This is the workhorse.
- **Crossref** — DOIs, funder acknowledgements, publication metadata.
- **ORCID** — the per-staff anchor. Getting every BERI member onto an ORCID iD is step zero and is
  worth doing regardless; it makes every downstream system work.
- **DOAJ** — open-access and predatory-journal screening.

What it produces:

- Per-staff and centre-wide output counts by year, type, and venue quartile.
- Citation and h-index trends without anyone logging into Scopus.
- **Co-authorship network** — the genuinely useful output. It shows which BERI members have never
  co-published with each other, and which external institutions you are one hop from. That is a
  collaboration strategy map, and it is the kind of figure that goes straight into a grant proposal.
- Auto-generated annual report tables and a promotion-file pack per staff member.
- MyRA-style category tallies. Note: **MyRA is mandatory for public universities and voluntary for
  private ones**, so for UTS this is leverage and internal KPI/SETARA support rather than a
  compliance obligation — but having the numbers ready is a positioning advantage, not a chore.

Caveats to design around: OpenAlex affiliation matching is imperfect for a young private university,
so expect to maintain a manual override table mapping staff to their author IDs. Do not try to
scrape Scopus or Web of Science — licensed, and it will get the university's IP blocked. Use them
only for the final quartile check, by hand.

### 3.2 Grant radar — and this one is time-critical

**SRDC's Strategic Research Grant Call 2026 opened 1 November 2025 and closed 31 January 2026.** If
the cycle repeats, the **2027 call opens in roughly one month.** Building the radar now means BERI
enters that window prepared instead of scrambling in December.

Why SRDC matters more to you than any other funder: **the Principal Investigator must be based in
Sarawak.** That is a structural advantage you hold and almost every Malaysian researcher does not.
Applications must align to **PCDS 2030**, are submitted through SRDC's **RPMON** system, and the
2026 thematic areas ran to sustainable petrochemicals, aerospace manufacturing, semiconductors,
advanced materials and electronics. **BrightSparX** is a separate SRDC scheme worth tracking.

What the radar does:

- Monitors SRDC, MOHE (FRGS / PRGS / TRGS), MOSTI, MTDC, relevant Sarawak agencies, and selected
  international calls on a schedule.
- Holds a structured profile per staff member (keywords, methods, past outputs, supervision
  capacity) and matches open calls against it — so the digest says *"this call fits Dr X and Dr Y,
  and here is the PCDS 2030 thematic it maps to"*, not just *"a call opened"*.
- Escalating reminders at T-60/30/14/7 days, delivered where staff actually read things — WhatsApp
  or email, not a portal nobody logs into.
- A post-mortem log: every submission, outcome, reviewer comment. After two cycles this tells you
  what actually wins, which is institutional knowledge that currently walks out the door with
  whoever wrote the last successful proposal.

Build note: funder sites change layout and several are JS-rendered, so treat scraping as
best-effort with a human confirmation step. A missed deadline caused by a silent scraper failure is
worse than no radar, so the digest should always state when each source was last successfully
checked.

## 4. The strategic one: a Sibu living lab

The instinct behind PastiKerja — instrument a real local system, collect data nobody else has — is
a good instinct. It is simply pointed at the wrong domain. Point it at buildings and energy in Sibu,
where your expertise, your school, your funder alignment and your student pipeline already are.

**Concretely:** instrument the UTS campus and a handful of partner buildings in Sibu — temperature,
humidity, CO₂, occupancy, power draw — with low-cost sensors, streaming to a dashboard and an open
dataset. Tropical, equatorial, Borneo-specific building performance and energy baselines are
genuinely thin in the literature, and Sibu sits in the SCORE corridor.

Why this compounds in a way a job board never could:

- **Publications** — baseline papers, then calibration and retrofit studies, for years off one
  installation.
- **Grants** — maps directly onto PCDS 2030 and SRDC's energy and sustainability priorities, with
  you as a Sarawak-based PI.
- **Students** — every sensor node is a final-year project; every building is a dissertation.
- **Industry** — Sibu contractors, developers and the local councils have a reason to sign an MOU
  with you, which is a centre KPI in its own right.
- **A moat of exactly the kind you wanted** — a longitudinal dataset that gets more valuable every
  month and that nobody can replicate retroactively.

Start small and cheap: 10–15 nodes in one campus building for one semester, one dashboard, one
dataset, one paper. Prove the pipeline before asking for money for 200 nodes.

*If BERI turns out to be business/economics-facing rather than energy, the same structure holds but
the instrument changes: a recurring Sibu/Sarawak SME panel survey — a standing longitudinal dataset
on local firm conditions — plays the identical role, and PastiKerja's response-behaviour study
becomes one wave of it.*

## 5. Sequence

1. **Weeks 1–2** — Get every BERI member an ORCID iD. Build the output dashboard. Show it at a
   centre meeting. This is your credibility purchase.
2. **Weeks 2–4** — Build the grant radar. Have it live before the SRDC 2027 window opens.
3. **Weeks 4–8** — Proposal factory, seeded with BERI's past successful submissions. Target the
   SRDC call with it.
4. **Semester 2** — Living lab pilot: one building, 10–15 nodes, one dataset.
5. **Ongoing** — Data vault and DMP generator once PDPA sign-off is in hand. Note the PDPA
   (Amendment) 2024 obligations apply to human-subject research data too: DPO, 72-hour breach
   notification, 7-day notice to affected individuals.
6. **PastiKerja** — shelved, or run once as a one-semester measurement study. Not a product.

## 6. Agents worth defining

| Agent | Job |
| --- | --- |
| `output-sync` | Nightly OpenAlex/Crossref/ORCID pull, dedupe, override table, dashboard rebuild |
| `grant-radar` | Scheduled funder monitoring, staff-profile matching, escalating digests, source-freshness reporting |
| `proposal-draft` | Drafts against funder templates, checks PCDS 2030 alignment, builds budget and Gantt tables |
| `data-steward` | PDPA screening of instruments and consent forms, DMP generation, retention checks |
| `lab-telemetry` | Sensor ingest, gap and drift detection, dataset versioning and release packaging |

Only the first two are worth creating today.
