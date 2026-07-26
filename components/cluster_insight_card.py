from dash import html
import dash_bootstrap_components as dbc


def cluster_insight_card(

    title,
    description,
    recommendation,
    color

):

    # Split bullet list automatically
    lines = description.split("\n")

    population = lines[0]

    bullets = lines[1:]


    return dbc.Card(

        dbc.CardBody(

            [

                # ==========================
                # HEADER
                # ==========================

                html.Div(

                    [

                        html.Div(

                            style={

                                "width": "10px",

                                "backgroundColor": color,

                                "borderRadius": "10px",

                                "marginRight": "18px"

                            }

                        ),

                        html.Div(

                            [

                                html.H4(

                                    title,

                                    className="fw-bold mb-1"

                                ),

                                html.P(

                                    population,

                                    className="text-muted mb-0"

                                )

                            ],

                            style={"flex": 1}

                        )

                    ],

                    style={

                        "display": "flex",

                        "alignItems": "stretch",

                        "marginBottom": "18px"

                    }

                ),

                html.Hr(),

                # ==========================
                # CHARACTERISTICS
                # ==========================

                html.H6(

                    "Key Characteristics",

                    className="fw-bold mt-3"

                ),

                html.Div(

                    [

                        dbc.Badge(

                            item.replace("•", "").strip(),

                            color="light",

                            text_color="dark",

                            className="me-2 mb-2 p-2"

                        )

                        for item in bullets

                        if item.strip()

                    ]

                ),

                html.Br(),

                # ==========================
                # BUSINESS STRATEGY
                # ==========================

                dbc.Card(

                    dbc.CardBody(

                        [

                            html.Div(

                                [

                                    html.Span(

                                        "💼",

                                        style={

                                            "fontSize": "24px",

                                            "marginRight": "10px"

                                        }

                                    ),

                                    html.Div(

                                        [

                                            html.Div(

                                                "Recommended Strategy",

                                                className="fw-bold"

                                            ),

                                            html.Div(

                                                recommendation,

                                                style={

                                                    "fontSize": "14px",

                                                    "color": "#6B7280"

                                                }

                                            )

                                        ]

                                    )

                                ],

                                style={

                                    "display": "flex",

                                    "alignItems": "center"

                                }

                            )

                        ]

                    ),

                    style={

                        "backgroundColor": "#F8FAFC",

                        "border": "none"

                    }

                )

            ]

        ),

        className="shadow-sm border-0 h-100",

        style={

            "borderRadius": "18px",

            "transition": "0.25s",

            "minHeight": "360px"

        }

    )