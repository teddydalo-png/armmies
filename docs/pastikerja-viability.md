# PastiKerja — Malaysia viability assessment

Assessed: 30 Sep 2026. Input: `PastiKerja.html` single-file clickable prototype.

## 1. Verdict

**The mechanic is worth doing. The Sarawak-first, ghosting-led framing as built is not the
version to launch, and the prototype cannot go live as a product — only as a landing page.**

Three separable judgements:

| Question | Answer |
| --- | --- |
| Is the problem real in Malaysia? | Yes, and bigger than ghosting — job **scams** and undisclosed salary are the acute pain. |
| Can this file go live? | As a waitlist/landing page: yes, in days, after the legal fixes in §5. As the product: no — it is a front-end mock with zero backend. |
| Is the wedge defensible? | The SLA/reliability data is. "Sarawak jobs" is not — that space is already taken (§3.3). |
| Would I fund/build it? | Bootstrapped and national-from-day-one, yes. Sarawak-only paid job board, no. |

## 2. What the prototype actually is

An honest read of the build state, because it determines the "go live" answer.

**Present:** 5 screens (jobs list, applications dashboard, candidate profile, employer profile,
post-a-job form), a two-tier listing model (Verified / Listed), client-side search + location +
tier filters, an apply modal, and genuinely good information design. The visual and copy work is
strong — the trust framing, the "this badge cannot be purchased" line, the reliability-both-ways
candidate profile, and the privacy note are the best parts of the whole thing.

**Absent:** everything behind the glass.

- No backend, database, auth, or sessions. All 7 jobs are a hardcoded `JOBS` array.
- Every action is an `alert()`. `submitApp()`, `postJob()`, `externalApply()` do nothing.
- "SSM verification" is `if (value.length >= 8)` in the browser.
- No payments, no pricing, no monetisation anywhere in the product.
- No notifications — and the whole SLA mechanic is a notification product at its core.
- No employer console. The SLA promise requires employers to change statuses; there is no screen
  where they can. This is the single largest missing surface.
- No SLA clock. Nothing computes elapsed working days, flags a breach, or recalculates a score.
- Dates are hardcoded to mid-2026 and will rot.
- Not accessible (no focus states, `alert()`-driven flow, icon-only meaning in the signal bars).
- English only — see §4.2.

Realistic effort to a launchable v1: **8–14 weeks** for one strong full-stack developer, with the
employer console and the notification pipeline as the bulk of it.

## 3. The Malaysian market case

### 3.1 The problem is real, but you have picked the second-best pain

Ghosting is a genuine grievance. But the acute, wallet-level, news-cycle pain in Malaysia right now
is **job scams**: police recorded 1,537 job scam cases with RM31.8 million in losses in Q1 2026
alone. Ghosting makes people bitter; scams make people destitute. Undisclosed salary is the other
universal complaint — the majority of Malaysian listings still show no pay band.

The prototype already contains both answers (mandatory salary bands on Verified listings, automated
scam-pattern screening) but buries them as supporting features under a ghosting headline.
**"No scams. Real salaries. A guaranteed answer."** is a stronger proposition in this market than
"you deserve an answer", and it is the same product.

### 3.2 Market size — the numbers that decide the shape of the business

- Sarawak labour force: **1.262 million** (Q1 2026).
- Sarawak business establishments: **83,463**; SMEs **74,000+**, which is only **6.8%** of Malaysia's.
- Of those, the number that hire formally, repeatedly, and would pay for a portal is realistically
  **3,000–5,000**.

At RM150–300/month, capturing 300–800 paying accounts over three years is **RM0.5m–2.9m ARR**.
That is a respectable bootstrapped business. It is not a venture-scale outcome, and it is a hard
ceiling. Sarawak works as a **beachhead for trust-building**, not as the market. The plan must be
national (Klang Valley + Johor + Penang carry the revenue) with Sarawak as the credibility story —
which the existing "Built in Sarawak, for all Malaysia" line already gets right.

### 3.3 Competition — the geographic wedge is already occupied

This is the finding that should most change the plan:

- **JobSarawak** (`job.sarawak.gov.my`) — the Sarawak state government's own one-stop job platform.
  Free to employers. You cannot win a price war with a state government.
- **SarawakJobs.com** — an established, award-winning localised Sarawak job site with a mobile app.
- **JobStreet by SEEK** — ~1,000 Kuching listings, job ads up 33% YoY in H1 2026. Plus Maukerja
  (4m+ users), Hiredly, Indeed, LinkedIn, FastJobs.

So "a job board for Sarawak" is not a gap — it is a crowded shelf with a free option on it. The only
thing none of them offer is the **enforced response commitment and the public reliability record**.
Position against the mechanic, never against the geography.

The good news: incumbents structurally *cannot* copy this quickly. Employers are their paying
customers, and this product's core feature is publicly grading paying customers. That conflict is
the moat, and the accumulated reliability history compounds into a real data asset.

### 3.4 A regulatory tailwind worth designing around

Malaysia is moving toward **mandatory job-vacancy reporting via PERKESO** — the EIS (Amendment)
Bill would require an employer to report a vacancy before hiring and update PERKESO once it is
filled, with a proposed maximum RM10,000 fine for non-notification (there is active lobbying as of
July 2026 to keep it voluntary, so treat the timing as uncertain).

Note what that obligation *is*: employers being compelled to declare when a role opens and when it
closes. That is precisely the dataset PastiKerja wants. **"Post once — fill your vacancy and satisfy
your reporting in one step"** is a far easier SME sale than "let us publish your ghosting rate", and
it converts a compliance chore into your distribution channel. Watch this bill closely; if it
passes, it is the single biggest growth lever available to you.

## 4. The three design problems that matter most

### 4.1 The SLA metric is gameable, and gaming it is the rational employer response

This is the deepest flaw. The score counts *any* status change inside the window. An employer who
bulk-marks every applicant "Viewed" then "Not Selected" on day one scores a **100% response rate
and a 0.2-day average** — and is a *worse* experience than one who takes 10 days and writes a real
reply. Your badge would reward the exact behaviour you exist to punish, and the fastest-moving
employers on your leaderboard would be the ones auto-rejecting everyone.

Fixes, in order of value:

1. **Require a reason code on rejection** (skills gap / experience / salary mismatch / role filled /
   internal hire), and surface the distribution publicly. The prototype's MegaTron rejection message
   is a perfect template — make that the enforced minimum, not a nicety.
2. **Candidate-confirmed outcomes.** You already built `selfReport()`. Make it central: score the
   *gap* between employer-declared and candidate-reported outcomes, and flag mismatches. That is
   the anti-gaming primitive, and it is your unique data.
3. **Publish a shortlist rate alongside the response rate.** 100% response with 0% interviews is
   visibly a rubber stamp.
4. **Weight by meaningfulness, not just speed.** A same-day templated rejection should not outrank a
   6-day personal one. Cap the benefit of sub-24h decisions.

### 4.2 English-only is fatal for the target segment

The roles in the prototype are Admin Clerk, Retail Supervisor, Customer Service Rep, Site Safety
Officer — the clerical and blue-collar segment. That segment does not job-hunt in English. A product
called *PastiKerja* presented entirely in English is a contradiction its own users will feel.

**Bahasa Malaysia must be the default**, with English and Chinese toggles. In Sarawak, Sarawak Malay
phrasing in the microcopy buys disproportionate trust. This is not a localisation backlog item; it
is a launch requirement.

### 4.3 The product is built for email and desktop; Malaysian SME hiring runs on WhatsApp

An SLA product is a reminder product. If the employer nudge and the candidate status update do not
arrive on WhatsApp, the loop does not close. Budget for WhatsApp Business API from day one —
phone-first identity (the profile's "Phone Verified" instinct is right), one-tap status updates from
the message itself, and no requirement that a candidate own a formatted CV.

### 4.4 Smaller but real

- **Reframe the employer pitch from punishment to tooling.** As written, the paying side is sold a
  public humiliation risk ("your score drops publicly"). Sell the tool — one-click statuses,
  automatic reminders, fewer WhatsApp chases, a badge as the reward — and make the downside
  *private first*: grace period, private nudge, then score impact. Same mechanism, several times
  the conversion. Expect "what if we get busy?" to be objection #1 in every sales call; the one
  2-day extension per role is a good start but too thin.
- **Adverse selection.** Only employers who already respond well will opt in, so early badges won't
  discriminate and the Verified pool will look thin. Plan for a deliberately small, hand-recruited
  launch cohort (20–30 Kuching employers) rather than an open signup.
- **SSM verification has a real unit cost.** There is no free official API; SSM e-Info company
  profiles run about **RM15.40** per lookup. At 3 lookups and some manual follow-up per employer,
  carry roughly RM20–50 CAC in verification alone, and design the callback step to be batched.
- **Verified/Listed is the right idea** and the honesty of the "Listed" disclosure is commendable —
  but see §5.2, it is also your biggest liability.
- **Hire confirmation is the weak link in monetisation.** "8 confirmed hires" is the number worth
  charging for, and self-reported hires are exactly what employers will under-declare to avoid a
  success fee. Do not build a success-fee model on it. Subscription or per-post pricing only.
- **No pricing exists anywhere in the prototype.** Decide it before you build: I would test
  RM99–199/month for unlimited Verified posts for SMEs, free for the first cohort, and never a
  per-application charge.

## 5. Blockers before anything is publicly accessible

These are not polish items. Two of them are litigation risks.

### 5.1 Remove the fabricated employers, immediately

The page names specific companies — *Teck Seng Trading Sdn Bhd*, *MegaTron Digital Sdn Bhd*,
*QuickCorp Trading*, *BorneoPlate Food Supply Sdn Bhd* — and attaches invented conduct to them:
QuickCorp is publicly flagged for ghosting an applicant, and Bintulu Industrial Services carries
"posted 3 times in 12 months with no confirmed hire". Several of these read like plausible real
Malaysian SME names. If any real company shares a name, that is a defamation claim with your own
HTML as the evidence, and possibly a Communications and Multimedia Act 1998 s.233 complaint.
Replace all of them with obviously fictional placeholders ("Company A") and label the page a demo.

### 5.2 The "Listed" aggregated tier is the single largest legal exposure

Scraping public postings and republishing them under a named employer with a dashed border, "we
have not confirmed this role is still open", "has not committed to responding", and a repost
warning is a negative statement about an identifiable business that never consented to being on
your platform. Combined exposure: defamation, the source platforms' terms of service, and
copyright in the advertisement text.

Options, best first: **(a)** drop the tier and launch Verified-only with a hand-recruited cohort;
**(b)** keep aggregation but show only neutral facts, no reliability inference, no repost warning,
link out, and honour takedown within 24 hours; **(c)** keep it as-is and accept the risk. I would
do (a). It is also the better product story — a small, all-Verified marketplace is more coherent
than a large one where most listings carry a warning.

### 5.3 Licensing — get a Malaysian opinion before launch

The **Private Employment Agencies Act 1981 (Act 246)** requires a licence for recruiting activity;
Licence A (placement within Malaysia) requires RM50,000 paid-up capital and a RM5,000 guarantee,
and the applicant must be a company incorporated under the Companies Act 2016. Pure advertising
platforms have generally operated outside it, but PastiKerja does matching-adjacent things
(status pipelines, applicant handling, shortlisting signals) that sit closer to the line.
Note that **Sarawak licenses separately** through the Sarawak Labour Department (JTK Sarawak), not
JTKSM. Budget for one employment-law opinion; do not guess at this.

### 5.4 PDPA compliance is now mandatory and enforced

The Personal Data Protection (Amendment) Act 2024 took effect in stages through **1 June 2025**:
you must appoint a **Data Protection Officer**, notify the Commissioner of a breach within **72
hours** and affected individuals within **7 days** where there is risk of significant harm, and
support data portability. Non-notification carries up to **RM250,000 and/or 2 years**. You are
building a database of CVs, phone numbers and employment histories — this is squarely in scope
from your first real user.

### 5.5 Trim the unprovable claims

"Malaysia's first guaranteed-response job platform" and the trust-bar statistics are stated as
established facts on a product with zero users. The Trade Descriptions Act 2011 makes false trade
descriptions an offence. Soften to intent ("We are building...") until the numbers are real. Also
run a **MyIPO trademark search** and secure the domain before spending anything on the brand.

## 6. Recommended next 90 days

1. **Week 1** — Strip the fake companies, soften the claims, add a BM toggle and a waitlist form.
   Ship it as a landing page. Buy nothing else yet.
2. **Weeks 1–4** — Talk to 25 Kuching/Sibu SME hiring managers and 50 jobseekers. The one question
   that decides this: *"would you accept a public response-rate score in exchange for cheaper,
   better-matched applicants?"* If fewer than a third say yes, the mechanic needs rework before
   any code. In parallel: employment-law opinion, MyIPO search, JobSarawak and SarawakJobs
   teardown.
3. **Weeks 4–12** — Build only if the interviews clear the bar. Order: employer console → SLA clock
   and scoring → WhatsApp notifications → candidate tracking → BM/EN/中文. Verified-only, one city,
   20–30 hand-recruited employers, free for the cohort.
4. **Ongoing** — Track the EIS vacancy-reporting bill. If it passes, pivot the SME pitch to
   compliance-plus-hiring and move nationally.

The honest summary: the insight is good, the design instincts are better than most funded
Malaysian startups I have seen, the metric design has a hole in it, and the aggregation tier is a
lawsuit. Fix the metric, drop the tier, launch in Malay, and test the employer objection before
writing a line of backend code.
