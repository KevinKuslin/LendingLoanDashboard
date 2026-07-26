from dash import html, dcc, dash_table 
import dash
import dash_bootstrap_components as dbc

from components.hero import hero
from components.metric_card import metric_card 
from components.anomaly_case_card import anomaly_case_card

from figures.anomaly_figures import create_anomaly_scatter

from utils.data_loader import (
    executive_summary,
    anomaly_scatter,
    anomaly_method_counts,
    anomaly_categories,
    anomaly_feature_difference,
    top10_anomalies,
)

dash.register_page(
    __name__,
    path="/anomalies",
    name="Anomaly Investigation"
)

summary = executive_summary.iloc[0]

TOTAL_LOANS = int(summary["total_loans"])
TOTAL_ANOMALIES = int(summary["total_anomalies"])
STRONG_ANOMALIES = int(summary["strong_anomalies"])

DETECTION_RATE = (
    TOTAL_ANOMALIES /
    TOTAL_LOANS
) * 100

layout = dbc.Container(

    [

        hero(),

        html.Br(),

        html.Div(

            [

                html.H2(
                    "Anomaly Investigation",
                    className="fw-bold mb-1"
                ),

                html.P(
                    "Investigate unusual borrower profiles detected using multiple anomaly detection techniques.",
                    className="text-muted mb-4"
                )

            ]

        ),

                dbc.Row(

            [

                dbc.Col(

                    metric_card(

                        icon="📄",

                        title="Total Loans",

                        value=f"{TOTAL_LOANS:,}",

                        color="#2563EB",

                        component_id="total-loans"

                    ),

                    lg=3,
                    md=6,
                    sm=12

                ),

                dbc.Col(

                    metric_card(

                        icon="🚨",

                        title="Detected Anomalies",

                        value=f"{TOTAL_ANOMALIES:,}",

                        color="#EF4444",

                        component_id="total-anomalies"

                    ),

                    lg=3,
                    md=6,
                    sm=12

                ),

                dbc.Col(

                    metric_card(

                        icon="⚠️",

                        title="Strong Anomalies",

                        value=f"{STRONG_ANOMALIES:,}",

                        color="#F59E0B",

                        component_id="strong-anomalies"

                    ),

                    lg=3,
                    md=6,
                    sm=12

                ),

                dbc.Col(

                    metric_card(

                        icon="📊",

                        title="Anomaly Detection Rate",

                        value=f"{DETECTION_RATE:.1f}%",

                        color="#10B981",

                        component_id="coverage-rate"

                    ),

                    lg=3,
                    md=6,
                    sm=12

                ),

            ],

            className="g-3 mb-4"

        ),

                dbc.Alert(

            [

                html.Div(

                    [

                        html.I(
                            className="bi bi-info-circle-fill me-2"
                        ),

                        html.Strong(
                            "Anomaly Detection Summary"
                        )

                    ],

                    className="mb-2"

                ),

                html.Div(

                    [

                        html.Span(
                            f"Strong: {summary['strong_anomalies']:,}"
                        ),

                        html.Span("  |  "),

                        html.Span(
                            f"Moderate: {summary['moderate_anomalies']:,}"
                        ),

                        html.Span("  |  "),

                        html.Span(
                            f"Weak: {summary['weak_anomalies']:,}"
                        ),

                        html.Span("  |  "),

                        html.Span(
                            f"Detection Coverage: {DETECTION_RATE:.1f}%"
                        )

                    ]

                )

            ],

            color="light",

            className="shadow-sm border-0"

        ),

        dbc.Card(

            dbc.CardBody(

                [

                    html.H4(
                        "Anomaly Landscape Explorer",
                        className="fw-bold mb-3"
                    ),

                    dbc.Row(

                        [

                            dbc.Col(

                                [

                                    html.Label("X-Axis"),

                                    dcc.Dropdown(

                                        id="scatter-x",

                                        value="annual_inc",

                                        clearable=False,

                                        options=[

                                            {
                                                "label":"Annual Income",
                                                "value":"annual_inc"
                                            },

                                            {
                                                "label":"Loan Amount",
                                                "value":"loan_amnt"
                                            },

                                            {
                                                "label":"FICO Score",
                                                "value":"fico_range_low"
                                            },

                                            {
                                                "label":"Debt-to-Income Ratio",
                                                "value":"dti"
                                            },

                                            {
                                                "label":"Recoveries",
                                                "value":"recoveries"
                                            }

                                        ]

                                    )

                                ],

                                md=3

                            ),

                            dbc.Col(

                                [

                                    html.Label("Y-Axis"),

                                    dcc.Dropdown(

                                        id="scatter-y",

                                        value="loan_amnt",

                                        clearable=False,

                                        options=[

                                            {
                                                "label":"Annual Income",
                                                "value":"annual_inc"
                                            },

                                            {
                                                "label":"Loan Amount",
                                                "value":"loan_amnt"
                                            },

                                            {
                                                "label":"FICO Score",
                                                "value":"fico_range_low"
                                            },

                                            {
                                                "label":"Debt-to-Income Ratio",
                                                "value":"dti"
                                            },

                                            {
                                                "label":"Recoveries",
                                                "value":"recoveries"
                                            }

                                        ]

                                    )

                                ],

                                md=3

                            ),

                            dbc.Col(

                                [

                                    html.Label("Category"),

                                    dcc.Dropdown(

                                        id="scatter-category",

                                        value="All",

                                        clearable=False,

                                        options=[

                                            {
                                                "label":"All",
                                                "value":"All"
                                            },

                                            {
                                                "label":"Weak anomaly",
                                                "value":"Weak anomaly"
                                            },

                                            {
                                                "label":"Moderate anomaly",
                                                "value":"Moderate anomaly"
                                            },

                                            {
                                                "label":"Strong anomaly",
                                                "value":"Strong anomaly"
                                            }

                                        ]

                                    )

                                ],

                                md=3

                            ),

                            dbc.Col(

                                [

                                    html.Label("Detected By"),

                                    dcc.Dropdown(

                                        id="scatter-methods",

                                        value="All",

                                        clearable=False,

                                        options=[

                                            {
                                                "label":"All",
                                                "value":"All"
                                            },

                                            {
                                                "label":"1 Method",
                                                "value":1
                                            },

                                            {
                                                "label":"2 Methods",
                                                "value":2
                                            },

                                            {
                                                "label":"3 Methods",
                                                "value":3
                                            }

                                        ]

                                    )

                                ],

                                md=3

                            )

                        ],

                        className="g-3"

                    ),

                    html.Br(),

                    dbc.Row(

                        [

                            dbc.Col(

                                html.Div(

                                    id="scatter-counter",

                                    className="text-muted fw-semibold"

                                )

                            ),

                            dbc.Col(

                                dbc.Button(

                                    "Reset Explorer",

                                    id="reset-scatter",

                                    color="secondary",

                                    outline=True,

                                    size="sm"

                                ),

                                width="auto"

                            )

                        ],

                        className="mb-3 align-items-center"

                    ),

                    dcc.Graph(
                        id="anomaly-scatter",
                        figure=create_anomaly_scatter(
                            anomaly_scatter,
                            "annual_inc",
                            "loan_amnt"
                        ),
                        config={"displayModeBar": False}
                    ), 

                    dbc.Alert(
                        [
                            html.Strong("How to interpret this visualization"),
                            html.Br(),
                            html.Span(
                                "Each point represents one borrower. "
                                "Points located farther from dense borrower clusters are more likely "
                                "to represent unusual lending profiles. "
                                "Colors indicate anomaly severity, while the filters allow investigation "
                                "of different anomaly categories and detection agreement."
                            )
                        ],
                        color="info",
                        className="mt-3 mb-0"
                    ),

                ]

            ),

            className="shadow-sm border-0"

        ),

        dbc.Card(

            dbc.CardBody(

                [

                    html.H4(
                        "Detection Method Comparison",
                        className="fw-bold mb-3"
                    ),

                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Label("Anomaly Category"),

                                    dcc.Dropdown(
                                        id="method-category",
                                        clearable=False,
                                        value="All",
                                        options=[
                                            {"label":"All", "value":"All"},
                                            {"label":"Weak anomaly", "value":"Weak anomaly"},
                                            {"label":"Moderate anomaly", "value":"Moderate anomaly"},
                                            {"label":"Strong anomaly", "value":"Strong anomaly"}
                                        ]
                                    )
                                ],
                                md=4
                            )
                        ],

                        className="mb-3"

                    ),

                    dcc.Graph(
                        id="method-chart",
                        config={"displayModeBar": False}
                    ),

                    html.Br(),

                    html.Div(

                        id="method-insight"

                    ), 

                ]

            ),

            className="shadow-sm border-0"

        ), 

        dbc.Card(

            dbc.CardBody(

                [

                    html.H4(
                        "Top Investigated Anomalies",
                        className="fw-bold mb-3"
                    ),

                    dbc.Row(

                        [

                            dbc.Col(

                                [

                                    html.Label("Business Reason"),

                                    dcc.Dropdown(

                                        id="anomaly-reason",

                                        value="All",

                                        clearable=False,

                                        options=[

                                            {
                                                "label": "All",
                                                "value": "All"
                                            },

                                            *[
                                                {
                                                    "label": i,
                                                    "value": i
                                                }

                                                for i in sorted(
                                                    top10_anomalies[
                                                        "business_reason"
                                                    ].unique()
                                                )

                                            ]

                                        ]

                                    )

                                ],

                                md=5

                            )

                        ],

                        className="mb-3"

                    ),

                    html.Div(

                        id="top-anomaly-cards"

                    )

                ]

            ),

            className="shadow-sm border-0"

        ),

        dbc.Card(

            dbc.CardBody(

                [

                    html.H4(
                        "Investigation Queue",
                        className="fw-bold mb-3"
                    ),

                    dbc.Row(

                        [

                            dbc.Col(

                                [

                                    html.Label(
                                        "Investigation Type",
                                        className="fw-semibold"
                                    ),

                                    dbc.RadioItems(

                                        id="investigation-type",

                                        value="risk",

                                        options=[

                                            {
                                                "label": "🚨 Potential Risk Signals",
                                                "value": "risk"
                                            },

                                            {
                                                "label": "💼 Rare Legitimate Cases",
                                                "value": "legitimate"
                                            },

                                            {
                                                "label": "🗂 Data Quality Review",
                                                "value": "quality"
                                            }

                                        ],

                                        className="mt-2"

                                    )

                                ],

                                md=4

                            ),


                            dbc.Col(

                                html.Div(

                                    id="investigation-panel"

                                ),

                                md=8

                            )

                        ]

                    )

                ]

            ),

            className="shadow-sm border-0 mt-4"

        )
    ]
)