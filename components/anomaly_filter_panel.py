from dash import html, dcc
import dash_bootstrap_components as dbc


def anomaly_filter_panel():

    return dbc.Card(

        dbc.CardBody(

            [

                html.H5(
                    "🔍 Anomaly Investigation",
                    className="mb-3"
                ),


                dbc.Row(

                    [

                        dbc.Col(

                            [

                                html.Label(
                                    "Risk Category"
                                ),

                                dcc.Dropdown(

                                    id="anomaly-category-filter",

                                    options=[

                                        {
                                            "label":"All",
                                            "value":"All"
                                        },

                                        {
                                            "label":"Strong",
                                            "value":"Strong anomaly"
                                        },

                                        {
                                            "label":"Moderate",
                                            "value":"Moderate anomaly"
                                        },

                                        {
                                            "label":"Weak",
                                            "value":"Weak anomaly"
                                        }

                                    ],

                                    value="All",

                                    clearable=False

                                )

                            ],

                            md=6

                        ),


                        dbc.Col(

                            [

                                html.Label(
                                    "Detection Agreement"
                                ),

                                dcc.Dropdown(

                                    id="anomaly-method-filter",

                                    options=[

                                        {
                                            "label":"All",
                                            "value":"All"
                                        },

                                        {
                                            "label":"1 Method",
                                            "value":1
                                        },

                                        {
                                            "label":"2 Methods",
                                            "value":2
                                        },

                                        {
                                            "label":"3 Methods",
                                            "value":3
                                        }

                                    ],

                                    value="All",

                                    clearable=False

                                )

                            ],

                            md=6

                        )

                    ]

                )

            ]

        ),

        className="dashboard-card"

    )