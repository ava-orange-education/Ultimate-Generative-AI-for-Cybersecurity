from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# Example dataset: phishing email text and labels (0: legit, 1: phishing)
emails = email_contents
labels = email_labels
# Convert text to features
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(emails)
# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25, random_state=100)
# Train Random Forest
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
# Predict and evaluate
y_pred = rf.predict(X_test)
print(classification_report(y_test, y_pred))
