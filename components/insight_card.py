from dash import html
import dash_bootstrap_components as dbc


def insight_card(
    title,
    description,
    icon="💡",
    color="#2563EB",
    card_id=None
):

    card = dbc.Card(

        dbc.CardBody(

            [

                html.Div(

                    [

                        html.Div(
                            icon,
                            className="insight-icon",
                            style={
                                "backgroundColor": color
                            }
                        ),

                        html.Div(

                            [

                                html.H5(
                                    title,
                                    className="insight-title"
                                ),

                                html.P(
                                    description,
                                    className="insight-description"
                                )

                            ],

                            className="insight-content"

                        )

                    ],

                    className="insight-row"

                )

            ]

        ),

        className="insight-card"

    )


    if card_id is not None:
        card.id = card_id

    return card