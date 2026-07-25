from dash import html


def section_title(

    title,

    subtitle=None

):

    children=[

        html.H2(

            title,

            className="section-title"

        )

    ]

    if subtitle:

        children.append(

            html.P(

                subtitle,

                className="section-subtitle"

            )

        )

    return html.Div(

        children,

        className="section-header"

    )