import plotly.express as px

from utils.data_loader import (
    loan_status_distribution,
    grade_distribution,
    state_distribution,
    loan_amount_distribution,
    interest_rate_distribution,
    executive_summary,
    accepted_raw
)


# ==========================================================
# Theme
# ==========================================================

def apply_dashboard_theme(fig):

    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="#F8FAFC",
        plot_bgcolor="white",
        font=dict(
            family="Inter",
            color="#0F172A",
            size=13
        ),
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_size=13
        ),
        transition_duration=500
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False
    )

    fig.update_yaxes(
        gridcolor="#E2E8F0",
        zeroline=False
    )

    return fig



# ==========================================================
# Loan Status
# ==========================================================

def create_status_chart(df=None):

    if df is None:

        data = loan_status_distribution.copy()

    else:

        data = (
            df["loan_status"]
            .value_counts()
            .reset_index()
        )

        data.columns = [
            "loan_status",
            "count"
        ]


    fig = px.pie(
        data,
        names="loan_status",
        values="count",
        hole=0.62,
        color_discrete_sequence=px.colors.qualitative.Set3
    )


    fig.update_traces(
        textinfo="percent",
        hovertemplate=
        "<b>%{label}</b><br>%{value:,} loans"
    )


    fig.update_layout(
        title="Loan Status Distribution"
    )


    return apply_dashboard_theme(fig)



# ==========================================================
# Grade
# ==========================================================

def create_grade_chart(df=None):

    if df is None:

        data = grade_distribution.copy()

    else:

        data = (
            df["grade"]
            .value_counts()
            .reset_index()
        )

        data.columns = [
            "grade",
            "count"
        ]


    fig = px.bar(
        data,
        x="grade",
        y="count",
        text_auto=True,
        color="count",
        color_continuous_scale="Blues"
    )


    fig.update_layout(
        title="Loan Grade Distribution",
        coloraxis_showscale=False
    )


    return apply_dashboard_theme(fig)



# ==========================================================
# State
# ==========================================================

def create_state_chart(df=None):

    if df is None:

        data = state_distribution.copy()

        data = (
            data
            .nlargest(10, "count")
        )

    else:

        data = (
            df["addr_state"]
            .value_counts()
            .nlargest(10)
            .reset_index()
        )

        data.columns = [
            "addr_state",
            "count"
        ]


    fig = px.bar(
        data,
        x="count",
        y="addr_state",
        orientation="h",
        text_auto=True,
        color="count",
        color_continuous_scale="Teal"
    )


    fig.update_layout(
        title="Top 10 States",
        coloraxis_showscale=False,
        yaxis=dict(
            categoryorder="total ascending"
        )
    )


    return apply_dashboard_theme(fig)



# ==========================================================
# Loan Amount
# ==========================================================

def create_loan_chart(df=None):

    if df is None:

        data = loan_amount_distribution.copy()

    else:

        data = df


    fig = px.histogram(
        data,
        x="loan_amnt",
        nbins=40,
        color_discrete_sequence=["#2563EB"]
    )


    fig.update_layout(
        title="Loan Amount Distribution"
    )


    return apply_dashboard_theme(fig)



# ==========================================================
# Interest Rate
# ==========================================================

def create_interest_chart(df=None):

    if df is None:

        data = interest_rate_distribution.copy()

    else:

        data = df


    fig = px.histogram(
        data,
        x="int_rate",
        nbins=35,
        color_discrete_sequence=["#7C3AED"]
    )


    fig.update_layout(
        title="Interest Rate Distribution"
    )


    return apply_dashboard_theme(fig)



# ==========================================================
# FICO
# ==========================================================

def create_fico_chart(df=None):

    if df is None:

        data = accepted_raw

    else:

        data = df


    fig = px.histogram(
        data,
        x="fico_range_low",
        nbins=35,
        color_discrete_sequence=["#10B981"]
    )


    fig.update_layout(
        title="Borrower FICO Distribution"
    )


    return apply_dashboard_theme(fig)



# ==========================================================
# Anomaly
# ==========================================================

def create_anomaly_chart(df=None):

    summary = executive_summary


    counts = {

        "Strong":
            int(summary["strong_anomalies"].iloc[0]),

        "Moderate":
            int(summary["moderate_anomalies"].iloc[0]),

        "Weak":
            int(summary["weak_anomalies"].iloc[0])

    }


    fig = px.pie(

        names=list(counts.keys()),

        values=list(counts.values()),

        hole=0.60,

        color_discrete_sequence=[

            "#EF4444",

            "#F59E0B",

            "#3B82F6"

        ]

    )


    fig.update_layout(
        title="Anomaly Categories"
    )


    return apply_dashboard_theme(fig)

# ==========================================================
# Anomaly Summary
# ==========================================================

def create_anomaly_chart(summary_df):

    counts = {
        "Strong": int(
            summary_df["strong_anomalies"].iloc[0]
        ),
        "Moderate": int(
            summary_df["moderate_anomalies"].iloc[0]
        ),
        "Weak": int(
            summary_df["weak_anomalies"].iloc[0]
        )
    }

    fig = px.pie(
        names=list(counts.keys()),
        values=list(counts.values()),
        hole=0.60,
        color_discrete_sequence=[
            "#EF4444",
            "#F59E0B",
            "#3B82F6"
        ]
    )

    fig.update_layout(
        title="Anomaly Categories"
    )

    fig.update_traces(
        textinfo="percent",
        hovertemplate=(
            "<b>%{label}</b><br>"
            "%{value:,} records"
            "<extra></extra>"
        )
    )

    return apply_dashboard_theme(fig)