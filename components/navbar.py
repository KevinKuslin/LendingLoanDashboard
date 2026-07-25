from dash import html, dcc

navbar = html.Div(

    [

        # -------------------------
        # Brand
        # -------------------------

        html.Div(

            [

                html.Div(
                    "📊",
                    className="logo-icon"
                ),

                html.Div(

                    [

                        html.H3(
                            "Lending Club Analytics",
                            className="logo-title"
                        ),

                        html.P(
                            "Interactive Data Mining Dashboard",
                            className="logo-subtitle"
                        )

                    ]

                )

            ],

            className="brand-section"

        ),

        # -------------------------
        # Navigation
        # -------------------------

        html.Div(

            [

                dcc.Link(
                    "Executive Summary",
                    href="/",
                    className="nav-link"
                ),

                dcc.Link(
                    "Customer Segmentation",
                    href="/clustering",
                    className="nav-link"
                ),

                dcc.Link(
                    "Pattern Discovery",
                    href="/patterns",
                    className="nav-link"
                ),

                dcc.Link(
                    "Anomaly Investigation",
                    href="/anomalies",
                    className="nav-link"
                )

            ],

            className="nav-menu"

        )

    ],

    className="navbar"

)