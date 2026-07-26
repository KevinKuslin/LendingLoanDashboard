pattern_insights = [

    {
        "rank": 1,
        "IF": "pub_rec=1",
        "THEN": "pub_rec_bankruptcies=True",
        "lift": 6.65,
        "confidence": 0.800,
        "support": 0.108,
        "category": "Credit Risk",
        "insight":
            "Borrowers with an existing public derogatory record are highly likely to also have bankruptcy records. This indicates a strong relationship between adverse public credit events.",
        "recommendation":
            "Flag these borrowers for enhanced credit review and stricter approval criteria."
    },

    {
        "rank": 2,
        "IF": "pub_rec_bankruptcies=True",
        "THEN": "pub_rec=1",
        "lift": 6.65,
        "confidence": 0.898,
        "support": 0.108,
        "category": "Credit Risk",
        "insight":
            "Borrowers who have experienced bankruptcy almost always possess public derogatory records, reinforcing their elevated credit risk profile.",
        "recommendation":
            "Consider additional documentation requirements or higher interest rates for these applicants."
    },

    {
        "rank": 3,
        "IF": "open_acc_6m=2+",
        "THEN": "open_rv_12m=2+",
        "lift": 3.54,
        "confidence": 0.731,
        "support": 0.107,
        "category": "Borrowing Behavior",
        "insight":
            "Borrowers opening multiple accounts within six months often continue opening revolving credit accounts over the following year.",
        "recommendation":
            "Monitor these borrowers for rapidly increasing credit exposure."
    },

    {
        "rank": 4,
        "IF": "open_rv_12m=2+",
        "THEN": "open_acc_6m=2+",
        "lift": 3.54,
        "confidence": 0.520,
        "support": 0.107,
        "category": "Borrowing Behavior",
        "insight":
            "Frequent revolving-account activity is commonly accompanied by recent account openings, suggesting active borrowing behavior.",
        "recommendation":
            "Evaluate whether recent borrowing aligns with the applicant's repayment capacity."
    },

    {
        "rank": 5,
        "IF": "mths_since_last_delinq=High",
        "THEN": "mths_since_recent_revol_delinq=High",
        "lift": 3.50,
        "confidence": 0.560,
        "support": 0.136,
        "category": "Credit History",
        "insight":
            "Borrowers without recent delinquency events generally maintain consistent repayment performance across revolving accounts.",
        "recommendation":
            "Reward these applicants with improved credit scores or more favorable lending terms."
    },

    {
        "rank": 6,
        "IF": "mths_since_recent_revol_delinq=High",
        "THEN": "mths_since_last_delinq=High",
        "lift": 3.50,
        "confidence": 0.850,
        "support": 0.136,
        "category": "Credit History",
        "insight":
            "Strong revolving-account repayment behavior usually reflects a longer history without delinquency.",
        "recommendation":
            "Treat these borrowers as lower-risk candidates during loan evaluation."
    },

    {
        "rank": 7,
        "IF": "inq_fi=0, inq_last_6mths=0",
        "THEN": "inq_last_12m=0",
        "lift": 3.38,
        "confidence": 0.598,
        "support": 0.133,
        "category": "Financial Stability",
        "insight":
            "Applicants with no recent financial inquiries typically maintain stable borrowing patterns throughout the year.",
        "recommendation":
            "Prioritize these borrowers for streamlined approval processes."
    },

    {
        "rank": 8,
        "IF": "inq_last_6mths=0, open_rv_12m=0",
        "THEN": "inq_last_12m=0",
        "lift": 3.16,
        "confidence": 0.559,
        "support": 0.100,
        "category": "Financial Stability",
        "insight":
            "Borrowers with neither recent credit inquiries nor new revolving accounts generally exhibit conservative financial behavior.",
        "recommendation":
            "Classify these applicants as financially stable for risk assessment."
    },

    {
        "rank": 9,
        "IF": "all_util=High, total_bal_ex_mort=High",
        "THEN": "open_act_il=High",
        "lift": 3.11,
        "confidence": 0.741,
        "support": 0.103,
        "category": "Credit Utilization",
        "insight":
            "High utilization together with large outstanding balances strongly correlates with a greater number of active installment loans.",
        "recommendation":
            "Assess debt-to-income ratios carefully before approving additional credit."
    },

    {
        "rank": 10,
        "IF": "delinq_2yrs=0, pct_tl_nvr_dlq=Low",
        "THEN": "mths_since_last_delinq=High",
        "lift": 3.03,
        "confidence": 0.735,
        "support": 0.149,
        "category": "Credit History",
        "insight":
            "Although these borrowers have no recent delinquencies, their historical repayment profile should still be reviewed holistically.",
        "recommendation":
            "Combine delinquency history with other credit metrics before making lending decisions."
    }

]