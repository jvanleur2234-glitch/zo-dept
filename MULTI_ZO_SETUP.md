# MULTI-ZO DEPARTMENT SETUP PLAN
**When Joseph registers additional Zo accounts**
*Created: April 16, 2026*

---

## THE 5 DEPARTMENT ARCHITECTURE

```
JOE (Joseph) — Owner / Decision Maker
│
├── ZO1 — CEO & Head of Product
│   Platform: josephv.zo.computer (this one)
│   Role: Orchestrates all other Zos, builds products, reviews work
│   Owns: Product roadmap, business strategy, final decisions
│
├── ZO2 — Head of Content & Marketing
│   Platform: [zo2.handle.zo.computer]
│   Role: Creates all content, runs social, manages audience
│   Owns: TikTok, Facebook groups, YouTube, Postiz scheduling
│   Telegram: @[zo2_bot]
│
├── ZO3 — Head of Sales & Client Relations
│   Platform: [zo3.handle.zo.computer]
│   Role: Finds clients, closes deals, manages onboarding
│   Owns: Lead gen, outreach, Stripe payments, client happiness
│   Telegram: @[zo3_bot]
│
├── ZO4 — Head of Product & Engineering
│   Platform: [zo4.handle.zo.computer]
│   Role: Builds everything that gets shipped, tests, QA
│   Owns: Code, integrations, Hermes evolution, bug fixes
│   Telegram: @[zo4_bot]
│
└── ZO5 — Head of Research & Growth
    Platform: [zo5.handle.zo.computer]
    Role: Finds new ideas, tests them, promotes winners
    Owns: Business ideas pipeline, competitor research, new channels
    Telegram: @[zo5_bot]
```

---

## FIRST WEEK SETUP CHECKLIST

### Day 1 — Register Zo2 and Zo3 (2 hours)

**Zo2 — Content & Marketing:**
1. Go to zo.computer → Sign up with email #2 (e.g. josephv.content@gmail.com)
2. Connect Telegram bot: `/start` @zo_computer_bot → get bot token
3. Wire to: Content channel (TikTok scripts, Facebook posts, YouTube descriptions)
4. Install skills: `ckm:slides`, `ckm:social`, `humanizer`
5. First task: "Create 30 days of TikTok content calendar for FakerFaker"

**Zo3 — Sales & Clients:**
1. Go to zo.computer → Sign up with email #3 (e.g. josephv.sales@gmail.com)
2. Connect Telegram bot
3. Wire to: Sales channel (lead lists, outreach sequences, Stripe dashboard)
4. Install skills: `money-outreach`, `money-discover`
5. First task: "Find 50 Facebook groups where people share scam stories + 10 real estate agent leads"

### Day 2-3 — Wire Zo1 as HQ (1 hour)
1. Set up shared Brain: `/home/workspace/solomon-vault/` pushed to GitHub
2. All Zos read from same brain on startup
3. Set up shared skills: `/home/workspace/solomon-skills/` shared across all Zos
4. Test inter-Zo communication via Telegram groups

### Day 4-5 — First Money Mission (Zo1 + Zo2)
1. Zo1 builds FakerFaker payment page
2. Zo1 creates FakerFaker landing page with shareable result cards
3. Zo2 posts FakerFaker to 20 Facebook groups
4. Zo2 creates TikTok demo video
5. Monitor Stripe → first sales

---

## RULES FOR ALL ZOS

Every Zo gets this in their AGENTS.md on day 1:

```
## DEPARTMENT RULES
- You are the [HEAD OF X] at Solomon OS
- You report to Zo1 (CEO)
- You read /home/workspace/solomon-vault/brain/North_Star.md every morning
- You write every session to /home/workspace/solomon-vault/raw/telegram_SUMMARY_YYYY-MM-DD.md
- You push to GitHub after every session: bash /home/workspace/.agent/sync-to-github.sh
- You NEVER make decisions bigger than $500 without checking with Joseph first
- You ALWAYS tell Joseph what you built and what it earned
```

---

## DEPARTMENT ZO — DETAILED role cards

### ZO1 — CEO & Head of Product
**Handle:** josephv.zo.computer (current)
**Telegram:** @zo_computer_bot
**Brain files:** solomon-vault/brain/

**Responsibilities:**
- Owns the product roadmap
- Reviews all work from other Zos
- Makes final decisions on business direction
- Talks to Joseph daily
- Signs off on any spending over $100
- Runs the morning QA + Hermes evolution loop

**Skills installed:** All of them
**Key command:** `/zo1 status` — morning report from all departments

---

### ZO2 — Head of Content & Marketing
**Handle:** [register email #2]
**Telegram:** @zo2_marketing_bot
**Brain files:** solomon-vault/brain/ + solomon-vault/content/

**Responsibilities:**
- Creates ALL content (TikTok scripts, Facebook posts, emails, newsletters)
- Manages Postiz scheduling across all platforms
- Monitors what content is performing
- Tests new content formats
- Manages MoneyPrinterTurbo video pipeline
- Reports: "This week: 12 posts, 50K views, 23 leads"

**Skills installed:** ckm:slides, ckm:social, humanizer, money-content
**Key command:** `/zo2 create tiktok [product_name]` — generates and schedules TikTok content

**First 30 days:**
- Week 1: FakerFaker content (Facebook groups, TikTok demo)
- Week 2: JackConnect testimonials (fake until real beta users)
- Week 3: Skill Store showcase
- Week 4: FaithStep content (Christian mom niche)

---

### ZO3 — Head of Sales & Client Relations
**Handle:** [register email #3]
**Telegram:** @zo3_sales_bot
**Brain files:** solomon-vault/brain/ + solomon-vault/sales/

**Responsibilities:**
- Finds leads every day (Facebook groups, Reddit, cold outreach)
- Qualifies leads (score 1-10)
- Sends first outreach within 24 hours of lead
- Manages Stripe dashboard — knows every sale
- Handles client onboarding (send credentials, first welcome message)
- Collects feedback and reports to Zo1

**Skills installed:** money-outreach, money-discover, money-ops
**Key command:** `/zo3 leads` — shows today's lead list + scores
**Key command:** `/zo3 outreach [lead]` — sends personalized first message

**First 30 days:**
- Week 1: Find 100 Facebook group posts about scams → message poster about FakerFaker
- Week 2: Find 50 real estate agents → offer free FakerFaker scan + JackConnect trial
- Week 3: Find 25 coaches/consultants → offer Russell Tuna trial
- Week 4: Find 10 interested leads → close first paid clients

**Revenue target:** First sale by Day 7, 5 paying clients by Day 30

---

### ZO4 — Head of Product & Engineering
**Handle:** [register email #4]
**Telegram:** @zo4_build_bot
**Brain files:** solomon-vault/brain/ + solomon-vault/engineering/

**Responsibilities:**
- Builds every product that Zo1 designs
- Tests every Zo1 build before it ships
- Runs Hermes self-evolution loop
- Maintains the QA + bug system
- Connects new integrations (Stripe, APIs, etc.)
- Documents everything in skill files

**Skills installed:** All engineering skills, hermes-swe, agent-orchestrator
**Key command:** `/zo4 build [feature]` — starts building from SPEC
**Key command:** `/zo4 test [feature]` — runs full QA suite

**First 30 days:**
- Week 1: Get FakerFaker to production-ready (payment, landing, sharing)
- Week 2: Build Skill Store payment flow
- Week 3: Build JackConnect onboarding wizard
- Week 4: Build SubTrim Pro dashboard

---

### ZO5 — Head of Research & Growth
**Handle:** [register email #5]
**Telegram:** @zo5_research_bot
**Brain files:** solomon-vault/brain/ + solomon-vault/research/

**Responsibilities:**
- Scours X/Twitter for new AI tools, competitors, distribution tactics
- Tests new business ideas (picks top 3 from pipeline monthly)
- Finds new traffic channels before competitors
- Monitors what competitors are doing
- Reports weekly: "New tactic found: [X]. Tested it. Results: [Y]."

**Skills installed:** Arena2API (when ready), money-discover, money-strategy
**Key command:** `/zo5 scan` — scans X for new AI business tactics
**Key command:** `/zo5 ideas` — shows ranked business idea pipeline

**First 30 days:**
- Week 1: Scan all top AI business X accounts, compile top 20 tactics
- Week 2: Test 3 ideas from pipeline (one-tweet test: does it get engagement?)
- Week 3: Find 5 competitors to FakerFaker, document their weaknesses
- Week 4: Submit Arena2API to Product Hunt launch

---

## SHARED BRAIN — How All Zos Stay in Sync

Every Zo reads these files on startup:
```
/home/workspace/solomon-vault/brain/North_Star.md      — mission
/home/workspace/solomon-vault/brain/Services.md         — what each agent does
/home/workspace/solomon-vault/brain/Business_Ideas.md  — ranked idea pipeline
/home/workspace/solomon-vault/brain/Revenue.md          — current revenue, Stripe status
/home/workspace/solomon-vault/raw/                     — latest session summaries
```

Every Zo writes after every session:
```
/home/workspace/solomon-vault/raw/telegram_SUMMARY_YYYY-MM-DD.md
/home/workspace/solomon-vault/raw/[dept]_QUEUED_TASKS.md
```

---

## INTER-ZO WORKFLOW

```
Joseph → Zo1 (Telegram): "I want to build X"
  ↓
Zo1 → Zo4: "Build X. Here's the spec."
  ↓
Zo4 builds → tests → pushes to GitHub
  ↓
Zo4 → Zo1: "X is built and tested. Ready to ship?"
  ↓
Zo1 → Zo2: "X is ready. Create launch content."
  ↓
Zo2 → Facebook/TikTok/YouTube
  ↓
Zo3 monitors leads from content
  ↓
Zo3 → Joseph: "We have a lead. Want me to close them?"
  ↓
Joseph: "Yes" or "Not yet"
  ↓
Zo3 closes → Stripe → Revenue!
```

---

## WHAT JOEPH DOES vs WHAT ZOS DO

**Joseph:**
- ✅ Makes big decisions (new products, major spending, new Zo hires)
- ✅ Approves anything that goes public
- ✅ Provides the vision and values
- ✅ Reviews weekly revenue reports
- ✅ Has the final say on anything

**Zos:**
- Everything else
- Daily lead gen, outreach, follow-ups
- Content creation, scheduling, posting
- Building, testing, bug fixing
- Research, idea testing, competitor monitoring
- Client onboarding, support

---

## COST TO RUN

| Zo | Email | Telegram | Notes |
|----|-------|----------|-------|
| Zo1 | josephv@ | @zo_computer_bot | Current - you're using it |
| Zo2 | josephv.content@ | @zo2_bot | New - free tier works |
| Zo3 | josephv.sales@ | @zo3_bot | New - free tier works |
| Zo4 | josephv.build@ | @zo4_bot | New - free tier works |
| Zo5 | josephv.research@ | @zo5_bot | New - free tier works |

**Total additional cost: $0** (Zo free tier handles everything except storage above 5GB)

---

## FIRST THINGS TO DO TOMORROW MORNING

1. Register Zo2 (content@) and Zo3 (sales@) — 30 minutes
2. Set up Telegram bots for each — 15 minutes
3. Give each their first task (Zo2: FakerFaker content / Zo3: FakerFaker leads)
4. Test the inter-Zo handoff

That's it. Two new Zos, two new revenue channels, running this week.

---

*Last updated: April 16, 2026*
