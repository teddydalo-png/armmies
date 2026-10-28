# Review: UTS Matching Grant (Cycle 4/2026) — API and outdoor fungal proliferation

Reviewed 28 Oct 2026, against the proposal text and the URCMS *Grant Add* form.

> **What I could not check.** The UMG scheme guidelines themselves (vot ceilings, whether
> in-kind counts as matching, undergraduate stipend eligibility) are not in front of me, and
> `uts.edu.my` is unreachable from this environment. Every point below marked **[verify]**
> depends on that document. I have also taken SRDC-TROPI's existence and remit from your
> proposal rather than confirming it.

## Verdict

**Not yet. One more week of work, not a rewrite.**

The idea is sound and the writing is well above the average internal proposal. But there
are four things a competent reviewer will find, and two of them threaten the headline
result rather than merely the presentation. There are also five places where the proposal
does not yet contain what the URCMS form demands, so in its current state you cannot
complete the submission even if the science were untouched.

Nothing here requires changing the project. All of it is revision.

---

## A. The two that threaten the result

### A1. You cannot compute an Air Pollution Index from the sensors listed

Malaysia's API is a specific Department of Environment index built from sub-indices for
**PM2.5, PM10, SO₂, NO₂, CO and O₃**, where the reported API is the highest sub-index.
Your sensor list is "PM2.5, PM10, CO, NOx, O₃, CO₂, Temp, RH". That is:

- **SO₂ missing**, so no API value you compute is an API.
- **NOx is not NO₂.** NOx is NO + NO₂; the index takes NO₂ specifically. A low-cost NOx
  sensor cannot be assumed to resolve the split.
- **CO₂ is in the list but is not an API pollutant** at all. It is useful for occupancy
  inference, so keep it — just do not imply it feeds the index.

The whole proposal is framed on "API classifications (Good, Moderate, Unhealthy)", including
Objective 2 and the sampling design. If a reviewer from MEITD, JKR or DOE reads this — and
your own Section 8 invites exactly those readers — this is the first thing they will catch,
and it undermines the framing rather than one sentence.

**Fix, cheapest version:** stop claiming API. Call it a **campus air-quality proxy index**
or report the pollutants individually, state plainly that it is not a DOE-equivalent API,
and define your own three-band classification from measured PM2.5 against WHO or Malaysian
ambient standards. This costs you nothing scientifically — PM2.5 is the pollutant that
actually matters for your hypothesis — and it removes an easy objection.

**Fix, stronger version:** add an SO₂ sensor and an NO₂-specific sensor, keep the API
framing, and validate the computed index against the nearest DOE station during the
calibration campaign. This is better but see the budget problem in C2; it is probably not
affordable at RM25,000.

Also worth a sentence: Sibu's nearest DOE API station gives you a free, continuous,
reference-grade comparator for the regional signal. Using it as ground truth for the haze
episodes, with your nodes providing the campus-scale spatial detail, is a much more
defensible design than low-cost nodes alone — and it is free.

### A2. Humidity bias will manufacture your correlation for you

This is the serious one, and it is not in the proposal at all.

Low-cost optical particle counters measure scattered light. Above roughly 85% RH, aerosol
particles take up water, grow, and scatter far more light, so reported PM rises sharply
**with no change in dry particle mass**. Your study sits precisely in that regime: Section
5.2 identifies RH above 85% as the critical fungal driver, and Sarawak sits above that
threshold routinely at night and through the wet monsoon.

So the chain of reasoning a reviewer will construct is:

1. High RH inflates your PM readings (instrument artifact).
2. High RH drives fungal colonisation (your own stated mechanism).
3. You report a correlation between PM and fungal abundance.
4. The correlation is explained entirely by RH, and your conclusion is an artifact.

You would be publishing a humidity-humidity correlation with a pollution label on it. The
project could run perfectly, produce clean data, and still yield a result that collapses
under one reviewer comment.

**This must be addressed in the methodology, not the discussion.** Minimum:

- Apply a published hygroscopic growth correction (κ-Köhler style, e.g. the Crilley et al.
  approach for low-cost OPCs) and **say so by name in Phase 1**.
- Report both corrected and uncorrected PM, so the correction is auditable.
- Pre-register RH as a covariate in every model, and state that the research question is
  the **partial** association of PM with fungal outcomes *after* adjusting for RH, rainfall
  and temperature. That is an honest, defensible claim.
- Keep at least one gravimetric or reference co-location period long enough to fit the
  correction, not a single calibration day (see C2).

### A3. The direction of causation is genuinely contested — and your own text says so

Section 3 states that fungal spores contribute "up to 20 percent of particulate matter mass
in warmer months". If spores are a component of PM, then PM and fungal abundance are
**mutually causal**, and a positive correlation is as consistent with "fungi raise PM" as
with "PM raises fungi". Your framing is uniformly the latter.

This is not fatal and it is quite interesting, but you must own it. Add a short subsection
stating the bidirectionality, and then use your design to break it: PM from combustion and
haze has a different size distribution and composition from spore-dominated coarse PM, your
time-lagged models test antecedent pollution against subsequent colonisation (not
simultaneous values), and the haze episodes are exogenous regional events not produced by
campus facades. Said explicitly, this turns a weakness into evidence that you understand
your system. Left unsaid, it is a reviewer's winning comment.

---

## B. Where the URCMS form wants something you have not written

These are mechanical, and they are the reason I would not submit this week.

| Form field | Status | What to do |
| --- | --- | --- |
| **Expected Result** (required) | **Absent.** You have "Significance" (§8), which is a different question. | The field wants: publications / theory / prototype / application / IP / human capital development / output to target community / return to UTS. Write it against those eight headings. You can fill all eight — 2 manuscripts, the dashboard as prototype, guidelines as application, FYP and GA training as human capital, the dataset as return to UTS. |
| **Budget split by Year 1 / Year 2 / Year 3** | **Absent.** You have one RM25,000 column. | The form totals per year. Dec 2026–Nov 2028 straddles three calendar years; decide whether the funder means calendar or project years and split accordingly. Equipment loads into Y1, sequencing and publication into Y2–Y3. |
| **Gantt chart, Milestone and Flow Chart PDFs** | Not prepared. | In the form these sit near the UBG block and the extraction is ambiguous about whether they are UBG-only. **[verify]** — but they are an afternoon's work and a Gantt strengthens any proposal, so prepare all three regardless. Your §10 is already most of the milestone file. |
| **Grant Type Remarks** ("compulsory for Matching Grant") | Not drafted. | Name SRDC-TROPI, the matched amount, the form the match takes, and the signed instrument that evidences it. See C1. |
| **Equipment / Equipment Location** | Not drafted. | List the reference-grade analyser (rented, UTS Sibu), PCR and sequencing platform (SRDC-TROPI, Kota Samarahan), and campus nodes. This field is also where you make SRDC-TROPI's facility contribution visible to assessors. |
| **Location of Research** | Would read "UTS" | Should be both sites. A meaningful share of the work is at Kota Samarahan. |
| **Research Centre** (optional) | Blank | Select BERI if it is listed. Centre-attributed grants support the centre's own reporting, and it costs you one dropdown. |

Two smaller things in the pre-filled header: **Office Telephone No. currently contains
"Room 43, Level 2, Block 6"** — your room, not a phone number — and **School and Programme
are blank**. Assessors see this page. Fix before submitting.

One piece of good news: the **Executive Summary limit is 300 words and yours is 183**. You
have 117 words spare, and the field explicitly asks for "expected output / outcomes /
implication", which your summary currently omits. Spend the headroom there.

---

## C. Budget and matching

### C1. The matching contribution is unevidenced, and the number looks engineered

RM24,987 against a RM25,000 request, described as in-kind with "no cash transfer between
parties". Two problems.

**First, is in-kind matching even eligible? [verify]** Many matching schemes require matched
*cash*, or cash plus documented in-kind up to a ceiling. If UMG requires cash, the proposal
fails on eligibility regardless of merit, and you need to know this before you spend another
day on the science. This is the single highest-value thing to check tomorrow morning.

**Second, RM24,987 reads as reverse-engineered** to clear a 1:1 bar by RM13. A reviewer's
instinct is to ask for the costing behind it. Either produce the itemisation — reagent
quantities, per-sample sequencing cost, technician hours at a stated rate, instrument
access fees — or round it honestly to RM25,000. An itemised RM24,987 is credible; a bare
RM24,987 invites the question.

In both cases you need **a signed letter from SRDC-TROPI** on letterhead, naming the
amount, the components, and the named staff committed. Right now the proposal asserts the
partner's contribution with nothing behind it. That is commonly an automatic deficiency on
matching schemes, and it is the item with the longest lead time because it depends on
someone else's signature. **Request it today**, ahead of all the revision work.

### C2. The instrumentation is underfunded by a wide margin

RM12,000 under VOT 26000 is carrying: microcontrollers, optical PM sensors, CO, NOx and O₃
sensors, CO₂ sensors, weather-resistant enclosures and gateways for 3–5 nodes — **and** all
the microbiology consumables (SDA, PDA, sterile swabs, settle plates, cryovials) — **and**
24 months of cloud hosting and data plans.

Research-usable electrochemical gas sensors run on the order of RM1,500–3,000 per gas per
node. Three gases across four nodes is RM18,000–36,000 by itself, before enclosures,
before a single petri dish. Cheap MOS-type gas sensors fit the budget but produce data too
drifty and cross-sensitive to support "correlate API parameters with fungal diversity".

So the budget and the science are describing two different projects. You must reconcile
them in one of these directions, and say which you chose:

- **Narrow to PM-only nodes** (plus T/RH), use the DOE station for the regional gas picture,
  and reallocate to a longer reference co-location. This fits RM25,000 comfortably, fixes A1
  and A2 at the same time, and is what I would do.
- **Keep the multi-gas ambition** and move it to a larger scheme. The UMG envelope will not
  buy it.

Either way, separate the two concerns in the budget table: putting sensors and petri dishes
in the same line hides the problem from you as much as from the reviewer.

### C3. Three vot misallocations

Against the form's vot list:

- **Instrument rental is in VOT 35000 (Accessories and Equipment).** The form has **VOT 24000
  – Rental**. Move it, or expect it to be queried.
- **Cloud hosting and data plans are in VOT 26000.** Those are Communications and Utilities,
  **VOT 23000**, which the form marks *"Only applicable for USRRG & UFSRRG"*. On a Matching
  Grant this expense may be **ineligible entirely [verify]**. If it is, your dashboard has no
  funded hosting for 24 months — plan on a free tier, on UTS infrastructure, or on an
  on-premise node, and remove it from the budget.
- **Open-access publication charges are inside RM3,000 of VOT 29000**, sharing that line with
  outsourced sequencing and permit fees. A single APC in this field is commonly
  RM7,000–14,000. As written, open access is unfunded. Target a no-APC or
  society journal, or say the APC will be sought separately — do not leave a promise the
  budget cannot keep.

Also **[verify]** whether an **undergraduate** stipend is allowable under VOT 11000: the form
has a separate *Graduate Assistant* section, which suggests the salary vot is oriented to
postgraduate GAs. If undergraduates are not eligible there, either recruit a GA or move the
work to FYP students, who cost nothing and who you want involved anyway (see F).

### C4. Travel is not plausible at RM2,000

That line covers repeated cold-chain courier runs Sibu → Kota Samarahan (roughly 300 km),
calibration site visits, **and** conference travel. Cold-chain shipping of live cultures
alone, across the multiple rounds your design implies, will consume most of RM2,000. Price
one actual shipment, multiply by your real number of rounds, and either raise the line or
cut conference travel from it explicitly.

---

## D. Design issues a methods reviewer will raise

### D1. No sample size, no replication, no power

The methodology says what you will do but never how much. There is no statement of: how
many sampling rounds, at what frequency, how many points per round, how many replicates per
point. Yet Phase 4 promises "correlation, regression and time-lagged models".

For those models the unit of analysis is the **sampling event**, not the swab. Two monsoon
campaigns gives you something close to n = 2 on the exposure of interest, and no amount of
swabbing within a campaign fixes that — those are pseudo-replicates. Time-lagged regression
on two time points is not a thing.

**Fix:** commit to a frequency — for example fortnightly sampling at fixed points across the
full 18 months of monitoring, with opportunistic intensive sampling triggered when the proxy
index crosses a pre-defined threshold (a haze episode). That gives roughly 35+ events,
captures several pollution episodes, and makes the lagged models honest. State the number in
the proposal. Add one short paragraph on expected effect size or at least a sensitivity
statement; even a crude power argument beats silence.

### D2. Season and pollution are confounded by construction

If pollution exposure is operationalised as "Northeast monsoon vs Southwest monsoon", then
pollution, rainfall, humidity, temperature, UV and wind direction all change together, and
no analysis can separate them. You cannot attribute a fungal difference to air quality.

This is solved by the same fix as D1: sample **within** seasons across varying pollution, so
that pollution varies while season is held approximately constant. Haze episodes are ideal
precisely because they are short, sharp and partly decoupled from the monsoon cycle. Make
the episode-triggered sampling a named element of the design rather than an afterthought.

Also, your monsoon labelling in §10 is off. In Sarawak the Northeast monsoon runs roughly
November to March and the Southwest roughly May to September. Phase 2 (Jun 2027 – Feb 2028)
is labelled "first (Northeast Monsoon)" but opens in the Southwest season; Phase 3
(Mar – Aug 2028) is labelled Southwest but opens in the Northeast tail. The phases are fine;
the season labels are swapped relative to the calendar. A Sarawak-based assessor will notice
immediately, and it is a one-line fix.

### D3. Only one cycle of each season

Even corrected, you sample each monsoon once. Any inter-annual anomaly — an El Niño year, an
unusually wet year, a severe or absent haze season — is indistinguishable from your effect.
You cannot fix this inside 24 months, so **say it**. One sentence in a limitations paragraph
("single-cycle design; inter-annual variability not estimable, addressed in the proposed
follow-on") is far stronger than letting a reviewer discover it.

### D4. Excluding algae weakens the controls, not just the scope

Section 5.1 defends a fungi-only focus on the grounds that algae are merely aesthetic. On
tropical facades, cyanobacteria and algae are typically the **pioneer** colonisers: they
condition the surface, retain moisture and raise water activity to the point where fungi can
establish. Two consequences:

- Your "clean" paired control surfaces may carry substantial algal or cyanobacterial biofilm,
  so they are not clean, they are pre-fungal. That weakens the pairing you rely on.
- The biodeterioration story is incomplete without the pioneers.

You do not need to add a workstream. Score algal and cyanobacterial cover visually at each
point (a simple percentage-cover or Braun-Blanquet-style scale, zero marginal cost) and carry
it as a covariate. Then reframe 5.1: fungi are the focus *because* they are the primary
biodeterioration agent, **while** algal pre-conditioning is measured as a covariate. That is
a stronger paragraph and it closes the gap.

### D5. Hypotheses are missing

Five objectives, all phrased as "to monitor / to collect / to correlate". No hypothesis, no
directional prediction. For a correlational study this matters, because without stated
hypotheses the analysis plan looks like a fishing expedition across six pollutants, multiple
diversity indices and several lags — which is a lot of implicit multiple comparisons.

State two or three directional hypotheses with the adjustment set named, e.g. *"H1: fungal
abundance on exterior surfaces is positively associated with antecedent 7-day mean PM2.5,
after adjustment for RH, rainfall and surface orientation."* Then pre-specify the primary
outcome and treat the rest as exploratory. The URCMS Background field explicitly asks for
"problem statements, **hypothesis**, research questions" — so this is a form requirement too,
not only good practice.

### D6. Objective 1 is a deliverable, not an objective

"...and to display the readings in real-time on a public campus dashboard" is an output.
Move it to Expected Result, where the form wants it, and leave Objective 1 as the
measurement objective. Minor, but it is the kind of tidy that signals a careful writer.

---

## E. Permits, biosafety and the schedule risk

Your §10 puts "SORAS application submitted and SBC Permit variation ... issued" in Phase 1,
with sampling beginning in Phase 2. That sequencing is right, and I am glad it is there —
most proposals forget it. But:

- **The permit is on someone else's clock.** A Sarawak Biodiversity Centre permit *variation*
  covering a changed title, scope, personnel and institutions is not a formality, and nothing
  in the proposal says what happens if it lands six months late. Since sampling cannot begin
  without it, a delay eats the first monsoon campaign and, in a single-cycle design, that is
  most of your exposure contrast. **Add an explicit contingency**: what you do with Phase 2
  if the variation slips (deploy and run monitoring only, defer biological sampling, extend
  into a third campaign) and who escalates.
- **Access and benefit-sharing.** Sequencing Sarawak-origin fungal isolates engages the
  state's access and utilisation framework, and transferring material from Sibu to Kota
  Samarahan is a transfer between institutions. Confirm that the variation covers *both* the
  transfer and the sequencing, and that the data-deposition plan (GenBank, presumably)
  is permitted. **[verify]** Depositing sequences derived from permitted material can carry
  conditions. Do not discover this after sequencing.
- **Biosafety is not mentioned at all.** You are deliberately culturing and concentrating
  *Aspergillus* and *Penicillium* — genera that include human pathogens and toxin producers —
  and the proposal says you will "identify toxigenic" species, with undergraduates doing the
  swabbing and culturing. You need a stated biosafety level for the UTS lab work, a risk
  assessment, PPE and waste-handling provisions, and confirmation that student involvement is
  cleared. A reviewer on a built-environment panel may not ask. Your institutional biosafety
  or OSH officer will, and finding out at that stage delays the project.

Add a short subsection covering all three. It reads as competence, and it is genuinely the
most likely cause of a 6-month slip.

---

## F. What is strong, and worth keeping exactly as it is

Said plainly because the above is long and the proposal is better than that length suggests:

- **The gap is real.** Coupling continuous outdoor air-quality monitoring with ITS-based
  community profiling on tropical facades is genuinely thin in the literature. Equatorial
  Borneo building-performance data is thinner still. This is a defensible niche.
- **The partner division of labour is clean.** UTS does instrumentation and field sampling,
  SRDC-TROPI does molecular work. No overlap, no ambiguity about who owns what. That is
  exactly what a matching scheme wants to see, and many proposals fail it.
- **Paired colonised/clean surfaces of the same material** as internal controls is a good
  design instinct, and cheap.
- **Policy alignment is specific, not decorative.** PCDS 2030 under Environmental
  Sustainability, with named downstream users (MEITD, JKR). Most proposals gesture at a
  strategy document; yours names the mechanism — haze reframed as a building-performance
  issue.
- **The living-lab shape compounds.** This is the instrument-your-own-campus strategy, and it
  is the right one: every node is an FYP, every facade is a dissertation, and the dataset
  gains value monthly in a way no one can retroactively replicate.

Two career notes, since they bear on how hard to push this:

Your 2026 KPI research section is **already capped at 30/30 with 54 raw points wasted**, so
this grant earns you **zero additional KPI marks this cycle**. That is not a reason to skip
it — the strategic value is real and it is the kind of thing promotion panels weigh
differently from the annual form — but it does mean you should not trade teaching marks for
it. Your only KPI headroom is the 15 marks in Teaching and Supervision.

Which suggests the efficient move: **run the fieldwork through FYP and postgraduate
supervisees.** Sensor fabrication, facade sampling, culturing and dashboard work are all
natural FYP projects. That converts grant activity into supervision marks — the one section
where marks are still available to you — while solving the C3 problem of whether an
undergraduate stipend is even eligible.

---

## G. Suggested order of work

Sequenced by lead time, not by importance, because two of these depend on other people.

**Today**
1. Request the signed letter of support and itemised costing from SRDC-TROPI (longest lead time).
2. Read the UMG guidelines for: in-kind matching eligibility, vot ceilings, VOT 23000
   eligibility, undergraduate stipends, and whether Gantt/Milestone/Flow Chart are required.

**This week**
3. Decide PM-only vs multi-gas (C2). Everything else in the budget follows from it.
4. Rewrite the index framing: proxy index, not API, plus the DOE station as comparator (A1).
5. Add the humidity-correction protocol to Phase 1 and RH adjustment to Phase 4 (A2).
6. Specify sampling frequency, rounds and replicates; add episode-triggered sampling (D1, D2).
7. Write the Expected Result field against the form's eight headings (B).
8. Split the budget by year; move rental to VOT 24000; resolve hosting and APC (B, C3).

**Before submitting**
9. Add hypotheses to Background; fix the monsoon labels; add the bidirectionality paragraph
   and the single-cycle limitation (A3, D3, D5).
10. Add the permit contingency and the biosafety subsection (E).
11. Add algal cover as a covariate and reframe §5.1 (D4).
12. **Add a references section.** The literature review currently has none, while making
    quantitative claims ("up to 20 percent of particulate matter mass", "exceeding 85
    percent"). The form asks for references explicitly. This is the most visible single
    defect in the document and the easiest to fix.
13. Fix the header fields: phone number, School, Programme, Research Centre.
14. Soften "virtually unexplored" and "unprecedented". Subaerial biofilm work on tropical
    facades is a real literature. Claim the *specific* novelty — API-coupled ITS profiling in
    equatorial Borneo — and you keep the claim while removing the invitation to be corrected.

Items 1, 2 and 12 are the ones that would most change a reviewer's verdict for the least
effort. Item 1 may be an eligibility gate, so do not leave it until the end.
