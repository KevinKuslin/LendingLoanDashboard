INVESTIGATION_QUEUE = {

    "risk": {

        "title": "🚨 Potential Risk Signals",

        "priority": "High Priority",

        "color": "danger",

        "impact": (
            "These borrowers show characteristics that may indicate elevated "
            "credit risk, unusual repayment behaviour, or financial instability. "
            "They should receive additional review before any lending decision "
            "or portfolio action is taken."
        ),

        "indicators": [

            (
                "Unusually high recoveries, which may indicate previous "
                "default resolution, collection activity, or distressed loans."
            ),

            (
                "Extreme debt-related characteristics, such as abnormal "
                "debt-to-income ratios or unusual credit behaviour."
            ),

            (
                "Multiple anomaly detection methods agreeing on the same borrower, "
                "increasing confidence that the record deserves investigation."
            ),

            (
                "Borrower attributes significantly different from the majority "
                "of Lending Club applicants."
            )

        ],

        "actions": [

            (
                "Review borrower repayment history and previous loan performance."
            ),

            (
                "Validate reported financial information against supporting documents."
            ),

            (
                "Compare the borrower profile with similar customers in the portfolio."
            ),

            (
                "Investigate whether the anomaly represents genuine risk or an unusual "
                "but legitimate customer profile."
            )

        ]

    },


    "legitimate": {

        "title": "💼 Rare Legitimate Cases",

        "priority": "Medium Priority",

        "color": "warning",

        "impact": (
            "Not all anomalies represent fraud or risk. Some borrowers are flagged "
            "because they have rare financial characteristics, such as exceptionally "
            "high income, large loan amounts, or unusual but valid credit profiles."
        ),

        "indicators": [

            (
                "Loan amount is significantly larger than the typical borrower profile."
            ),

            (
                "Annual income is unusually high compared with the overall borrower population."
            ),

            (
                "Credit characteristics may represent premium customers rather than risky borrowers."
            ),

            (
                "The borrower differs from the majority of applicants but does not necessarily "
                "show negative financial behaviour."
            )

        ],

        "actions": [

            (
                "Verify income and employment information."
            ),

            (
                "Compare against high-value borrower segments."
            ),

            (
                "Avoid automatically classifying rare profiles as risky."
            ),

            (
                "Consider whether the borrower represents a valuable customer segment."
            )

        ]

    },


    "quality": {

        "title": "🗂 Data Quality Review",

        "priority": "Review Required",

        "color": "primary",

        "impact": (
            "Some anomalies may originate from incorrect, inconsistent, or unusual "
            "data records rather than genuine borrower behaviour. These cases should "
            "be validated to ensure model reliability."
        ),

        "indicators": [

            (
                "Multiple financial attributes simultaneously deviate from normal patterns."
            ),

            (
                "Extreme values may indicate data entry mistakes or inconsistent reporting."
            ),

            (
                "Records may contain combinations of attributes rarely observed in the dataset."
            ),

            (
                "The anomaly may be caused by preprocessing or data transformation effects."
            )

        ],

        "actions": [

            (
                "Check the original borrower record for data inconsistencies."
            ),

            (
                "Validate numerical ranges and feature distributions."
            ),

            (
                "Compare suspicious records with similar borrowers."
            ),

            (
                "Document confirmed data issues before model deployment."
            )

        ]

    }

}