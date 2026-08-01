from dash import html
import dash
import dash_bootstrap_components as dbc


from utils.data_loader import (
    executive_raw,
    cluster_profiles,
    executive_summary, 
    association_rule_summary
)


from figures.executive_figures import (
    create_status_chart,
    create_grade_chart,
    create_state_chart,
    create_interest_chart,
    create_loan_chart,
    create_fico_chart,
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

TOTAL_RULES = int(
    association_rule_summary["final_rules"].iloc[0]
)

MAX_LIFT = float(
    association_rule_summary["max_lift"].iloc[0]
)

loan_status_options = sorted(
    executive_raw["loan_status"]
    .dropna()
    .unique()
)


grade_options = sorted(
    executive_raw["grade"]
    .dropna()
    .unique()
)


state_options = sorted(
    executive_raw["addr_state"]
    .dropna()
    .unique()
)


loan_min = int(
    executive_raw["loan_amnt"].min()
)


loan_max = int(
    executive_raw["loan_amnt"].max()
)



# ==========================================================
# INITIAL FIGURES
# ==========================================================

initial_status = create_status_chart()
initial_grade = create_grade_chart()
initial_state = create_state_chart()
initial_loan = create_loan_chart()
initial_interest = create_interest_chart(
    executive_raw
)
initial_fico = create_fico_chart()

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



        # ==================================================
        # KPI SECTION
        # ==================================================

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

                ),

                dbc.Col(
                    metric_card(
                        "🔗",
                        "Risk Patterns",
                        f"{TOTAL_RULES:,}",
                        "#2563EB",
                        "kpi-risk-patterns"
                    ),
                    xl=3,
                    md=6
                ),


                dbc.Col(
                    metric_card(
                        "⚡",
                        "Highest Risk Lift",
                        f"{MAX_LIFT:.2f}x",
                        "#F59E0B",
                        "kpi-highest-lift"
                    ),
                    xl=3,
                    md=6
                ), 

                dbc.Col(

                    metric_card(
                        "🚨",
                        "Total Anomalies",
                        f"{TOTAL_ANOMALIES:,}",
                        "#EF4444",
                        "kpi-total-anomalies"
                    ),

                    xl=3,
                    md=6

                ),



                dbc.Col(

                    metric_card(
                        "🔥",
                        "Strong Anomalies",
                        f"{STRONG_ANOMALIES:,}",
                        "#DC2626",
                        "kpi-strong-anomalies"
                    ),

                    xl=3,
                    md=6

                )

            ],

            className="g-4 mb-4"

        ),



        # ==================================================
        # DISTRIBUTION CHARTS
        # ==================================================

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
                        "Top Borrower States",
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



        # ==================================================
        # BUSINESS INSIGHTS
        # ==================================================

        dbc.Row(

            [

                dbc.Col(

                    insight_card(

                        "Portfolio Overview",

                        (
                            "The Lending Club portfolio contains "
                            f"{len(executive_raw):,} accepted loans. "
                            "Borrowers are mainly distributed across "
                            "standard credit grades, providing a broad "
                            "view of consumer lending behavior."
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
                            "Pattern mining indicates that credit "
                            "deterioration signals are strongly related "
                            "to loan performance. Recoveries and recent "
                            "FICO deterioration provide important risk "
                            "monitoring indicators."
                        ),

                        "⚠️",

                        "#F59E0B"

                    ),

                    lg=4

                ),



                dbc.Col(

                    insight_card(

                        "Customer Segmentation",

                        (
                            "Clustering analysis reveals different "
                            "borrower profiles based on financial "
                            "characteristics, allowing deeper analysis "
                            "of lending behavior and portfolio structure."
                        ),

                        "🧩",

                        "#10B981"

                    ),

                    lg=4

                )

            ],

            className="mt-4"

        )



    ],

    fluid=True,

    className="py-4"

)