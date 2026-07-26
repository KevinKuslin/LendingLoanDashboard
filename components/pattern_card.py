from dash import html
import dash_bootstrap_components as dbc

CATEGORY_INFO = {
    "Credit Risk": {
        "icon": "🔴",
        "color": "danger"
    },
    "Borrowing Behavior": {
        "icon": "🟡",
        "color": "warning"
    },
    "Financial Stability": {
        "icon": "🟢",
        "color": "success"
    },
    "Credit Utilization": {
        "icon": "🔵",
        "color": "primary"
    }
}

def pattern_card(rule):
    info = CATEGORY_INFO[rule["category"]] 

    return dbc.Card(

        dbc.CardBody(

            [

                html.H5(
                    f"🥇 Rule #{rule['rank']}"
                ),

                dbc.Badge(
                    f"{info['icon']} {rule['category']}",
                    color=info["color"],
                    className="mb-3"
                ),

                html.P([
                    html.Strong("IF: "),
                    rule["IF"]
                ]),

                html.P([
                    html.Strong("THEN: "),
                    rule["THEN"]
                ]),

                dbc.Row([

                    dbc.Col([

                        html.Small("Lift"),
                        html.H5(f"{rule['lift']:.2f}×")

                    ]),

                    dbc.Col([

                        html.Small("Confidence"),
                        html.H5(f"{rule['confidence']:.1%}")

                    ]),

                    dbc.Col([

                        html.Small("Support"),
                        html.H5(f"{rule['support']:.1%}")

                    ])

                ]),

                html.Hr(),

                html.H6("Business Insight"),

                html.P(rule["insight"]),

                html.H6("Recommended Action"),

                dbc.Alert(
                    rule["recommendation"],
                    color="light",
                    className="mb-0"
                )

            ]

        ),

        className="shadow-sm h-100"

    )