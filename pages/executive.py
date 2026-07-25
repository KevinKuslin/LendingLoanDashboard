from dash import html
import dash
import dash_bootstrap_components as dbc

from utils.data_loader import (
    accepted_raw,
    executive_summary,
    cluster_profiles,
    anomaly_categories,
    anomaly_method_counts,
    anomaly_feature_difference
)

from components.risk_overview_card import risk_overview_card

from figures.anomaly_figures import (
    create_risk_distribution_chart,
    create_detection_method_chart,
    create_anomaly_feature_chart
)

from figures.executive_figures import (
    create_status_chart,
    create_grade_chart,
    create_state_chart,
    create_interest_chart,
    create_loan_chart,
    create_fico_chart, 
    create_anomaly_chart
)

from components.hero import hero
from components.metric_card import metric_card
from components.chart_card import chart_card
from components.filter_panel import filter_panel
from components.insight_card import insight_card

dash.register_page(
    __name__,
    path="/",
    name="Executive Summary"
)

# ==========================================================
# STATIC VALUES
# ==========================================================

TOTAL_SEGMENTS = len(cluster_profiles)

TOTAL_ANOMALIES = int(
    executive_summary["total_anomalies"].iloc[0]
)

STRONG_ANOMALIES = int(
    executive_summary["strong_anomalies"].iloc[0]
)

MODERATE_ANOMALIES = int(
    executive_summary["moderate_anomalies"].iloc[0]
)

WEAK_ANOMALIES = int(
    executive_summary["weak_anomalies"].iloc[0]
)

loan_status_options = sorted(
    accepted_raw["loan_status"].dropna().unique()
)

grade_options = sorted(
    accepted_raw["grade"].dropna().unique()
)

state_options = sorted(
    accepted_raw["addr_state"].dropna().unique()
)

loan_min = int(accepted_raw["loan_amnt"].min())
loan_max = int(accepted_raw["loan_amnt"].max())

# Initial Figures 

initial_status = create_status_chart()

initial_grade = create_grade_chart()

initial_state = create_state_chart()

initial_loan = create_loan_chart(
    accepted_raw
)

initial_interest = create_interest_chart(
    accepted_raw
)

initial_fico = create_fico_chart(
    accepted_raw
)

initial_risk_distribution = create_risk_distribution_chart(
    anomaly_categories
)


initial_detection_method = create_detection_method_chart(
    anomaly_method_counts
)


initial_feature_difference = create_anomaly_feature_chart(
    anomaly_feature_difference
)

initial_anomaly = create_anomaly_chart(
    executive_summary
)

initial_risk_distribution = create_risk_distribution_chart(
    anomaly_categories
)


initial_detection_method = create_detection_method_chart(
    anomaly_method_counts
)


initial_feature_difference = create_anomaly_feature_chart(
    anomaly_feature_difference
)

# ==========================================================
# LAYOUT
# ==========================================================

layout = dbc.Container(

    [

        hero(),

        html.Br(),

        filter_panel(
            loan_status_options,
            grade_options,
            state_options,
            loan_min,
            loan_max
        ),

        html.Br(),

        dbc.Row(

            [

                dbc.Col(
                    metric_card(
                        "👥",
                        "Total Loans",
                        "0",
                        "#2563EB",
                        "kpi-total-loans"
                    ),
                    xl=3,
                    md=6
                ),

                dbc.Col(
                    metric_card(
                        "💵",
                        "Average Loan",
                        "$0",
                        "#10B981",
                        "kpi-average-loan"
                    ),
                    xl=3,
                    md=6
                ),

                dbc.Col(
                    metric_card(
                        "📈",
                        "Average Interest",
                        "0%",
                        "#7C3AED",
                        "kpi-interest"
                    ),
                    xl=3,
                    md=6
                ),

                dbc.Col(
                    metric_card(
                        "🧩",
                        "Customer Segments",
                        str(TOTAL_SEGMENTS),
                        "#F59E0B",
                        "kpi-segments"
                    ),
                    xl=3,
                    md=6
                )

            ],

            className="g-4 mb-4"

        ),

        dbc.Row(

            [

                dbc.Col(
                    chart_card(
                        "Loan Status Distribution",
                        initial_status,
                        "loan-status-chart"
                    ), 
                    lg=6
                ),

                dbc.Col(
                    chart_card(
                        "Loan Grade Distribution",
                        initial_grade,
                        "grade-chart"
                    ),
                    lg=6
                )

            ],

            className="g-4 mb-4"

        ),

        dbc.Row(

            [

                dbc.Col(
                    chart_card(
                        "Top States",
                        initial_state,
                        "state-chart"
                    ),
                    lg=6
                ),

                dbc.Col(
                    chart_card(
                        "Interest Rate Distribution",
                        initial_interest,
                        "interest-chart"
                    ),
                    lg=6
                )

            ],

            className="g-4 mb-4"

        ),

        dbc.Row(

            [

                dbc.Col(
                    chart_card(
                        "Loan Amount Distribution",
                        initial_loan,
                        "loan-chart"
                    ),
                    lg=6
                ),

                dbc.Col(
                    chart_card(
                        "Borrower FICO Distribution",
                        initial_fico,
                        "fico-chart"
                    ),
                    lg=6
                )

            ],

            className="g-4 mb-4"

        ),

        dbc.Row(
            [

                dbc.Col(

                    insight_card(
                        "Portfolio Overview",

                        (
                            "The Lending Club portfolio contains "
                            f"{len(accepted_raw):,} accepted loans. "
                            "Most borrowers are concentrated within "
                            "standard loan grades, while customer segmentation "
                            "reveals distinct borrower profiles."
                        ),

                        "📊",

                        "#2563EB"
                    ),

                    lg=4

                ),


                dbc.Col(

                    insight_card(
                        "Risk Insight",

                        (
                            "Pattern mining shows that borrower deterioration "
                            "signals are strongly associated with loan failure. "
                            "Positive recoveries and declining recent FICO scores "
                            "are among the strongest charge-off indicators."
                        ),

                        "⚠️",

                        "#F59E0B"
                    ),

                    lg=4

                ),


                dbc.Col(

                    insight_card(
                        "Anomaly Detection",

                        (
                            "Strong anomalies are mainly characterized by "
                            "higher annual income, larger loan amounts, "
                            "higher DTI, and increased delinquency indicators. "
                            "Multiple detection methods confirm high-risk "
                            "borrower patterns."
                        ),

                        "💡",

                        "#10B981"
                    ),

                    lg=4

                )

            ],

            className="mt-4"

        ), 

        html.Hr(),
        html.H3(
            "Anomaly & Risk Overview",
            className="section-title"
        ),

        dbc.Row(

            [

                dbc.Col(

                    risk_overview_card(
                        "🔥",
                        "Strong Anomalies",
                        f"{STRONG_ANOMALIES:,}",
                        "#EF4444"
                    ),

                    lg=4

                ),


                dbc.Col(

                    risk_overview_card(
                        "⚠️",
                        "Moderate Anomalies",
                        f"{MODERATE_ANOMALIES:,}",
                        "#F59E0B"
                    ),

                    lg=4

                ),


                dbc.Col(

                    risk_overview_card(
                        "🔎",
                        "Weak Anomalies",
                        f"{WEAK_ANOMALIES:,}",
                        "#3B82F6"
                    ),

                    lg=4

                )

            ],

            className="g-4 mb-4"

        ),


        dbc.Row(

            [

                dbc.Col(

                    chart_card(
                        "Risk Distribution",
                        initial_risk_distribution,
                        "risk-distribution-chart"
                    ),

                    lg=6

                ),


                dbc.Col(

                    chart_card(
                        "Detection Method Agreement",
                        initial_detection_method,
                        "detection-method-chart"
                    ),

                    lg=6

                )

            ],

            className="g-4 mb-4"

        ),


        dbc.Row(

            [

                dbc.Col(

                    chart_card(
                        "Main Anomaly Drivers",
                        initial_feature_difference,
                        "anomaly-feature-chart"
                    ),

                    lg=12

                )

            ],

            className="g-4"

        )
    ],

    fluid=True,
    className="py-4"

)