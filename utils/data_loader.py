from pathlib import Path
import pandas as pd

# Base Directory

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Raw Dataset

accepted_raw = pd.read_parquet(
    DATA_DIR / "accepted_raw.parquet"
)

# Processed Dataset

processed_df = pd.read_parquet(
    DATA_DIR / "processed_lendingclub.parquet"
)

# Clustering Outputs

CLUSTER_DIR = DATA_DIR / "clustering_output"

cluster_profiles = pd.read_parquet(
    CLUSTER_DIR / "cluster_profiles.parquet"
)

kmeans_elbow = pd.read_parquet(
    CLUSTER_DIR / "kmeans_elbow.parquet"
)

kmeans_silhouette = pd.read_parquet(
    CLUSTER_DIR / "kmeans_silhouette.parquet"
)

kmeans_visualization = pd.read_parquet(
    CLUSTER_DIR / "kmeans_visualization.parquet"
)

dbscan_umap = pd.read_parquet(
    CLUSTER_DIR / "dbscan_umap.parquet"
)

hierarchy_elbow = pd.read_parquet(
    CLUSTER_DIR / "hierarchy_elbow.parquet"
)

hierarchy_silhouette = pd.read_parquet(
    CLUSTER_DIR / "hierarchy_silhouette.parquet"
)

hierarchy_group_clusters = pd.read_parquet(
    CLUSTER_DIR / "hierarchy_group_clusters.parquet"
)

# Pattern Outputs

PATTERN_DIR = DATA_DIR / "pattern_output"

association_rule_summary = pd.read_parquet(
    PATTERN_DIR / "association_rule_summary.parquet"
)

association_rules = pd.read_parquet(
    PATTERN_DIR / "association_rules.parquet"
)

association_rule_scatter = pd.read_parquet(
    PATTERN_DIR / "association_rule_scatter.parquet"
)

top_lift_rules = pd.read_parquet(
    PATTERN_DIR / "top_lift_rules.parquet"
)

frequent_itemsets = pd.read_parquet(
    PATTERN_DIR / "frequent_itemsets.parquet"
)

bin_edges = pd.read_parquet(
    PATTERN_DIR / "bin_edges.parquet"
)

business_insights = pd.read_parquet(
    PATTERN_DIR / "business_insights.parquet"
)

# Anomaly Outputs

ANOMALY_DIR = DATA_DIR / "anomaly_output"

executive_summary = pd.read_parquet(
    ANOMALY_DIR / "executive_summary.parquet"
)


anomaly_method_counts = pd.read_parquet(
    ANOMALY_DIR / "anomaly_method_counts.parquet"
)


anomaly_categories = pd.read_parquet(
    ANOMALY_DIR / "anomaly_categories.parquet"
)


anomaly_scatter = pd.read_parquet(
    ANOMALY_DIR / "anomaly_scatter.parquet"
)


anomaly_feature_difference = pd.read_parquet(
    ANOMALY_DIR / "anomaly_feature_difference.parquet"
)


top10_anomalies = pd.read_parquet(
    ANOMALY_DIR / "top10_anomalies.parquet"
)

# ==========================================================
# Dashboard Output
# ==========================================================

loan_status_distribution = pd.read_parquet(
    DATA_DIR / "dashboard_output" / "loan_status_distribution.parquet"
)

grade_distribution = pd.read_parquet(
    DATA_DIR / "dashboard_output" / "grade_distribution.parquet"
)

state_distribution = pd.read_parquet(
    DATA_DIR / "dashboard_output" / "state_distribution.parquet"
)

loan_amount_distribution = pd.read_parquet(
    DATA_DIR / "dashboard_output" / "loan_amount_distribution.parquet"
)

interest_rate_distribution = pd.read_parquet(
    DATA_DIR / "dashboard_output" / "interest_rate_distribution.parquet"
)

# Quick Check

if __name__ == "__main__":

    print("All parquet files loaded successfully.\n")

    print("Raw Dataset:", accepted_raw.shape)
    print("Processed Dataset:", processed_df.shape)

    print("Cluster Profiles:", cluster_profiles.shape)
    print("Association Rules:", association_rules.shape)
    print("Anomaly Scatter:", anomaly_scatter.shape) 

    # print(executive_summary.columns.tolist())
    # print(anomaly_method_counts.columns.tolist())
    # print(anomaly_categories.columns.tolist())
    # print(anomaly_scatter.columns.tolist())
    # print(anomaly_feature_difference.columns.tolist())

    print(association_rules.columns.tolist())
    print(association_rule_scatter.columns.tolist())
    print(association_rule_summary.columns.tolist())
    print(top_lift_rules.columns.tolist())
    print(business_insights.columns.tolist())
    print(frequent_itemsets.columns.tolist())
    print(bin_edges.columns.tolist())