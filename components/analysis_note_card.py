from dash import html
import dash_bootstrap_components as dbc


def analysis_note_card():

    return dbc.Card(

        [

            dbc.CardHeader(

                html.H5(
                    "Why Hierarchical Clustering Is Used",
                    className="mb-0"
                )

            ),

            dbc.CardBody(

                [

                    html.P(

                        [
                            html.Strong(
                                "Hierarchical clustering "
                            ),

                            (
                                "is applied as a supporting analysis "
                                "method to discover hidden structures "
                                "within different borrower feature groups."
                            )

                        ]

                    ),


                    html.Ul(

                        [

                            html.Li(
                                "Loan features are clustered to identify borrowing patterns."
                            ),

                            html.Li(
                                "Credit history clustering reveals borrower credit behavior."
                            ),

                            html.Li(
                                "Risk behavior clustering highlights potential risk groups."
                            ),

                            html.Li(
                                "Payment outcome clustering identifies repayment patterns."
                            )

                        ]

                    ),


                    html.Hr(),


                    html.P(

                        [

                            html.Strong(
                                "Final segmentation decision: "
                            ),

                            (
                                "The overall borrower segmentation "
                                "is based on K-Means clustering applied "
                                "to the complete dataset because it "
                                "creates holistic customer profiles "
                                "combining multiple financial factors."
                            )

                        ]

                    )

                ]

            )

        ],

        className="dashboard-card"

    )