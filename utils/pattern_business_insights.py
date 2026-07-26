pattern_business_insights = [

    {
        "title": "Credit Risk Detection",
        "icon": "⚠️",
        "category": "Credit Risk",

        "metric":
        "Lift 6.65× | Confidence 80.0% | Support 10.8%",

        "insight":
        """
        Association rules reveal that borrowers with public derogatory records
        are 6.65 times more likely than random borrowers to also have bankruptcy
        indicators. This relationship appears across 10.8% of transactions,
        showing that adverse public credit events frequently occur together
        within the borrower population.
        """,

        "recommendation":
        """
        Apply enhanced verification procedures and stricter risk evaluation
        when applicants exhibit combinations of adverse public credit records.
        """
    },


    {
        "title": "Borrowing Activity Monitoring",
        "icon": "📈",
        "category": "Borrowing Behavior",

        "metric":
        "Lift 3.54× | Confidence 73.1% | Support 10.7%",

        "insight":
        """
        Borrowers opening multiple accounts within six months frequently also
        increase revolving credit activity. The 3.54× lift indicates that this
        borrowing expansion pattern occurs significantly more often than random
        expectation, identifying applicants with rapidly changing credit usage.
        """,

        "recommendation":
        """
        Monitor applicants showing accelerated account growth to evaluate
        whether additional borrowing aligns with repayment capacity.
        """
    },


    {
        "title": "Stable Borrower Identification",
        "icon": "✅",
        "category": "Financial Stability",

        "metric":
        "Lift 3.38× | Confidence 59.8% | Support 13.3%",

        "insight":
        """
        Borrowers with no recent credit inquiries tend to consistently show
        fewer new credit activities. The discovered relationship highlights a
        recurring conservative borrowing profile rather than relying on a
        single financial indicator.
        """,

        "recommendation":
        """
        Consider these behavioral patterns as supporting evidence for lower-risk
        applicants during automated or streamlined approval processes.
        """
    },


    {
        "title": "Credit Utilization Management",
        "icon": "💳",
        "category": "Debt Exposure",

        "metric":
        "Lift 3.11× | Confidence 74.1% | Support 10.3%",

        "insight":
        """
        High utilization combined with large outstanding balances is strongly
        associated with a higher number of active installment obligations.
        The pattern reveals how multiple debt-related characteristics interact,
        providing a broader view of borrower exposure than individual metrics.
        """,

        "recommendation":
        """
        Include combined utilization and outstanding balance patterns when
        assessing affordability and potential repayment pressure.
        """
    },


    {
        "title": "Delinquency History Analysis",
        "icon": "📋",
        "category": "Credit History",

        "metric":
        "Lift 3.50× | Confidence 85.0% | Support 13.6%",

        "insight":
        """
        Borrowers with longer periods since their last delinquency tend to also
        show longer periods since recent revolving-account delinquency events.
        This indicates consistency between different repayment history measures,
        helping identify borrowers with stable credit behavior.
        """,

        "recommendation":
        """
        Combine delinquency timing patterns with other borrower attributes to
        improve repayment reliability assessment.
        """
    },


    {
        "title": "Conservative Credit Behavior",
        "icon": "🔍",
        "category": "Financial Stability",

        "metric":
        "Lift 3.16× | Confidence 55.9% | Support 10.0%",

        "insight":
        """
        Applicants with no recent inquiries and no new revolving accounts often
        maintain zero recent credit inquiries over longer periods. This pattern
        identifies borrowers with limited credit expansion activity.
        """,

        "recommendation":
        """
        Use conservative credit activity patterns as an additional signal when
        prioritizing stable borrower profiles.
        """
    }

]