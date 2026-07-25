import plotly.express as px


# ==========================================================
# Theme
# ==========================================================

def apply_anomaly_theme(fig):

    fig.update_layout(

        template="plotly_white",

        paper_bgcolor="#F8FAFC",

        plot_bgcolor="white",

        font=dict(

            family="Inter",

            color="#0F172A",

            size=13

        ),

        margin=dict(

            l=20,
            r=20,
            t=60,
            b=20

        ),

        hoverlabel=dict(

            bgcolor="white"

        )

    )


    return fig



# ==========================================================
# Risk Distribution
# Uses anomaly_categories.parquet
# Columns:
# category | count
# ==========================================================

def create_risk_distribution_chart(df):


    fig = px.pie(

        df,

        names="category",

        values="count",

        hole=0.60,

        color="category",

        color_discrete_map={

            "Normal": "#10B981",

            "Weak anomaly": "#3B82F6",

            "Moderate anomaly": "#F59E0B",

            "Strong anomaly": "#EF4444"

        }

    )


    fig.update_layout(

        title="Risk Distribution"

    )


    fig.update_traces(

        textinfo="percent",

        hovertemplate=

        "<b>%{label}</b><br>" +

        "%{value:,} loans"

    )


    return apply_anomaly_theme(fig)



# ==========================================================
# Detection Method Agreement
# Uses anomaly_method_counts.parquet
# Columns:
# method | count
# ==========================================================

def create_detection_method_chart(df):


    fig = px.bar(

        df,

        x="method",

        y="count",

        text="count",

        color="count",

        color_continuous_scale="Blues"

    )


    fig.update_layout(

        title="Anomaly Detection Agreement",

        coloraxis_showscale=False

    )


    fig.update_traces(

        hovertemplate=

        "Detection Methods: %{x}<br>" +

        "Loans: %{y:,}"

    )


    return apply_anomaly_theme(fig)



# ==========================================================
# Feature Difference
# Uses anomaly_feature_difference.parquet
# Columns:
# feature | difference
# ==========================================================

def create_anomaly_feature_chart(df):


    data = (

        df

        .sort_values(

            "difference",

            ascending=True

        )

    )


    fig = px.bar(

        data,

        x="difference",

        y="feature",

        orientation="h",

        text="difference",

        color="difference",

        color_continuous_scale="RdBu"

    )


    fig.update_layout(

        title="Main Anomaly Feature Differences",

        coloraxis_showscale=False

    )


    fig.update_traces(

        hovertemplate=

        "%{y}<br>" +

        "Difference: %{x:.2f}"

    )


    return apply_anomaly_theme(fig)