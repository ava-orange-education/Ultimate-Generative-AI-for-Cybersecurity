from sklearn.cluster import KMeans
import numpy as np
# Features from network sessions (unlabeled)
X = network_session_features
# Find clusters
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(X)
# Analyze cluster assignments for anomalies (e.g., small or isolated clusters)
counts = np.bincount(clusters)
print("Cluster assignment counts:", counts)
