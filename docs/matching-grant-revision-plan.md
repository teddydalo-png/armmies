# Revision plan — UTS Matching Grant, under the corrected premise

28 Oct 2026. **Supersedes parts of `matching-grant-review.md`.** That review assumed the
API–fungal correlation was the core claim. You have since said the **microbiology is the
primary work and the air-quality monitoring is supplementary**, and the grant is **2 years
(Year 1 and Year 2 only)**.

That inverts the proposal's own emphasis, and it is good news: the two issues I flagged as
threatening the headline result were both consequences of hanging a causal claim on the
air-quality side. Demote that side and they largely go away. What replaces them is a
different problem — **the primary workstream is the least specified part of the document.**

> Planning figures for sequencing and consumables below are order-of-magnitude, for
> structuring the budget. Get real quotes before submitting. Everything marked **[verify]**
> needs the UMG guidelines, which I cannot reach.

---

## 1. The framing problem, in one line

The title, the executive summary, the first objective and 68% of the budget all lead with air
quality. The science you actually care about appears as Phase 3, in three sentences.

A reviewer reads priority off the title and the budget, not off your intentions. Right now
both say "this is an air-quality project with a microbiology appendix". Fix the framing first,
because the budget and methodology edits follow from it.

**Title.** Lead with the biology and the material, and keep air quality as context:

> *Molecular characterisation of fungal communities driving biodeterioration of tropical
> educational building exteriors, with campus air-quality and microclimate context at UTS Sibu*

Clumsier than yours, but it puts the contribution where the work is. Tighten the wording;
keep the order.

**Executive summary.** You have 117 words spare against the 300 limit. Reorder so the
molecular work leads, air quality appears as environmental context, and spend the headroom on
the expected outputs the field asks for and your draft omits.

**Objective order.** Promote the characterisation and identification objectives to 1 and 2.
Demote monitoring to 3 as context. Move the dashboard clause out of the objectives entirely —
it is a deliverable, and the form has a field for those.

---

## 2. What this fixes for free

Worth saying explicitly, because it removes work rather than adding it:

- **The API-validity problem is gone.** You no longer need a DOE-equivalent index, so no SO₂
  sensor, no NO₂-specific sensor, no claim to compute an API. Report PM2.5, temperature and
  RH as microclimate and air-quality *context*. Name it that. The whole
  Good/Moderate/Unhealthy classification can go, along with the objection it invited.
- **The humidity-bias trap drops from fatal to manageable.** It mattered because the headline
  claim was a PM–fungal correlation. As context, it needs only honesty: apply a published
  hygroscopic correction, report corrected and uncorrected PM, and keep RH in any model. Do
  not drop this entirely — if you report *any* PM–fungal association, the artifact argument
  still applies to that specific claim.
- **The confounding and power problems shrink.** Season-confounded exposure was a problem for
  a causal air-quality claim. For a descriptive-plus-mechanistic microbiology study, monsoon
  contrast is a legitimate sampling stratification rather than a contested exposure variable.
  You still need sample numbers (§4.1), but you no longer need to defend causal identification.

---

## 3. REMOVE

| Item | Why | Frees |
| --- | --- | --- |
| Public API display unit in a high-traffic area | Pure optics. No research value, and it is the single largest discretionary line in a budget that cannot afford its own primary workstream. | ~RM5,000 |
| Reference-grade instrument rental | Only needed to validate an API you are no longer claiming. Use the nearest DOE station as a free regional comparator. | part of RM5,000 |
| CO, NOx, O₃ sensors | Cannot be bought at research quality within this envelope, and unnecessary for a contextual role. | ~RM4,000–6,000 |
| CO₂ sensor | Not an air-quality index pollutant. Keep **only** if you explicitly use it for occupancy inference; otherwise drop. | small |
| "API classifications (Good, Moderate, Unhealthy)" as a design axis | Replaced by continuous PM2.5 plus monsoon stratification. | — |
| The claim to "identify toxigenic species" | Not supportable as designed. See §5.2 — either add an assay or reframe to "potentially toxigenic taxa". | — |
| "virtually unexplored", "unprecedented evidence base" | Subaerial biofilm work on tropical facades is a real literature. Claim the specific novelty instead. | — |
| Conference travel inside VOT 21000 | The line cannot carry it alongside cold-chain shipping. State that dissemination travel is sought separately. | — |
| Open-access APC inside VOT 29000 | A single APC exceeds that whole line. Target a no-APC or society journal, or seek the APC separately. | — |

Removing the display unit and the gas sensors alone is roughly **RM10,000 released** — which
is very close to what a properly specified molecular workstream costs.

---

## 4. ADD — the primary workstream needs real methodology

Phase 3 is currently three sentences for what you now say is the main work. A microbiology
reviewer will spend their whole review here. Every item below is expected in a molecular
community-profiling study.

### 4.1 Sampling, specified

State the numbers. At minimum:

- **Surface area standardised** per sample (e.g. 10 × 10 cm template), swab versus tape-lift
  versus scrape, and which for which material.
- **Number of sampling points** per building, per orientation, per material.
- **Replicates per point** — at least duplicates, ideally triplicates.
- **Frequency and rounds**, with a total sample count. A defensible floor for community
  profiling with monsoon contrast is roughly 40–60 samples; say your number.
- Paired colonised/clean surfaces retained — this is already a good instinct, keep it.
- **Algal and cyanobacterial cover scored visually** at every point as a covariate. On tropical
  facades these are the pioneer colonisers that condition the surface for fungi, so your
  "clean" controls are probably pre-fungal rather than clean. A percentage-cover scale costs
  nothing and closes the hole in §5.1. Reframe 5.1 accordingly: fungi are the focus *because*
  they are the primary biodeterioration agent, *while* algal pre-conditioning is measured.

### 4.2 Resolve the contradiction in your own §5.4

Your literature review states that culture-based methods "significantly underestimate
non-culturable or stressed environmental species" and advocates a dual approach. Your
methodology then describes a culture-only pipeline: culture at UTS, transport live isolates,
sub-culture, extract DNA from isolates, Sanger-sequence ITS.

That is culture-dependent profiling. You will characterise what grows on SDA and PDA, which
is a well-known minority of a facade community. A reviewer will quote your own §5.4 back at
you.

**Recommended:** do both, which is what your own review argues for.

- **Culture-independent ITS metabarcoding** (Illumina amplicon sequencing) on DNA extracted
  directly from surface samples. This is the novel contribution — a community profile of
  tropical facade mycobiota in equatorial Borneo — and it is now standard, outsourceable, and
  the single most publishable element of the project.
- **Culture plus Sanger** on the isolate subset you need *alive* for the degradation assay and
  for deposition in a culture collection.

If budget forces a choice, metabarcoding is the one to keep: it answers the community question
and does not depend on culturability. Culturing is then a small parallel effort for live
isolates only.

### 4.3 ITS alone will not resolve your two headline genera

This is the sharpest technical correction, and it goes to the heart of the work.

ITS is the accepted primary fungal barcode, but it is **well documented as under-resolving
*Aspergillus* and *Penicillium* at species level** — precisely the two genera you emphasise
throughout. Species-level identification in those genera conventionally requires a secondary
protein-coding marker: **β-tubulin (benA)**, **calmodulin (CaM)** or **RPB2**.

As written, the proposal promises species-level identification of toxigenic *Aspergillus* and
*Penicillium* from ITS. That claim will not survive review.

**Fix:** state ITS as the primary barcode for community profiling, and add benA and/or CaM
sequencing for the *Aspergillus* and *Penicillium* isolates specifically. Budget for the extra
reactions. Name **UNITE** as your ITS reference database and name your pipeline (DADA2 or
QIIME2) with a stated taxonomic confidence threshold. Dr Sharon Lau is already listed on
bioinformatics; naming the pipeline costs a sentence and buys a lot of credibility.

### 4.4 Low-biomass contamination control — currently absent

Facade swabs are low-biomass samples. In low-biomass molecular work, reagent and kit
contaminants can dominate the resulting profile, and reviewers in this area treat controls as
non-negotiable. The proposal mentions none.

Add: **extraction blanks, PCR no-template controls, and field blanks** (a swab exposed and
handled but not contacted with a surface), all carried through sequencing and reported, plus a
stated approach for in-silico decontamination. Also name a DNA extraction kit suited to low
biomass and to the inhibitors in cementitious dust.

This is cheap, and its absence is the kind of thing that makes a methods reviewer doubt
everything downstream.

### 4.5 "Material-degrading" needs a functional assay, not a taxonomy

Identifying a taxon reported in the literature as biodeteriogenic is not the same as
demonstrating that your isolates degrade your materials. Right now Objective 4 promises the
former and the title implies the latter.

**Cheap, high-value addition:** an in-vitro degradation screen on the isolates you cultured —
mortar or cement coupons inoculated and incubated, with mass loss, surface pH change, and acid
or oxalate production measured against uninoculated controls. A few hundred ringgit of coupons
and some incubator time.

This is worth doing for three reasons: it makes the degradation claim defensible, it is a
second publishable unit on its own, and **it is squarely your own expertise.** Your
biomineralisation and microbially induced mineral-process background is about exactly this
interface — microbial activity dissolving and precipitating minerals in cementitious systems.
Your §5.3 describes acid secretion, calcium oxalate crystal formation and cement matrix
dissolution, which is your home ground, and the proposal never says so.

### 4.6 Deposition and data

State that sequences go to **GenBank** with accessions, and isolates to a recognised culture
collection. Check this against the SBC permit conditions **[verify]** — permitted material can
carry restrictions on deposition and on derived sequence data, and you do not want to discover
that after sequencing. Add a one-paragraph data-sharing plan regardless of whether the form
requires it for your scheme.

### 4.7 Biosafety — still missing

You will deliberately culture and concentrate *Aspergillus* and *Penicillium*, with students
handling the samples, and you say you will identify toxigenic species. Add a short subsection:
containment level for the UTS work, risk assessment, PPE, waste autoclaving, and confirmation
that student involvement is cleared. Your institutional biosafety or OSH officer will ask even
if the panel does not, and that is a delay you can pre-empt.

### 4.8 Hypotheses

Still needed, and the URCMS Background field asks for them explicitly. Under the corrected
premise they should be about community composition, not air quality — for example: fungal
community composition differs significantly between monsoon phases and between facade
orientations; *Aspergillus* and *Penicillium* relative abundance is higher on cementitious than
on timber substrates; isolates from colonised surfaces produce measurable mass loss on mortar
coupons relative to controls. Those are testable with the design and they frame the statistics.

---

## 5. Rebalanced budget, Year 1 and Year 2

Built on the corrected premise: roughly **three quarters of spend on the primary workstream**,
which is both correct and a visible argument to the assessor that the proposal means what it
says. Project years, Y1 = Dec 2026–Nov 2027, Y2 = Dec 2027–Nov 2028.

| Vot | Line | Y1 (RM) | Y2 (RM) | Total | Notes |
| --- | --- | --- | --- | --- | --- |
| 11000 | Salary and wages | 1,000 | 2,000 | 3,000 | Research assistant stipend, weighted to the fieldwork-heavy second year. **[verify]** whether an undergraduate is eligible here or whether this must be a Graduate Assistant. |
| 21000 | Travelling and transportation | 1,000 | 2,000 | 3,000 | Cold-chain courier, Sibu → Kota Samarahan. Now load-bearing: the primary workstream depends on it. Price one real shipment × your number of rounds. Conference travel removed. |
| 26000 | Research materials and supplies | 8,000 | 4,000 | 12,000 | **Split this line explicitly.** Microbiology ~RM9,000: media, sterile swabs, settle plates, cryovials, low-biomass DNA extraction kits, PCR reagents and primers (ITS + benA/CaM), electrophoresis, mortar coupons. Sensors ~RM3,000: three PM2.5 + T/RH nodes with enclosures. |
| 29000 | Professional services | 1,000 | 6,000 | 7,000 | The main cost under the corrected premise: outsourced ITS metabarcoding (~40–60 samples), Sanger for isolates, secondary-marker reactions for *Aspergillus* and *Penicillium*. Plus SORAS and SBC permit fees. **Get a quote — this line drives the whole budget.** |
| 24000 | Rental | 0 | 0 | 0 | Reference-instrument rental removed; DOE station used as comparator. |
| 35000 | Accessories and equipment | 0 | 0 | 0 | Display unit removed. Use this line only if UTS genuinely lacks an incubator or −20 °C storage, in which case move money from 26000. |
| | **TOTAL** | **11,000** | **14,000** | **25,000** | |

Sanity check: sequencing plus microbiology consumables is **RM19,000 of RM25,000 (76%)**,
sensors **RM3,000 (12%)**. Against your current draft's 68% on the supplementary side, that is
the single clearest signal to a reviewer that the proposal is coherent.

**Matching side.** The SRDC-TROPI contribution becomes more defensible under this premise, not
less — they are contributing the facilities and personnel for the *primary* workstream. Say
that. But the itemisation and the signed letter are still outstanding, and in-kind eligibility
is still **[verify]**. This remains the item with the longest lead time; request it today.

---

## 6. Timeline consequences

Two changes follow from the premise inversion.

**The molecular work can no longer sit at the end.** Your Phase 3 compresses DNA extraction,
PCR, sequencing and analysis into Mar–Aug 2028, after all sampling completes. For the primary
workstream that is both a schedule risk and a waste of Year 1. Switch to **rolling processing**:
transport and process each sampling round as it completes, so Year 1 samples are sequenced
while Year 2 sampling runs. You get an interim result, an earlier first manuscript, and the
chance to fix a protocol problem before it has contaminated two years of samples.

**The permit now gates the primary workstream.** The SBC permit variation was a schedule risk
before; now a delay stops the main science rather than one phase. Add the explicit contingency:
if the variation slips, deploy monitoring and run non-destructive surface scoring and material
characterisation while waiting, and name who escalates.

Also fix the monsoon labels in §10 — in Sarawak the Northeast monsoon runs roughly November to
March and the Southwest roughly May to September, so the labels on Phases 2 and 3 are swapped
relative to the calendar.

---

## 7. Citations — you are right, and this is the most visible defect

Confirmed: **no citations in the Background (§3), the Problem Statement (§4), or the Literature
Review (§5)**, while all three make specific empirical and quantitative claims. The URCMS
Background field asks for references explicitly. Of everything in this document, this is the
cheapest fix with the largest effect on how the proposal reads.

**I am not going to generate the reference list.** I cannot reach any literature database from
this environment, and inventing plausible-looking citations for a document you are submitting
under your own name is the worst thing I could do to you here. What I can give you is the
precise list of claims that need a source, so the search is mechanical.

### Claims requiring citation

**Background (§3)**
1. Moisture dynamics driven by climate, design and occupancy are central to fungal proliferation.
2. RH above 85% and persistent surface moisture are the most critical factors, especially in monsoon seasons.
3. Atmospheric particulate matter correlates positively with fungal spore concentrations.
4. **Spores contribute up to 20% of PM mass in warmer months** — a specific number, needs a specific source.
5. Occupancy elevates indoor and outdoor fungal levels.
6. *Penicillium*, *Aspergillus*, *Cladosporium* dominate building exteriors.
7. Osmoregulation and melanisation as humidity adaptations.
8. Fungi secrete acids and ligands that dissolve cement matrices; calcium oxalate formation; increased porosity; crack formation.
9. Moisture and carbohydrate-rich adhesives promote decay fungi in wood-based materials.

**Problem statement (§4)**
10. Sarawak experiences seasonal regional haze with elevated API readings.
11. Chemical washing is costly and environmentally taxing.
12. **"There is no continuous, auditable API monitoring network..."** — a negative existence claim. Either cite a survey or soften to "to our knowledge, no...". As stated it is unfalsifiable and a local reviewer may simply know a counterexample.

**Literature review (§5)**
13. Algae cause primarily aesthetic discolouration while fungi penetrate porous materials (the §5.1 justification — this is doing load-bearing work and is uncited).
14. Facade orientation, shading and ventilation modulate surface moisture retention.
15. PM acts as physical carrier and nutrient substrate for spores on facades.
16. **Reduced UV during haze favours fungal survival by mitigating photoinhibition** — the most speculative claim in the document. Cite it or label it explicitly as a hypothesis.
17. *Cladosporium sphaerospermum* xerotolerance at low water activity.
18. Fungal biofilms accelerate biodeterioration via EPS production and PM accumulation.
19. Culture-based methods underestimate non-culturable or stressed species.
20. qPCR, NGS and ITS sequencing performance for community profiling.
21. Lack of standardised detection protocols for tropical buildings.
22. PCDS 2030 — cite the strategy document itself.

Add two to the revised text: the **hygroscopic growth correction** method you adopt, and the
**ITS under-resolution of *Aspergillus*/*Penicillium*** point, since both are now method
justifications rather than background.

Twenty-two claims, most of which one good review article will cover three or four of at once.
A focused day in Scopus or Google Scholar closes this.

Two routes if you want help: run the literature search on your own machine and paste the
candidates here and I will match them to claims and format the list; or add
`api.openalex.org`, `api.crossref.org` and `pub.orcid.org` to this environment's allowed
domains and I can query them directly. The PubMed connector in this session also failed to
connect, so it would need re-authorising.

---

## 8. Still outstanding from the first review

Unchanged by the premise inversion:

- **Expected Result** field — still absent, still required, eight headings to write against.
- **Gantt, Milestone, Flow Chart** PDFs — not prepared. **[verify]** whether required.
- **Grant Type Remarks** — compulsory for Matching Grant, undrafted.
- **Equipment / Equipment Location** — undrafted; this is where SRDC-TROPI's PCR and sequencing
  facilities become visible to assessors, which matters more now that they hold the primary
  workstream.
- **Location of Research** — should name both sites.
- Header fields: Office Telephone contains your room number; School and Programme blank;
  Research Centre not selected.
- Executive summary has 117 words of headroom and omits expected outputs.

---

## 9. Honest overall read

Under the corrected premise this is a **better proposal than it currently presents as**, and
the fixes are mostly subtraction and reordering rather than new science. The molecular
characterisation of tropical facade mycobiota in equatorial Borneo, tied to a functional
degradation assay on cementitious materials, with air quality and microclimate as context, is a
coherent and genuinely under-studied contribution that sits on your actual expertise.

What is currently in front of a reviewer is a sensor project with a microbiology appendix, an
uncited literature review, a budget that spends two thirds of its money on the supplementary
component, and a species-identification claim its chosen marker cannot support.

Those are all fixable in the week you have. The three that would most change a verdict:
**reframe to put the microbiology first (§1), rebalance the budget to match (§5), and add the
references (§7).** The two that are not in your control — the SRDC-TROPI letter and the
guidelines check — should be moving today.
