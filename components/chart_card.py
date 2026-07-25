from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


def chart_card(title, figure, graph_id):

    if figure is None:

        figure = go.Figure()

        figure.update_layout(

            template="plotly_white",

            paper_bgcolor="#F8FAFC",

            plot_bgcolor="white",

            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),

            xaxis=dict(
                visible=False
            ),

            yaxis=dict(
                visible=False
            ),

            annotations=[

                dict(

                    text="Loading...",

                    x=0.5,

                    y=0.5,

                    showarrow=False,

                    font=dict(
                        size=18,
                        color="gray"
                    )

                )

            ]

        )

    return dbc.Card(

        [

            dbc.CardHeader(

                html.H5(
                    title,
                    className="chart-title"
                )

            ),

            dbc.CardBody(

                dcc.Graph(

                    id=graph_id,

                    figure=figure,

                    config={

                        "displayModeBar": False,

                        "responsive": True

                    },

                    style={

                        "height": "380px"

                    }

                )

            )

        ],

        className="dashboard-card"

    )