from pathlib import Path
import streamlit as st
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
A = pd.read_csv(ROOT / "data/processed/sanctions_screening_alerts.csv")
T = pd.read_csv(ROOT / "data/processed/transactions_screened.csv")

st.set_page_config(
    page_title="Sanctions Compliance Analytics",
    layout="wide"
)

st.title("Sanctions Screening & Compliance Analytics")
st.caption(
    "Synthetic portfolio project | A simple view of sanctions screening results, "
    "true matches, escalations, false positives, flagged payments, and recommended actions."
)

with st.sidebar:
    st.header("Filters")
    st.caption("Use the dropdowns below to filter the dashboard.")

    program_options = ["All"] + sorted(
        A.sanctions_program.dropna().astype(str).unique().tolist()
    )
    selected_program = st.selectbox(
        "Sanctions Program",
        program_options,
        index=0,
        key="sidebar_sanctions_program"
    )

    disposition_options = ["All"] + sorted(
        A.disposition.dropna().astype(str).unique().tolist()
    )
    selected_disposition = st.selectbox(
        "Disposition",
        disposition_options,
        index=0,
        key="sidebar_disposition"
    )

    score_options = ["All", "40+", "50+", "60+", "70+", "80+", "90+"]
    selected_match_score = st.selectbox(
        "Minimum Match Score",
        score_options,
        index=0,
        key="sidebar_match_score"
    )

F = A.copy()

if selected_program != "All":
    F = F[
        F.sanctions_program.astype(str).eq(selected_program)
    ]

if selected_disposition != "All":
    F = F[
        F.disposition.astype(str).eq(selected_disposition)
    ]

if selected_match_score != "All":
    minscore = int(selected_match_score.replace("+", ""))
    F = F[
        pd.to_numeric(F.name_match_score, errors="coerce").fillna(0) >= minscore
    ]

# -------------------------
# Portfolio KPIs
# -------------------------
potential_matches = len(F)
true_matches = (F.disposition == "True Match").sum() if potential_matches else 0
escalated = (F.disposition == "Escalated").sum() if potential_matches else 0
false_positives = (F.disposition == "False Positive").sum() if potential_matches else 0
flagged_amount = float(F.flagged_amount.sum()) if potential_matches else 0.0

true_match_rate = (
    true_matches / potential_matches * 100 if potential_matches else 0.0
)
escalation_rate = (
    escalated / potential_matches * 100 if potential_matches else 0.0
)
false_positive_rate = (
    false_positives / potential_matches * 100 if potential_matches else 0.0
)

# -------------------------
# Portfolio status logic
# -------------------------
def get_portfolio_status():
    if true_matches > 0:
        return (
            "Confirmed Sanctions Risk",
            "The selected screening population contains one or more true sanctions matches requiring immediate compliance action."
        )
    elif escalated > 0:
        return (
            "Escalated Review Required",
            "No confirmed sanctions match is shown in the selected view, but one or more alerts require specialist review."
        )
    else:
        return (
            "No Confirmed Match",
            "The selected population does not currently contain a true match or escalation requiring immediate action."
        )

portfolio_status, portfolio_message = get_portfolio_status()

# -------------------------
# Executive summary
# -------------------------
st.subheader("Executive Summary")

if potential_matches == 0:
    st.warning("No sanctions alerts match the selected filters.")
else:
    s1, s2, s3 = st.columns([1.2, 1.0, 2.8])

    with s1:
        st.metric("Portfolio Status", portfolio_status)

    with s2:
        st.metric("True Matches", f"{true_matches:,}")

    with s3:
        st.info(portfolio_message)

    st.markdown(
        f"""
        The selected view contains **{potential_matches:,} potential sanctions matches**.
        **{true_matches:,}** were determined to be true matches, **{escalated:,}** were escalated for additional review,
        and **{false_positives:,}** were resolved as false positives. The total flagged payment exposure is approximately
        **${flagged_amount/1e6:.1f}M**.
        """
    )

    st.markdown("#### What this means")

    insights = []

    if true_matches > 0:
        insights.append(
            f"{true_matches} confirmed sanctions match(es) require immediate compliance handling and payment/customer restrictions according to policy."
        )

    if escalated > 0:
        insights.append(
            f"{escalated} alert(s) still require specialist sanctions review before a final disposition can be reached."
        )

    if false_positives > 0:
        insights.append(
            f"{false_positives} alert(s) were false positives, showing where screening logic or name similarity generated non-actionable matches."
        )

    if false_positive_rate > 70:
        insights.append(
            "The false-positive rate is high, which may indicate an opportunity to improve screening efficiency without weakening sanctions controls."
        )

    for item in insights:
        st.write(f"• {item}")

    st.markdown("#### Final Portfolio Decision")

    if true_matches > 0:
        st.error(
            "Prioritize confirmed true matches immediately. Place affected payments or counterparties into the appropriate compliance workflow, "
            "and ensure required escalation, blocking/rejection, documentation, and reporting steps are completed."
        )
    elif escalated > 0:
        st.warning(
            "Maintain the escalated alerts in review until identity, ownership, geography, and sanctions-program details are sufficiently resolved."
        )
    else:
        st.success(
            "No immediate sanctions action is indicated by the selected alerts. Continue routine screening and monitoring."
        )

st.divider()

# -------------------------
# KPI scorecard
# -------------------------
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Potential Matches", f"{potential_matches:,}")
c2.metric("True Matches", f"{true_matches:,}")
c3.metric("Escalated", f"{escalated:,}")
c4.metric("False Positives", f"{false_positives:,}")
c5.metric("Flagged Amount", f"${flagged_amount/1e6:.1f}M")

# -------------------------
# Counterparty-level explanation
# -------------------------
st.subheader("Counterparty Sanctions Decision Summary")

available_counterparties = (
    F.counterparty_id.tolist()
    if len(F)
    else A.counterparty_id.tolist()
)

selected_cp = st.selectbox(
    "Select a counterparty to understand the sanctions decision",
    available_counterparties
)

cp_rows = A[A.counterparty_id == selected_cp].copy()

if len(cp_rows):
    cp_row = cp_rows.sort_values(
        "screening_risk_score",
        ascending=False
    ).iloc[0]

    x1, x2, x3, x4 = st.columns(4)

    with x1:
        st.metric(
            "Match Score",
            f"{cp_row.get('name_match_score', 'N/A')}"
        )

    with x2:
        st.metric(
            "Risk Score",
            f"{cp_row.get('screening_risk_score', 'N/A')}"
        )

    with x3:
        st.metric(
            "Sanctions Program",
            str(cp_row.get("sanctions_program", "N/A"))
        )

    with x4:
        st.metric(
            "Disposition",
            str(cp_row.get("disposition", "N/A"))
        )

    st.markdown("#### Why this counterparty matters")

    reasons = [
        f"The screening alert produced a name-match score of **{cp_row.get('name_match_score', 'N/A')}**.",
        f"The alert is associated with the **{cp_row.get('sanctions_program', 'N/A')}** sanctions program.",
        f"The final screening disposition is **{cp_row.get('disposition', 'N/A')}**."
    ]

    if "flagged_amount" in cp_row.index and pd.notna(cp_row["flagged_amount"]):
        reasons.append(
            f"The related flagged amount is approximately **${float(cp_row['flagged_amount']):,.0f}**."
        )

    st.write(" ".join(reasons))

    st.markdown("#### Final Counterparty Decision")

    cp_disposition = str(cp_row.get("disposition", ""))

    if cp_disposition == "True Match":
        st.error(
            "Decision: **TRUE MATCH — IMMEDIATE SANCTIONS ACTION**. "
            "The counterparty should move into the required sanctions compliance workflow."
        )
    elif cp_disposition == "Escalated":
        st.warning(
            "Decision: **ESCALATED REVIEW**. Additional identity or sanctions analysis is required before the alert can be closed."
        )
    elif cp_disposition == "False Positive":
        st.success(
            "Decision: **FALSE POSITIVE — CLOSE ALERT**. The available screening evidence supports closing the match as non-sanctioned."
        )
    else:
        st.info(
            f"Decision: **{cp_disposition or 'REVIEW REQUIRED'}**. Follow the applicable sanctions-review procedure for the current disposition."
        )

    st.markdown("#### Counterparty Screening Record")
    st.dataframe(
        cp_rows.sort_values(
            "screening_risk_score",
            ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )

st.divider()

# -------------------------
# Detailed tabs
# -------------------------
tabs = st.tabs([
    "Screening Queue",
    "Counterparty 360",
    "Payment Review",
    "Portfolio Analytics",
    "Tableau Gallery"
])

with tabs[0]:
    st.subheader("Screening Queue")
    st.caption(
        "Alerts are ranked by screening risk and flagged amount so reviewers can focus on the most important sanctions matches first."
    )

    st.dataframe(
        F.sort_values(
            ["screening_risk_score", "flagged_amount"],
            ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )

with tabs[1]:
    st.subheader("Counterparty 360")
    st.caption(
        "Detailed sanctions-screening history for the selected counterparty."
    )

    st.dataframe(
        cp_rows,
        use_container_width=True,
        hide_index=True
    )

with tabs[2]:
    st.subheader("Payment Review")
    st.caption(
        "Shows payments associated with sanctions alerts so reviewers can identify the largest and most urgent transactions."
    )

    flagged_tx = T[T.sanctions_alert_flag == 1].sort_values(
        "amount",
        ascending=False
    ).head(500)

    st.dataframe(
        flagged_tx,
        use_container_width=True,
        hide_index=True
    )

    if len(flagged_tx):
        p1, p2 = st.columns(2)
        p1.metric(
            "Flagged Payments",
            f"{len(flagged_tx):,}"
        )
        p2.metric(
            "Flagged Payment Value",
            f"${flagged_tx['amount'].sum()/1e6:.1f}M"
        )

with tabs[3]:
    st.subheader("Portfolio Analytics")

    a, b = st.columns(2)

    with a:
        st.markdown("##### Sanctions Programs")
        st.caption(
            "Shows which sanctions programs are generating the selected alerts."
        )
        st.bar_chart(
            F.sanctions_program.value_counts()
        )

    with b:
        st.markdown("##### Alert Dispositions")
        st.caption(
            "Shows how screening alerts were resolved across true matches, escalations, and false positives."
        )
        st.bar_chart(
            F.disposition.value_counts()
        )

with tabs[4]:
    st.subheader("Tableau Gallery")
    st.caption(
        "Refreshed executive dashboard synchronized to the current sanctions-screening datasets."
    )

    dashboard = ROOT / "images" / "02_executive_dashboard.png"

    if dashboard.exists():
        st.image(
            str(dashboard),
            caption="Sanctions Screening & Compliance Analytics — Executive Dashboard",
            use_container_width=True
        )

st.caption(
    "Synthetic educational portfolio project. No real customer, bank, or sanctions-screening data."
)
