<!-- HI | TDP: 2026-03-10T11:00:00Z | Turin, Italy | Himalaya -->
---
name: Himalaya
description: Himalaya expedition and travel planning project — personal adventure journal for HI's January 2026 trip from Turin covering Pakistan (Karachi, DG Khan, Lahore, Faisalabad, Okara, Islamabad), Himalaya mountains, and Uzbekistan. Contains the FKUnited license.
---

# Himalaya Agent — Expedition & Travel Planning

## Identity

- **Owner:** Hamza Ilyas (GitHub: hamsta25)
- **Account:** hamsta25
- **Remote:** https://github.com/hamsta25/Himalaya.git
- **Branch:** main
- **Location:** `C:\Users\Maria\source\repos\Himalaya\`
- **Phase:** Early / Planning — README-driven, minimal structure

---

## Purpose

**Himalaya** is HI's personal travel and expedition planning repository. It documents a multi-destination trip starting from Turin, Italy, with a return base in Karachi, Pakistan — covering family events, cultural stops, and the Himalaya mountain region, with an extension to Uzbekistan.

### The January 2026 Trip (from README.md)

**Route:**
- Depart from Turin, Italy → Land in **Karachi** (January 10, 2026)
- **Karachi** (Jan 10–12): Attend two weddings — Ammar's and Arooj's
- **DG Khan (DJ Khan)**: Family visit
- **Lahore**: Cultural stop
- **Faisalabad**: Birthplace visit
- **Okara**: Visit
- **Islamabad**: Lunch/dinner stop
- **Himalaya**: The main expedition destination
- **Uzbekistan**: Extension leg
- **Return flight**: January 25, 2026 (Sunday) from Karachi

---

## FKUnited License

The repository contains a `FKUnited_license/` directory — establishing the connection between this personal project and the FKUnited Inc. ecosystem. This means:

- The project operates under FKUnited's licensing terms
- Any documentation, tools, or resources developed here can be used within the FKU ecosystem
- Maintains ownership clarity for any content produced

---

## Current Structure

```
Himalaya/
├── README.md            # Trip overview (the source of truth)
└── FKUnited_license/    # FKUnited Inc. license materials
```

---

## How to Expand This Project

The repo is intentionally minimal right now. Here's the natural growth path:

### Recommended Docs to Add

```
Himalaya/
├── README.md                    # Keep updated as trip evolves
├── FKUnited_license/
│
├── itinerary/
│   ├── master_itinerary.md      # Full day-by-day schedule
│   ├── karachi.md               # Jan 10–12 details, contacts
│   ├── dg_khan.md
│   ├── lahore.md
│   ├── faisalabad.md
│   ├── okara_islamabad.md
│   ├── himalaya_expedition.md   # The main event
│   └── uzbekistan.md
│
├── logistics/
│   ├── flights.md               # Flight numbers, booking refs
│   ├── accommodation.md         # Hotels, family stays
│   ├── visa_docs.md             # Visa requirements (EU→PK, PK→UZ)
│   ├── budget.md                # Trip budget tracker
│   └── emergency_contacts.md
│
├── gear/
│   ├── packing_list.md          # What to bring
│   └── himalaya_gear.md         # Mountain-specific equipment
│
├── research/
│   ├── himalaya_routes.md       # Route options, permits
│   ├── uzbekistan_highlights.md # Must-see places
│   └── health_safety.md         # Altitude sickness, vaccinations
│
└── journal/
    └── entries/                 # Trip journal entries
```

### Conventions for Adding Content

- **One file per location** in `itinerary/` — keep focused
- **Dates in ISO format:** `2026-01-10`
- **Sensitive data** (passport numbers, booking references) → use a password manager, NOT this repo
- **Photos** → use Git LFS or external photo service (don't commit large image files)
- Commit messages: `feat(itinerary): add Himalaya expedition route plan`

---

## Relationship to HI Ecosystem

| Connection | Detail |
|-----------|--------|
| **FKUnited Inc.** | FKUnited license applied; any tools or frameworks built for trip planning become FKU assets |
| **DUMP** | Trip evaluated as personal project; time allocation budgeted against PoliTo semester |
| **LifeOS** | Travel planning connects to life OS and personal goal tracking |
| **PK-DJ-UNI** | DG Khan (DJ Khan) is HI's family hometown — the `PK-DJ-UNI` repo may share context |

---

## Quick Commands

```bash
# View the trip overview
cat README.md

# Open for editing (VS Code)
code README.md

# Add a new location file
cp itinerary/_template.md itinerary/<location>.md

# Check what's tracked
git log --oneline

# See full repo structure
find . -not -path "./.git/*" | sort
```

---

## Health Check

- [ ] README.md reflects current trip plan
- [ ] FKUnited_license/ directory intact
- [ ] No sensitive data (passport numbers, booking refs, passwords) committed
- [ ] Photos not committed directly (use LFS if needed)
- [ ] Trip dates still accurate

---

## Current State Assessment

**Status: Early planning phase.** The README contains the core trip outline but the repo has room to grow into a full expedition planning system. Priority is keeping the README accurate and adding structured itinerary docs as the trip approaches.

---

*Owner: Hamza Ilyas | GitHub: hamsta25 | MSc Embedded Systems @ PoliTo | CEO, FKUnited Inc.*
