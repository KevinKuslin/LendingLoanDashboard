from dash import callback, Input, Output

from utils.data_loader import (
    get_kmeans_visualization,
    get_hierarchy_group_clusters_visualization,
    get_hierarchy_elbow,
    get_hierarchy_silhouette,
)

from figures.clustering_figures import (
    create_cluster_scatter,
    create_hierarchy_scatter,
    create_hierarchy_elbow_chart,
    create_hierarchy_silhouette_chart
)

# ==========================================================
# KMEANS SCATTER
# ==========================================================

@callback(
    Output("cluster-scatter", "figure"),
    Input("cluster-k-selector", "value")
)
def update_cluster_scatter(k):

    return create_cluster_scatter(
        get_kmeans_visualization(),
        k
    )


# ==========================================================
# HIERARCHY FEATURE EXPLORER
# ==========================================================

@callback(
    Output("hierarchy-profile", "figure"),
    Input("hierarchy-group", "value"),
    Input("hierarchy-x", "value"),
    Input("hierarchy-y", "value")
)
def update_hierarchy(
    group,
    x,
    y
):

    return create_hierarchy_scatter(
        get_hierarchy_group_clusters_visualization(),
        group,
        x,
        y
    )


# ==========================================================
# HIERARCHY EVALUATION
# ==========================================================

@callback(
    Output("hierarchy-elbow", "figure"),
    Output("hierarchy-silhouette", "figure"),
    Input("hierarchy-group-selector", "value")
)
def update_hierarchy_evaluation(group):

    elbow = create_hierarchy_elbow_chart(
        get_hierarchy_elbow(),
        group
    )

    silhouette = create_hierarchy_silhouette_chart(
        get_hierarchy_silhouette(),
        group
    )

    return elbow, silhouette