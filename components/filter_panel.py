from dash import html, dcc
import dash_bootstrap_components as dbc


def filter_panel(
    loan_status_options,
    grade_options,
    state_options,
    loan_min,
    loan_max,
):

    return dbc.Card(

        dbc.CardBody(

            [

                html.H4(
                    "🔎 Global Dashboard Filters",
                    className="mb-4 fw-bold"
                ),

                dbc.Row(

                    [

                        dbc.Col(

                            [

                                html.Label("Loan Status"),

                                dcc.Dropdown(

                                    id="loan-status-filter",

                                    options=[
                                        {
                                            "label": "All",
                                            "value": "All"
                                        }
                                    ] + [
                                        {
                                            "label": x,
                                            "value": x
                                        }
                                        for x in loan_status_options
                                    ],

                                    value="All",

                                    clearable=False

                                )

                            ],

                            md=4

                        ),

                        dbc.Col(

                            [

                                html.Label("Loan Grade"),

                                dcc.Dropdown(

                                    id="grade-filter",

                                    options=[
                                        {
                                            "label": "All",
                                            "value": "All"
                                        }
                                    ] + [
                                        {
                                            "label": x,
                                            "value": x
                                        }
                                        for x in grade_options
                                    ],

                                    value="All",

                                    clearable=False

                                )

                            ],

                            md=4

                        ),

                        dbc.Col(

                            [

                                html.Label("State"),

                                dcc.Dropdown(

                                    id="state-filter",

                                    options=[
                                        {
                                            "label": "All",
                                            "value": "All"
                                        }
                                    ] + [
                                        {
                                            "label": x,
                                            "value": x
                                        }
                                        for x in state_options
                                    ],

                                    value="All",

                                    clearable=False

                                )

                            ],

                            md=4

                        )

                    ]

                ),

                html.Br(),

                html.Label("Loan Amount"),

                dcc.RangeSlider(

                    id="loan-slider",

                    min=loan_min,

                    max=loan_max,

                    value=[loan_min, loan_max],

                    tooltip={
                        "always_visible": False
                    }

                ),

                html.Br(),

                dbc.Button(

                    "Reset Filters",

                    id="reset-button",

                    color="primary",

                    className="mt-3"

                )

            ]

        ),

        className="dashboard-card"

    )