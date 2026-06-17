from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

urls = ["http://safe.com", "http://phishingsite.fake"]
labels = [0, 1]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(urls)

model = RandomForestClassifier()
model.fit(X, labels)

test_url = vectorizer.transform(["http://malicious-site.fake"])
prediction = model.predict(test_url)
print("Phishing" if prediction[0] else "Legitimate")
