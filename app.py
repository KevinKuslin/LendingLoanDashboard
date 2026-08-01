from dash import Dash, html, page_container
import dash_bootstrap_components as dbc

print("START APP")

import callbacks.executive_callbacks
print("EXECUTIVE CALLBACKS LOADED")

import callbacks.clustering_callbacks
print("CLUSTERING CALLBACKS LOADED")

import callbacks.pattern_callbacks
print("PATTERN CALLBACKS LOADED")

import callbacks.anomaly_callbacks
print("ANOMALY CALLBACKS LOADED")

from components.navbar import navbar
print("NAVBAR LOADED")

import os

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

print("LAYOUT CREATED")


# if __name__ == "__main__":

#     app.run(debug=True)

server = app.server

print("SERVER CREATED")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        debug=False
    ) 
