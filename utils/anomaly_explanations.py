def generate_anomaly_explanation(row):

    reasons = []

    # -------------------------
    # Recoveries
    # -------------------------
    if row["recoveries"] > 3:
        reasons.append(
            "Exceptionally high recovery amount compared with typical charged-off loans."
        )

    # -------------------------
    # Loan amount
    # -------------------------
    if row["loan_amnt"] > 2:
        reasons.append(
            "Requested loan amount is unusually large relative to the portfolio."
        )

    # -------------------------
    # Income
    # -------------------------
    if row["annual_inc"] > 3:
        reasons.append(
            "Borrower reports extremely high annual income."
        )

    elif row["annual_inc"] < -2:
        reasons.append(
            "Borrower reports exceptionally low annual income."
        )

    # -------------------------
    # Credit score
    # -------------------------
    if row["fico_range_low"] < -1:
        reasons.append(
            "Credit score is significantly below the population average."
        )

    elif row["fico_range_low"] > 2:
        reasons.append(
            "Credit score is unusually high."
        )

    # -------------------------
    # Debt-to-income
    # -------------------------
    if row["dti"] > 2:
        reasons.append(
            "Debt-to-income ratio is extremely high."
        )

    elif row["dti"] < -2:
        reasons.append(
            "Debt-to-income ratio is exceptionally low."
        )

    if not reasons:

        reasons.append(
            "Several financial attributes jointly differ from normal borrower behaviour."
        )

    return reasons

def determine_business_category(row):

    if row["recoveries"] > 3:

        return (
            "Potential Risk Signal",
            "danger",
            "🚨"
        )

    if row["loan_amnt"] > 2:

        return (
            "Rare Legitimate Case",
            "warning",
            "💼"
        )

    if row["annual_inc"] > 3:

        return (
            "Rare Legitimate Case",
            "primary",
            "💰"
        )

    if row["fico_range_low"] < -1:

        return (
            "Potential Risk Signal",
            "danger",
            "📉"
        )

    if row["dti"] > 2:

        return (
            "Potential Risk Signal",
            "danger",
            "⚠️"
        )

    return (
        "Needs Review",
        "secondary",
        "🔍"
    )