from dash import callback, Input, Output

from utils.data_loader import (
    association_rules,
    association_rule_summary
)

pattern_summary = association_rule_summary.iloc[0]


# =====================================================
# Association Rule Explorer
# =====================================================

@callback(

    Output("rules-table", "data"),
    Output("rules-table", "columns"),
    Output("rule-counter", "children"),

    Input("if-filter", "value"),
    Input("then-filter", "value"),
    Input("support-slider", "value"),
    Input("confidence-slider", "value"),
    Input("lift-slider", "value"),
    Input("sort-rules", "value")

)
def update_rules(

    if_rule,
    then_rule,
    support,
    confidence,
    lift,
    sort_by

):

    df = association_rules.copy()

    # -------------------------
    # Apply dropdown filters
    # -------------------------

    if if_rule:

        df = df[df["IF"] == if_rule]

    if then_rule:

        df = df[df["THEN"] == then_rule]

    # -------------------------
    # Apply sliders
    # -------------------------

    df = df[
        (df["support"] >= support)
        &
        (df["confidence"] >= confidence)
        &
        (df["lift"] >= lift)
    ]

    # -------------------------
    # Sort
    # -------------------------

    df = df.sort_values(
        sort_by,
        ascending=False
    )

    rule_count = len(df)

    # -------------------------
    # Round values only
    # (keep numeric!)
    # -------------------------

    display_df = df.copy()

    display_df["support"] = (
        display_df["support"] * 100
    ).round(1)

    display_df["confidence"] = (
        display_df["confidence"] * 100
    ).round(1)

    display_df["lift"] = (
        display_df["lift"]
        .round(2)
    )

    columns = [
        {"name": "Rank", "id": "rank"},
        {"name": "IF", "id": "IF"},
        {"name": "THEN", "id": "THEN"},
        {"name": "Support (%)", "id": "support"},
        {"name": "Confidence (%)", "id": "confidence"},
        {"name": "Lift (×)", "id": "lift"},
    ]

    if display_df.empty:
        return (
            [],
            columns,
            "Showing 0 association rules"
        )

    return (

        display_df.to_dict("records"),

        columns,

        f"Showing {rule_count:,} association rules"

    )


# =====================================================
# Reset Rule Explorer Filters
# =====================================================

@callback(

    Output("if-filter", "value"),
    Output("then-filter", "value"),
    Output("sort-rules", "value"),
    Output("support-slider", "value"),
    Output("confidence-slider", "value"),
    Output("lift-slider", "value"),

    Input("reset-rule-filters", "n_clicks"),

    prevent_initial_call=True

)
def reset_rule_filters(n_clicks):

    return (

        None,

        None,

        "lift",

        float(pattern_summary["min_support"]),

        0,

        float(pattern_summary["min_lift"])

    )