from dash import callback, Input, Output

from utils.data_loader import accepted_raw

from figures.executive_figures import (
    create_status_chart,
    create_grade_chart,
    create_state_chart,
    create_loan_chart,
    create_interest_chart,
)

# ==========================================================
# FILTER FUNCTION
# ==========================================================

def filter_loans(
    loan_status,
    grade,
    state,
    loan_range
):

    df = accepted_raw.copy()


    if loan_status != "All":

        df = df[
            df["loan_status"] == loan_status
        ]


    if grade != "All":

        df = df[
            df["grade"] == grade
        ]


    if state != "All":

        df = df[
            df["addr_state"] == state
        ]


    df = df[
        (df["loan_amnt"] >= loan_range[0])
        &
        (df["loan_amnt"] <= loan_range[1])
    ]


    return df



# ==========================================================
# EXECUTIVE CALLBACK
# ==========================================================

@callback(

    Output(
        "kpi-total-loans",
        "children"
    ),

    Output(
        "kpi-average-loan",
        "children"
    ),

    Output(
        "kpi-interest",
        "children"
    ),

    Output(
        "loan-status-chart",
        "figure"
    ),

    Output(
        "grade-chart",
        "figure"
    ),

    Output(
        "state-chart",
        "figure"
    ),

    Output(
        "loan-chart",
        "figure"
    ),

    Output(
        "interest-chart",
        "figure"
    ),

    Input(
        "loan-status-filter",
        "value"
    ),

    Input(
        "grade-filter",
        "value"
    ),

    Input(
        "state-filter",
        "value"
    ),

    Input(
        "loan-slider",
        "value"
    )

)

def update_executive_dashboard(
    loan_status,
    grade,
    state,
    loan_range
):


    df = filter_loans(

        loan_status,
        grade,
        state,
        loan_range

    )

    if (len(df) > 0):
        avg_loan = df["loan_amnt"].mean()
        avg_interest = df["int_rate"].mean()
    else:
        avg_loan = 0
        avg_interest = 0

    return (
        f"{len(df):,}",
        f"${avg_loan:,.0f}",
        f"{avg_interest:.2f}%",
        create_status_chart(df),
        create_grade_chart(df),
        create_state_chart(df),
        create_loan_chart(df),
        create_interest_chart(df)
    )