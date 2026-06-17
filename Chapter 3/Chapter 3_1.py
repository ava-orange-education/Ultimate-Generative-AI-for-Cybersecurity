from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Example dataset: features extracted from malware samples
X = malware_feature_vectors  # your features
y = malware_labels           # labels: 0 for benign, 1 for malware

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree
dt = DecisionTreeClassifier(max_depth=5)
dt.fit(X_train, y_train)

# Predict and evaluate
y_pred = dt.predict(X_test)
print(classification_report(y_test, y_pred))
