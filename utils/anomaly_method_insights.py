METHOD_INSIGHTS = {

    "All": {
        "title": "Overall Detection",
        "icon": "📊",
        "text":
        (
            "IQR identifies the largest number of anomalies because it captures "
            "extreme statistical deviations across individual features. "
            "Isolation Forest detects fewer observations but focuses on "
            "multidimensional anomalies that traditional statistical methods "
            "may overlook."
        )
    },

    "Weak anomaly": {
        "title": "Weak Anomalies",
        "icon": "🟦",
        "text":
        (
            "Weak anomalies are primarily detected by IQR, indicating that "
            "these borrowers usually deviate in only one or two numerical "
            "attributes instead of exhibiting complex abnormal behavior."
        )
    },

    "Moderate anomaly": {
        "title": "Moderate Anomalies",
        "icon": "🟧",
        "text":
        (
            "Moderate anomalies are frequently identified by both IQR and "
            "Z-Score, suggesting agreement between multiple statistical "
            "techniques and indicating more reliable abnormal observations."
        )
    },

    "Strong anomaly": {
        "title": "Strong Anomalies",
        "icon": "🟥",
        "text":
        (
            "Strong anomalies are commonly supported by all detection methods. "
            "This agreement indicates highly unusual borrower profiles that "
            "deserve manual investigation before lending decisions."
        )
    }

}