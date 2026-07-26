from dash import html


def hero(

    title="Lending Club Analytics Dashboard",

    subtitle=(
        "Interactive analytics platform for customer segmentation, "
        "pattern discovery, and anomaly investigation using "
        "unsupervised machine learning."
    ),

    tag="PPTI 21 • GROUP 2"

):

    return html.Div(

        [

            html.Div(

                tag,

                className="hero-tag"

            ),

            html.H1(

                title,

                className="hero-title"

            ),

            html.P(

                subtitle,

                className="hero-subtitle"

            )

        ],

        className="hero-section"

    )