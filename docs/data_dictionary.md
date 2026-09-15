# Data Dictionary

## Sanctions Compliance & Screening Analytics

This data dictionary documents the customer, counterparty, sanctions-watchlist, transaction, screening-alert, and screened-transaction datasets used in this portfolio project. It distinguishes operational source fields from derived and engineered screening features so the project's EDA, feature engineering, and sanctions analytics workflow is clear to GitHub reviewers.

> **Portfolio note:** These datasets are structured for analytical demonstration. Definitions describe their use within this project and do not represent any specific financial institution's production screening system or data standard.

## Dataset Overview

| Dataset | Rows | Columns | Purpose |
|---|---:|---:|---|
| `counterparties.csv` | 8,000 | 3 | Counterparty reference dataset used to provide entity and geographic context for sanctions screening. |
| `customers(20260914-025617).csv` | 2,000 | 5 | Customer reference dataset used to provide customer identity and risk context. |
| `sanctions_watchlist.csv` | 180 | 6 | Sanctions/watchlist reference dataset containing subjects and attributes used in screening. |
| `transactions(20260914-025617).csv` | 32,000 | 8 | Raw transaction-level dataset used as the operational input to sanctions screening. |
| `sanctions_screening_alerts.csv` | 701 | 18 | Alert-level dataset containing potential sanctions matches and analyst screening outcomes. |
| `transactions_screened.csv` | 32,000 | 12 | Analytics-ready transaction dataset containing original transaction attributes plus sanctions-screening results and engineered screening fields. |

## `counterparties.csv`

Counterparty reference dataset used to provide entity and geographic context for sanctions screening.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `counterparty_id` | String | Source / Operational | Unique identifier assigned to the transaction counterparty. | `CP20000` |
| `counterparty_name` | String | Source / Operational | Name of the counterparty associated with the transaction. | `Jin Wang` |
| `country` | String | Source / Operational | Country associated with the customer, counterparty, or watchlist subject. | `Belarus` |

## `customers(20260914-025617).csv`

Customer reference dataset used to provide customer identity and risk context.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST10000` |
| `customer_name` | String | Source / Operational | Customer or legal-entity name used in screening and investigation. | `Wei Johnson` |
| `country` | String | Source / Operational | Country associated with the customer, counterparty, or watchlist subject. | `Iran` |
| `customer_type` | String | Source / Operational | Field representing customer type within the sanctions-compliance screening workflow. | `Business` |
| `kyc_risk` | String | Source / Operational | Attribute used to assess kyc risk. | `Low` |

## `sanctions_watchlist.csv`

Sanctions/watchlist reference dataset containing subjects and attributes used in screening.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `watchlist_id` | String | Source / Operational | Unique identifier assigned to the sanctions watchlist record. | `WL0001` |
| `primary_name` | String | Source / Operational | Field representing primary name within the sanctions-compliance screening workflow. | `Farid Zhang` |
| `alias_name` | String | Source / Operational | Field representing alias name within the sanctions-compliance screening workflow. | `Farid Zhang` |
| `country` | String | Source / Operational | Country associated with the customer, counterparty, or watchlist subject. | `North Korea` |
| `sanctions_program` | String | Source / Operational | Sanctions program or regime associated with the watchlist record. | `OFAC SDN` |
| `date_of_birth` | String | Source / Operational | Date associated with date of birth. | `1961-07-08` |

## `transactions(20260914-025617).csv`

Raw transaction-level dataset used as the operational input to sanctions screening.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `transaction_id` | String | Source / Operational | Unique identifier assigned to the transaction. | `PAY300000` |
| `transaction_date` | String | Source / Operational | Date on which the transaction occurred. | `2026-03-14` |
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST11575` |
| `counterparty_id` | String | Source / Operational | Unique identifier assigned to the transaction counterparty. | `CP27697` |
| `amount` | Float | Source / Operational | Monetary value associated with the transaction. | `839.66` |
| `channel` | String | Source / Operational | Field representing channel within the sanctions-compliance screening workflow. | `ACH` |
| `counterparty_name` | String | Source / Operational | Name of the counterparty associated with the transaction. | `Hassan Smith` |
| `country` | String | Source / Operational | Country associated with the customer, counterparty, or watchlist subject. | `Turkey` |

## `sanctions_screening_alerts.csv`

Alert-level dataset containing potential sanctions matches and analyst screening outcomes.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `screening_alert_id` | String | Source / Operational | Unique identifier for the screening alert. | `SAN00001` |
| `counterparty_id` | String | Source / Operational | Unique identifier assigned to the transaction counterparty. | `CP21571` |
| `screened_name` | String | Source / Operational | Field representing screened name within the sanctions-compliance screening workflow. | `Farid Zhang` |
| `screened_country` | String | Source / Operational | Field representing screened country within the sanctions-compliance screening workflow. | `North Korea` |
| `watchlist_id` | String | Source / Operational | Unique identifier assigned to the sanctions watchlist record. | `WL0001` |
| `matched_name` | String | Derived / Screening | Field used to evaluate or describe matched name during sanctions screening. | `Farid Zhang` |
| `watchlist_country` | String | Source / Operational | Field representing watchlist country within the sanctions-compliance screening workflow. | `North Korea` |
| `sanctions_program` | String | Source / Operational | Sanctions program or regime associated with the watchlist record. | `OFAC SDN` |
| `name_match_score` | Integer | Derived / Screening | Numeric analytical score representing name match. | `100` |
| `country_match` | Integer | Derived / Screening | Field used to evaluate or describe country match during sanctions screening. | `1` |
| `screening_risk_score` | Integer | Derived / Screening | Numeric analytical score representing screening risk. | `100` |
| `disposition` | String | Source / Operational | Final analyst disposition of the sanctions-screening alert. | `True Match` |
| `screening_volume` | Float | Source / Operational | Field representing screening volume within the sanctions-compliance screening workflow. | `5` |
| `flagged_amount` | Float | Derived / Screening | Indicator identifying whether flagged amount applies. | `25691.07` |
| `first_activity` | String | Source / Operational | Field representing first activity within the sanctions-compliance screening workflow. | `2026-01-01` |
| `last_activity` | String | Source / Operational | Field representing last activity within the sanctions-compliance screening workflow. | `2026-09-03` |
| `alert_date` | String | Source / Operational | Date associated with alert. | `2026-09-03` |
| `risk_level` | String | Derived / Screening | Attribute used to assess risk level. | `Critical` |

## `transactions_screened.csv`

Analytics-ready transaction dataset containing original transaction attributes plus sanctions-screening results and engineered screening fields.

| Column | Data Type | Classification | Description | Example |
|---|---|---|---|---|
| `transaction_id` | String | Source / Operational | Unique identifier assigned to the transaction. | `PAY300000` |
| `transaction_date` | String | Source / Operational | Date on which the transaction occurred. | `2026-03-14` |
| `customer_id` | String | Source / Operational | Unique identifier assigned to the customer. | `CUST11575` |
| `counterparty_id` | String | Source / Operational | Unique identifier assigned to the transaction counterparty. | `CP27697` |
| `amount` | Float | Source / Operational | Monetary value associated with the transaction. | `839.66` |
| `channel` | String | Source / Operational | Field representing channel within the sanctions-compliance screening workflow. | `ACH` |
| `counterparty_name` | String | Source / Operational | Name of the counterparty associated with the transaction. | `Hassan Smith` |
| `country` | String | Source / Operational | Country associated with the customer, counterparty, or watchlist subject. | `Turkey` |
| `screening_alert_id` | String | Engineered / Screening | Unique identifier for the screening alert. | `SAN00202` |
| `screening_risk_score` | Float | Engineered / Screening | Numeric analytical score representing screening risk. | `100` |
| `disposition` | String | Engineered / Screening | Final analyst disposition of the sanctions-screening alert. | `True Match` |
| `sanctions_alert_flag` | Integer | Engineered / Screening | Indicator identifying whether sanctions alert applies. | `0` |

## Dataset Relationships

- `counterparties.csv.counterparty_id` ↔ `transactions(20260914-025617).csv.counterparty_id` provides a shared identifier for screening analysis and joins.
- `counterparties.csv.counterparty_id` ↔ `sanctions_screening_alerts.csv.counterparty_id` provides a shared identifier for screening analysis and joins.
- `counterparties.csv.counterparty_id` ↔ `transactions_screened.csv.counterparty_id` provides a shared identifier for screening analysis and joins.
- `customers(20260914-025617).csv.customer_id` ↔ `transactions(20260914-025617).csv.customer_id` provides a shared identifier for screening analysis and joins.
- `customers(20260914-025617).csv.customer_id` ↔ `transactions_screened.csv.customer_id` provides a shared identifier for screening analysis and joins.
- `sanctions_watchlist.csv.watchlist_id` ↔ `sanctions_screening_alerts.csv.watchlist_id` provides a shared identifier for screening analysis and joins.
- `transactions(20260914-025617).csv.counterparty_id` ↔ `sanctions_screening_alerts.csv.counterparty_id` provides a shared identifier for screening analysis and joins.
- `transactions(20260914-025617).csv.transaction_id` ↔ `transactions_screened.csv.transaction_id` provides a shared identifier for screening analysis and joins.
- `transactions(20260914-025617).csv.customer_id` ↔ `transactions_screened.csv.customer_id` provides a shared identifier for screening analysis and joins.
- `transactions(20260914-025617).csv.counterparty_id` ↔ `transactions_screened.csv.counterparty_id` provides a shared identifier for screening analysis and joins.
- `sanctions_screening_alerts.csv.screening_alert_id` ↔ `transactions_screened.csv.screening_alert_id` provides a shared identifier for screening analysis and joins.
- `sanctions_screening_alerts.csv.counterparty_id` ↔ `transactions_screened.csv.counterparty_id` provides a shared identifier for screening analysis and joins.

## Sanctions Screening Workflow

**Customer / Counterparty Profiles → Raw Transactions → Watchlist Screening → Match Scoring & Alert Generation → Analyst Disposition → Screened Transaction Analytics**

The project structure supports sanctions-compliance analysis by combining customer and counterparty information with transactional activity and watchlist data. Potential matches are represented in the screening-alert layer, while `transactions_screened.csv` provides an analytics-ready layer for reviewing screening outcomes and patterns.

## EDA & Feature Engineering Context

The raw reference and transaction datasets provide the source layer for exploratory analysis. Screening-derived attributes—including match, risk, or screening indicators where present—represent analytical features created or used during the screening workflow. The separation between raw transactions and `transactions_screened.csv` makes the project's feature-engineering and enrichment process visible to portfolio reviewers.

## Data Quality Conventions

- Validate customer, counterparty, transaction, alert, and watchlist identifiers before joining datasets.
- Standardize names and textual entity attributes before performing similarity or match analysis.
- Standardize country and jurisdiction values before geographic sanctions analysis.
- Validate transaction amounts and dates for missing, duplicate, or implausible values.
- Review screening scores and match indicators against the project's documented business rules.
- Treat missing values according to business meaning rather than automatically removing them.
- Reconcile engineered screening fields in the screened dataset to the underlying transaction, counterparty, and watchlist records.

---

*Prepared for the Sanctions Compliance & Screening Analytics GitHub portfolio project.*