# Travel Charts and Visualizations

## Timeline Chart (Mermaid Diagram)

```mermaid
gantt
    title Himalaya Travel Journey - January 10-25, 2026
    dateFormat YYYY-MM-DD
    section Karachi
    Arrival & Check-in           :done, karachi1, 2026-01-10, 1d
    Ammar's Wedding             :done, wedding1, 2026-01-11, 1d
    Arooj's Wedding             :done, wedding2, 2026-01-12, 1d
    
    section Punjab Tour
    Travel to DG Khan            :active, dgkhan, 2026-01-13, 1d
    Travel to Lahore             :active, lahore1, 2026-01-14, 1d
    Explore Lahore               :active, lahore2, 2026-01-15, 1d
    Travel to Faisalabad         :active, faisalabad, 2026-01-16, 1d
    Travel to Okara              :active, okara, 2026-01-17, 1d
    
    section Islamabad
    Travel to Islamabad          :crit, islamabad1, 2026-01-18, 1d
    Explore & Prepare            :crit, islamabad2, 2026-01-19, 1d
    
    section Mountains
    Travel to Hunza (KKH)        :milestone, hunza1, 2026-01-20, 1d
    Explore Hunza Valley         :milestone, hunza2, 2026-01-21, 1d
    Gilgit & Return              :milestone, gilgit, 2026-01-22, 1d
    
    section International
    Fly to Tashkent              :active, uzbek1, 2026-01-23, 1d
    Explore Tashkent             :active, uzbek2, 2026-01-24, 1d
    
    section Return
    Return via Karachi           :done, return, 2026-01-25, 1d
```

---

## Distance & Travel Time Chart

```mermaid
graph TD
    A[Karachi<br/>START] -->|480 km<br/>7-8 hrs| B[DG Khan]
    B -->|450 km<br/>6-7 hrs| C[Lahore]
    C -->|130 km<br/>2-3 hrs| D[Faisalabad]
    D -->|100 km<br/>1.5-2 hrs| E[Okara]
    E -->|300 km<br/>4-5 hrs| F[Islamabad]
    F -->|580 km<br/>12-14 hrs<br/>OR Fly 1hr| G[Hunza Valley]
    G -->|100 km<br/>2-3 hrs| H[Gilgit]
    H -->|Via Islamabad<br/>Flight 3 hrs| I[Tashkent<br/>Uzbekistan]
    I -->|Flight<br/>2.5 hrs| J[Karachi]
    J -->|Flight| K[Home<br/>END]
    
    style A fill:#d5e8d4,stroke:#82b366
    style B fill:#fff2cc,stroke:#d6b656
    style C fill:#fff2cc,stroke:#d6b656
    style D fill:#fff2cc,stroke:#d6b656
    style E fill:#fff2cc,stroke:#d6b656
    style F fill:#fff2cc,stroke:#d6b656
    style G fill:#dae8fc,stroke:#6c8ebf
    style H fill:#dae8fc,stroke:#6c8ebf
    style I fill:#f8cecc,stroke:#b85450
    style J fill:#d5e8d4,stroke:#82b366
    style K fill:#d5e8d4,stroke:#82b366
```

---

## Daily Activity Breakdown

```mermaid
pie title Trip Activities Distribution (16 Days)
    "Weddings & Events" : 2
    "Road Travel" : 4
    "City Sightseeing" : 5
    "Mountain Exploration" : 3
    "International Travel" : 2
```

---

## Budget Distribution Chart

```mermaid
pie title Budget Distribution (Total ~$7,000 USD)
    "Flights (Int'l & Domestic)" : 2500
    "Accommodation (16 nights)" : 1000
    "Transportation & Car Rental" : 650
    "Food & Dining" : 500
    "Wedding Gifts" : 350
    "Activities & Tours" : 400
    "Shopping & Souvenirs" : 300
    "Miscellaneous & Tips" : 250
    "Visa & Insurance" : 300
    "Emergency Fund" : 750
```

---

## Accommodation Breakdown

```mermaid
gantt
    title Accommodation Schedule
    dateFormat YYYY-MM-DD
    section Hotels
    Karachi Hotel (3 nights)     :hotel1, 2026-01-10, 3d
    DG Khan Hotel (1 night)      :hotel2, 2026-01-13, 1d
    Lahore Hotel (2 nights)      :hotel3, 2026-01-14, 2d
    Faisalabad Hotel (1 night)   :hotel4, 2026-01-16, 1d
    Okara Hotel (1 night)        :hotel5, 2026-01-17, 1d
    Islamabad Hotel (3 nights)   :hotel6, 2026-01-18, 3d
    Hunza Resort (2 nights)      :hotel7, 2026-01-20, 2d
    Gilgit Hotel (1 night)       :hotel8, 2026-01-22, 1d
    Tashkent Hotel (2 nights)    :hotel9, 2026-01-23, 2d
```

---

## Journey Flow Diagram

```mermaid
flowchart TD
    Start([Arrive Karachi<br/>Jan 10]) --> Wedding1{Ammar's Wedding<br/>Jan 11}
    Wedding1 --> Wedding2{Arooj's Wedding<br/>Jan 12}
    Wedding2 --> PunjabStart[Begin Punjab Tour<br/>Jan 13]
    PunjabStart --> DGK[DG Khan<br/>1 night]
    DGK --> LHR[Lahore<br/>2 nights<br/>Sightseeing]
    LHR --> FSD[Faisalabad<br/>Birthplace Visit]
    FSD --> OKR[Okara<br/>1 night]
    OKR --> ISB[Islamabad<br/>3 nights]
    ISB --> SpecialDinner{Special Dinner<br/>Monal Restaurant}
    SpecialDinner --> MountainPrep[Prepare for<br/>Mountains]
    MountainPrep --> KKH[Karakoram Highway<br/>Journey]
    KKH --> Hunza[Hunza Valley<br/>2 nights<br/>Forts & Lakes]
    Hunza --> Gilgit[Gilgit<br/>1 night]
    Gilgit --> ReturnISB[Return to<br/>Islamabad]
    ReturnISB --> FlyUzbekistan[Fly to Tashkent<br/>Jan 23]
    FlyUzbekistan --> Tashkent[Explore Tashkent<br/>2 days]
    Tashkent --> FlyBack[Fly to Karachi<br/>Jan 24/25]
    FlyBack --> End([Departure<br/>Jan 25])
    
    style Start fill:#d5e8d4
    style Wedding1 fill:#d5e8d4
    style Wedding2 fill:#d5e8d4
    style LHR fill:#fff2cc
    style FSD fill:#fff2cc
    style ISB fill:#fff2cc
    style SpecialDinner fill:#fff2cc
    style Hunza fill:#dae8fc
    style KKH fill:#dae8fc
    style Tashkent fill:#f8cecc
    style End fill:#d5e8d4
```

---

## Temperature Chart by Location

| Location | Average Jan Temp | Notes |
|----------|-----------------|-------|
| **Karachi** | 15-25°C (60-77°F) | Mild winter, pleasant |
| **Lahore** | 5-20°C (41-68°F) | Cool, possible fog |
| **Islamabad** | 2-15°C (36-59°F) | Cold, clear skies |
| **Hunza** | -10 to 5°C (14-41°F) | Very cold, possible snow |
| **Tashkent** | -5 to 5°C (23-41°F) | Cold, winter weather |

**Visual:**
```
Karachi      ████████████████░░░░  Mild
Lahore       ████████████░░░░░░░░  Cool
Islamabad    ██████████░░░░░░░░░░  Cold
Hunza        ████░░░░░░░░░░░░░░░░  Very Cold
Tashkent     ██████░░░░░░░░░░░░░░  Cold
             ←─────────────────→
             Warmest    Coldest
```

---

## Packing Weight Distribution

```mermaid
pie title Luggage Composition Recommendation
    "Warm Clothing (Mountains)" : 35
    "Formal Wear (Weddings)" : 20
    "Casual Daily Wear" : 20
    "Toiletries & Medicine" : 10
    "Electronics & Camera" : 10
    "Documents & Misc" : 5
```

---

## Key Highlights by Region

```mermaid
mindmap
  root((Himalaya<br/>Journey))
    Karachi
      2 Weddings
      Arrival/Departure
      City Experience
    Punjab
      DG Khan
      Lahore Heritage
      Faisalabad Birthplace
      Cultural Tour
    Islamabad
      Capital City
      Special Dinner
      Modern Pakistan
      Mountain Gateway
    Mountains
      Karakoram Highway
      Hunza Valley
      Baltit & Altit Forts
      Rakaposhi Views
      Attabad Lake
    Uzbekistan
      Tashkent City
      Silk Road Culture
      Chorsu Bazaar
      Metro Architecture
```

---

## Trip Statistics

### By the Numbers

| Metric | Value |
|--------|-------|
| **Total Duration** | 16 days |
| **Countries Visited** | 2 (Pakistan, Uzbekistan) |
| **Cities/Locations** | 9 major stops |
| **Weddings Attended** | 2 |
| **Road Distance** | ~2,500+ km |
| **Flights** | 4-5 (international + domestic) |
| **Hotel Nights** | 16 |
| **Mountain Days** | 3 |
| **UNESCO Sites** | 2+ (Lahore Fort, potential others) |

---

## Risk Level by Activity

```mermaid
graph LR
    A[Activities] --> B[Low Risk]
    A --> C[Medium Risk]
    A --> D[High Risk]
    
    B --> B1[City Sightseeing]
    B --> B2[Restaurant Dining]
    B --> B3[Hotel Stays]
    
    C --> C1[Long Road Trips]
    C --> C2[Street Food]
    C --> C3[Wedding Events]
    
    D --> D1[Winter KKH Drive]
    D --> D2[High Altitude]
    D --> D3[January Weather]
    
    style B fill:#d5e8d4
    style C fill:#fff2cc
    style D fill:#f8cecc
```

---

## Recommended Photo Opportunities

### Top 10 Photo Spots

1. **Badshahi Mosque, Lahore** - Sunset/illuminated
2. **Hunza Valley Panorama** - Eagles Nest sunrise
3. **Attabad Lake** - Turquoise water + mountains
4. **Karakoram Highway** - Multiple viewpoints
5. **Monal Restaurant** - Islamabad city lights view
6. **Baltit Fort** - Historic architecture + mountain backdrop
7. **Faisal Mosque, Islamabad** - Modern Islamic architecture
8. **Rakaposhi Mountain** - 7,788m peak from Hunza
9. **Chorsu Bazaar, Tashkent** - Market architecture
10. **Wedding Ceremonies** - Traditional Pakistani celebrations

---

## Best Times for Activities

```mermaid
timeline
    title Daily Activity Timing Recommendations
    section Morning (6-10 AM)
        Eagles Nest Sunrise : Hunza photography
        Faisal Mosque Visit : Less crowded
        Breakfast Experiences : Traditional foods
    section Midday (10 AM-2 PM)
        Fort Visits : Lahore, Hunza
        Shopping : Bazaars less hot
        Driving : KKH in daylight
    section Afternoon (2-6 PM)
        Museum Visits : Indoor activities
        Rest Time : Hotel break
        Tea Houses : Local experience
    section Evening (6-10 PM)
        Food Streets : Lahore dining
        Monal Dinner : Sunset views
        City Lights : Photography
    section Night (10 PM+)
        Wedding Functions : Traditional timings
        Return to Hotel : Post-celebration
```

---

## Transportation Methods Used

```mermaid
pie title Transportation Mode Distribution
    "Private Car/Rental" : 60
    "International Flights" : 20
    "Domestic Flight (optional)" : 5
    "Local Taxis/Uber" : 10
    "Walking" : 5
```

---

*These charts and visualizations provide a comprehensive overview of the journey.*
*Refer to detailed documents for specific information.*
