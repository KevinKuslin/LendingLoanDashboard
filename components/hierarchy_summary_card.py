from dash import html
import dash_bootstrap_components as dbc


def hierarchy_summary_card(
    group,
    optimal_k,
    silhouette
):

    descriptions = {

        "loan_cluster":
            "Groups borrowers based on loan characteristics such as amount, interest rate, and loan terms.",

        "credit_history_cluster":
            "Groups borrowers according to credit quality, account history, and previous borrowing behaviour.",

        "risk_behavior_cluster":
            "Identifies borrower risk patterns using financial stress and delinquency indicators.",

        "payment_outcome_cluster":
            "Segments borrowers according to repayment performance and loan outcomes."

    }


    return dbc.Card(

        [

            dbc.CardBody(

                [

                    html.Div(

                        group.replace("_", " ").title(),

                        className="text-uppercase text-muted small"

                    ),


                    html.H2(

                        f"{optimal_k}",

                        className="fw-bold mb-0"

                    ),


                    html.P(

                        "Optimal Clusters",

                        className="text-muted"

                    ),


                    html.Hr(),


                    html.P(

                        [

                            html.Strong("Silhouette Score: "),

                            f"{silhouette:.3f}"

                        ]

                    ),


                    html.P(

                        descriptions.get(
                            group,
                            "Feature-based borrower segmentation."
                        ),

                        className="small"

                    )

                ]

            )

        ],


        className="dashboard-card h-100"

    )