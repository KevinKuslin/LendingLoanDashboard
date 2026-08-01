from pathlib import Path
import pandas as pd
from functools import lru_cache 

# Base Directory

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def load_parquet(*parts):
    return pd.read_parquet(DATA_DIR.joinpath(*parts))


# ==========================================================
# Raw Dataset
# ==========================================================

@lru_cache(maxsize=1)
def get_executive_raw():
    return load_parquet("executive_raw.parquet")


# ==========================================================
# Clustering Outputs
# ==========================================================

@lru_cache(maxsize=1)
def get_cluster_profiles():
    return load_parquet(
        "clustering_output",
        "cluster_profiles.parquet"
    )

@lru_cache(maxsize=1)
def get_kmeans_elbow():
    return load_parquet(
        "clustering_output",
        "kmeans_elbow.parquet"
    )

@lru_cache(maxsize=1)
def get_kmeans_silhouette():
    return load_parquet(
        "clustering_output",
        "kmeans_silhouette.parquet"
    )

@lru_cache(maxsize=1)
def get_kmeans_visualization():
    return load_parquet(
        "clustering_output",
        "kmeans_visualization.parquet"
    )

@lru_cache(maxsize=1)
def get_dbscan_umap():
    return load_parquet(
        "clustering_output",
        "dbscan_umap.parquet"
    )

@lru_cache(maxsize=1)
def get_hierarchy_elbow():
    return load_parquet(
        "clustering_output",
        "hierarchy_elbow.parquet"
    )

@lru_cache(maxsize=1)
def get_hierarchy_silhouette():
    return load_parquet(
        "clustering_output",
        "hierarchy_silhouette.parquet"
    )

@lru_cache(maxsize=1)
def get_hierarchy_group_clusters_visualization():
    return load_parquet(
        "clustering_output",
        "hierarchy_group_clusters_visualization.parquet"
    )

# ==========================================================
# Pattern Outputs
# ==========================================================

@lru_cache(maxsize=1)
def get_association_rule_summary():
    return load_parquet(
        "pattern_output",
        "association_rule_summary.parquet"
    )

@lru_cache(maxsize=1)
def get_association_rules():
    return load_parquet(
        "pattern_output",
        "association_rules.parquet"
    )

@lru_cache(maxsize=1)
def get_association_rule_scatter():
    return load_parquet(
        "pattern_output",
        "association_rule_scatter.parquet"
    )

@lru_cache(maxsize=1)
def get_top_lift_rules():
    return load_parquet(
        "pattern_output",
        "top_lift_rules.parquet"
    )

@lru_cache(maxsize=1)
def get_frequent_itemsets():
    return load_parquet(
        "pattern_output",
        "frequent_itemsets.parquet"
    )

@lru_cache(maxsize=1)
def get_bin_edges():
    return load_parquet(
        "pattern_output",
        "bin_edges.parquet"
    )

@lru_cache(maxsize=1)
def get_business_insights():
    return load_parquet(
        "pattern_output",
        "business_insights.parquet"
    )

# ==========================================================
# Anomaly Outputs
# ==========================================================

@lru_cache(maxsize=1)
def get_executive_summary():
    return load_parquet(
        "anomaly_output",
        "executive_summary.parquet"
    )

@lru_cache(maxsize=1)
def get_anomaly_method_counts():
    return load_parquet(
        "anomaly_output",
        "anomaly_method_counts.parquet"
    )

@lru_cache(maxsize=1)
def get_anomaly_categories():
    return load_parquet(
        "anomaly_output",
        "anomaly_categories.parquet"
    )

@lru_cache(maxsize=1)
def get_anomaly_scatter():
    return load_parquet(
        "anomaly_output",
        "anomaly_scatter.parquet"
    )

@lru_cache(maxsize=1)
def get_anomaly_feature_difference():
    return load_parquet(
        "anomaly_output",
        "anomaly_feature_difference.parquet"
    )

@lru_cache(maxsize=1)
def get_cluster_anomaly_cross_reference():
    return load_parquet(
        "anomaly_output",
        "cluster_anomaly_cross_reference.parquet"
    )

@lru_cache(maxsize=1)
def get_cluster_category_summary():
    return load_parquet(
        "anomaly_output",
        "cluster_category_summary.parquet"
    )

@lru_cache(maxsize=1)
def get_cluster_summary():
    return load_parquet(
        "anomaly_output",
        "cluster_summary.parquet"
    )

@lru_cache(maxsize=1)
def get_top10_anomalies():
    return load_parquet(
        "anomaly_output",
        "top10_anomalies.parquet"
    )

@lru_cache(maxsize=1)
def get_anomaly_method_breakdown():
    return load_parquet(
        "anomaly_output",
        "anomaly_method_breakdown.parquet"
    )

# ==========================================================
# Dashboard Outputs
# ==========================================================

@lru_cache(maxsize=1)
def get_loan_status_distribution():
    return load_parquet(
        "dashboard_output",
        "loan_status_distribution.parquet"
    )

@lru_cache(maxsize=1)
def get_grade_distribution():
    return load_parquet(
        "dashboard_output",
        "grade_distribution.parquet"
    )

@lru_cache(maxsize=1)
def get_state_distribution():
    return load_parquet(
        "dashboard_output",
        "state_distribution.parquet"
    )

@lru_cache(maxsize=1)
def get_loan_amount_distribution():
    return load_parquet(
        "dashboard_output",
        "loan_amount_distribution.parquet"
    )

@lru_cache(maxsize=1)
def get_interest_rate_distribution():
    return load_parquet(
        "dashboard_output",
        "interest_rate_distribution.parquet"
    )