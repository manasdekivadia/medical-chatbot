# Medical Chatbot

Welcome to the **Medical Chatbot** project! This intelligent assistant is designed to provide medical information and support using advanced AI and NLP techniques. It can help users with medical queries, symptoms, and general healthcare information.

---

## Project Overview

The Medical Chatbot leverages state-of-the-art language models and knowledge retrieval to answer health-related questions accurately and efficiently. It is built for easy integration, extensibility, and deployment as a web or desktop app.

---
## Tech Stack / Technologies Used

### Languages & Frameworks:
- Python 3.10
- Flask (Web backend framework)
- HTML/CSS (Frontend templates)
- 
### Libraries & Tools:
- LangChain (Context-aware chains for retrieval-based QA)
- Hugging Face Transformers (Language models)
- FAISS / Similarity Search (for document retrieval)
- SentenceTransformers (Embeddings for semantic similarity)
- PyPDFLoader (Loading and parsing PDFs)
- Jupyter Notebook (Exploratory analysis and prototyping)

## Repository Structure
```
medical-chatbot/
│
├── app.py # Main Flask backend app
├── requirements.txt # Python dependencies
├── README.md # This file
├── data/ # Medical documents, datasets, and knowledge base
├── notebooks/ # Jupyter notebooks for prototyping and experiments
├── models/ # Pretrained or fine-tuned models
├── static/ # Frontend static files (CSS, JS)
├── templates/ # HTML templates for Flask app
└── utils/ # Utility scripts and helpers
```


---

## Features

- Conversational AI: Natural language understanding to handle medical queries.
- Knowledge Retrieval: Uses document search and similarity matching for accurate answers.
- Medical Data Support: Trained or integrated with trusted medical datasets.
- Context Awareness: Maintains conversation context for meaningful interactions.
- Privacy Considerations: No storage of personal medical data by default.
- Easy Deployment: Runs with minimal setup, suitable for local or cloud hosting.

---

## Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/manasdekivadia/medical-chatbot.git
   cd medical-chatbot
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate
3. Create a .env FILE:
   ```bash
   PINECONE_API_KEY = "your-api-key'
4. Install Dependencies:
   ```bash
   pip install -r requirements.txt
5. Run the Flask App:
   ```bash
   python app.py
6. Open your browser:
   ```bash
   http://127.0.0.1:5000

<p align="center"><strong>Happy to help</strong></p>
