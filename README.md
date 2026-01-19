# EcoSort AI 🌿  
AI-powered Waste Segregation & Recycling Guidance Assistant (SDG 12)

EcoSort AI is a sustainability-focused web application that helps users correctly segregate household waste using AI and provides recycling/disposal guidance. It includes a Machine Learning waste classifier and a RAG-based assistant that answers disposal rules from a knowledge base.

---

## 🎯 SDG Alignment
**Primary SDG:** SDG 12 – Responsible Consumption and Production  
**Secondary SDGs:** SDG 11 – Sustainable Cities & Communities, SDG 13 – Climate Action

---

## 🧩 Problem Statement
Many households incorrectly segregate waste due to confusion about disposal rules. This leads to contamination of recyclable material and increased landfill waste.  
EcoSort AI solves this by using AI to classify waste items and guide users toward correct disposal.

---

## ✅ Key Features
### 🔹 Waste Classifier (ML)
- Classifies waste items into:
  - Wet Waste
  - Dry Waste
  - Hazardous Waste
  - E-Waste
- Provides:
  - Category prediction
  - Disposal instructions
  - Explanation
  - Impact score (CO₂ savings estimate)

### 🔹 Disposal Rules Assistant (RAG)
- Users can ask questions like:
  - "Where to dispose lithium battery?"
  - "Is paper recyclable?"
- Retrieves answers from a curated sustainability knowledge base.

---

## ⚙️ Tech Stack
### Backend
- Python
- Flask + Flask-CORS
- Scikit-learn (TF-IDF + Logistic Regression)
- Joblib (model saving/loading)

### Frontend
- HTML
- CSS (modern UI)
- JavaScript (Fetch API)

---

## 📂 Project Folder Structure
```txt
ECOSORTAI/
├── .venv/
├── backend/
│   ├── ml/
│   │   ├── train_model.py
│   │   ├── vectorizer.pkl
│   │   └── waste_classifier.pkl
│   ├── rag/
│   │   ├── knowledge_base.txt
│   │   └── rag_engine.py
│   ├── utils/
│   │   └── impact.py
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── styles.css
├── .gitignore
└── README.md

---

## 🔗 Project Links

- ✅ GitHub Repository: https://github.com/mohammedriyashad/EcoSortAI
- ✅ Backend (Render): https://ecosortai-backend.onrender.com
- ✅ Frontend (Netlify): https://ecosortai-ml.netlify.app
