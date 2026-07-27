from dash import callback, Input, Output, html, ctx 
import dash_bootstrap_components as dbc
import plotly.express as px 


from utils.data_loader import (
    executive_summary, 
    anomaly_method_counts, 
    anomaly_categories, 
    anomaly_scatter, 
    anomaly_feature_difference, 
    top10_anomalies, 
    anomaly_method_breakdown, 
    cluster_summary,
    cluster_category_summary,
    cluster_anomaly_cross_reference
)

from components.insight_card import insight_card
from components.anomaly_case_card import anomaly_case_card

from utils.anomaly_method_insights import METHOD_INSIGHTS
from utils.investigation_queue import INVESTIGATION_QUEUE

from figures.anomaly_figures import (
    create_anomaly_scatter, 
    create_anomaly_feature_chart, 
    create_method_chart, 
    create_cluster_stacked_bar,
    create_cluster_pie
)

@callback(

    Output(
        "anomaly-scatter",
        "figure"
    ),

    Output(
        "scatter-counter",
        "children"
    ),

    Input(
        "scatter-x",
        "value"
    ),

    Input(
        "scatter-y",
        "value"
    ),

    Input(
        "scatter-category",
        "value"
    ),

    Input(
        "scatter-methods",
        "value"
    )

)

def update_anomaly_scatter(

    x_axis,
    y_axis,
    category,
    methods

):

    df = anomaly_scatter.copy()

    if category != "All":

        df = df[
            df["category"] == category
        ]

    if methods != "All":

        df = df[
            df["methods_detected"] == methods
        ]

    total_points = len(df)
    MAX_POINTS = 50_000
    shown_points = min(
        total_points,
        MAX_POINTS
    )
        
    return (
        create_anomaly_scatter(
            df,
            x_axis,
            y_axis
        ),
        f"Showing {shown_points:,} of {total_points:,} borrowers"
    )

# =====================================================
# Reset Scatter Explorer
# =====================================================

@callback(

    Output("scatter-x", "value"),
    Output("scatter-y", "value"),
    Output("scatter-category", "value"),
    Output("scatter-methods", "value"),

    Input("reset-scatter", "n_clicks"),

    prevent_initial_call=True

)

def reset_scatter(_):

    return (

        "annual_inc",
        "loan_amnt",
        "All",
        "All"

    )

METHOD_INFO = {

    "All":
        (
            "Comparison",
            "Shows how many borrowers were flagged by each anomaly detection algorithm."
        ),

    "IQR":
        (
            "IQR",
            "Detects extreme values independently within each feature. It is highly sensitive to univariate outliers and therefore identifies the largest number of anomalies."
        ),

    "Z-Score":
        (
            "Z-Score",
            "Measures how far a borrower deviates from the population mean. Effective when variables approximately follow a normal distribution."
        ),

    "Isolation Forest":
        (
            "Isolation Forest",
            "Uses machine learning to isolate unusual borrower profiles across multiple features simultaneously, making it effective for detecting multivariate anomalies."
        )

}

@callback(
    Output("method-chart", "figure"),
    Output("method-insight", "children"),
    Input("method-category", "value")
)

def update_method_chart(category):

    info = METHOD_INSIGHTS.get(
        category,
        METHOD_INSIGHTS["All"]
    )

    return (
        create_method_chart(
            anomaly_method_breakdown,
            category
        ),

        insight_card(
            title=f"{info['icon']} {info['title']}",
            description=info["text"],
            color="#2563EB"
        )
    )

@callback(
    Output("top-anomaly-cards", "children"),
    Input("anomaly-reason", "value")
)
def update_top_anomalies(reason):

    df = top10_anomalies.copy()

    if reason != "All":
        df = df[
            df["business_reason"] == reason
        ]

    if df.empty:

        return dbc.Alert(

            "No anomalies match the selected reason.",

            color="secondary"

        )

    cards = [

        dbc.Col(

            anomaly_case_card(row),

            lg=6,
            md=12

        )

        for _, row in df.iterrows()

    ]

    return dbc.Row(

        cards,

        className="g-4"

    )

@callback(
    Output(
        "investigation-panel",
        "children"
    ),

    Input(
        "investigation-type",
        "value"
    )
)

def update_investigation_panel(queue_type):

    info = INVESTIGATION_QUEUE[queue_type]

    return dbc.Card(

        dbc.CardBody(

            [

                dbc.Row(

                    [

                        dbc.Col(

                            [

                                html.H5(
                                    info["title"],
                                    className="fw-bold mb-2"
                                ),

                                dbc.Badge(
                                    f"Priority: {info['priority']}",
                                    color=info["color"],
                                    className="mb-3"
                                ),

                            ],

                            md=6

                        ),

                    ]

                ),


                html.Hr(),


                html.H6(
                    "Business Impact",
                    className="fw-bold"
                ),

                html.P(
                    info["impact"],
                    className="text-muted"
                ),


                html.H6(
                    "Typical Indicators",
                    className="fw-bold mt-3"
                ),

                html.Ul(

                    [

                        html.Li(item)

                        for item in info["indicators"]

                    ]

                ),


                html.H6(
                    "Recommended Actions",
                    className="fw-bold mt-3"
                ),

                dbc.Alert(

                    html.Ul(

                        [

                            html.Li(action)

                            for action in info["actions"]

                        ]

                    ),

                    color=info["color"]

                )

            ]

        ),

        className="shadow-sm border-0"

    )

@callback(

    Output(
        "feature-difference-chart",
        "figure"
    ),

    Input(
        "feature-top-n",
        "value"
    )

)

def update_feature_difference(top_n):

    df = anomaly_feature_difference.head(top_n)

    fig = px.bar(

        df.sort_values(
            "difference"
        ),

        x="difference",

        y="feature",

        orientation="h",

        title="Most Influential Features Separating Anomalies"

    )


    return fig

@callback(

    Output("cluster-stacked-bar","figure"),

    Output("cluster-pie","figure"),

    Output("cluster-table","data"),

    Output("cluster-table","columns"),

    Input("cluster-dropdown","value")

)
def update_cluster_explorer(cluster):

    stacked = create_cluster_stacked_bar(

        cluster_category_summary

    )

    filtered = cluster_category_summary[

        cluster_category_summary.cluster == cluster

    ]

    pie = create_cluster_pie(

        filtered

    )

    severity_order = {
        "Strong anomaly": 3,
        "Moderate anomaly": 2,
        "Weak anomaly": 1,
        "Normal": 0
    }

    table = (
        cluster_anomaly_cross_reference[
            cluster_anomaly_cross_reference.cluster == cluster
        ]
        .assign(
            severity_rank=lambda d: d["Category"].map(severity_order)
        )
        .sort_values(
            by=["severity_rank", "methods_detected"],
            ascending=[False, False]
        )
        .drop(columns="severity_rank")
        [
            [
                "loan_amnt",
                "annual_inc",
                "fico_range_low",
                "int_rate",
                "Category",
                "methods_detected"
            ]
        ]
        .head(50)
    )

    return (

        stacked,

        pie,

        table.to_dict("records"),

        [

            {

                "name":i,

                "id":i

            }

            for i in table.columns

        ]

    )