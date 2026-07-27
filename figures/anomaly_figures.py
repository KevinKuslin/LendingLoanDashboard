import plotly.express as px

def apply_theme(fig):

    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="#F8FAFC",
        plot_bgcolor="white",
        font=dict(
            family="Inter",
            color="#0F172A"
        ),
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    return fig

# =====================================
# Risk Distribution
# =====================================

def create_risk_distribution_chart(df):

    fig = px.pie(

        df,

        names="category",

        values="count",

        hole=0.6

    )


    fig.update_layout(
        title="Anomaly Risk Distribution"
    )


    return apply_theme(fig)




# =====================================
# Detection Agreement
# =====================================

def create_detection_method_chart(df):

    fig = px.bar(

        df,

        x="method",

        y="count",

        text_auto=True

    )


    fig.update_layout(
        title="Detection Method Agreement"
    )


    return apply_theme(fig)




# =====================================
# Feature Difference
# =====================================

def create_anomaly_feature_chart(df):

    fig = px.bar(

        df,

        x="difference",

        y="feature",

        orientation="h",

        text_auto=".2f"

    )


    fig.update_layout(
        title="Main Anomaly Drivers"
    )


    return apply_theme(fig) 


def create_anomaly_scatter(df, x_axis, y_axis):

    MAX_POINTS = 50_000

    if len(df) > MAX_POINTS:
        df = df.sample(
            n=MAX_POINTS,
            random_state=42
        )

    fig = px.scatter(

        df,

        x=x_axis,

        y=y_axis,

        color="category",

        hover_data={
            "annual_inc": ":.2f",
            "loan_amnt": ":.2f",
            "fico_range_low": True,
            "dti": ":.2f",
            "recoveries": ":.2f",
            "methods_detected": True,
        },

        color_discrete_map={
            "Normal": "#CBD5E1",
            "Weak anomaly": "#3B82F6",
            "Moderate anomaly": "#F59E0B",
            "Strong anomaly": "#EF4444",
        },

        category_orders={
            "category": [
                "Normal",
                "Weak anomaly",
                "Moderate anomaly",
                "Strong anomaly",
            ]
        }

    )

    fig.update_traces(

        marker=dict(
            size=5,
            opacity=0.35
        )

    )

    fig.update_layout(

        title=f"{x_axis.replace('_', ' ').title()} vs {y_axis.replace('_', ' ').title()}",

        legend_title="Category"

    )

    return apply_theme(fig) 

# =====================================
# Detection Agreement
# =====================================

def create_method_chart(df, category="All"):

    df = df.copy()

    # ------------------------
    # Filter category
    # ------------------------

    if category != "All":

        df = df[
            df["category"] == category
        ]

    # ------------------------
    # Count detections
    # ------------------------

    plot_df = df[
        ["IQR", "ZScore", "IsolationForest"]
    ].sum().reset_index()

    plot_df.columns = [
        "method",
        "count"
    ]

    plot_df["percentage"] = (
        plot_df["count"]
        / len(df)
        * 100
    ).round(1)

    color_map = {

        "IQR": "#2563EB",

        "ZScore": "#F59E0B",

        "IsolationForest": "#EF4444"

    }

    fig = px.bar(

        plot_df,

        x="method",

        y="count",

        text_auto=True

    )

    fig.update_traces(

        marker_color=[
            color_map[m]
            for m in plot_df["method"]
        ],

        customdata=plot_df[["percentage"]],

        hovertemplate=
        "<b>%{x}</b><br>"
        "Detected Loans: %{y:,}<br>"
        "Within Category: %{customdata[0]}%<extra></extra>"

    )

    fig.update_layout(

        title=f"Detection Methods ({category})",

        xaxis_title="Detection Method",

        yaxis_title="Detected Loans"

    )

    return apply_theme(fig)


def create_anomaly_category_chart(df):

    fig = px.pie(

        df,

        names="category",

        values="count",

        hole=0.55,

        title="Distribution of Anomaly Severity"

    )

    fig.update_traces(

        textinfo="percent+label",

        hovertemplate=
        "<b>%{label}</b><br>"
        "Cases: %{value:,}<br>"
        "Percentage: %{percent}"

    )

    fig.update_layout(

        showlegend=True,

        margin=dict(
            t=50,
            b=20,
            l=20,
            r=20
        ),

        legend_title_text="Severity"

    )

    return fig

def create_cluster_stacked_bar(df):

    fig = px.bar(

        df,

        x="cluster",

        y="count",

        color="Category",

        barmode="stack",

        color_discrete_map={

            "Normal":"#10B981",
            "Weak anomaly":"#FACC15",
            "Moderate anomaly":"#FB923C",
            "Strong anomaly":"#EF4444"

        }

    )

    fig.update_layout(

        template="plotly_white",

        xaxis_title="Customer Segment",

        yaxis_title="Borrowers",

        legend_title="Category"

    )

    return fig

def create_cluster_pie(df):

    fig = px.pie(

        df,

        names="Category",

        values="count",

        hole=.45,

        color="Category",

        color_discrete_map={

            "Normal":"#10B981",
            "Weak anomaly":"#FACC15",
            "Moderate anomaly":"#FB923C",
            "Strong anomaly":"#EF4444"

        }

    )

    fig.update_layout(

        template="plotly_white"

    )

    return fig