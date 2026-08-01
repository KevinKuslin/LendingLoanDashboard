from dash import html, dcc, dash_table 
import dash
import dash_bootstrap_components as dbc

from components.hero import hero
from components.metric_card import metric_card 
from components.anomaly_case_card import anomaly_case_card

print("IMPORTING ANOMALY FIGURES")

from figures.anomaly_figures import (
    create_anomaly_scatter,
    create_anomaly_category_chart
)

print("IMPORTING ANOMALY DATA")

from utils.data_loader import (
    executive_summary,
    anomaly_scatter,
    anomaly_method_counts,
    anomaly_categories,
    anomaly_feature_difference,
    top10_anomalies,
    cluster_anomaly_cross_reference,
    cluster_category_summary,
    cluster_summary
)

print("ANOMALY DATA LOADED")

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

# layout = dbc.Container(

#     [

#         hero(),

#         html.Br(),

#         html.Div(

#             [

#                 html.H2(
#                     "Anomaly Investigation",
#                     className="fw-bold mb-1"
#                 ),

#                 html.P(
#                     "Investigate unusual borrower profiles detected using multiple anomaly detection techniques.",
#                     className="text-muted mb-4"
#                 )

#             ]

#         ),

#                 dbc.Row(

#             [

#                 dbc.Col(

#                     metric_card(

#                         icon="📄",

#                         title="Total Loans",

#                         value=f"{TOTAL_LOANS:,}",

#                         color="#2563EB",

#                         component_id="total-loans"

#                     ),

#                     lg=3,
#                     md=6,
#                     sm=12

#                 ),

#                 dbc.Col(

#                     metric_card(

#                         icon="🚨",

#                         title="Detected Anomalies",

#                         value=f"{TOTAL_ANOMALIES:,}",

#                         color="#EF4444",

#                         component_id="total-anomalies"

#                     ),

#                     lg=3,
#                     md=6,
#                     sm=12

#                 ),

#                 dbc.Col(

#                     metric_card(

#                         icon="⚠️",

#                         title="Strong Anomalies",

#                         value=f"{STRONG_ANOMALIES:,}",

#                         color="#F59E0B",

#                         component_id="strong-anomalies"

#                     ),

#                     lg=3,
#                     md=6,
#                     sm=12

#                 ),

#                 dbc.Col(

#                     metric_card(

#                         icon="📊",

#                         title="Anomaly Detection Rate",

#                         value=f"{DETECTION_RATE:.1f}%",

#                         color="#10B981",

#                         component_id="coverage-rate"

#                     ),

#                     lg=3,
#                     md=6,
#                     sm=12

#                 ),

#             ],

#             className="g-3 mb-4"

#         ),

#                 dbc.Alert(

#             [

#                 html.Div(

#                     [

#                         html.I(
#                             className="bi bi-info-circle-fill me-2"
#                         ),

#                         html.Strong(
#                             "Anomaly Detection Summary"
#                         )

#                     ],

#                     className="mb-2"

#                 ),

#                 html.Div(

#                     [

#                         html.Span(
#                             f"Strong: {summary['strong_anomalies']:,}"
#                         ),

#                         html.Span("  |  "),

#                         html.Span(
#                             f"Moderate: {summary['moderate_anomalies']:,}"
#                         ),

#                         html.Span("  |  "),

#                         html.Span(
#                             f"Weak: {summary['weak_anomalies']:,}"
#                         ),

#                         html.Span("  |  "),

#                         html.Span(
#                             f"Detection Coverage: {DETECTION_RATE:.1f}%"
#                         )

#                     ]

#                 )

#             ],

#             color="light",

#             className="shadow-sm border-0"

#         ),

#         dbc.Card(

#             dbc.CardBody(

#                 [

#                     html.H4(
#                         "Anomaly Landscape Explorer",
#                         className="fw-bold mb-3"
#                     ),

#                     dbc.Row(

#                         [

#                             dbc.Col(

#                                 [

#                                     html.Label("X-Axis"),

#                                     dcc.Dropdown(

#                                         id="scatter-x",

#                                         value="annual_inc",

#                                         clearable=False,

#                                         options=[

#                                             {
#                                                 "label":"Annual Income",
#                                                 "value":"annual_inc"
#                                             },

#                                             {
#                                                 "label":"Loan Amount",
#                                                 "value":"loan_amnt"
#                                             },

#                                             {
#                                                 "label":"FICO Score",
#                                                 "value":"fico_range_low"
#                                             },

#                                             {
#                                                 "label":"Debt-to-Income Ratio",
#                                                 "value":"dti"
#                                             },

#                                             {
#                                                 "label":"Recoveries",
#                                                 "value":"recoveries"
#                                             }

#                                         ]

#                                     )

#                                 ],

#                                 md=3

#                             ),

#                             dbc.Col(

#                                 [

#                                     html.Label("Y-Axis"),

#                                     dcc.Dropdown(

#                                         id="scatter-y",

#                                         value="loan_amnt",

#                                         clearable=False,

#                                         options=[

#                                             {
#                                                 "label":"Annual Income",
#                                                 "value":"annual_inc"
#                                             },

#                                             {
#                                                 "label":"Loan Amount",
#                                                 "value":"loan_amnt"
#                                             },

#                                             {
#                                                 "label":"FICO Score",
#                                                 "value":"fico_range_low"
#                                             },

#                                             {
#                                                 "label":"Debt-to-Income Ratio",
#                                                 "value":"dti"
#                                             },

#                                             {
#                                                 "label":"Recoveries",
#                                                 "value":"recoveries"
#                                             }

#                                         ]

#                                     )

#                                 ],

#                                 md=3

#                             ),

#                             dbc.Col(

#                                 [

#                                     html.Label("Category"),

#                                     dcc.Dropdown(

#                                         id="scatter-category",

#                                         value="All",

#                                         clearable=False,

#                                         options=[

#                                             {
#                                                 "label":"All",
#                                                 "value":"All"
#                                             },

#                                             {
#                                                 "label":"Weak anomaly",
#                                                 "value":"Weak anomaly"
#                                             },

#                                             {
#                                                 "label":"Moderate anomaly",
#                                                 "value":"Moderate anomaly"
#                                             },

#                                             {
#                                                 "label":"Strong anomaly",
#                                                 "value":"Strong anomaly"
#                                             }

#                                         ]

#                                     )

#                                 ],

#                                 md=3

#                             ),

#                             dbc.Col(

#                                 [

#                                     html.Label("Detected By"),

#                                     dcc.Dropdown(

#                                         id="scatter-methods",

#                                         value="All",

#                                         clearable=False,

#                                         options=[

#                                             {
#                                                 "label":"All",
#                                                 "value":"All"
#                                             },

#                                             {
#                                                 "label":"1 Method",
#                                                 "value":1
#                                             },

#                                             {
#                                                 "label":"2 Methods",
#                                                 "value":2
#                                             },

#                                             {
#                                                 "label":"3 Methods",
#                                                 "value":3
#                                             }

#                                         ]

#                                     )

#                                 ],

#                                 md=3

#                             )

#                         ],

#                         className="g-3"

#                     ),

#                     html.Br(),

#                     dbc.Row(

#                         [

#                             dbc.Col(

#                                 html.Div(

#                                     id="scatter-counter",

#                                     className="text-muted fw-semibold"

#                                 )

#                             ),

#                             dbc.Col(

#                                 dbc.Button(

#                                     "Reset Explorer",

#                                     id="reset-scatter",

#                                     color="secondary",

#                                     outline=True,

#                                     size="sm"

#                                 ),

#                                 width="auto"

#                             )

#                         ],

#                         className="mb-3 align-items-center"

#                     ),

#                     dcc.Graph(
#                         id="anomaly-scatter",
#                         figure=create_anomaly_scatter(
#                             anomaly_scatter,
#                             "annual_inc",
#                             "loan_amnt"
#                         ),
#                         config={"displayModeBar": False}
#                     ), 

#                     dbc.Alert(
#                         [
#                             html.Strong("How to interpret this visualization"),
#                             html.Br(),
#                             html.Span(
#                                 "Each point represents one borrower. "
#                                 "Points located farther from dense borrower clusters are more likely "
#                                 "to represent unusual lending profiles. "
#                                 "Colors indicate anomaly severity, while the filters allow investigation "
#                                 "of different anomaly categories and detection agreement."
#                             )
#                         ],
#                         color="info",
#                         className="mt-3 mb-0"
#                     ),

#                 ]

#             ),

#             className="shadow-sm border-0"

#         ),

#         dbc.Card(

#             dbc.CardBody(

#                 [

#                     html.H4(
#                         "Detection Method Comparison",
#                         className="fw-bold mb-3"
#                     ),

#                     dbc.Row(
#                         [
#                             dbc.Col(
#                                 [
#                                     html.Label("Anomaly Category"),

#                                     dcc.Dropdown(
#                                         id="method-category",
#                                         clearable=False,
#                                         value="All",
#                                         options=[
#                                             {"label":"All", "value":"All"},
#                                             {"label":"Weak anomaly", "value":"Weak anomaly"},
#                                             {"label":"Moderate anomaly", "value":"Moderate anomaly"},
#                                             {"label":"Strong anomaly", "value":"Strong anomaly"}
#                                         ]
#                                     )
#                                 ],
#                                 md=4
#                             )
#                         ],

#                         className="mb-3"

#                     ),

#                     dcc.Graph(
#                         id="method-chart",
#                         config={"displayModeBar": False}
#                     ),

#                     html.Br(),

#                     html.Div(

#                         id="method-insight"

#                     ), 

#                 ]

#             ),

#             className="shadow-sm border-0"

#         ), 

#         dbc.Card(

#             dbc.CardBody(

#                 [

#                     html.H4(
#                         "Top Investigated Anomalies",
#                         className="fw-bold mb-3"
#                     ),

#                     dbc.Row(

#                         [

#                             dbc.Col(

#                                 [

#                                     html.Label("Business Reason"),

#                                     dcc.Dropdown(

#                                         id="anomaly-reason",

#                                         value="All",

#                                         clearable=False,

#                                         options=[

#                                             {
#                                                 "label": "All",
#                                                 "value": "All"
#                                             },

#                                             *[
#                                                 {
#                                                     "label": i,
#                                                     "value": i
#                                                 }

#                                                 for i in sorted(
#                                                     top10_anomalies[
#                                                         "business_reason"
#                                                     ].unique()
#                                                 )

#                                             ]

#                                         ]

#                                     )

#                                 ],

#                                 md=5

#                             )

#                         ],

#                         className="mb-3"

#                     ),

#                     html.Div(

#                         id="top-anomaly-cards"

#                     )

#                 ]

#             ),

#             className="shadow-sm border-0"

#         ),

#         dbc.Alert(

#             [

#                 html.Div(

#                     [

#                         html.I(
#                             className="bi bi-lightbulb-fill"
#                         ),

#                         html.Strong(
#                             "Anomaly Score Explanation"
#                         )

#                     ],

#                     className="mb-2"

#                 ),

#                 html.P(

#                     "Anomaly score generated by Isolation Forest. "
#                     "Lower values indicate borrower profiles that are more unusual "
#                     "compared with typical portfolio behaviour.",

#                     className="mb-0"

#                 )

#             ],

#             color="info",

#             className="mt-3 shadow-sm border-0"

#         ),

#         dbc.Card(

#             dbc.CardBody(

#                 [

#                     html.H4(
#                         "Investigation Queue",
#                         className="fw-bold mb-3"
#                     ),

#                     dbc.Row(

#                         [

#                             dbc.Col(

#                                 [

#                                     html.Label(
#                                         "Investigation Type",
#                                         className="fw-semibold"
#                                     ),

#                                     dbc.RadioItems(

#                                         id="investigation-type",

#                                         value="risk",

#                                         options=[

#                                             {
#                                                 "label": "🚨 Potential Risk Signals",
#                                                 "value": "risk"
#                                             },

#                                             {
#                                                 "label": "💼 Rare Legitimate Cases",
#                                                 "value": "legitimate"
#                                             },

#                                             {
#                                                 "label": "🗂 Data Quality Review",
#                                                 "value": "quality"
#                                             }

#                                         ],

#                                         className="mt-2"

#                                     )

#                                 ],

#                                 md=4

#                             ),


#                             dbc.Col(

#                                 html.Div(

#                                     id="investigation-panel"

#                                 ),

#                                 md=8

#                             )

#                         ]

#                     )

#                 ]

#             ),

#             className="shadow-sm border-0 mt-4"

#         ), 

#         dbc.Card(

#             dbc.CardBody(

#                 [

#                     html.H4(
#                         "Key Drivers of Anomalous Behaviour",
#                         className="fw-bold mb-3"
#                     ),

#                     html.P(
#                         "Features with the largest differences between anomalous and normal borrowers.",
#                         className="text-muted"
#                     ),

#                     dcc.Dropdown(

#                         id="feature-top-n",

#                         value=10,

#                         clearable=False,

#                         options=[

#                             {
#                                 "label":"Top 5 Features",
#                                 "value":5
#                             },

#                             {
#                                 "label":"Top 10 Features",
#                                 "value":10
#                             },

#                             {
#                                 "label":"Top 15 Features",
#                                 "value":15
#                             }

#                         ]

#                     ),

#                     dcc.Graph(
#                         id="feature-difference-chart"
#                     )

#                 ]

#             ),

#             className="shadow-sm border-0 mt-4"

#         ), 

#         dbc.Card(

#             dbc.CardBody(

#                 [

#                     html.H4(
#                         "Anomaly Severity Distribution",
#                         className="fw-bold mb-3"
#                     ),

#                     html.P(

#                         "Distribution of detected anomalies based on severity classification.",

#                         className="text-muted"

#                     ),

#                     dcc.Graph(

#                         id="anomaly-category-chart",

#                         figure=create_anomaly_category_chart(
#                             anomaly_categories
#                         ),

#                         config={
#                             "displayModeBar": False
#                         }

#                     ),

#                     dbc.Alert(

#                         [

#                             html.Strong(
#                                 "Interpretation"
#                             ),

#                             html.Br(),

#                             html.Span(

#                                 "The distribution highlights how anomaly cases "
#                                 "are distributed across severity levels. Strong anomalies "
#                                 "represent the highest priority cases requiring further review, "
#                                 "while weak anomalies indicate less extreme deviations."

#                             )

#                         ],

#                         color="info",

#                         className="mt-3 mb-0"

#                     )

#                 ]

#             ),

#             className="shadow-sm border-0 mt-4"

#         ), 

#         dbc.Card(

#             dbc.CardBody(

#                 [

#                     html.H4(
#                         "Key Findings",
#                         className="fw-bold mb-3"
#                     ),

#                     html.Ul(

#                         [

#                             html.Li(
#                                 "🚨 4.2% of borrowers were identified as anomalous based on combined anomaly detection techniques."
#                             ),

#                             html.Li(
#                                 "📌 Recoveries and recent credit behaviour showed the largest differences between anomalous and typical borrowers."
#                             ),

#                             html.Li(
#                                 "🔍 Isolation Forest detected the strongest multivariate anomalies by identifying unusual borrower profiles."
#                             ),

#                             html.Li(
#                                 "⚠️ Detected anomalies should be treated as investigation priorities rather than automatic rejection decisions."
#                             )

#                         ],

#                         className="mb-0"

#                     )

#                 ]

#             ),

#             className="shadow-sm border-0 mt-4"

#         ), 

#         dbc.Card(

#             dbc.CardBody(

#                 [

#                     html.H4(
#                         "Customer Segment × Anomaly Explorer",
#                         className="fw-bold mb-3"
#                     ),

#                     html.P(

#                         "Explore how anomaly severity is distributed across customer segments.",

#                         className="text-muted"

#                     ),

#                     dbc.Row(

#                         [

#                             dbc.Col(

#                                 [

#                                     html.Label("Customer Segment"),

#                                     dcc.Dropdown(

#                                         id="cluster-dropdown",

#                                         value=0,

#                                         clearable=False,

#                                         options=[

#                                             {
#                                                 "label":f"Cluster {i}",
#                                                 "value":i
#                                             }

#                                             for i in sorted(
#                                                 cluster_summary["cluster"].unique()
#                                             )

#                                         ]

#                                     )

#                                 ],

#                                 md=3

#                             )

#                         ],

#                         className="mb-3"

#                     ),

#                     dbc.Row(

#                         [

#                             dbc.Col(

#                                 dcc.Graph(

#                                     id="cluster-stacked-bar",

#                                     config={
#                                         "displayModeBar":False
#                                     }

#                                 ),

#                                 md=7

#                             ),

#                             dbc.Col(

#                                 dcc.Graph(

#                                     id="cluster-pie",

#                                     config={
#                                         "displayModeBar":False
#                                     }

#                                 ),

#                                 md=5

#                             )

#                         ]

#                     ),

#                     html.Br(),

#                     dash_table.DataTable(

#                         id="cluster-table",

#                         page_size=10,

#                         sort_action="native",

#                         filter_action="native",

#                         style_table={

#                             "overflowX":"auto"

#                         },

#                         style_cell={

#                             "textAlign":"center"

#                         }

#                     )

#                 ]

#             ),

#             className="shadow-sm border-0 mt-4"

#         ),
#     ]
# )

layout = html.Div([
    hero,
    html.H3("Anomaly loading...")
])

print("=== ANOMALY PAGE LOADED")