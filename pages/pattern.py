from dash import html, dash_table, dcc 
import dash
import dash_bootstrap_components as dbc

from components.metric_card import metric_card
from components.hero import hero

from utils.data_loader import (
    association_rule_summary,
    association_rules,
)

dash.register_page(
    __name__,
    path="/patterns",
    name="Pattern Analysis"
)

pattern_summary = association_rule_summary.iloc[0]

TRANSACTIONS = int(pattern_summary["total_transactions"])
FREQUENT_ITEMSETS = int(pattern_summary["frequent_itemsets"])
ASSOCIATION_RULES = len(association_rules)

layout = dbc.Container(
    [

        hero(),

        html.Br(),

        html.Div(
            [
                html.H2(
                    "Pattern Analysis",
                    className="fw-bold mb-1"
                ),

                html.P(
                    "Discover hidden relationships between borrower characteristics using Association Rule Mining.",
                    className="text-muted mb-4"
                )
            ]
        ),

        dbc.Row(
            [

                dbc.Col(
                    metric_card(
                        "💳",
                        "Transactions",
                        f"{int(TRANSACTIONS):,}",
                        "#2563EB",
                        "transactions-card"
                    ),
                    lg=3,
                    md=6,
                    sm=12
                ),

                dbc.Col(
                    metric_card(
                        "🧺",
                        "Frequent Itemsets",
                        f"{int(FREQUENT_ITEMSETS):,}",
                        "#10B981",
                        "itemsets-card"
                    ), 
                    lg=3,
                    md=6,
                    sm=12
                ),

                dbc.Col(
                    metric_card(
                        "🔗",
                        "Association Rules",
                        f"{int(ASSOCIATION_RULES):,}",
                        "#BB57C3",
                        "rules-card"
                    ),
                    lg=3,
                    md=6,
                    sm=12
                ),

                dbc.Col(
                    metric_card(
                        icon="🏆",
                        title="Maximum Lift",
                        value=f"{pattern_summary['max_lift']:.2f}×",
                        color="#F59E0B",
                        component_id="pattern-max-lift"
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
                        html.I(className="bi bi-info-circle-fill"),

                        html.Strong("Mining Configuration")
                    ],

                    className="mb-2"
                ),

                html.Div(
                    [

                        html.Span(
                            f"Minimum Support: {pattern_summary['min_support']:.1%}"
                        ),

                        html.Span("  |  "),

                        html.Span(
                            f"Minimum Lift: {pattern_summary['min_lift']:.2f}"
                        ),

                        html.Span("  |  "),

                        html.Span(
                            f"Average Confidence: {pattern_summary['avg_confidence']:.1%}"
                        ),

                        html.Span("  |  "),

                        html.Span(
                            f"Average Lift: {pattern_summary['avg_lift']:.2f}"
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
                        "🧠 How Association Rule Mining Works",
                        className="fw-bold mb-3"
                    ),

                    dbc.Row(

                        [

                            dbc.Col(

                                [

                                    html.H5("Support"),

                                    html.P(
                                        "Measures how frequently a borrower pattern appears within the entire Lending Club dataset."
                                    )

                                ],

                                md=4

                            ),

                            dbc.Col(

                                [

                                    html.H5("Confidence"),

                                    html.P(
                                        "Represents the probability that the THEN condition occurs whenever the IF condition is observed."
                                    )

                                ],

                                md=4

                            ),

                            dbc.Col(

                                [

                                    html.H5("Lift"),

                                    html.P(
                                        "Measures how much stronger a relationship is compared to random chance. Higher Lift indicates a more meaningful borrower relationship."
                                    )

                                ],

                                md=4

                            )

                        ]

                    ),

                    html.Hr(),

                    dbc.Alert(

                        [

                            html.Strong("Interpretation"),

                            html.Br(),

                            html.Span(
                                "Rules with high Support occur frequently, "
                                "high Confidence indicates reliability, "
                                "and Lift greater than 1 suggests a meaningful relationship."
                            )

                        ],

                        color="info",

                        className="mb-0"

                    )

                ]

            ),

            className="shadow-sm border-0 mb-4"

        ), 

        dbc.Card(

            dbc.CardBody(

                [

                    html.H4(
                        "Association Rule Explorer",
                        className="fw-bold mb-3"
                    ),

                    dbc.Row(

                        [

                            dbc.Col(

                                dcc.Dropdown(

                                    id="if-filter",
                                    searchable=True, 
                                    placeholder="Filter IF...",

                                    options=[
                                        {
                                            "label": i,
                                            "value": i
                                        }
                                        for i in sorted(
                                            association_rules["IF"].unique()
                                        )
                                    ],

                                    clearable=True

                                ),

                                md=4

                            ),

                            dbc.Col(

                                dcc.Dropdown(

                                    id="then-filter",

                                    placeholder="Filter THEN...",

                                    options=[
                                        {
                                            "label": i,
                                            "value": i
                                        }
                                        for i in sorted(
                                            association_rules["THEN"].unique()
                                        )
                                    ],

                                    clearable=True

                                ),

                                md=4

                            ),

                            dbc.Col(

                                dcc.Dropdown(

                                    id="sort-rules",

                                    value="lift",

                                    clearable=False,

                                    options=[

                                        {
                                            "label":"Sort by Lift",
                                            "value":"lift"
                                        },

                                        {
                                            "label":"Sort by Confidence",
                                            "value":"confidence"
                                        },

                                        {
                                            "label":"Sort by Support",
                                            "value":"support"
                                        }

                                    ]

                                ),

                                md=4

                            )

                        ]

                    ),

                    html.Br(),

                    dbc.Row(

                        [

                            dbc.Col(

                                [

                                    html.Label("Minimum Support"),

                                    dcc.Slider(
                                        id="support-slider",
                                        min=0,
                                        max=float(association_rules["support"].max()),
                                        value=0,
                                        step=0.01,
                                        marks={
                                            0:"0",
                                            0.05:"5%",
                                            0.10:"10%",
                                            0.15:"15%"
                                        }
                                    )

                                ],

                                md=4

                            ),

                            dbc.Col(

                                [

                                    html.Label("Minimum Confidence"),

                                    dcc.Slider(

                                        id="confidence-slider",

                                        min=0,
                                        max=1,
                                        value=0,
                                        step=0.05,

                                        tooltip={
                                            "placement":"bottom",
                                            "always_visible":True
                                        }, 

                                        marks={
                                            0:"0",
                                            0.25:"25%",
                                            0.50:"50%",
                                            0.75:"75%",
                                            1:"100%"
                                        }

                                    )

                                ],

                                md=4

                            ),

                            dbc.Col(

                                [

                                    html.Label("Minimum Lift"),

                                    dcc.Slider(

                                        id="lift-slider",

                                        min=1,
                                        max=float(association_rules["lift"].max()),
                                        value=1,
                                        step=0.1,

                                        tooltip={
                                            "placement":"bottom",
                                            "always_visible":True
                                        }, 

                                        marks={
                                            1:"1",
                                            2:"2",
                                            4:"4",
                                            6:"6"
                                        }

                                    )

                                ],

                                md=4

                            )

                        ],

                        className="mb-4"

                    ),

                    html.Br(),

                    dbc.Row(

                        [

                            dbc.Col(

                                html.Div(

                                    id="rule-counter",

                                    className="text-muted fw-semibold"

                                )

                            ),

                            dbc.Col(

                                dbc.Button(

                                    "Reset Filters",

                                    id="reset-rule-filters",

                                    color="secondary",

                                    outline=True,

                                    size="sm"

                                ),

                                width="auto"

                            )

                        ],

                        className="mb-3 align-items-center"

                    ),

                ]

            ),

            className="shadow-sm border-0"

        ),

        html.Br(),

        dash_table.DataTable(

            id="rules-table",
            page_size=12,
            sort_action="native",
            filter_action="native",
            style_table={
                "overflowX":"auto"
            },
            style_cell={
                "textAlign":"left",
                "padding":"10px"
            },
            style_header={
                "fontWeight":"bold",
                "backgroundColor":"#F8FAFC"
            }, 
            style_data_conditional=[
                {
                    "if":{
                        "column_id":"lift",
                        "filter_query":"{lift} >= 3"
                    },
                    "backgroundColor":"#DCFCE7",
                    "color":"#166534",
                    "fontWeight":"bold"
                },
                {
                    "if":{
                        "column_id":"confidence",
                        "filter_query":"{confidence} >= 0.8"
                    },
                    "backgroundColor":"#DBEAFE",
                    "color":"#1E40AF"
                }
            ]

        ), 

        dbc.Card(

            dbc.CardBody(

                [

                    html.H4(
                        "Support vs Confidence Analysis",
                        className="fw-bold mb-3"
                    ),

                    dbc.Row(

                        [

                            dbc.Col(

                                [

                                    html.Label("Minimum Lift"),

                                    dcc.Slider(
                                        id="scatter-lift",
                                        min=1,
                                        max=float(
                                            association_rules["lift"].max()
                                        ),
                                        value=1,
                                        step=0.1,
                                    )

                                ],

                                md=4

                            ),

                            dbc.Col(

                                [

                                    html.Label("Color By"),

                                    dcc.Dropdown(

                                        id="scatter-color",

                                        value="lift",

                                        clearable=False,

                                        options=[

                                            {
                                                "label":"Lift",
                                                "value":"lift"
                                            },

                                            {
                                                "label":"Confidence",
                                                "value":"confidence"
                                            },

                                            {
                                                "label":"Support",
                                                "value":"support"
                                            }

                                        ]

                                    )

                                ],

                                md=4

                            ),

                            dbc.Col(

                                [

                                    html.Label("Bubble Size"),

                                    dcc.Dropdown(

                                        id="scatter-size",

                                        value="lift",

                                        clearable=False,

                                        options=[

                                            {
                                                "label":"Lift",
                                                "value":"lift"
                                            },

                                            {
                                                "label":"Confidence",
                                                "value":"confidence"
                                            },

                                            {
                                                "label":"Support",
                                                "value":"support"
                                            }

                                        ]

                                    )

                                ],

                                md=4

                            )

                        ]

                    ),

                    dcc.Graph(
                        id="support-confidence-scatter"
                    )

                ]

            ),

            className="shadow-sm border-0 mb-4"

        ),
    ],

    fluid=True,
    className="py-4"
)