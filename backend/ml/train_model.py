import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

data = [
    ("banana peel", "wet"),
    ("food waste", "wet"),
    ("vegetable waste", "wet"),
    ("paper", "dry"),
    ("cardboard", "dry"),
    ("plastic bottle", "dry"),
    ("glass bottle", "dry"),
    ("battery", "hazardous"),
    ("medicine", "hazardous"),
    ("paint", "hazardous"),
    ("mobile phone", "e-waste"),
    ("laptop", "e-waste"),
    ("charger", "e-waste"),
]

X = [x[0] for x in data]
y = [x[1] for x in data]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

joblib.dump(model, os.path.join(BASE_DIR, "waste_classifier.pkl"))
joblib.dump(vectorizer, os.path.join(BASE_DIR, "vectorizer.pkl"))

print("✅ Model trained and saved successfully!")