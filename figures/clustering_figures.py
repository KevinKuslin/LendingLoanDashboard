import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# KMEANS EVALUATION
# ==========================================================

def create_elbow_chart(df):

    fig = px.line(
        df,
        x="k",
        y="inertia",
        markers=True,
        title="K-Means Elbow Method",
    )

    fig.update_layout(
        xaxis_title="Number of Clusters (k)",
        yaxis_title="Inertia",
        template="plotly_white"
    )

    return fig



def create_silhouette_chart(df):

    fig = px.bar(
        df,
        x="k",
        y="silhouette",
        text="silhouette",
        title="K-Means Silhouette Score"
    )

    fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Number of Clusters",
        yaxis_title="Silhouette Score",
        template="plotly_white"
    )

    return fig



# ==========================================================
# KMEANS VISUALIZATION
# ==========================================================

import plotly.express as px


def create_cluster_scatter(df, selected_k):

    filtered = df[df["k"] == selected_k] 

    filtered = filtered.sample(
        min(30000, len(filtered)),
        random_state=42
    )

    fig = px.scatter(

        filtered,

        x="x",
        y="y",

        color=filtered["cluster"].astype(str),

        title=f"K-Means Visualization (k={selected_k})",

        opacity=0.7,

        hover_data=["cluster"]

    )

    fig.update_traces(
        marker=dict(size=5)
    )

    fig.update_layout(

        template="plotly_white",

        legend_title="Cluster",

        xaxis_title="Component 1",

        yaxis_title="Component 2"

    )

    fig.update_layout(

        transition_duration=400,

        legend=dict(

            orientation="h",

            y=1.08,

            x=0

        )

    )

    return fig

# ==========================================================
# CLUSTER PROFILE
# ==========================================================

def create_cluster_profile_heatmap(df):

    profile = df.copy()


    numeric_columns = [
        "loan_amnt",
        "annual_inc",
        "int_rate",
        "dti",
        "fico_range_low",
        "total_acc",
        "delinq_2yrs",
        "recoveries",
        "loan_status_charged off"
    ]


    profile = profile[
        [
            "cluster"
        ]
        +
        numeric_columns
    ]


    profile = profile.set_index(
        "cluster"
    )

    profile.columns = [

        "Loan Amount",
        "Annual Income",
        "Interest Rate",
        "DTI",
        "FICO",
        "Total Accounts",
        "Delinquencies",
        "Recoveries",
        "Charge Off Rate"
    ]

    fig = px.imshow(
        profile.T,
        text_auto=".2f",
        aspect="auto",
        title="Cluster Financial Profile (Normalized)"
    )


    fig.update_layout(
        template="plotly_white"
    )


    return fig



# ==========================================================
# HIERARCHICAL CLUSTERING
# ==========================================================


def create_hierarchy_silhouette_chart(df):

    fig = px.bar(
        df,
        x="k",
        y="silhouette",
        color="group",
        barmode="group",
        title="Hierarchical Clustering Silhouette Score"
    )


    fig.update_layout(
        template="plotly_white"
    )


    return fig



def create_hierarchy_cluster_heatmap(df):

    heatmap_df = df.copy()


    fig = px.imshow(
        heatmap_df.corr(numeric_only=True),
        text_auto=".2f",
        title="Hierarchical Cluster Relationship"
    )


    fig.update_layout(
        template="plotly_white"
    )


    return fig



# ==========================================================
# DBSCAN + UMAP
# ==========================================================


def create_dbscan_umap_chart(df):

    fig = px.scatter(
        df,
        x="x",
        y="y",
        color="cluster",
        title="DBSCAN Cluster Visualization (UMAP)",
        opacity=0.7
    )


    fig.update_layout(
        template="plotly_white",
        xaxis_title="UMAP 1",
        yaxis_title="UMAP 2"
    )


    return fig