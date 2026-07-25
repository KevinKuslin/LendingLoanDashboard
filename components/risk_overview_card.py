from dash import html
import dash_bootstrap_components as dbc


def risk_overview_card(
    icon,
    title,
    value,
    color
):

    return dbc.Card(

        dbc.CardBody(

            html.Div(

                [

                    html.Div(

                        icon,

                        className="risk-icon",

                        style={
                            "backgroundColor": color
                        }

                    ),

                    html.Div(

                        [

                            html.H6(

                                title,

                                className="risk-title"

                            ),

                            html.H3(

                                value,

                                className="risk-value"

                            )

                        ]

                    )

                ],

                className="d-flex align-items-center gap-3"

            )

        ),

        className="dashboard-card h-100"

    )