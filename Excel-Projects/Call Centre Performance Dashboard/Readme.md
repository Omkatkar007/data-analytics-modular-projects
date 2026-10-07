# Call Centre Performance Dashboard (Excel)

An interactive Excel dashboard analyzing **1,000 customer calls** handled by **5 representatives** across **3 cities** in 2023, built to answer one question: **what actually drives customer satisfaction and revenue in a call centre?**


## Business Problem

Call centres often treat short calls as the goal. This project tests that assumption and looks for where operations should focus instead: rep coaching, staffing, and customer experience.

**Questions answered**

1. Does call length affect customer satisfaction or revenue?
2. Which representative creates the most value: the one with the most calls or the most revenue?
3. How do satisfaction and revenue differ by city?
4. When is demand highest (weekday and month)?

---

## Dataset

| Field | Description |
|---|---|
| Call number | Unique call ID |
| Customer ID | Links to the customer table |
| Duration | Call duration, as recorded in the source data (unit: [add unit]) |
| Representative | R01 to R05 |
| Date of Call | 1 Jan 2023 to 31 Dec 2023 |
| Purchase Amount | Revenue from the call |
| Satisfaction Rating | Customer rating, 0 to 5 |
| Gender, Age, City | Customer attributes (Cincinnati, Cleveland, Columbus) |

**Calculated columns:** day of week, duration bucket, rounded rating, fiscal year.

**Data check:** 1,000 records, no duplicate call numbers, no blanks in duration, amount or rating.

---

## Key Findings

| # | Finding | Evidence |
|---|---|---|
| 1 | **Call length does not drive satisfaction** | Average rating stays between 3.87 and 3.92 in every duration band. The 5-star rate is 29.6% to 31.4% in every band. Correlation between duration and rating: 0.01 |
| 2 | **Customers are mostly satisfied** | 73.5% of calls were rated 4 or higher. 307 calls received a 5 |
| 3 | **Volume is not value** | R02 took the most calls (218), but R03 earned the most revenue ($20,872) from 207 calls: $100.83 per call vs $94.41 |
| 4 | **R04 is the main coaching opportunity** | Longest average call (95.7) and lowest revenue per call ($89.52), 12.6% below R03 |
| 5 | **Satisfaction differs by city** | Cincinnati 4.03, Cleveland 3.88, Columbus 3.77 |
| 6 | **Demand is uneven** | Saturday is the busiest day (161 calls). Monthly peaks in March (155) and October (114) |

### Representative summary

| Rep | Calls | Revenue | Revenue per call | Avg call length | Avg rating |
|---|---|---|---|---|---|
| R01 | 189 | $18,415 | $97.43 | 89.1 | 3.92 |
| R02 | 218 | $20,581 | $94.41 | 88.5 | 3.87 |
| R03 | 207 | $20,872 | $100.83 | 85.5 | 3.86 |
| R04 | 186 | $16,651 | $89.52 | 95.7 | 3.90 |
| R05 | 200 | $20,104 | $100.52 | 91.0 | 3.88 |
| **Total** | **1,000** | **$96,623** | **$96.62** | **89.8** | **3.89** |

### Rating by call length

| Duration band | Calls | Avg rating | % rated 5 |
|---|---|---|---|
| Under 30 | 54 | 3.92 | 29.6% |
| 30 to 59 | 175 | 3.87 | 31.4% |
| 60 to 119 | 527 | 3.88 | 30.4% |
| 120+ | 244 | 3.89 | 31.1% |

*Ratings are rounded to the nearest whole number (half rounds up) when counting 5-star calls and the 4+ share. Averages use the raw ratings.*

---

## Recommendations

- Stop using call length as a quality target. Track **satisfaction and revenue per call** instead.
- Pair **R04** with **R03** for coaching on conversion.
- Investigate what is driving lower satisfaction in **Columbus**.
- Plan **weekend staffing** and prepare for **March and October** peaks.

---

## Dashboard Features

- KPI cards: total calls, revenue, duration, average rating, 5-star calls
- Representative slicer that filters every chart and the table
- Highlighting of the selected rep in the Amount and Calls charts
- Dynamic rank and percentage-of-calls callout for the selected rep
- Call trend by month, calls by weekday, gender split by city, rating distribution
- PivotTable of revenue by city, customer and rep

---

## Tools and Skills

Microsoft Excel: PivotTables, PivotCharts, slicers, conditional formatting, calculated columns, KPI design, dashboard layout.
Analysis skills: data validation, KPI definition, segmentation, root-cause thinking, business recommendations.

---

## Repository Structure

```
Call Centre Performance Dashboard/
├── Dataset/        # Source data
├── Dashboard/      # Excel dashboard (.xlsx)
├── Projects-Visuals/         # Dashboard screenshot
└── README.md
```

---

## About

Built by **Om Katkar** as part of a data analytics portfolio.
Open to Data Analyst, Business Analyst and MIS Reporting roles.

[LinkedIn](www.linkedin.com/in/omkatkar) | [GitHub](https://github.com/Omkatkar007)
