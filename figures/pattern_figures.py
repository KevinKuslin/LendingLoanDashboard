import plotly.express as px


import plotly.express as px


def create_support_confidence_scatter(
    df,
    min_lift=1,
    if_filter=None,
    then_filter=None,
    color_by="lift",
    size_by="lift",
):

    plot_df = df.copy()

    if if_filter:
        plot_df = plot_df[
            plot_df["IF"] == if_filter
        ]

    if then_filter:
        plot_df = plot_df[
            plot_df["THEN"] == then_filter
        ]

    plot_df = plot_df[
        plot_df["lift"] >= min_lift
    ]

    fig = px.scatter(

        plot_df,

        x="support",
        y="confidence",

        color=color_by,
        size=size_by,

        size_max=30,

        color_continuous_scale="Turbo",

        hover_data={

            "IF":True,
            "THEN":True,
            "support":":.2%",
            "confidence":":.2%",
            "lift":":.2f"

        }

    )

    fig.update_traces(

        marker=dict(

            opacity=0.82,

            line=dict(
                width=1,
                color="white"
            )

        ),

        hovertemplate=

        "<b>%{customdata[0]}</b><br><br>"

        "<b>THEN</b><br>"
        "%{customdata[1]}<br><br>"

        "<b>Support</b><br>"
        "%{x:.2%}<br><br>"

        "<b>Confidence</b><br>"
        "%{y:.2%}<br><br>"

        "<b>Lift</b><br>"
        "%{marker.color:.2f}×"

        "<extra></extra>"

    )

    fig.update_layout(

        template="plotly_white",

        height=600,

        xaxis_title="Support",

        yaxis_title="Confidence",

        coloraxis_colorbar_title="Lift",

        margin=dict(
            l=30,
            r=30,
            t=60,
            b=30
        )

    )

    # ----------------------------
    # Reference Lines
    # ----------------------------

    fig.add_vline(

        x=0.05,

        line_dash="dash",

        line_color="gray",

        opacity=0.5

    )

    fig.add_hline(

        y=0.50,

        line_dash="dash",

        line_color="gray",

        opacity=0.5

    )

    return fig