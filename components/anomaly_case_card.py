from dash import html
import dash_bootstrap_components as dbc

from utils.anomaly_explanations import (
    generate_anomaly_explanation,
    determine_business_category,
)


def anomaly_case_card(row):

    category, color, icon = determine_business_category(row)

    score = abs(row["anomaly_score"])

    if score >= 0.135:
        severity = "Very High"

    elif score >= 0.125:
        severity = "High"

    else:
        severity = "Moderate"

    if category == "Potential Risk Signal":
        insight_text = (
            "The borrower exhibits financial characteristics that are statistically unusual "
            "and may indicate elevated lending or collection risk."
        )
    elif category == "Rare Legitimate Case":
        insight_text = (
            "Although this borrower appears unusual compared with the overall portfolio, "
            "the pattern may simply represent an uncommon but legitimate customer profile."
        )
    else:
        insight_text = (
            "The anomaly is primarily driven by unusual attribute combinations and should "
            "be reviewed to rule out data quality issues."
        )

    reasons = generate_anomaly_explanation(row)

    insight_text = (
        "This borrower was identified because multiple financial characteristics "
        "deviate from the normal Lending Club borrower population."
    )

    if category == "Potential Risk Signal":

        recommendation = (
            "Review borrower history and verify supporting financial documents."
        )

    elif category == "Rare Legitimate Case":

        recommendation = (
            "Compare this borrower with applicants of similar income before making a lending decision."
        )

    else:

        recommendation = (
            "Perform manual review to determine whether this represents a genuine customer or a data-quality issue."
        )

    return dbc.Card(

        dbc.CardBody(

            [

                dbc.Row(

                    [

                        dbc.Col(

                            [

                                html.H5(
                                    f"Borrower #{row['index']}",
                                    className="fw-bold mb-1"
                                ),

                                dbc.Badge(
                                    f"{icon} {category}",
                                    color=color,
                                    className="mb-2"
                                )

                            ],

                            width=8

                        ),

                        dbc.Col(

                            html.Div(

                                [

                                    html.Div(
                                        "Anomaly Score",
                                        className="small text-muted"
                                    ),

                                    html.H4(
                                        f"{score:.3f}",
                                        className="fw-bold text-danger mb-2"
                                    ),

                                    dbc.Badge(
                                        severity,
                                        color=(
                                            "danger"
                                            if severity == "Very High"
                                            else "warning"
                                            if severity == "High"
                                            else "primary"
                                        ),
                                        className="px-2 py-1"
                                    )

                                ],

                                className="text-end"

                            ),

                            width=4

                        )

                    ],

                    className="mb-3"

                ),

                html.Hr(),

                html.H6(
                    "Detection Summary",
                    className="fw-bold"
                ),

                html.Ul(

                    [
                        html.Li(reason)
                        for reason in reasons
                    ],

                    className="mb-3"

                ),

                html.H6(
                    "Business Insight",
                    className="fw-bold"
                ),

                html.P(
                    insight_text,
                    className="text-muted"
                ), 

                html.H6(
                    "Recommendation",
                    className="fw-bold mt-3"
                ),

                dbc.Alert(

                    recommendation,

                    color=color,

                    className="mb-0"

                ),

            ]

        ),

        className="shadow-sm border-0 h-100"

    )