from dash import html, dash_table, dcc 
import dash
import dash_bootstrap_components as dbc

from components.metric_card import metric_card
from components.hero import hero

print("IMPORTING PATTERN DATA")

from utils.data_loader import (
    get_association_rule_summary,
    get_association_rules,
    # get_top_lift_rules,
    # get_business_insights,
    # get_frequent_itemsets,
)

from components.pattern_insight_card import pattern_insight_card

from utils.pattern_business_insights import (
    pattern_business_insights
)

from utils.pattern_insights import pattern_insights
# from figures.pattern_figures import create_frequent_itemsets_chart

print("PATTERN DATA LOADED")

dash.register_page(
    __name__,
    path="/patterns",
    name="Pattern Analysis"
)

def layout():

    association_rule_summary = get_association_rule_summary()
    association_rules = get_association_rules()
    # top_lift_rules = get_top_lift_rules()
    # business_insights = get_business_insights()

    pattern_summary = association_rule_summary.iloc[0]

    # top_patterns = (
    #     top_lift_rules
    #     .merge(
    #         business_insights[["rank", "title", "description"]],
    #         on="rank",
    #         how="left"
    #     )
    #     .sort_values("lift", ascending=False)
    #     .head(10)
    # )

    transactions = int(pattern_summary["total_transactions"])
    frequent_itemsets = int(pattern_summary["frequent_itemsets"])
    association_rules_count = len(association_rules)

    return dbc.Container(
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
                            f"{int(transactions):,}",
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
                            f"{int(frequent_itemsets):,}",
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
                            f"{int(association_rules_count):,}",
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
                                            )[:100]
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
                                            )[:100]
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

            html.Br(), 

            dbc.Card(

                dbc.CardBody(

                    [

                        html.H4(
                            "🏆 Top 10 High-Impact Association Patterns",
                            className="fw-bold mb-4"
                        ),

                        dbc.Row(

                            [

                                dbc.Col(

                                    dbc.Card(

                                        dbc.CardBody(

                                            [

                                                html.H5(
                                                    f"🥇 Rule #{rule['rank']}",
                                                    className="fw-bold text-primary"
                                                ),

                                                dbc.Badge(
                                                    rule["category"],
                                                    color="primary",
                                                    className="mb-3"
                                                ),

                                                html.P([
                                                    html.Strong("IF: "),
                                                    rule["IF"]
                                                ]),

                                                html.P([
                                                    html.Strong("THEN: "),
                                                    rule["THEN"]
                                                ]),

                                                dbc.Row(

                                                    [

                                                        dbc.Col(
                                                            [
                                                                html.Small("Support"),
                                                                html.H6(
                                                                    f"{rule['support']*100:.1f}%"
                                                                )
                                                            ]
                                                        ),

                                                        dbc.Col(
                                                            [
                                                                html.Small("Confidence"),
                                                                html.H6(
                                                                    f"{rule['confidence']*100:.1f}%"
                                                                )
                                                            ]
                                                        ),

                                                        dbc.Col(
                                                            [
                                                                html.Small("Lift"),
                                                                html.H6(
                                                                    f"{rule['lift']:.2f}×"
                                                                )
                                                            ]
                                                        )

                                                    ],

                                                    className="mb-3"

                                                ),

                                                html.H6("Business Insight"),

                                                html.P(
                                                    rule["insight"],
                                                    className="text-muted"
                                                ),

                                                dbc.Alert(
                                                    rule["recommendation"],
                                                    color="warning",
                                                    className="mb-0"
                                                )

                                            ]

                                        ),

                                        className="shadow-sm h-100"

                                    ),

                                    lg=6,
                                    className="mb-4"

                                )

                                for rule in pattern_insights[:10]

                            ]

                        )

                    ]

                ),

                className="shadow-sm border-0"

            ), 

            html.Br(),

            dbc.Card(

                dbc.CardBody(

                    [

                        html.H4(
                            "Frequent Borrower Characteristics",
                            className="fw-bold mb-3"
                        ),

                        html.P(

                            "The chart below displays the borrower characteristics that appear most frequently in the Lending Club dataset. Higher support indicates that the characteristic occurs more often across all loan applications.",

                            className="text-muted"

                        ),

                        dcc.Graph(
                            id="frequent-itemsets-chart",
                            config={
                                "displayModeBar": False
                            }
                        )

                    ]

                ),

                className="shadow-sm border-0 mb-4"

            ),

            html.Br(),

            html.H3(
                "📌 Business Insights",
                className="fw-bold mb-3"
            ),

            dbc.Row(

                [

                    dbc.Col(

                        pattern_insight_card(item),

                        lg=3,
                        md=6,
                        sm=12

                    )

                    for item in pattern_business_insights

                ],

                className="g-4"

            )
        ],

        fluid=True,
        className="py-4"
    )

print("Pattern Page Completely Rendered, Loaded. This is the last line of pattern.py")