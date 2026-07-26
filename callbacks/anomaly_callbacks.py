from dash import callback, Input, Output

from utils.data_loader import (
    executive_summary, 
    anomaly_method_counts, 
    anomaly_categories, 
    anomaly_scatter, 
    anomaly_feature_difference, 
    top10_anomalies
)

from figures.anomaly_figures import (
    create_anomaly_scatter, 
    create_anomaly_feature_chart
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