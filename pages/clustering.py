from dash import html, dcc
import dash
import dash_bootstrap_components as dbc

print("IMPORTING CLUSTERING PAGE")

from utils.data_loader import (
    cluster_profiles,
    kmeans_elbow,
    kmeans_silhouette,
    kmeans_visualization,
    hierarchy_elbow,
    hierarchy_silhouette,
    hierarchy_group_clusters_visualization,
    dbscan_umap
)

from components.cluster_insight_card import cluster_insight_card
from components.metric_card import metric_card
from components.chart_card import chart_card
from components.insight_card import insight_card
from components.hero import hero
from components.hierarchy_summary_card import hierarchy_summary_card
from components.analysis_note_card import analysis_note_card
from components.card import dbscan_explanation_card

print("IMPORTING CLUSTERING FIGURES")

from figures.clustering_figures import (
    create_elbow_chart,
    create_silhouette_chart,
    create_cluster_scatter,
    create_cluster_profile_heatmap,

    create_hierarchy_elbow_chart,
    create_hierarchy_silhouette_chart,
    create_hierarchy_scatter,

    create_dbscan_umap_chart
)

print("CLUSTERING DATA LOADED")

dash.register_page(
    __name__,
    path="/clustering",
    name="Customer Segmentation"
)

# ==========================================================
# STATIC METRICS
# ==========================================================


TOTAL_CLUSTERS = (
    cluster_profiles["cluster"]
    .nunique()
)

# ==========================================================
# STATIC METRICS
# ==========================================================

# ==========================================================
# STATIC METRICS
# ==========================================================

TOTAL_SEGMENTS = cluster_profiles["cluster"].nunique()

HIERARCHY_CATEGORIES = 4

FEATURES_PROFILED = 9

BEST_SILHOUETTE = (
    kmeans_silhouette["silhouette"].max()
)

# ==========================================================
# FEATURE OPTIONS
# ==========================================================

HIERARCHY_FEATURES = [
    "loan_amnt",
    "annual_inc",
    "int_rate",
    "dti",
    "fico_range_low",
    "total_acc",
    "delinq_2yrs",
    "loan_status_charged off",
    "verification_status_verified"
]

HIERARCHY_GROUPS = [
    "loan_cluster",
    "credit_history_cluster",
    "risk_behavior_cluster",
    "payment_outcome_cluster"
]

largest_cluster = (
    cluster_profiles
    .sort_values(
        "count",
        ascending=False
    )
    .iloc[0]
)


largest_cluster_name = (
    f"Cluster {largest_cluster['cluster']}"
)


largest_cluster_size = (
    f"{largest_cluster['count']:,}"
)



highest_risk_cluster = (
    cluster_profiles
    .sort_values(
        "loan_status_charged off",
        ascending=False
    )
    .iloc[0]["cluster"]
)

# ==========================================================
# INITIAL FIGURES
# ==========================================================

initial_elbow = create_elbow_chart(
    kmeans_elbow
)

initial_silhouette = create_silhouette_chart(
    kmeans_silhouette
)

initial_cluster_scatter = create_cluster_scatter(
    kmeans_visualization,
    3
)

initial_profile = create_cluster_profile_heatmap(
    cluster_profiles
)

initial_dbscan = create_dbscan_umap_chart(
    dbscan_umap
)

def generate_cluster_business_rules(df):

    cards = []

    # Identify rankings
    highest_income = df["annual_inc"].idxmax()
    highest_loan = df["loan_amnt"].idxmax()
    highest_fico = df["fico_range_low"].idxmax()
    highest_default = df["loan_status_charged off"].idxmax()
    highest_recovery = df["recoveries"].idxmax()
    lowest_dti = df["dti"].idxmin()
    largest_cluster = df["count"].idxmax()

    for idx, row in df.iterrows():

        cluster = int(row["cluster"])
        population = int(row["count"])

        description = []
        recommendation = []
        title = f"Cluster {cluster}"

        # --------------------------------------------------
        # Largest customer segment
        # --------------------------------------------------

        if idx == largest_cluster:

            description.append(
                "Largest borrower population in the portfolio."
            )

        # --------------------------------------------------
        # Income
        # --------------------------------------------------

        if idx == highest_income:

            description.append(
                "Highest annual income among all customer segments."
            )

        # --------------------------------------------------
        # Loan Amount
        # --------------------------------------------------

        if idx == highest_loan:

            description.append(
                "Receives the largest average loan amounts."
            )

        elif row["loan_amnt"] < 0:

            description.append(
                "Typically borrows smaller loan amounts."
            )

        # --------------------------------------------------
        # Credit Quality
        # --------------------------------------------------

        if idx == highest_fico:

            description.append(
                "Best average credit quality (highest FICO score)."
            )

        # --------------------------------------------------
        # Default Risk
        # --------------------------------------------------

        if idx == highest_default:

            description.append(
                "Highest charge-off risk among all clusters."
            )

            recommendation.append(
                "Increase monitoring and apply stricter approval policies."
            )

        # --------------------------------------------------
        # Recovery
        # --------------------------------------------------

        if idx == highest_recovery:

            description.append(
                "Highest recovery activity, indicating more defaulted loans."
            )

        # --------------------------------------------------
        # Debt-to-Income
        # --------------------------------------------------

        if idx == lowest_dti:

            description.append(
                "Maintains the healthiest debt-to-income profile."
            )

        # --------------------------------------------------
        # Business Interpretation
        # --------------------------------------------------

        if (
            idx == highest_income
            and idx == highest_fico
        ):

            title += " • Prime Borrowers"

            recommendation.append(
                "Suitable for premium lending products, higher credit limits, and customer retention programs."
            )

        elif idx == highest_default:

            title += " • High Risk Segment"

            recommendation.append(
                "Prioritize early-warning monitoring and tighter credit assessment."
            )

        elif row["loan_amnt"] < 0 and row["loan_status_charged off"] < 0.10:

            title += " • Everyday Borrowers"

            recommendation.append(
                "Well suited for standard consumer lending with routine monitoring."
            )

        if len(recommendation) == 0:

            recommendation.append(
                "Continue monitoring this segment using existing lending policies."
            ),

        cards.append(

            cluster_insight_card(

                title,

                description = (
                    f"👥 {population:,} borrowers\n"
                    + "\n".join(
                        f"• {item}" for item in description
                    )
                ),

                recommendation=" ".join(recommendation),

                color="#2563EB"

            )

        )

    return cards

cluster_business_cards = generate_cluster_business_rules(
    cluster_profiles
)

DEFAULT_GROUP = hierarchy_elbow["group"].iloc[0]

# ==========================================================
# HIERARCHY SUMMARY
# ==========================================================


hierarchy_summary = (

    hierarchy_silhouette

    .sort_values(
        "silhouette",
        ascending=False
    )

    .groupby(
        "group"
    )

    .first()

    .reset_index()

)

hierarchy_cards = [

    hierarchy_summary_card(

        row["group"],

        row["k"],

        row["silhouette"]

    )

    for _, row in hierarchy_summary.iterrows()

]

initial_hierarchy_elbow = create_hierarchy_elbow_chart(
    hierarchy_elbow,
    DEFAULT_GROUP
)

initial_hierarchy_silhouette = create_hierarchy_silhouette_chart(
    hierarchy_silhouette,
    DEFAULT_GROUP
)

# ==========================================================
# HIERARCHY EXPLORER
# ==========================================================

initial_hierarchy_scatter = create_hierarchy_scatter(

    hierarchy_group_clusters_visualization,

    hierarchy_group="loan_cluster",

    x_feature="annual_inc",

    y_feature="loan_amnt"

)

# ==========================================================
# LAYOUT
# ==========================================================


# layout = dbc.Container(

#     [

#         hero(
#             title="Customer Segmentation Analysis",
#             subtitle=
#             "Explore borrower segments generated using K-Means, "
#             "Hierarchical Clustering, and DBSCAN to understand "
#             "customer characteristics and portfolio risk."
#         ),


#         html.Br(),

#         dbc.Row(

#             [

#                 dbc.Col(metric_card(
#                     "🏆",
#                     "Largest Segment",
#                     "Cluster 1",
#                     "#2563EB",
#                     "largest-segment"
#                 )),

#                 dbc.Col(metric_card(
#                     "⭐",
#                     "Best Credit",
#                     "Cluster 1",
#                     "#10B981",
#                     "best-credit"
#                 )),

#                 dbc.Col(metric_card(
#                     "⚠",
#                     "Highest Risk",
#                     "Cluster 0",
#                     "#EF4444",
#                     "highest-risk"
#                 )),

#                 dbc.Col(metric_card(
#                     "💰",
#                     "Highest Income",
#                     "Cluster 1",
#                     "#F59E0B",
#                     "highest-income"
#                 ))

#             ],

#             className="g-3 mb-4"

#         ),


#         # ==============================
#         # KPI CARDS
#         # ==============================


#         dbc.Row(

#             [

#                 dbc.Col(

#                     metric_card(

#                         "🧩",

#                         "Customer Segments",

#                         str(TOTAL_SEGMENTS),

#                         "#2563EB",

#                         "cluster-total"

#                     ),

#                     lg=3

#                 ),


#                 dbc.Col(

#                     metric_card(

#                         "🌳",

#                         "Hierarchy Categories",

#                         str(HIERARCHY_CATEGORIES),

#                         "#10B981",

#                         "hierarchy-groups"

#                     ),

#                     lg=3

#                 ),


#                 dbc.Col(

#                     metric_card(

#                         "📈",

#                         "Features Profiled",

#                         str(FEATURES_PROFILED),

#                         "#F59E0B",

#                         "profiled-features"

#                     ),

#                     lg=3

#                 ),


#                 dbc.Col(

#                     metric_card(

#                         "📊",

#                         "Best Silhouette",

#                         f"{BEST_SILHOUETTE:.3f}",

#                         "#7C3AED",

#                         "best-silhouette"

#                     ),

#                     lg=3

#                 )

#             ],

#             className="g-4 mb-4"

#         ), 



#         html.Hr(),


#         html.H3(
#             "K-Means Optimization",
#             className="section-title"
#         ),



#         dbc.Row(

#             [

#                 dbc.Col(

#                     chart_card(
#                         "Elbow Method",
#                         initial_elbow,
#                         "kmeans-elbow"
#                     ),

#                     lg=6

#                 ),


#                 dbc.Col(

#                     chart_card(
#                         "Silhouette Score",
#                         initial_silhouette,
#                         "kmeans-silhouette"
#                     ),

#                     lg=6

#                 )

#             ],

#             className="g-4"

#         ),



#         html.Br(),



#         html.H3(
#             "Interactive Cluster Visualization",
#             className="section-title"
#         ),


#         dbc.Row(

#             dbc.Col(

#                 dcc.Dropdown(

#                     id="cluster-k-selector",

#                     options=[

#                         {
#                             "label":f"K = {k}",
#                             "value":k
#                         }

#                         for k in sorted(
#                             kmeans_visualization["k"].unique()
#                         )

#                     ],

#                     value=3,

#                     clearable=False,

#                     style={
#                         "maxWidth":"250px"
#                     }

#                 ),

#                 width="auto"

#             ),

#             className="mb-3"

#         ),

#         html.Br(),

#         dbc.Row(

#             [

#                 dbc.Col(

#                     chart_card(
#                         "Interactive Cluster Explorer",
#                         initial_cluster_scatter,
#                         "cluster-scatter"
#                     ),

#                     lg=12

#                 )

#             ]

#         ),



#         html.Br(),


#         html.H3(
#             "Cluster Characteristics",
#             className="section-title"
#         ),



#         dbc.Row(

#             [

#                 dbc.Col(

#                     chart_card(
#                         "Normalized Cluster Profiles",
#                         initial_profile,
#                         "cluster-profile"
#                     ),

#                     lg=12

#                 )

#             ]

#         ),

#         html.Br(),

#         html.H3(
#             "Hierarchical Clustering Summary",
#             className="section-title"
#         ),


#         html.P(

#             """
#             Hierarchical clustering was applied independently across four
#             borrower feature domains. Each domain selected its optimal number
#             of clusters using silhouette evaluation.
#             """,

#             className="text-muted"

#         ),


#         dbc.Row(

#             [

#                 dbc.Col(

#                     card,

#                     lg=3

#                 )

#                 for card in hierarchy_cards

#             ],

#             className="g-4 mb-4"

#         ),

#         html.Br(),

#         html.H3(
#             "Hierarchical Clustering Explorer",
#             className="section-title"
#         ),

#         dbc.Row(

#             dbc.Col(

#                 dcc.Dropdown(

#                     id="hierarchy-group-selector",

#                     options=[
#                         {
#                             "label":g,
#                             "value":g
#                         }
#                         for g in hierarchy_elbow["group"].unique()
#                     ],

#                     value=DEFAULT_GROUP,

#                     clearable=False,

#                     style={
#                         "maxWidth":"350px"
#                     }

#                 ),

#                 width="auto"

#             ),

#             className="mb-3"

#         ),

#         dbc.Row(

#             [

#                 dbc.Col(

#                     chart_card(
#                         "Hierarchical Elbow",
#                         initial_hierarchy_elbow,
#                         "hierarchy-elbow"
#                     ),

#                     lg=6

#                 ),

#                 dbc.Col(

#                     chart_card(
#                         "Hierarchical Silhouette",
#                         initial_hierarchy_silhouette,
#                         "hierarchy-silhouette"
#                     ),

#                     lg=6

#                 )

#             ],

#             className="g-4 mb-4"

#         ),

#         dbc.Row(

#             [

#                 dbc.Col(

#                     dcc.Dropdown(

#                         id="hierarchy-group",

#                         options=[

#                             {
#                                 "label":i.replace("_"," ").title(),
#                                 "value":i
#                             }

#                             for i in HIERARCHY_GROUPS

#                         ],

#                         value="loan_cluster",

#                         clearable=False

#                     ),

#                     lg=4

#                 ),

#                 dbc.Col(

#                     dcc.Dropdown(

#                         id="hierarchy-x",

#                         options=[

#                             {
#                                 "label":i.replace("_"," ").title(),
#                                 "value":i
#                             }

#                             for i in HIERARCHY_FEATURES

#                         ],

#                         value="annual_inc",

#                         clearable=False

#                     ),

#                     lg=4

#                 ),

#                 dbc.Col(

#                     dcc.Dropdown(

#                         id="hierarchy-y",

#                         options=[

#                             {
#                                 "label":i.replace("_"," ").title(),
#                                 "value":i
#                             }

#                             for i in HIERARCHY_FEATURES

#                         ],

#                         value="loan_amnt",

#                         clearable=False

#                     ),

#                     lg=4

#                 )

#             ],

#             className="mb-3"

#         ),

#         dbc.Row(

#             dbc.Col(

#                 chart_card(

#                     "Hierarchy Feature Explorer",

#                     initial_hierarchy_scatter,

#                     "hierarchy-profile"

#                 ),

#                 lg=12

#             )

#         ),

#         html.Br(),

#         html.H3(

#             "Cluster Business Interpretation",

#             className="section-title"

#         ),

#         dbc.Row(

#             [

#                 dbc.Col(

#                     card,

#                     lg=4

#                 )

#                 for card in cluster_business_cards

#             ],

#             className="g-4"

#         ),

#         html.Br(), 

#         analysis_note_card(),

#         html.Br(), 

#         dbc.Row(
#             [

#                 dbc.Col(
#                     dbscan_explanation_card(),
#                     lg=12
#                 )

#             ],
#             className="mb-4"
#         ),

#         dbc.Row(

#             [

#                 dbc.Col(

#                     chart_card(
#                         "DBSCAN + UMAP Projection",
#                         initial_dbscan,
#                         "dbscan-chart"
#                     ),

#                     lg=12

#                 )

#             ]

#         ), 

#         html.Br(),

#         dbc.Row(

#         [
#             dbc.Col(

#                 insight_card(

#                     "Cluster Quality",

#                     (
#                         "K-Means achieved the highest silhouette score at "
#                         "k=3, indicating three borrower groups provide the "
#                         "best balance between cohesion and separation."
#                     ),

#                     "📈",

#                     "#2563EB"

#                 ),

#                 lg=4

#             ),

#             dbc.Col(

#                 insight_card(

#                     "Risk Segment",

#                     (
#                         "Cluster "
#                         f"{int(highest_risk_cluster)} "
#                         "contains the highest charge-off proportion, making it "
#                         "the primary target for credit monitoring."
#                     ),

#                     "⚠️",

#                     "#EF4444"

#                 ),

#                 lg=4

#             ),

#             dbc.Col(

#                 insight_card(

#                     "Business Value",

#                     (
#                         "Customer segmentation enables differentiated lending "
#                         "strategies, pricing, and monitoring instead of treating "
#                         "every borrower as a single population."
#                     ),

#                     "💡",

#                     "#10B981"

#                 ),

#                 lg=4

#             )

#         ],

#         className="mt-4"
#         )


#     ],

#     fluid=True,
#     className="py-4"

# )

layout = html.Div([
    hero(),
    html.H3("Clustering loaded...")
])

print("Clustering Page Loaded")