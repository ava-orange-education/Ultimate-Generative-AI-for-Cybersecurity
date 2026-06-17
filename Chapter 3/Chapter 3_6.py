from sklearn.ensemble import IsolationForest
import numpy as np

# Sample data: network connection features (e.g., duration, packets)
X = np.array([[10, 300], [12, 500], [11, 350], [1000, 10]])  # Last point is an anomaly

# Train Isolation Forest for anomaly detection
iso_forest = IsolationForest(contamination=0.1, random_state=42)
iso_forest.fit(X)

# Predict anomalies (-1 indicates anomaly)
pred = iso_forest.predict(X)
print("Anomaly labels:", pred)
