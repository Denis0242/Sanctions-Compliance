# Sanctions Screening & Compliance Analytics

**Sanctions / Financial Crime Analytics Portfolio Project**

An end-to-end sanctions-screening analytics project using **Python, SQL,
Tableau, and Streamlit** to analyze potential watchlist matches,
name-match risk, sanctions programs, payment exposure, alert
dispositions, and counterparty-level compliance decisions.

> **Portfolio scope:** All data is synthetic. Screening scores, match
> thresholds, dispositions, sanctions programs, and compliance decisions
> are illustrative analytical outputs and do not represent any financial
> institution's production screening rules.

------------------------------------------------------------------------

## Project Overview

Sanctions screening requires analysts to distinguish potentially
actionable matches from false positives while preserving a clear audit
trail of the underlying customer, counterparty, watchlist, and payment
activity.

This project models that workflow across:

-   **2,000 synthetic customers**
-   **8,000 counterparties**
-   **180 synthetic watchlist records**
-   **32,000 transactions/payments**
-   **701 potential sanctions-screening alerts**
-   An analytics-ready screened-transaction layer

The project connects entity screening with transaction exposure and
analyst disposition to support explainable sanctions-review
prioritization.

------------------------------------------------------------------------

## Business & Compliance Questions

-   Which counterparties generate potential sanctions matches?
-   Which alerts are True Matches, Escalated, or False Positives?
-   Which sanctions programs generate the greatest screening activity?
-   Which alerts have the highest name-match and screening-risk scores?
-   Which countries account for the greatest flagged payment exposure?
-   Which payments are associated with sanctions alerts?
-   Where should sanctions reviewers focus first?
-   How can screening outcomes be summarized for compliance management
    without replacing analyst judgment?

------------------------------------------------------------------------

## Data Model

  -------------------------------------------------------------------------------------
  Dataset                                                    Rows Purpose
  ---------------------------------- ---------------------------- ---------------------
  Customer reference                                        2,000 Customer identity and
                                                                  KYC-risk context

  Counterparties                                            8,000 Counterparty identity
                                                                  and geographic
                                                                  context

  Sanctions watchlist                                         180 Synthetic watchlist
                                                                  subjects and
                                                                  sanctions programs

  Raw transactions                                         32,000 Payment activity
                                                                  submitted to
                                                                  screening

  `sanctions_screening_alerts.csv`                            701 Potential matches and
                                                                  analyst dispositions

  `transactions_screened.csv`                              32,000 Analytics-ready
                                                                  payment layer with
                                                                  screening results
  -------------------------------------------------------------------------------------

See [`docs/data_dictionary.md`](docs/data_dictionary.md) for detailed
fields and relationships.

------------------------------------------------------------------------

## Exploratory Data Analysis & Data Quality

The notebook includes:

-   Dataset/schema review
-   Missing-value analysis
-   Duplicate validation
-   Datatype and range checks
-   Summary statistics
-   IQR-based outlier review
-   Screening-score validation
-   Flagged-amount review
-   Business-rule/KPI validation
-   Final dataset validation

Unusual values are treated as potential compliance signals rather than
automatically removed.

------------------------------------------------------------------------

## Feature Engineering

The project uses explainable screening features including:

-   `name_match_score`
-   `country_match`
-   `screening_risk_score`
-   `risk_level`
-   `sanctions_alert_flag`
-   `flagged_amount`

The notebook additionally demonstrates:

-   `match_score_band`
-   `high_match_flag`
-   `flagged_amount_band`
-   `escalation_flag`

The match-score bands and thresholds are portfolio/demo logic and should
be calibrated to the screening platform and institution policy in a
production environment.

------------------------------------------------------------------------

## Sanctions Screening Analysis

The analytical workflow covers:

**Entity screening** --- comparing screened counterparties against
synthetic watchlist subjects.

**Match assessment** --- evaluating name similarity, geography and
screening-risk indicators.

**Alert disposition** --- distinguishing True Match, Escalated and False
Positive outcomes.

**Payment review** --- connecting screening alerts to payment activity
and flagged exposure.

**Program analysis** --- identifying sanctions programs driving
screening workload.

**Counterparty decision support** --- presenting an explainable
screening record and recommended review path.

------------------------------------------------------------------------

## SQL Analysis

The SQL file contains **12 analytical queries/statements** covering
sanctions-alert review, match scoring, dispositions, programs,
geography, payment exposure and screening prioritization.

See [`sql/`](sql/) for the full SQL analysis.

------------------------------------------------------------------------

## Verified Current KPIs

  KPI                              Current Result
  ------------------------------ ----------------
  Screened Transactions                **32,000**
  Potential Matches                       **701**
  High/Critical Matches                   **475**
  True Matches                            **201**
  Escalated                               **309**
  False Positives                         **191**
  True-Match Rate                       **28.7%**
  Escalation Rate                       **44.1%**
  False-Positive Rate                   **27.2%**
  Flagged Payment Exposure            **\$29.2M**
  Average Name-Match Score               **90.7**
  Average Screening-Risk Score           **91.0**

------------------------------------------------------------------------

## Key Findings

-   **201 potential matches** were dispositioned as True Match.
-   **309 alerts** require additional sanctions review.
-   **191 alerts** were resolved as False Positives.
-   **475 alerts** are classified High/Critical risk.
-   Total flagged payment exposure is approximately **\$29.2M**.
-   The leading sanctions program is **Sectoral Sanctions (173
    alerts)**.
-   The largest flagged-amount geography is **Russia**, at approximately
    **\$4.1M**.

These findings support sanctions-review prioritization; they do not
automate blocking, rejection, reporting, or customer disposition.

------------------------------------------------------------------------

## Streamlit Compliance Application

The Streamlit application loads the processed sanctions-alert and
screened-transaction layers and provides filters for **Sanctions
Program, Disposition, and Minimum Match Score**.

### Portfolio Decision Support

The filtered population is summarized as:

-   **Confirmed Sanctions Risk**
-   **Escalated Review Required**
-   **No Confirmed Match**

### Counterparty Sanctions Decision Summary

For a selected counterparty, the application shows:

-   Name-match score
-   Screening-risk score
-   Sanctions program
-   Disposition
-   Flagged amount
-   Screening history

The application then provides an explainable review outcome for True
Match, Escalated, False Positive, or other review status.

### Interactive Tabs

-   Screening Queue
-   Counterparty 360
-   Payment Review
-   Portfolio Analytics
-   Tableau Gallery

The **Tableau Gallery already follows the preferred portfolio design and
displays only the Executive Dashboard**.

------------------------------------------------------------------------

## Tableau Executive Dashboard

The refreshed executive dashboard is synchronized to the current processed datasets and presents six complementary views:

1. Screening Trend & Match Rate
2. Alert Disposition
3. Top 5 Countries by Flagged Exposure
4. Screening Activity Heatmap
5. Name-Match Score vs. Screening Risk
6. Alerts by Sanctions Program

### Dashboard Preview

![Sanctions Screening & Compliance Analytics Dashboard](images/02_executive_dashboard.png)

The dashboard uses the same verified project data while replacing the older visual design with a more varied recruiter-facing presentation.

---

## Analytical Workflow

``` text
Customer / Counterparty Profiles
            ↓
Raw Payments
            ↓
Synthetic Watchlist Screening
            ↓
Match Scoring & Alert Generation
            ↓
EDA + Feature Engineering
            ↓
Analyst Disposition
            ↓
Payment / Exposure Review
            ↓
Tableau + Streamlit Decision Support
```

------------------------------------------------------------------------

## Tools & Technologies

  -----------------------------------------------------------------------
  Tool                                Use
  ----------------------------------- -----------------------------------
  **Python / Pandas**                 EDA, feature engineering and
                                      sanctions analysis

  **SQL**                             Screening, disposition, program and
                                      payment analysis

  **Tableau**                         Executive sanctions dashboard

  **Streamlit**                       Counterparty review and decision
                                      support

  **Jupyter Notebook**                Reproducible analysis

  **Git / GitHub**                    Version control and portfolio
                                      presentation
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Repository Structure

``` text
Sanctions-Compliance/
├── app/             # Streamlit compliance application
├── data/            # Synthetic source and processed datasets
├── docs/            # Data dictionary and documentation
├── images/          # Executive dashboard
├── notebooks/       # EDA and feature engineering
├── sql/             # Sanctions analytics queries
├── src/             # Supporting project logic
├── tableau/         # Tableau workbook
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

------------------------------------------------------------------------

## How to Run

``` bash
git clone https://github.com/Denis0242/Sanctions-Compliance.git
cd Sanctions-Compliance
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

------------------------------------------------------------------------

## Skills Demonstrated

### Sanctions / Financial Crime

-   Sanctions Screening
-   Watchlist Screening
-   Name-Match Analysis
-   False-Positive Adjudication
-   Escalation Analysis
-   True-Match Review
-   Counterparty Screening
-   Payment Review
-   Sanctions Program Analysis
-   Geographic Risk Analysis
-   Compliance Decision Support

### Data & Analytics

-   Exploratory Data Analysis
-   Feature Engineering
-   Data Quality Validation
-   SQL
-   Python / Pandas
-   Risk Segmentation
-   KPI Development
-   Exposure Analysis
-   Business-Rule Validation

### Visualization & Decision Support

-   Tableau
-   Streamlit
-   Screening Queues
-   Counterparty 360
-   Executive Dashboards
-   Interactive Filtering
-   Data Storytelling

------------------------------------------------------------------------

## Disclaimer

This project uses **synthetic data** created for educational and
portfolio purposes. No real customer, counterparty, payment, watchlist
record, sanctions alert, financial institution, or confidential
screening data is included.

Sanctions programs, match scores, risk scores, alert dispositions,
engineered features and decision-support labels are illustrative. They
should not be interpreted as actual screening thresholds, legal
determinations, blocking/rejection instructions, reporting requirements,
or financial-institution policy.
