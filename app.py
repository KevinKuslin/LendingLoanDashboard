from dash import Dash, html, page_container
import dash_bootstrap_components as dbc
import callbacks.executive_callbacks
import callbacks.clustering_callbacks
from components.navbar import navbar

app = Dash(

    __name__,

    use_pages=True,

    external_stylesheets=[dbc.themes.BOOTSTRAP]

)

app.layout = html.Div(

    [

        navbar,

        html.Div(

            page_container,

            className="page"

        )

    ]

)

server = app.server

if __name__ == "__main__":

    app.run(debug=True)