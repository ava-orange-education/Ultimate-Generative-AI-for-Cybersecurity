from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
# Features extracted from network traffic and labels for normal/attack
X = network_features
y = network_labels
# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=10)
# Train SVM classifier
svm = SVC(kernel='rbf', C=1.0, gamma='scale')
svm.fit(X_train, y_train)
# Predict and evaluate
y_pred = svm.predict(X_test)
print(classification_report(y_test, y_pred))
