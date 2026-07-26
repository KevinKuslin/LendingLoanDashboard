import dash_bootstrap_components as dbc
from dash import html


def dbscan_explanation_card():

    return dbc.Card(
        [
            dbc.CardHeader(
                [
                    html.I(
                        className="bi bi-diagram-3-fill me-2"
                    ),
                    "DBSCAN + UMAP Methodology"
                ],
                className="fw-bold"
            ),

            dbc.CardBody(
                [

                    # Why DBSCAN
                    html.H6(
                        "Why DBSCAN?",
                        className="text-primary fw-bold"
                    ),

                    html.P(
                        [
                            "DBSCAN identifies borrower groups based on "
                            "density patterns instead of requiring a "
                            "predefined number of clusters. "
                            "It can also detect outliers as noise."
                        ],
                        className="text-muted"
                    ),


                    # Why UMAP
                    html.H6(
                        "Why UMAP?",
                        className="text-primary fw-bold mt-3"
                    ),

                    html.P(
                        [
                            "The dataset contains many borrower attributes. "
                            "UMAP reduces these high-dimensional features "
                            "into a 2D space while preserving local "
                            "relationships for visualization."
                        ],
                        className="text-muted"
                    ),


                    # Result section
                    dbc.Alert(
                        [
                            html.H6(
                                "Clustering Result",
                                className="fw-bold"
                            ),

                            html.Div(
                                [
                                    html.Span(
                                        "Detected Clusters: ",
                                        className="fw-bold"
                                    ),
                                    html.Span("1")
                                ]
                            ),

                            html.Div(
                                [
                                    html.Span(
                                        "Interpretation: ",
                                        className="fw-bold"
                                    ),
                                    html.Span(
                                        "A dominant borrower group "
                                        "was identified, while "
                                        "low-density observations "
                                        "were classified as noise."
                                    )
                                ]
                            )
                        ],
                        color="light",
                        className="mt-3"
                    )

                ]
            )
        ],

        className="shadow-sm border-0 h-100",
        style={
            "borderRadius": "15px"
        }
    )