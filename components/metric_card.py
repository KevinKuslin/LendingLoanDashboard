from dash import html
import dash_bootstrap_components as dbc


def metric_card(
    icon,
    title,
    value,
    color="#2563EB", 
    component_id=None
):
    """
    Reusable KPI metric card.
    """

    return dbc.Card(

        dbc.CardBody(

            [

                html.Div(

                    icon,

                    className="metric-icon",

                    style={

                        "background": color

                    }

                ),

                html.H2(

                    value,
                    id=component_id,

                    className="metric-value"

                ),

                html.Div(

                    title,

                    className="metric-title"

                )

            ]

        ),

        className="metric-card"

    )