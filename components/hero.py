from dash import html


def hero():

    return html.Div(

        [

            html.Div(

                "PPTI 21 • GROUP 2",

                className="hero-tag"

            ),

            html.H1(

                "Lending Club Analytics Dashboard",

                className="hero-title"

            ),

            html.P(

                "Interactive analytics platform for customer segmentation, pattern discovery, and anomaly investigation using unsupervised machine learning.",

                className="hero-subtitle"

            )

        ],

        className="hero-section"

    )