from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from utils.impact import impact_score
from rag.rag_engine import retrieve_answer
import os

app = Flask(__name__)
CORS(app)

# Load model
model = joblib.load(os.path.join("ml", "waste_classifier.pkl"))
vectorizer = joblib.load(os.path.join("ml", "vectorizer.pkl"))

# Load KB
with open("rag/knowledge_base.txt", "r", encoding="utf-8") as f:
    KB = f.read()

DISPOSAL_GUIDE = {
    "wet": "Put in wet bin / compost pit. Avoid plastic liners.",
    "dry": "Clean & dry item. Put in dry recycling bin.",
    "hazardous": "Store separately and give to hazardous waste collection center.",
    "e-waste": "Submit to authorized e-waste recycler / collection drive."
}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    item = data.get("item", "").strip()

    if not item:
        return jsonify({"error": "Item name is required"}), 400

    X = vectorizer.transform([item])
    pred = model.predict(X)[0]

    impact = impact_score(pred)

    response = {
        "item": item,
        "category": pred,
        "disposal": DISPOSAL_GUIDE.get(pred, "Dispose responsibly."),
        "explanation": f"The model predicted '{pred}' based on learned patterns from waste examples.",
        "impact": impact
    }
    return jsonify(response)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "Query is required"}), 400

    answer = retrieve_answer(query, KB)

    return jsonify({
        "query": query,
        "answer": answer,
        "note": "This answer is retrieved from the knowledge base (RAG)."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)