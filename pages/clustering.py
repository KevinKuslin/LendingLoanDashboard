from dash import html, dcc
import dash
import dash_bootstrap_components as dbc

from utils.data_loader import (
    cluster_profiles,
    kmeans_elbow,
    kmeans_silhouette,
    kmeans_visualization,
    hierarchy_elbow,
    hierarchy_silhouette,
    hierarchy_group_clusters,
    dbscan_umap
)


from components.metric_card import metric_card
from components.chart_card import chart_card
from components.insight_card import insight_card
from components.hero import hero

from figures.clustering_figures import (

    create_elbow_chart,
    create_silhouette_chart,

    create_cluster_scatter,

    create_cluster_profile_heatmap,

    create_hierarchy_silhouette_chart,
    create_hierarchy_cluster_heatmap,

    create_dbscan_umap_chart

)

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

initial_hierarchy = create_hierarchy_silhouette_chart(
    hierarchy_silhouette
)

# ==========================================================
# LAYOUT
# ==========================================================


layout = dbc.Container(

    [

        hero(
            # title="Customer Segmentation Analysis",
            # subtitle=
            # "Interactive clustering analysis using K-Means, Hierarchical Clustering, and DBSCAN"
        ),


        html.Br(),


        # ==============================
        # KPI CARDS
        # ==============================


        dbc.Row(

            [

                dbc.Col(
                    metric_card(
                        "🧩",
                        "Total Segments",
                        str(TOTAL_CLUSTERS),
                        "#2563EB",
                        "cluster-total"
                    ),
                    lg=3
                ),


                dbc.Col(
                    metric_card(
                        "👥",
                        "Largest Segment",
                        largest_cluster_name,
                        "#10B981",
                        "largest-cluster"
                    ),
                    lg=3
                ),


                dbc.Col(
                    metric_card(
                        "📊",
                        "Segment Population",
                        largest_cluster_size,
                        "#7C3AED",
                        "segment-size"
                    ),
                    lg=3
                ),


                dbc.Col(
                    metric_card(
                        "⚠️",
                        "Highest Risk Cluster",
                        f"Cluster {highest_risk_cluster}",
                        "#EF4444",
                        "risk-cluster"
                    ),
                    lg=3
                )

            ],

            className="g-4 mb-4"

        ),



        html.Hr(),


        html.H3(
            "K-Means Optimization",
            className="section-title"
        ),



        dbc.Row(

            [

                dbc.Col(

                    chart_card(
                        "Elbow Method",
                        initial_elbow,
                        "kmeans-elbow"
                    ),

                    lg=6

                ),


                dbc.Col(

                    chart_card(
                        "Silhouette Score",
                        initial_silhouette,
                        "kmeans-silhouette"
                    ),

                    lg=6

                )

            ],

            className="g-4"

        ),



        html.Br(),



        html.H3(
            "Interactive Cluster Visualization",
            className="section-title"
        ),


        dcc.Dropdown(

            id="cluster-k-selector",

            options=[
                {
                    "label":f"K={k}",
                    "value":k
                }

                for k in sorted(
                    kmeans_visualization["k"].unique()
                )
            ],

            value=3,

            clearable=False

        ),



        dbc.Row(

            [

                dbc.Col(

                    chart_card(
                        "2D Cluster Projection",
                        initial_cluster_scatter,
                        "cluster-scatter"
                    ),

                    lg=12

                )

            ]

        ),



        html.Br(),


        html.H3(
            "Cluster Characteristics",
            className="section-title"
        ),



        dbc.Row(

            [

                dbc.Col(

                    chart_card(
                        "Normalized Cluster Profiles",
                        initial_profile,
                        "cluster-profile"
                    ),

                    lg=12

                )

            ]

        ),



        html.Br(),


        html.H3(
            "Alternative Clustering Methods",
            className="section-title"
        ),

        dbc.Row(
            [
                dbc.Col(

                    chart_card(
                        "Hierarchical Silhouette",
                        initial_hierarchy,
                        "hierarchy-chart"
                    ),

                    lg=6

                ),

                dbc.Col(

                    chart_card(
                        "Hierarchical Cluster Profiles",
                        create_hierarchy_cluster_heatmap(
                            hierarchy_group_clusters
                        ),
                        "hierarchy-profile"
                    ),

                    lg=6

                )

            ],

            className="g-4 mb-4"

        ),

        dbc.Row(

            [

                dbc.Col(

                    chart_card(
                        "DBSCAN + UMAP Projection",
                        initial_dbscan,
                        "dbscan-chart"
                    ),

                    lg=12

                )

            ]

        ), 

        html.Br(),

        dbc.Row(

        [
            dbc.Col(

                insight_card(

                    "Cluster Quality",

                    (
                        "K-Means achieved the highest silhouette score at "
                        "k=3, indicating three borrower groups provide the "
                        "best balance between cohesion and separation."
                    ),

                    "📈",

                    "#2563EB"

                ),

                lg=4

            ),

            dbc.Col(

                insight_card(

                    "Risk Segment",

                    (
                        "Cluster "
                        f"{highest_risk_cluster} "
                        "contains the highest charge-off proportion, making it "
                        "the primary target for credit monitoring."
                    ),

                    "⚠️",

                    "#EF4444"

                ),

                lg=4

            ),

            dbc.Col(

                insight_card(

                    "Business Value",

                    (
                        "Customer segmentation enables differentiated lending "
                        "strategies, pricing, and monitoring instead of treating "
                        "every borrower as a single population."
                    ),

                    "💡",

                    "#10B981"

                ),

                lg=4

            )

        ],

        className="mt-4"
        )


    ],

    fluid=True,
    className="py-4"

)