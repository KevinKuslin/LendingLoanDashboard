from dash import callback, Input, Output, html, ctx 

from utils.data_loader import (
    executive_summary, 
    anomaly_method_counts, 
    anomaly_categories, 
    anomaly_scatter, 
    anomaly_feature_difference, 
    top10_anomalies, 
    anomaly_method_breakdown
)

from components.insight_card import insight_card

from utils.anomaly_method_insights import METHOD_INSIGHTS

from figures.anomaly_figures import (
    create_anomaly_scatter, 
    create_anomaly_feature_chart, 
    create_method_chart
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