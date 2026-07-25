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