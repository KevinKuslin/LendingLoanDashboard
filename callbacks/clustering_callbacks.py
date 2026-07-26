from dash import callback, Input, Output

from utils.data_loader import (
    kmeans_visualization
)

from figures.clustering_figures import (
    create_cluster_scatter
)

@callback(
    Output("cluster-scatter", "figure"),
    Input("cluster-k-selector", "value")
)
def update_cluster_scatter(k):
    return create_cluster_scatter(
        kmeans_visualization,
        k
    )