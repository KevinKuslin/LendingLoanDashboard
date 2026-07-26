from dash import html
import dash_bootstrap_components as dbc


def pattern_insight_card(item):

    return dbc.Card(

        dbc.CardBody(

            [

                html.H4(
                    f"{item['icon']} {item['title']}",
                    className="fw-bold"
                ),

                dbc.Badge(
                    item["category"],
                    color="primary",
                    className="mb-3"
                ),

                html.H6(
                    "Key Finding",
                    className="fw-bold"
                ),

                html.P(
                    item["insight"]
                ),


                html.H6(
                    "Recommendation",
                    className="fw-bold"
                ),

                html.P(
                    item["recommendation"]
                )

            ]

        ),

        className="shadow-sm border-0 h-100"

    )