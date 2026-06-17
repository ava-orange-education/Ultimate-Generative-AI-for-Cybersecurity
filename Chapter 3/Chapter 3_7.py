from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample URLs and labels (1=phishing,0=legitimate)
urls = ["http://safe-site.com", "http://phishing123.com"]
labels = [0,1]

# Feature extraction
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(urls)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.5, random_state=0)

# Train Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Prediction and accuracy
y_pred = rf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
